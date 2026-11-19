<style>pre:has(> code[class*="typst"]) { display: none; }</style>

# 来源、归属与形式覆盖

第二版论文作者为 Haobo Ma（Chrono AI，Singapore）与 Wenlin Zhang（National University of Singapore 及 Chrono AI，Singapore）。精确版本 DOI 为 [10.5281/zenodo.23920598](https://doi.org/10.5281/zenodo.23920598)；[10.5281/zenodo.23920597](https://doi.org/10.5281/zenodo.23920597) 标识版本家族。论文与本讲解采用 CC BY 4.0；原问题、先前回答及关联讨论保留各自的署名和许可。

## 原始数学来源

- Lucid，[MathOverflow 513954 第二修订版](https://mathoverflow.net/revisions/513954/2)，2026 年 8 月 5 日：奇异对角矩阵惯性问题、所提超平面论证与连续族问题（CC BY-SA 4.0）。
- user1551，[Mathematics Stack Exchange 回答 5146353](https://math.stackexchange.com/a/5146353)，2026 年 8 月 7 日：更早的矩阵惯性公式证明，Ma 与 Zhang 已明确归功于该回答（CC BY-SA 4.0）。零计数由总维数减去正负计数得到。
- Lucid，[Mathematics Stack Exchange 问题 5146381](https://math.stackexchange.com/questions/5146381)，2026 年 8 月 7 日：球面比值、分子估计、驻点讨论及少量活跃坐标约化问题。[负坐标交班的评论](https://math.stackexchange.com/questions/5146335#comment11110130_5146335)由开闭集论证回答。
- daw，[评论 11110291](https://math.stackexchange.com/questions/5146381#comment11110291_5146381)，2026 年 8 月 8 日：选择 $h(t)=1$（CC BY-SA 4.0）。
- Exodd，[回答 5146715](https://math.stackexchange.com/a/5146715)，2026 年 8 月 11 日：选择 $h(t)=1/t$（CC BY-SA 4.0）。

Ma 与 Zhang 给出自洽的实对称矩阵证明及核、秩推论，连通族论证和推广，以及精确多项式球面结果。先前问题与例子的归属如上。导读与[证明章](statements.md)解释的是同一版本，不替代其原始记录。

## 精确所钉声明

所钉提交为 `0f1f822c673c1903dc6b0a209a23dacebca2aa6c`。两个源模块均使用命名空间 `D5.S3.QuadraticForms`。下列链接直接指向该版本的声明。

| 陈述 | 声明 | 精确数学范围 |
| --- | --- | --- |
| 两种惯性三元组 | [`StructuredRankOneInertia.inertia_downdate`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneInertia.lean#L262) | 任意实对称矩阵，含奇异输入；主元非零 |
| 核直和 | [`StructuredRankOneInertia.kernel_split`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneInertia.lean#L97) | 核等式与交集为零；矩阵假设相同 |
| 零度增加 | [`StructuredRankOneInertia.nullity_downdate`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneInertia.lean#L141) | 核维数恰增加一 |
| 对角符号计数 | [`StructuredRankOneInertia.diagonal_counts`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneInertia.lean#L68) | 正负惯性指数等于相应符号对角元个数 |
| 有限删点拓扑 | [`StructuredRankOneFamily.punctured_simplex_pathConnected`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneFamily.lean#L91) | 有限删点、维数至少二的开单纯形；余集非空且道路连通 |
| 原问题域连续族 | [`StructuredRankOneFamily.continuous_family`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneFamily.lean#L105) | 有限删点域；主元符号固定；负分支有唯一固定负坐标 |
| 原问题合取 | [`StructuredRankOneFamily.mo513954_revision2`](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/D5/S3/QuadraticForms/StructuredRankOneFamily.lean#L186) | 对角惯性公式与上述原问题域连续族结论的合取 |

原文完整秩一定理把精确惯性、核、零度结论与书面的秩与零度推论合并。一般连通域连续族定理比所钉有限删点声明更广；正分支的对角元非负由书面半正定分类推出，并未列在 `continuous_family` 的结论中。公开道路连通声明仍假设有限删点，尽管其证明调用可数余集定理。可数删点、二维反例、块移除、系数变化与球面结果的完整书面证明在前章。

原论文验证附件报告精确有理数的有限实例检查。它们用于展示恒等式，不替代全参数书面证明或所钉声明。这里的覆盖说明不会提升论文另有的公开验证状态。

## 现有形式化贡献请求

以下为与原文结果关联的十个规范请求。贡献应复用上面的精确声明：秩推论无须重建惯性或核证明，半正定分类由惯性计数推出。有限删点的原问题结果已有对应声明，没有另设新请求。

| 原文定位 | 余下数学范围 | 规范请求 |
| --- | --- | --- |
| 定理 1 | 秩推论与完整合取 | [#169](https://github.com/the-omega-institute/trureturing-requests/issues/169) |
| 推论 2 | 两个半正定分支及对角分类 | [#170](https://github.com/the-omega-institute/trureturing-requests/issues/170) |
| 推论 3 | 非退化块移除 | [#171](https://github.com/the-omega-institute/trureturing-requests/issues/171) |
| 推论 4 | 全实数系数恒等式 | [#172](https://github.com/the-omega-institute/trureturing-requests/issues/172) |
| 定理 5 | 一般连通域及完整正分支 | [#173](https://github.com/the-omega-institute/trureturing-requests/issues/173) |
| 推论 7 | 可数删点推广 | [#174](https://github.com/the-omega-institute/trureturing-requests/issues/174) |
| 推论 8 | 二维见证与尖锐门槛 | [#175](https://github.com/the-omega-institute/trureturing-requests/issues/175) |
| 推论 9 | 分子下界与附条件驻点式 | [#176](https://github.com/the-omega-institute/trureturing-requests/issues/176) |
| 推论 10 | 已归属先前例子的下确界 | [#177](https://github.com/the-omega-institute/trureturing-requests/issues/177) |
| 定理 11 | 多项式矩、差值、下确界与不达到性 | [#178](https://github.com/the-omega-institute/trureturing-requests/issues/178) |

请求是补齐形式陈述的贡献入口，不是证明证书。具体贡献遵循上游[贡献说明](https://github.com/the-omega-institute/trureturing/blob/0f1f822c673c1903dc6b0a209a23dacebca2aa6c/CONTRIBUTING.md)，并关联已有请求。

## 数学边界

矩阵公式要求主元非零，允许矩阵奇异。连通族定理允许其余非负对角元取零。单纯形维数门槛针对删点后结论的统一成立性，不限制秩一矩阵恒等式。多项式构造否定普遍二坐标缩减，并算出该多项式不限维数的精确下确界；它不分类任意连续 $h$，也不确定源问题作者未明确写出的多项式。

```{=typst}
#pagebreak()
```
