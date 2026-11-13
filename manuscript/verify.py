import itertools
import json
from fractions import Fraction


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def multiply(left, right):
    columns = transpose(right)
    return [[sum(first * second for first, second in zip(row, column))
             for column in columns] for row in left]


def identity(dimension):
    return [[Fraction(row == column) for column in range(dimension)]
            for row in range(dimension)]


def matrix_rank(matrix):
    remaining = [list(map(Fraction, row)) for row in matrix]
    if not remaining:
        return 0
    pivot_row = 0
    for column in range(len(remaining[0])):
        found = next((row for row in range(pivot_row, len(remaining))
                      if remaining[row][column]), None)
        if found is None:
            continue
        remaining[pivot_row], remaining[found] = remaining[found], remaining[pivot_row]
        divisor = remaining[pivot_row][column]
        remaining[pivot_row] = [entry / divisor for entry in remaining[pivot_row]]
        for row in range(pivot_row + 1, len(remaining)):
            factor = remaining[row][column]
            remaining[row] = [entry - factor * pivot for entry, pivot in
                              zip(remaining[row], remaining[pivot_row])]
        pivot_row += 1
        if pivot_row == len(remaining):
            break
    return pivot_row


def exact_inertia(matrix):
    remaining = [list(map(Fraction, row)) for row in matrix]
    positive = negative = zero = 0
    while remaining:
        dimension = len(remaining)
        pivot = next((index for index in range(dimension) if remaining[index][index]), None)
        if pivot is not None:
            order = [pivot] + [index for index in range(dimension) if index != pivot]
            permuted = [[remaining[row][column] for column in order] for row in order]
            scalar = permuted[0][0]
            positive += scalar > 0
            negative += scalar < 0
            remaining = [[permuted[row][column] - permuted[row][0] * permuted[0][column] / scalar
                          for column in range(1, dimension)] for row in range(1, dimension)]
            continue
        pair = next(((row, column) for row in range(dimension)
                     for column in range(row + 1, dimension) if remaining[row][column]), None)
        if pair is None:
            zero += dimension
            break
        order = list(pair) + [index for index in range(dimension) if index not in pair]
        permuted = [[remaining[row][column] for column in order] for row in order]
        scalar = permuted[0][1]
        positive += 1
        negative += 1
        remaining = [[permuted[row][column] -
                      (permuted[row][0] * permuted[1][column] +
                       permuted[row][1] * permuted[0][column]) / scalar
                      for column in range(2, dimension)] for row in range(2, dimension)]
    return [positive, negative, zero]


def nullspace_basis(matrix):
    reduced = [list(map(Fraction, row)) for row in matrix]
    dimension = len(reduced)
    pivot_columns = []
    for column in range(dimension):
        pivot_row = len(pivot_columns)
        found = next((row for row in range(pivot_row, dimension) if reduced[row][column]), None)
        if found is None:
            continue
        reduced[pivot_row], reduced[found] = reduced[found], reduced[pivot_row]
        divisor = reduced[pivot_row][column]
        reduced[pivot_row] = [entry / divisor for entry in reduced[pivot_row]]
        for row in range(dimension):
            if row != pivot_row:
                factor = reduced[row][column]
                reduced[row] = [entry - factor * pivot for entry, pivot in
                                zip(reduced[row], reduced[pivot_row])]
        pivot_columns.append(column)
    basis = []
    for free_column in range(dimension):
        if free_column in pivot_columns:
            continue
        vector = [Fraction(index == free_column) for index in range(dimension)]
        for row, pivot_column in enumerate(pivot_columns):
            vector[pivot_column] = -reduced[row][free_column]
        basis.append(vector)
    return basis


