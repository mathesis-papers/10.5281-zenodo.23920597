# 精确陈述与证明

矩阵结论把一个非零标量块置零；连续族结论再用连通性锁定负坐标。球面结论则用矩把不限维数的下界化成一元问题。下面完整展开 Ma 与 Zhang 的[第二版论文](https://doi.org/10.5281/zenodo.23920598)中的论证，证据链接保留原文结果编号。归属与 Lean 的精确范围集中列于[来源与覆盖](coverage.md)。

## 可能奇异的二次型中的非零主元

实对称 $n\times n$ 矩阵 $B$ 的惯性 $\operatorname{In}(B)=(n_+(B),n_-(B),n_0(B))$ 依次计数正、负、零特征值，含重数。$B\succeq0$ 表示半正定。本节固定

$$
\begin{gathered}
\Delta=x^{\mathsf T}Ax\ne0\\ w=Ax\\ M=A-\frac{ww^{\mathsf T}}{\Delta}.
\end{gathered}
$$

这个假设蕴含 $x\ne0$ 与 $w\ne0$，却不要求 $A$ 可逆。$\Delta<0$ 时公式实际加上一个半正定秩一矩阵；“带符号降秩”包含两种符号。

::: {.theorem #lean-inertia title="两种符号的惯性公式" lean="D5/S3/QuadraticForms/StructuredRankOneInertia.inertia_downdate" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s1"}
设 $A$ 是任意实对称 $n\times n$ 矩阵，$x\in\mathbb R^n$ 且 $\Delta\ne0$。则

$$
\begin{gathered}
\Delta>0:\quad\operatorname{In}(M)=\\
(n_+(A)-1,n_-(A),n_0(A)+1),\\
\Delta<0:\quad\operatorname{In}(M)=\\
(n_+(A),n_-(A)-1,n_0(A)+1).
\end{gathered}
$$
:::

::: {.theorem #thm-s1 title="秩一改动的惯性、核与秩" status="written-proof" proof="pf-s1" doi="10.5281/zenodo.23920598" source="Theorem 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/169" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s1"}
设 $A$ 是任意实对称 $n\times n$ 矩阵，$x\in\mathbb R^n$ 且 $\Delta\ne0$。则

$$
\begin{gathered}
\Delta>0:\quad\operatorname{In}(M)=\\
(n_+(A)-1,n_-(A),n_0(A)+1),\\
\Delta<0:\quad\operatorname{In}(M)=\\
(n_+(A),n_-(A)-1,n_0(A)+1).
\end{gathered}
$$

并且

$$
\begin{gathered}
\ker M=\ker A\oplus\operatorname{span}\{x\}\\
\operatorname{rank}M=\operatorname{rank}A-1.
\end{gathered}
$$

这里直和描述被矩阵消去的向量，不是所有二次量为零的向量。
:::

::: {.proof #pf-s1}
令 $H=\ker(w^{\mathsf T})$。任意 $v\in\mathbb R^n$ 可写成

$$
v=\left(v-\frac{w^{\mathsf T}v}{\Delta}x\right)+\frac{w^{\mathsf T}v}{\Delta}x.
$$

因 $w^{\mathsf T}x=\Delta$，第一项属于 $H$。若 $tx\in H$，则 $t\Delta=0$，故 $t=0$。于是 $\mathbb R^n=H\oplus\operatorname{span}\{x\}$。取 $H$ 的基矩阵 $Z$ 并令 $P=[Z\ \ x]$；即使 $A$ 奇异，$P$ 仍可逆。对称性给出 $Z^{\mathsf T}Ax=Z^{\mathsf T}w=0$，又有 $Mx=0$，而秩一项在 $H$ 上为零。因此令 $C=Z^{\mathsf T}AZ$，便得

$$
\begin{gathered}
P^{\mathsf T}AP=\begin{pmatrix}C&0\\0&\Delta\end{pmatrix}\\
P^{\mathsf T}MP=\begin{pmatrix}C&0\\0&0\end{pmatrix}.
\end{gathered}
$$

为说明惯性定律适用于奇异矩阵，用谱定理把 $n_+(B)$ 识别为使 $v^{\mathsf T}Bv$ 正定的子空间的最大维数。正特征空间达到这个维数；更大维子空间必与非正特征空间有非零交点，所以不可能正定。可逆变量代换保持该最大维数。对 $-B$ 重复论证得到 $n_-$ 不变，再由 $n_0=n-n_+-n_-$ 得零计数不变。这就证明了所需的 Sylvester 惯性定律，无须非奇异假设。将它应用于上述分块，利用直和的可加性即得两种公式；被减一的计数必至少为一。

若 $Av=0$，对称性给 $w^{\mathsf T}v=x^{\mathsf T}Av=0$，故 $Mv=0$。反之 $Mv=0$ 蕴含

$$
A(v-tx)=0,\qquad t=\frac{w^{\mathsf T}v}{\Delta}.
$$

配合 $Mx=0$，这证明核等于所述和。若 $tx\in\ker A$，则 $0=x^{\mathsf T}A(tx)=t\Delta$，故交集为零。因此核维数为 $\dim\ker A+1$，再由秩与零度定理得到秩公式。$n=1$ 时 $C$ 为空块，论证仍成立；$\Delta=0$ 时定义中的商无意义，故必须排除。

这是原文定理 1 的书面证明。超平面机制来自 Lucid 的问题，user1551 更早的惯性证明见[来源章](coverage.md)的归属说明。
:::

::: {.theorem #lean-kernel title="精确核分解" lean="D5/S3/QuadraticForms/StructuredRankOneInertia.kernel_split" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s1"}
在相同假设下，$\ker M=\ker A+\operatorname{span}\{x\}$ 且 $\ker A\cap\operatorname{span}\{x\}=\{0\}$。
:::

::: {.theorem #lean-nullity title="精确零度增加" lean="D5/S3/QuadraticForms/StructuredRankOneInertia.nullity_downdate" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s1"}
在相同假设下，$\dim\ker M=\dim\ker A+1$。
:::

上面两条子陈述分别对应核与零度的精确声明；完整定理中的秩结论由书面秩与零度推论得到。

::: {.corollary #thm-s2 title="半正定分类" status="written-proof" proof="pf-s2" doi="10.5281/zenodo.23920598" source="Corollary 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/170" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s2"}
在[秩一定理](#thm-s1)的假设下，

$$
M\succeq0\quad\Longleftrightarrow\quad
\begin{cases}A\succeq0,&\Delta>0,\\n_-(A)=1,&\Delta<0.\end{cases}
$$

当 $A=\operatorname{diag}(d_i)$ 且主元为负时，这等价于恰有一个 $d_j<0$，其余 $d_i\ge0$；其余项允许为零。
:::

::: {.proof #pf-s2}
实对称矩阵半正定当且仅当负惯性指数为零。代入所钉的 `inertia_downdate` 声明中的负计数即可。对角矩阵的特征值就是对角元。这证明原文推论 2。
:::

::: {.corollary #thm-s3 title="移除非退化块" status="written-proof" proof="pf-s3" doi="10.5281/zenodo.23920598" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/171" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s3"}
设 $A$ 实对称，$X\in\mathbb R^{n\times k}$，且 $G=X^{\mathsf T}AX$ 可逆。令 $N=A-AXG^{-1}X^{\mathsf T}A$，则

$$
\begin{aligned}
n_+(N)&=n_+(A)-n_+(G),\\
n_-(N)&=n_-(A)-n_-(G),\\
n_0(N)&=n_0(A)+k.
\end{aligned}
$$

$$
\begin{gathered}
\ker N=\ker A\oplus\operatorname{im}X\\
\operatorname{rank}N=\operatorname{rank}A-k.
\end{gathered}
$$
:::

::: {.proof #pf-s3}
若 $Xc=0$，则 $Gc=0$，故 $c=0$，所以 $X$ 的秩为 $k$。令 $H=\ker(X^{\mathsf T}A)$。任意 $v$ 有分解

$$
v=(v-XG^{-1}X^{\mathsf T}Av)+XG^{-1}X^{\mathsf T}Av.
$$

第一项属于 $H$。若 $Xc\in H$，则 $Gc=0$，故 $H+\operatorname{im}X$ 是直和。在适配基 $P=[Z\ X]$ 中，

$$
\begin{gathered}
P^{\mathsf T}AP=\operatorname{diag}(Z^{\mathsf T}AZ,G)\\
P^{\mathsf T}NP=\operatorname{diag}(Z^{\mathsf T}AZ,0_k).
\end{gathered}
$$

这里用到 $Z^{\mathsf T}AX=0$ 与 $NX=0$。Sylvester 惯性定律给出惯性公式。若 $Nv=0$，则 $A(v-XG^{-1}X^{\mathsf T}Av)=0$；反之 $N$ 消去 $\ker A$ 与 $\operatorname{im}X$。由于 $AXc=0$ 蕴含 $Gc=0$，两者交集为零。秩与零度定理完成原文推论 3。$k=0$ 按空块约定给出 $N=A$。
:::

::: {.corollary #thm-s4 title="改变系数" status="written-proof" proof="pf-s4" doi="10.5281/zenodo.23920598" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/172" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s4"}
在[秩一假设](#thm-s1)下，令 $t\in\mathbb R$，$M_t=A-tww^{\mathsf T}/\Delta$。逐分量有

$$
\operatorname{In}(M_t)=\operatorname{In}(A)-\operatorname{In}([\Delta])+\operatorname{In}([(1-t)\Delta]).
$$

因此 $t<1$ 时惯性不变；$t=1$ 为秩一定理；$t>1$ 将一个符号翻转，零度不变。
:::

::: {.proof #pf-s4}
[秩一证明](#pf-s1)的同一个 $P$ 给出 $P^{\mathsf T}M_tP=\operatorname{diag}(C,(1-t)\Delta)$。减去 $[\Delta]$ 的贡献，再加 $[(1-t)\Delta]$ 的贡献即可。$t<1$ 时符号与 $\Delta$ 相同；$t=1$ 时为零；$t>1$ 时非零且符号相反。这证明原文推论 4。
:::

## 连续族与删点

给定连续映射 $d,x:Y\to\mathbb R^n$，定义

$$
\begin{gathered}
D(y)=\operatorname{diag}(d_1(y),\ldots,d_n(y))\\
\Delta(y)=\sum_i d_i(y)x_i(y)^2,
\end{gathered}
$$

$$
M(y)=D(y)-\frac{D(y)x(y)x(y)^{\mathsf T}D(y)}{\Delta(y)}.
$$

::: {.theorem #thm-s5 title="连通域上的固定坐标" status="written-proof" proof="pf-s5" doi="10.5281/zenodo.23920598" source="Theorem 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/173" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s5"}
设 $Y$ 为非空连通拓扑空间，$d,x:Y\to\mathbb R^n$ 连续，并且每个 $y$ 都有 $\Delta(y)\ne0$ 与 $M(y)\succeq0$。则以下两种情形恰有一种成立：

1. 所有 $y$ 均有 $\Delta(y)>0$，且所有 $i$ 均有 $d_i(y)\ge0$。
2. 所有 $y$ 均有 $\Delta(y)<0$，且存在唯一指标 $j$，使所有 $y$ 均有 $d_j(y)<0$；其余 $i\ne j$ 在所有 $y$ 上均有 $d_i(y)\ge0$。
:::

::: {.proof #pf-s5}
连续函数 $\Delta$ 不为零，其正、负值的原像是两个不交开集，覆盖 $Y$。由连通性与非空性，恰有一个原像为空，所以符号固定。正分支逐点应用[半正定分类](#thm-s2)。负分支由同一分类知每点恰有一个负对角元。令 $U_i=\{y:d_i(y)<0\}$，则各集合开、彼此不交且覆盖 $Y$；每个 $U_i$ 的补集是其余集合之并，所以它也闭。至少一个 $U_j$ 非空，而连通空间中的非空开闭子集只能是全空间，故 $U_j=Y$，其余集合为空。$Y$ 非空还保证 $j$ 唯一。其余对角元允许为零。这证明原文定理 5。
:::

::: {.theorem #lean-path title="有限删点后的道路连通性" lean="D5/S3/QuadraticForms/StructuredRankOneFamily.punctured_simplex_pathConnected" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s6"}
设 $n\ge3$，$X$ 同胚于开 $(n-1)$ 维单纯形，$F\subset X$ 有限。则 $X\setminus F$ 非空且道路连通。
:::

::: {.theorem #thm-s6 title="有限删点连续族定理" lean="D5/S3/QuadraticForms/StructuredRankOneFamily.continuous_family" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s6"}
在所钉的 `punctured_simplex_pathConnected` 声明的域假设下，设 $d,x:X\setminus F\to\mathbb R^n$ 连续。若处处 $\Delta\ne0$ 且 $M\succeq0$，则 $X\setminus F$ 非空，并且或者处处 $\Delta>0$，或者处处 $\Delta<0$ 且存在唯一指标 $j$，使 $d_j$ 处处为负而其余 $d_i$ 处处非负。
:::


原文推论 6 将[连通域定理](#thm-s5)的全部结论用于有限删点域，包含正分支的 $d_i\ge0$。刚才的精确连续族声明给出符号与负分支结论；附加的正分支分类由[书面半正定推论](#thm-s2)得到。

直接证明域性质如下。把域及删点集转移到

$$
S=\{u\in\mathbb R^{n-1}:u_i>0,\ \sum_i u_i<1\}
$$

及其有限子集 $B$。给定 $p,q\in S\setminus B$，考虑所有过 $p,b$ 或 $q,b$ 的直线，其中 $b\in B$。在包含于 $S$ 的二维仿射平面内取一个小圆。每条禁用直线与圆最多交于两点，所以可选圆上一点 $z$ 避开全部禁线。凸性保证 $[p,z]$ 和 $[z,q]$ 在 $S$ 内；若线段碰到删点，$z$ 就在某条禁线上，矛盾。两段构成所需道路。小圆也说明删去有限集后非空。转回原空间，再用[连通域定理](#thm-s5)即可。

::: {.corollary #thm-s7 title="可数个删点" status="written-proof" proof="pf-s7" doi="10.5281/zenodo.23920598" source="Corollary 7" request="https://github.com/the-omega-institute/trureturing-requests/issues/174" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s7"}
有限删点的完整结论对可数 $F$ 仍成立：$n\ge3$ 时，若 $X$ 同胚于开 $(n-1)$ 维单纯形，则 $X\setminus F$ 非空且道路连通；在该域上满足[连续族定理](#thm-s5)假设的函数具有它的两种择一结论。
:::

::: {.proof #pf-s7}
上面的两段道路构造现在有可数条禁线。它们与小圆的交点至多可数，而圆不可数，因此仍能选到合适的 $z$。开单纯形含有这个圆，故可数个点无法把它删空。域于是非空且道路连通，从而连通，再应用[连续族定理](#thm-s5)。这证明原文推论 7。所钉道路连通声明要求删点集有限；这里的可数推广由书面论证给出。
:::

::: {.corollary #thm-s8 title="尖锐维数门槛" status="written-proof" proof="pf-s8" doi="10.5281/zenodo.23920598" source="Corollary 8" request="https://github.com/the-omega-institute/trureturing-requests/issues/175" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s8"}
要求有限删点连续族结论对所有有限删点集统一成立时，$n\ge3$ 的门槛是尖锐的。$n=2$ 时删去一点，就可能让负坐标在两个分支之间换位。
:::

::: {.proof #pf-s8}
取 $X=(-1,1)$、$F=\{0\}$。$y<0$ 时令 $D=\operatorname{diag}(-1,1)$、$x=(1,0)^{\mathsf T}$；$y>0$ 时令 $D=\operatorname{diag}(1,-1)$、$x=(0,1)^{\mathsf T}$。映射在两个开分支上各为常值，因此在 $X\setminus F$ 上连续。两边均有 $\Delta=-1$，得到的 $M$ 分别为 $\operatorname{diag}(0,1)$ 与 $\operatorname{diag}(1,0)$，均半正定；负坐标却分别是第一与第二个。区间同胚于开一维单纯形，故满足 $n=2$ 的域描述，反驳结论的统一推广。它不与连通域上的定理矛盾。这证明原文推论 8。
:::

## 球面比值：正则性与先前例子

关联问题设连续函数 $h:(0,1]\to\mathbb R$ 满足 $h(t)\ge h(1)t>0$（$0<t\le1$）。对正坐标单位向量 $x\in\mathbb R^d$，令

$$
\begin{gathered}
N=\sum_i x_i h(x_i)\\ D=\sqrt{\sum_i h(x_i)^2}\\ R_h(x)=N/D.
\end{gathered}
$$

这里 $D>0$。“活跃坐标”约定是省略零坐标，因为一般 $h$ 没有指定零点取值。下文多项式满足 $h(0)=0$，故添加零坐标不改变比值。

::: {.corollary #thm-s9 title="分子下界与驻点条件" status="written-proof" proof="pf-s9" doi="10.5281/zenodo.23920598" source="Corollary 9" request="https://github.com/the-omega-institute/trureturing-requests/issues/176" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s9"}
在上述假设下，$N\ge h(1)$。若 $h$ 在正坐标单位向量的各活跃坐标附近可微，且所有 $x_i<1$，则内点驻点满足：存在实数 $\lambda$，使每个 $i$ 均有

$$
\begin{gathered}
D^2[h(x_i)+x_i h'(x_i)]-N h(x_i)h'(x_i)\\
=2\lambda x_iD^3.
\end{gathered}
$$

仅有连续性不足以支持这些导数。
:::

::: {.proof #pf-s9}
将 $h(x_i)\ge h(1)x_i$ 乘以 $x_i>0$ 后求和，得 $N\ge h(1)\sum_i x_i^2=h(1)$；这个逐项论证已在 Lucid 的关联问题中。在可微假设下，$\partial_iN=h(x_i)+x_i h'(x_i)$，$\partial_iD=h(x_i)h'(x_i)/D$。商法则给出 $\partial_i(N/D)$ 等于所示左边除以 $D^3$。球面约束的梯度为 $2x\ne0$，故 Lagrange 乘子法给出方程。$0<x_i<1$ 保证每个活跃坐标都能取通常的邻域。这证明原文推论 9。
:::

::: {.corollary #thm-s10 title="先前例子的下确界" status="written-proof" proof="pf-s10" doi="10.5281/zenodo.23920598" source="Corollary 10" request="https://github.com/the-omega-institute/trureturing-requests/issues/177" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s10"}
按活跃坐标约定，$h=1$ 在固定维数 $d$ 的下确界为 $1/\sqrt d$，不限有限维数时为零；最多两个活跃坐标时下确界为 $1/\sqrt2$。对 $h(t)=1/t$，二维中的下确界已经为零。
:::

::: {.proof #pf-s10}
对 $h=1$，有 $R_h=(\sum_i x_i)/\sqrt d\ge1/\sqrt d$，因为 $(\sum_i x_i)^2=1+2\sum_{i<j}x_ix_j\ge1$。$d>1$ 时取趋于 $(1,0,\ldots,0)$ 的正坐标单位向量逼近下界；$d=1$ 时达到下界。再令 $d\to\infty$ 得零，而在 $d=1,2$ 中取较小的下确界便是 $1/\sqrt2$。对 $h(t)=1/t$、$d=2$，令 $p=x_1^2\in(0,1)$，则 $N=2$、$D^2=1/p+1/(1-p)$，所以 $R_h^2=4p(1-p)\to0$（$p\to0$）。比值为正，故这些极限下界确为下确界。两函数均满足源问题的不等式。$h=1$ 和 $h=1/t$ 分别归于 daw 与 Exodd，见[来源章](coverage.md)。这证明原文推论 10。
:::

## 多项式：矩恒等式与分散尾部

::: {.theorem #thm-s11 title="尖锐多项式球面界" status="written-proof" proof="pf-s11" doi="10.5281/zenodo.23920598" source="Theorem 11" request="https://github.com/the-omega-institute/trureturing-requests/issues/178" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s11"}
令 $h(t)=(3t-t^3)/2$（$0\le t\le1$）。它是奇多项式的限制，严格递增，满足 $h(1)=1$，且 $h(t)/t=(3-t^2)/2$ 在 $(0,1]$ 严格递减。对任意有限维的非负坐标单位向量，

$$
\inf R_h(x)^2=\frac{16(17-9\sqrt3)}{23}.
$$

没有有限维向量达到这个下确界。若限制最多两个非零坐标，则可达到的最小值为

$$
\min R_h(x)^2=\frac{80}{81}.
$$

平方坐标 $(4/5,1/10,1/10)$ 给出 $13689/13885<80/81$。取一个平方坐标 $a_*=6-3\sqrt3$，另取 $m$ 个平方坐标 $(1-a_*)/m$，在 $m\to\infty$ 时逼近不限维下确界。
:::

::: {.proof #pf-s11}
**多项式与矩恒等式。** $h'(t)=3(1-t^2)/2>0$（$0\le t<1$），在任意非退化子区间积分便证明严格递增，也包括端点 $1$。$h(t)/t$ 的公式直接给出严格递减与 $h(t)\ge t=h(1)t$。令 $p_i=x_i^2$、$s_2=\sum_i p_i^2$、$s_3=\sum_i p_i^3$，则 $p_i\ge0$ 且 $\sum_i p_i=1$。展开有

$$
\begin{gathered}
\sum_i x_i h(x_i)=\tfrac12(3-s_2)\\
\sum_i h(x_i)^2=\tfrac14(9-6s_2+s_3),
\end{gathered}
$$

因此得到矩恒等式

$$
R_h(x)^2=\frac{(3-s_2)^2}{9-6s_2+s_3}.
$$

因 $s_2\le1$、$s_3\ge0$，分母至少为 $3$，故为正。

**精确二坐标差值。** 将两个平方坐标写成 $p,1-p$，端点表示只有一个活跃坐标。令 $u=p(1-p)\in[0,1/4]$，则 $s_2=1-2u$、$s_3=1-3u$，从而

$$
\begin{gathered}
R_h(x)^2=\frac{(1+u)^2}{1+9u/4}\\
R_h(x)^2-\frac{80}{81}=\frac{(9u-1)^2}{81(1+9u/4)}.
\end{gathered}
$$

等号恰在 $u=1/9$ 成立，对应可行值 $p=(3+\sqrt5)/6$ 或 $(3-\sqrt5)/6$，两坐标均正。端点的比值平方则为 $1$。

**三坐标已经改进。** 对 $(p_1,p_2,p_3)=(4/5,1/10,1/10)$，有 $s_2=33/50$、$s_3=257/500$。代入得 $R_h^2=13689/13885$，精确差值为

$$
\frac{80}{81}-\frac{13689}{13885}=\frac{1991}{81\cdot13885}>0.
$$

所以即使满足所述多项式正则条件，普遍的二坐标缩减仍不成立。

**与维数无关的下界。** 令 $a=\sqrt{s_2}\in(0,1]$。因 $p_i^2\le s_2$，每项 $p_i\le a$，于是 $s_3\le a s_2=a^3$。利用分母为正，

$$
R_h(x)^2\ge f(a):=\frac{(3-a^2)^2}{9-6a^2+a^3}.
$$

在 $[0,1]$ 上分母至少为 $3$。求导得

$$
f'(a)=-\frac{a^2(3-a^2)(a^2-12a+9)}{(9-6a^2+a^3)^2}.
$$

末尾二次式的根为 $6\pm3\sqrt3$，只有 $a_*=6-3\sqrt3$ 属于 $(0,1)$。其余所示因子在内部均正，故 $f$ 在 $a_*$ 前递减、之后递增。唯一最小值为 $f(a_*)=16(17-9\sqrt3)/23$。

**分散尾部证明尖锐性。** 对每个正整数 $m$，取平方坐标 $a_*,(1-a_*)/m,\ldots,(1-a_*)/m$，尾部共 $m$ 项。各项正、总和为一，其矩为

$$
\begin{gathered}
s_2=a_*^2+\frac{(1-a_*)^2}{m}\\
s_3=a_*^3+\frac{(1-a_*)^3}{m^2}.
\end{gathered}
$$

它们分别趋于 $a_*^2,a_*^3$。极限分母为正，故有理式的连续性保证比值平方趋于 $f(a_*)$。这证明在维数逐渐增加的有限向量中下界尖锐。

**不达到性。** 达到下界必须在 $s_3\le a s_2$ 取等号。非负项 $p_i^2(a-p_i)$ 必须全部为零，所以每个正 $p_i=a$。因此 $s_2=a\sum_i p_i=a$，而定义又有 $s_2=a^2$。因 $a>0$，得 $a=1$，即只有一个活跃坐标，且 $R_h^2=1$。但 $f(a_*)<1$（例如 $f(1/2)<1$，最小值更不大于它），故有限向量不能达到较小的下确界。这完成原文定理 11 的证明。
:::

## 形式声明覆盖什么

| 数学陈述 | 精确的所钉 Lean 声明 | 仍由书面论证给出的范围 |
| --- | --- | --- |
| 任意实对称 $A$ 的两种惯性三元组 | `StructuredRankOneInertia.inertia_downdate` | 完整定理还包含秩 |
| 核直和与零度增加 | 同模块的 `kernel_split`、`nullity_downdate` | 秩与零度的推论 |
| 有限删点道路连通性 | `StructuredRankOneFamily.punctured_simplex_pathConnected` | 可数删点及二维边界 |
| 有限删点的符号与固定负指标 | `StructuredRankOneFamily.continuous_family` | 一般连通空间与正分支的对角元分类 |
| 块移除、系数变化、球面结果 | 两个已检查的所钉模块中没有匹配声明 | 上面的完整书面证明 |

表中名称省略命名空间 `D5.S3.QuadraticForms`。[覆盖章](coverage.md)给出完整所钉版本的声明链接及现有贡献请求。一般 $h$ 的分类，以及源问题对某个未明确写出的奇多项式的数值观察，并未在此解决。
