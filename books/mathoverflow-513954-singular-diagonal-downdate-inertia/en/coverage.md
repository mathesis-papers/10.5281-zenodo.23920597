<style>pre:has(> code[class*="typst"]) { display: none; }</style>

# Sources, attribution and formal coverage

Haobo Ma (Chrono AI, Singapore) and Wenlin Zhang (National University of Singapore and Chrono AI, Singapore) are the authors of the version-2 paper. Its exact-version DOI is [10.5281/zenodo.23920598](https://doi.org/10.5281/zenodo.23920598); [10.5281/zenodo.23920597](https://doi.org/10.5281/zenodo.23920597) identifies the version family. The paper and this authored explanation carry CC BY 4.0. The original question, earlier answer and linked discussion retain their own attribution and licences.

## Original mathematical sources

- Lucid, [MathOverflow 513954, revision 2](https://mathoverflow.net/revisions/513954/2), 5 August 2026: the singular diagonal inertia question, proposed hyperplane argument and continuous-family question (CC BY-SA 4.0).
- user1551, [Mathematics Stack Exchange answer 5146353](https://math.stackexchange.com/a/5146353), 7 August 2026: the earlier proof of the matrix inertia formula, credited by Ma and Zhang (CC BY-SA 4.0). The zero count follows from dimension minus the positive and negative counts.
- Lucid, [Mathematics Stack Exchange question 5146381](https://math.stackexchange.com/questions/5146381), 7 August 2026: the sphere ratio, numerator estimate, stationarity discussion and proposed reduction to few active coordinates. The [negative-coordinate handoff comment](https://math.stackexchange.com/questions/5146335#comment11110130_5146335) is answered by the clopen-set argument.
- daw, [comment 11110291](https://math.stackexchange.com/questions/5146381#comment11110291_5146381), 8 August 2026: the choice $h(t)=1$ (CC BY-SA 4.0).
- Exodd, [answer 5146715](https://math.stackexchange.com/a/5146715), 11 August 2026: the choice $h(t)=1/t$ (CC BY-SA 4.0).

Ma and Zhang give the self-contained symmetric-matrix proof and its kernel/rank consequences, the connected-family argument and extensions, and the exact polynomial sphere result. The earlier questions and examples retain the credit just listed. The accessible guide and [proof chapter](statements.md) explain this same version; they do not replace its source record.

## Exact pinned declarations

The pin is `0f1f822c673c1903dc6b0a209a23dacebca2aa6c`. Both source modules use the namespace `D5.S3.QuadraticForms`. The links below go directly to the declarations in that revision.

| Statement | Declaration | Exact mathematical scope |
| --- | --- | --- |
| Both signed inertia triples | [`StructuredRankOneInertia.inertia_downdate`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneInertia.lean#L262) | Arbitrary real symmetric matrix, including singular input; nonzero pivot |
| Kernel direct sum | [`StructuredRankOneInertia.kernel_split`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneInertia.lean#L97) | Kernel equality and disjointness; same matrix hypotheses |
| Nullity increase | [`StructuredRankOneInertia.nullity_downdate`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneInertia.lean#L141) | Kernel dimension increases by exactly one |
| Diagonal sign counts | [`StructuredRankOneInertia.diagonal_counts`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneInertia.lean#L68) | Positive and negative indices equal the entry sign counts |
| Finite-puncture topology | [`StructuredRankOneFamily.punctured_simplex_pathConnected`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneFamily.lean#L91) | Finite deletion, open simplex of dimension at least two; nonempty path-connected complement |
| Source-domain family | [`StructuredRankOneFamily.continuous_family`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneFamily.lean#L105) | Finite-puncture domain; constant pivot sign; unique fixed negative coordinate in negative branch |
| Original source conjunction | [`StructuredRankOneFamily.mo513954_revision2`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneFamily.lean#L186) | Diagonal inertia formulas together with the preceding source-domain family conclusion |

The full rank-one manuscript theorem combines these exact inertia/kernel/nullity results with a written rank-nullity consequence. The general connected-domain family theorem is broader than the pinned finite-puncture declaration. In its positive branch, entrywise nonnegativity follows from the written PSD classification; that clause is not listed in `continuous_family`. The public path-connectedness declaration assumes finite deletion even though its proof uses a countable-complement theorem. Countable punctures, the dimension-two counterexample, block removal, coefficient changes and the sphere results have the complete written proofs in the preceding chapter.

Exact rational finite-instance checks are reported in the original paper's verification supplement. They illustrate the identities and do not replace either the all-parameter written proofs or the pinned declarations. No claim here promotes the paper's separate public verification status.

## Existing formalization contributions

These are the ten canonical requests associated with the manuscript results. The requested work should reuse the exact declarations above: the rank consequence does not require reconstructing the inertia or kernel proofs, and the PSD classification follows from the inertia counts. The finite-puncture source result has existing declarations and no separate new request.

| Manuscript locator | Remaining mathematical scope | Canonical request |
| --- | --- | --- |
| Theorem 1 | Rank consequence and complete conjunction | [#169](https://github.com/the-omega-institute/trureturing-requests/issues/169) |
| Corollary 2 | Both PSD branches and diagonal classification | [#170](https://github.com/the-omega-institute/trureturing-requests/issues/170) |
| Corollary 3 | Nondegenerate block removal | [#171](https://github.com/the-omega-institute/trureturing-requests/issues/171) |
| Corollary 4 | All-real coefficient identity | [#172](https://github.com/the-omega-institute/trureturing-requests/issues/172) |
| Theorem 5 | General connected domain and full positive branch | [#173](https://github.com/the-omega-institute/trureturing-requests/issues/173) |
| Corollary 7 | Countable-puncture extension | [#174](https://github.com/the-omega-institute/trureturing-requests/issues/174) |
| Corollary 8 | Dimension-two witness and sharp threshold | [#175](https://github.com/the-omega-institute/trureturing-requests/issues/175) |
| Corollary 9 | Numerator bound and qualified stationarity | [#176](https://github.com/the-omega-institute/trureturing-requests/issues/176) |
| Corollary 10 | Infima for the attributed earlier examples | [#177](https://github.com/the-omega-institute/trureturing-requests/issues/177) |
| Theorem 11 | Polynomial moments, gap, infimum and nonattainment | [#178](https://github.com/the-omega-institute/trureturing-requests/issues/178) |

A request is a place to contribute a missing formal statement, not a proof certificate. Focused contributions follow the upstream [contribution instructions](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/CONTRIBUTING.md) and should link the relevant existing request.

## Mathematical boundary

The matrix formula assumes a nonzero pivot and permits singular matrices. The connected-family theorem permits zero values among the other diagonal entries. The simplex dimension threshold concerns uniform survival under punctures, not the rank-one matrix identity. The polynomial construction disproves universal two-coordinate reduction and computes this polynomial's exact all-dimension infimum; it does not classify arbitrary continuous $h$ or identify the source author's unspecified polynomial.

```{=typst}
#pagebreak()
```