def check_case(matrix, vector):
    dimension = len(vector)
    matrix = [list(map(Fraction, row)) for row in matrix]
    vector = list(map(Fraction, vector))
    image = [sum(entry * coordinate for entry, coordinate in zip(row, vector)) for row in matrix]
    delta = sum(coordinate * entry for coordinate, entry in zip(vector, image))
    if not delta:
        return None
    updated = [[matrix[row][column] - image[row] * image[column] / delta
                for column in range(dimension)] for row in range(dimension)]
    before = exact_inertia(matrix)
    expected = [before[0] - (delta > 0), before[1] - (delta < 0), before[2] + 1]
    assert exact_inertia(updated) == expected
    assert matrix_rank(updated) == matrix_rank(matrix) - 1
    assert all(sum(entry * coordinate for entry, coordinate in zip(row, vector)) == 0
               for row in updated)
    old_kernel = nullspace_basis(matrix)
    for element in old_kernel:
        assert all(sum(entry * coordinate for entry, coordinate in zip(row, element)) == 0
                   for row in updated)
    kernel_generators = old_kernel + [vector]
    assert matrix_rank(transpose(kernel_generators)) == len(kernel_generators)
    assert len(kernel_generators) == dimension - matrix_rank(updated)
    pivot = next(index for index, entry in enumerate(image) if entry)
    basis = []
    for column in range(dimension):
        if column != pivot:
            element = [Fraction(index == column) for index in range(dimension)]
            element[pivot] = -image[column] / image[pivot]
            basis.append(element)
    transform = transpose(basis + [vector])
    assert matrix_rank(transform) == dimension
    original_blocks = multiply(multiply(transpose(transform), matrix), transform)
    updated_blocks = multiply(multiply(transpose(transform), updated), transform)
    assert original_blocks[-1][-1] == delta
    assert updated_blocks[-1][-1] == 0
    for index in range(dimension - 1):
        assert original_blocks[index][-1] == original_blocks[-1][index] == 0
        assert updated_blocks[index][-1] == updated_blocks[-1][index] == 0
    for row in range(dimension - 1):
        for column in range(dimension - 1):
            assert original_blocks[row][column] == updated_blocks[row][column]
    psd_expected = before[1] == (delta < 0)
    assert (exact_inertia(updated)[1] == 0) == psd_expected
    return {"positive_pivot": delta > 0, "singular": matrix_rank(matrix) < dimension}


def matrix_inverse(matrix):
    dimension = len(matrix)
    augmented = [list(map(Fraction, row)) + identity(dimension)[index]
                 for index, row in enumerate(matrix)]
    for column in range(dimension):
        pivot = next((index for index in range(column, dimension)
                      if augmented[index][column]), None)
        if pivot is None:
            return None
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [entry / divisor for entry in augmented[column]]
        for row in range(dimension):
            if row != column:
                factor = augmented[row][column]
                augmented[row] = [entry - factor * selected for entry, selected
                                  in zip(augmented[row], augmented[column])]
    return [row[dimension:] for row in augmented]


