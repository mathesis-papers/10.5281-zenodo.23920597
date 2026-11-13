# MathOverflow 513954, revision 2: source package

Haobo Ma (ChronoAI Pte Ltd, Singapore) and Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore).

License: CC BY 4.0, identifier `cc-by-4.0`. The independently written exposition and checking code are supplied under this license. Lucid's MathOverflow post is separately attributed and licensed CC BY-SA 4.0; the post itself is not included.

## Mathematical contents

The note proves the structured rank-one inertia formula for all real symmetric matrices with nonzero quadratic pivot, including singular matrices, and the kernel direct-sum identity. It proves both sign and fixed-negative-coordinate assertions on the original punctured-simplex domain, together with a connected-domain formulation and the positive-semidefinite classification. Corollaries give nondegenerate block removal, arbitrary real coefficient changes, and countably punctured simplices. All statements have written proofs.

The exact posing source is https://mathoverflow.net/revisions/513954/2, revision GUID `1084D752-1BBD-405E-B335-28FBDD1F4D6D`. The hyperplane congruence mechanism is due to Lucid, the posing author.

The matrix inertia formula already has a proof by user1551 on Lucid's Mathematics Stack Exchange cross-post, answer 5146353 (August 7, 2026), https://math.stackexchange.com/a/5146353. The note credits this prior answer and gives a self-contained hyperplane argument and the continuous-family proof.

For the linked Mathematics Stack Exchange question 5146381, the strictly increasing odd polynomial `h(t)=(3t-t^3)/2` has squared ratio infimum `16*(17-9*sqrt(3))/23` over all dimensions, approached by one squared coordinate `6-3*sqrt(3)` and an increasingly diffuse remainder. The finite-dimensional infimum is not attained. At most two active coordinates instead give minimum `80/81`; the three-coordinate witness with squared coordinates `(4/5,1/10,1/10)` gives `13689/13885`, strictly smaller. Thus a universal two-coordinate reduction fails even with increasing polynomial `h` and decreasing `h(t)/t`. Zero coordinates cause no ambiguity for this polynomial because `h(0)=0`.

daw's earlier `h(t)=1` suggestion (August 8, 2026) and Exodd's `h(t)=1/t` example (August 11, 2026) are credited separately. The note proves their respective infima and identifies the missing value at zero in the original general formulation. A classification for arbitrary `h` and the source author's unspecified polynomial is not asserted. The coverage table in the PDF maps every question and linked comment to its mathematical scope.

## Build the PDF

The package has one main source, `note.tex`, with its bibliography embedded and no external figures or bibliography files.

Using Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, use a standard LaTeX distribution containing the packages listed in the source:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is embedded, so BibTeX is unnecessary. These commands produce `note.pdf`.

## Exact finite checks

Python 3.10 or later, using the standard library:

```sh
python3 verify.py > verification.rebuilt.json
cmp verification.json verification.rebuilt.json
```

Run with assertions enabled, without `-O` or `PYTHONOPTIMIZE`; the script rejects optimized execution.

The script exhausts diagonal entries and vector coordinates in `{-1,0,1}` in dimensions 1 through 4, omitting zero pivots. It separately checks rational non-diagonal examples obtained by invertible integer congruences, both pivot signs, singular matrices, and the disconnected one-dimensional domain example. Inertia is obtained by rational symmetric elimination, with two-by-two pivots when all remaining diagonal entries vanish. Rational Gaussian elimination checks rank and the kernel direct sum. The block congruences are checked independently entry by entry. These are finite checks, not a replacement for the general written proofs.

The output field `congruence_transformed_cases` counts the entire congruence-generated series: 226 instances. The separate fields `genuinely_non_diagonal_cases` and `diagonal_cases_in_congruence_family` give its 214 genuinely non-diagonal matrices and 12 diagonal endpoints. `two_by_two_pivot_controls` counts the two controls for the two-by-two elimination branch; `disconnected_example_algebraic_cases` counts the algebraic witnesses on the two components, whose topological properties have written proofs in the note.

The supplementary matrix checks exhaust the same diagonal alphabet in dimensions 2 through 4, after the stated invertible integer congruence, for nondegenerate leading coordinate blocks and six real rational coefficient values. They check block inertia subtraction, rank and kernel identities, and the coefficient formula. The sphere checks enumerate all positive partitions of 12 into 1 through 6 parts (1,024 cases), 101 two-coordinate rational partitions, and the explicit three-coordinate witness. They check the moment identity, moment inequality and radical lower bound by exact rational comparisons. The formula for the infimum at `6-3*sqrt(3)` is additionally checked in the field `Q(sqrt(3))`. These are finite algebraic checks; the all-dimension infimum and limiting construction have written proofs.

## Lean correspondence

Pinned upstream revision: `0f1f822c673c1903dc6b0a209a23dacebca2aa6c`.

- `D5.S3.QuadraticForms.StructuredRankOneInertia.inertia_downdate`: both real symmetric inertia triples.
- `D5.S3.QuadraticForms.StructuredRankOneInertia.kernel_split` and `nullity_downdate`: the kernel direct sum and nullity increase.
- `D5.S3.QuadraticForms.StructuredRankOneFamily.punctured_simplex_pathConnected`: the source-domain topology.
- `D5.S3.QuadraticForms.StructuredRankOneFamily.continuous_family`: source-domain sign constancy and the fixed negative coordinate.
- `D5.S3.QuadraticForms.StructuredRankOneFamily.mo513954_revision2`: the conjunction covering both source questions.

The arbitrary-connected-space formulation, positive-pivot classification, rank identity, sharpness example, block removal, coefficient changes, countable punctures and sphere results have written proofs in the note. The listed Lean declarations cover the matrix statements and the original finite-puncture family; the additional results are distinguished from that scope. Both exact Lean files are linked in its body.

## Files

- `note.tex`: complete mathematical source.
- `metadata.json`: title, authors, license, problem identifier and pinned source.
- `verify.py`: dependency-free rational checks.
- `verification.json`: deterministic finite-check output.
- `README.md`: build instructions and scientific scope.

The PDF is supplied alongside this source archive.