def supplementary_matrix_checks():
    block_count = coefficient_count = 0
    block_sizes = set()
    for dimension in range(2, 5):
        transform = identity(dimension)
        for index in range(dimension - 1):
            transform[index][index + 1] = Fraction(index + 1)
        for diagonal in itertools.product((-1, 0, 1), repeat=dimension):
            original = [[Fraction(diagonal[row] if row == column else 0)
                         for column in range(dimension)] for row in range(dimension)]
            matrix = multiply(multiply(transpose(transform), original), transform)
            before = exact_inertia(matrix)
            for block_size in range(1, dimension + 1):
                frame = [row[:block_size] for row in identity(dimension)]
                gram = multiply(multiply(transpose(frame), matrix), frame)
                inverse = matrix_inverse(gram)
                if inverse is None:
                    continue
                image = multiply(matrix, frame)
                removed = multiply(multiply(image, inverse), transpose(image))
                modified = [[matrix[row][column] - removed[row][column]
                             for column in range(dimension)] for row in range(dimension)]
                gram_inertia = exact_inertia(gram)
                assert exact_inertia(modified) == [before[0] - gram_inertia[0],
                                                  before[1] - gram_inertia[1],
                                                  before[2] + block_size]
                assert matrix_rank(modified) == matrix_rank(matrix) - block_size
                assert not any(entry for row in multiply(modified, frame) for entry in row)
                generators = nullspace_basis(matrix) + transpose(frame)
                assert matrix_rank(transpose(generators)) == len(generators)
                assert len(generators) == dimension - matrix_rank(modified)
                assert not any(entry for row in multiply(modified, transpose(generators))
                               for entry in row)
                block_count += 1
                block_sizes.add(block_size)
            vector = [[Fraction(index + 1)] for index in range(dimension)]
            image = multiply(matrix, vector)
            delta = multiply(transpose(vector), image)[0][0]
            if not delta:
                continue
            for coefficient in (Fraction(-2), Fraction(0), Fraction(1, 2),
                                Fraction(1), Fraction(3, 2), Fraction(2)):
                modified = [[matrix[row][column] - coefficient * image[row][0] * image[column][0] / delta
                             for column in range(dimension)] for row in range(dimension)]
                scalar = (1 - coefficient) * delta
                expected = [before[0] - (delta > 0) + (scalar > 0),
                            before[1] - (delta < 0) + (scalar < 0),
                            before[2] + (scalar == 0)]
                assert exact_inertia(modified) == expected
                coefficient_count += 1
    return {'block_removal_cases': block_count, 'block_sizes': sorted(block_sizes),
            'coefficient_cases': coefficient_count,
            'coefficient_values': ['-2', '0', '1/2', '1', '3/2', '2']}


def positive_compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(1, total - length + 2):
        for tail in positive_compositions(total - first, length - 1):
            yield (first,) + tail


def sphere_ratio_squared(weights):
    assert sum(weights) == 1 and all(weight >= 0 for weight in weights)
    second = sum(weight ** 2 for weight in weights)
    third = sum(weight ** 3 for weight in weights)
    numerator = sum(weight * (3 - weight) / 2 for weight in weights)
    denominator = sum(weight * ((3 - weight) / 2) ** 2 for weight in weights)
    result = numerator ** 2 / denominator
    assert result == (3 - second) ** 2 / (9 - 6 * second + third)
    assert third ** 2 <= second ** 3
    threshold = 272 - 23 * result
    assert threshold <= 0 or threshold ** 2 <= 144 ** 2 * 3
    return result


def quadratic_add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def quadratic_multiply(left, right):
    return (left[0] * right[0] + 3 * left[1] * right[1],
            left[0] * right[1] + left[1] * right[0])


def supplementary_sphere_checks():
    count = 0
    for dimension in range(1, 7):
        for composition in positive_compositions(12, dimension):
            sphere_ratio_squared([Fraction(entry, 12) for entry in composition])
            count += 1
    for numerator in range(101):
        first = Fraction(numerator, 100)
        product = first * (1 - first)
        result = sphere_ratio_squared([first, 1 - first])
        assert result - Fraction(80, 81) == (9 * product - 1) ** 2 / (81 * (1 + Fraction(9, 4) * product))
    witness = sphere_ratio_squared([Fraction(4, 5), Fraction(1, 10), Fraction(1, 10)])
    assert witness == Fraction(13689, 13885) < Fraction(80, 81)
    optimum = (Fraction(6), Fraction(-3))
    squared = quadratic_multiply(optimum, optimum)
    cubed = quadratic_multiply(squared, optimum)
    numerator = quadratic_add((Fraction(3), Fraction(0)), (-squared[0], -squared[1]))
    numerator = quadratic_multiply(numerator, numerator)
    denominator = quadratic_add((Fraction(9), Fraction(0)), (-6 * squared[0], -6 * squared[1]))
    denominator = quadratic_add(denominator, cubed)
    claimed = (Fraction(272, 23), Fraction(-144, 23))
    assert numerator == quadratic_multiply(claimed, denominator)
    assert quadratic_add(squared, (-12 * optimum[0] + 9, -12 * optimum[1])) == (0, 0)
    return {'rational_partition_cases': count, 'partition_denominator': 12,
            'dimensions': [1, 2, 3, 4, 5, 6], 'two_coordinate_cases': 101,
            'three_coordinate_squared_ratio': str(witness),
            'two_coordinate_minimum_squared': '80/81',
            'all_dimension_infimum_squared': '16*(17-9*sqrt(3))/23',
            'radical_identity_arithmetic': 'exact Q(sqrt(3))'}


def main():
    if not __debug__:
        raise RuntimeError("Exact checks require assertions; run Python without -O.")
    results = []
    for dimension in range(1, 5):
        counts = {"dimension": dimension, "checked": 0, "zero_pivot_omitted": 0,
                  "positive_pivot": 0, "negative_pivot": 0, "singular": 0}
        for diagonal in itertools.product((-1, 0, 1), repeat=dimension):
            matrix = [[Fraction(diagonal[row] if row == column else 0)
                       for column in range(dimension)] for row in range(dimension)]
            assert exact_inertia(matrix) == [sum(entry > 0 for entry in diagonal),
                                             sum(entry < 0 for entry in diagonal),
                                             sum(entry == 0 for entry in diagonal)]
            for vector in itertools.product((-1, 0, 1), repeat=dimension):
                result = check_case(matrix, vector)
                if result is None:
                    counts["zero_pivot_omitted"] += 1
                    continue
                counts["checked"] += 1
                counts["positive_pivot"] += result["positive_pivot"]
                counts["negative_pivot"] += not result["positive_pivot"]
                counts["singular"] += result["singular"]
        results.append(counts)
    general_count = 0
    genuinely_non_diagonal = 0
    for dimension in range(2, 5):
        transform = identity(dimension)
        for index in range(dimension - 1):
            transform[index][index + 1] = Fraction(index + 1)
        assert matrix_rank(transform) == dimension
        for diagonal in itertools.product((-1, 0, 1), repeat=dimension):
            matrix = [[Fraction(diagonal[row] if row == column else 0)
                       for column in range(dimension)] for row in range(dimension)]
            matrix = multiply(multiply(transpose(transform), matrix), transform)
            assert exact_inertia(matrix) == [sum(entry > 0 for entry in diagonal),
                                             sum(entry < 0 for entry in diagonal),
                                             sum(entry == 0 for entry in diagonal)]
            for vector in [list(range(1, dimension + 1)), [Fraction(1, index + 1) for index in range(dimension)]]:
                if check_case(matrix, vector) is not None:
                    general_count += 1
                    genuinely_non_diagonal += any(matrix[row][column]
                                                   for row in range(dimension)
                                                   for column in range(dimension) if row != column)
    assert exact_inertia([[0, 1], [1, 0]]) == [1, 1, 0]
    assert exact_inertia([[0, 0, 2], [0, 0, 0], [2, 0, 0]]) == [1, 1, 1]
    assert check_case([[-1, 0], [0, 1]], [1, 0])["positive_pivot"] is False
    assert check_case([[1, 0], [0, -1]], [0, 1])["positive_pivot"] is False
    result = {"arithmetic": "exact rational", "diagonal_alphabet": [-1, 0, 1],
              "diagonal_cases": results, "congruence_transformed_cases": general_count,
              "genuinely_non_diagonal_cases": genuinely_non_diagonal,
              "diagonal_cases_in_congruence_family": general_count - genuinely_non_diagonal,
              "two_by_two_pivot_controls": 2,
              "disconnected_example_algebraic_cases": 2,
              "identities": ["inertia", "rank decrease", "kernel direct sum", "new null vector", "invertible hyperplane basis",
                             "two block congruences", "positive-semidefinite classification"],
              "supplementary_matrix_checks": supplementary_matrix_checks(),
              "sphere_checks": supplementary_sphere_checks(),
              "scope": "finite instances; general statements have written proofs in note.tex"}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
