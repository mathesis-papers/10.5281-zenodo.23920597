# Precise statements and proofs

The matrix result replaces one nonzero scalar block by zero; the family result then uses connectedness to keep the negative coordinate fixed. The sphere result uses moments to reduce an arbitrary-dimensional lower bound to one variable. We give the complete arguments from Ma and Zhang's [version-2 paper](https://doi.org/10.5281/zenodo.23920598), with the original result numbers in the evidence links. The attribution and exact Lean scope are collected in [Sources and coverage](coverage.md).

## A nonzero pivot in a possibly singular form

For a real symmetric $n\times n$ matrix $B$, let $\operatorname{In}(B)=(n_+(B),n_-(B),n_0(B))$ count positive, negative and zero eigenvalues with multiplicity. Write $B\succeq0$ for positive semidefiniteness. For the rest of this section set

$$
\begin{gathered}
\Delta=x^{\mathsf T}Ax\ne0\\ w=Ax\\ M=A-\frac{ww^{\mathsf T}}{\Delta}.
\end{gathered}
$$

The assumption implies $x\ne0$ and $w\ne0$. It does not require $A$ to be invertible. When $\Delta<0$ the formula adds a positive-semidefinite rank-one matrix; “signed downdate” covers both signs.

::: {.theorem #lean-inertia title="Both signed inertia formulas" lean="D5/S3/QuadraticForms/StructuredRankOneInertia.inertia_downdate" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s1"}
Let $A$ be any real symmetric $n\times n$ matrix and $x\in\mathbb R^n$ with $\Delta\ne0$. Then

$$
\begin{gathered}
\Delta>0:\quad\operatorname{In}(M)=\\
(n_+(A)-1,n_-(A),n_0(A)+1),\\
\Delta<0:\quad\operatorname{In}(M)=\\
(n_+(A),n_-(A)-1,n_0(A)+1).
\end{gathered}
$$
:::

::: {.theorem #thm-s1 title="Rank-one inertia, kernel and rank" status="written-proof" proof="pf-s1" doi="10.5281/zenodo.23920598" source="Theorem 1" request="https://github.com/the-omega-institute/trureturing-requests/issues/169" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s1"}
Let $A$ be any real symmetric $n\times n$ matrix and $x\in\mathbb R^n$ with $\Delta\ne0$. Then

$$
\begin{gathered}
\Delta>0:\quad\operatorname{In}(M)=\\
(n_+(A)-1,n_-(A),n_0(A)+1),\\
\Delta<0:\quad\operatorname{In}(M)=\\
(n_+(A),n_-(A)-1,n_0(A)+1).
\end{gathered}
$$

Moreover,

$$
\begin{gathered}
\ker M=\ker A\oplus\operatorname{span}\{x\}\\
\operatorname{rank}M=\operatorname{rank}A-1.
\end{gathered}
$$

The direct sum describes vectors annihilated by the matrix, not all vectors with zero quadratic value.
:::

::: {.proof #pf-s1}
Put $H=\ker(w^{\mathsf T})$. Every $v\in\mathbb R^n$ decomposes as

$$
v=\left(v-\frac{w^{\mathsf T}v}{\Delta}x\right)+\frac{w^{\mathsf T}v}{\Delta}x.
$$

The first summand lies in $H$ because $w^{\mathsf T}x=\Delta$. If $tx\in H$, then $t\Delta=0$, so $t=0$. Thus $\mathbb R^n=H\oplus\operatorname{span}\{x\}$. Choose a basis matrix $Z$ of $H$ and put $P=[Z\ \ x]$. This matrix is invertible even when $A$ is singular. Symmetry gives $Z^{\mathsf T}Ax=Z^{\mathsf T}w=0$. Also $Mx=0$ and the rank-one term vanishes on $H$. Therefore, with $C=Z^{\mathsf T}AZ$,

$$
\begin{gathered}
P^{\mathsf T}AP=\begin{pmatrix}C&0\\0&\Delta\end{pmatrix}\\
P^{\mathsf T}MP=\begin{pmatrix}C&0\\0&0\end{pmatrix}.
\end{gathered}
$$

To justify inertia invariance for singular matrices, the spectral theorem identifies $n_+(B)$ with the largest dimension of a subspace on which $v^{\mathsf T}Bv$ is positive definite. The positive eigenspace attains that dimension. Any subspace of larger dimension intersects the nonpositive eigenspace nontrivially, so cannot be positive definite. An invertible substitution preserves this maximal dimension. Apply the same reasoning to $-B$ for $n_-$; then $n_0=n-n_+-n_-$. This proves the required Sylvester law without a nonsingularity hypothesis. Additivity on the displayed blocks yields the two inertia formulas. In particular the count from which one is subtracted is at least one.

If $Av=0$, symmetry gives $w^{\mathsf T}v=x^{\mathsf T}Av=0$, hence $Mv=0$. Conversely, $Mv=0$ implies

$$
A(v-tx)=0,\qquad t=\frac{w^{\mathsf T}v}{\Delta}.
$$

Together with $Mx=0$, this proves the sum of kernels. If $tx\in\ker A$, then $0=x^{\mathsf T}A(tx)=t\Delta$, so the intersection is zero. Its dimension is therefore $\dim\ker A+1$, and rank-nullity gives the rank formula. For $n=1$ the block $C$ is empty and the same proof applies. The case $\Delta=0$ is excluded: the defining quotient is then undefined.

This is the written proof of manuscript Theorem 1; its hyperplane mechanism is proposed in Lucid's question, and user1551's earlier inertia proof is credited in [the sources](coverage.md).
:::

::: {.theorem #lean-kernel title="Exact kernel split" lean="D5/S3/QuadraticForms/StructuredRankOneInertia.kernel_split" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s1"}
Under the same hypotheses, $\ker M=\ker A+\operatorname{span}\{x\}$ and $\ker A\cap\operatorname{span}\{x\}=\{0\}$.
:::

::: {.theorem #lean-nullity title="Exact nullity increase" lean="D5/S3/QuadraticForms/StructuredRankOneInertia.nullity_downdate" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s1"}
Under the same hypotheses, $\dim\ker M=\dim\ker A+1$.
:::

The preceding two substatements isolate exactly the kernel and nullity declarations; the rank conclusion in the full theorem follows by the written rank-nullity deduction.

::: {.corollary #thm-s2 title="Positive-semidefinite classification" status="written-proof" proof="pf-s2" doi="10.5281/zenodo.23920598" source="Corollary 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/170" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s2"}
Under the hypotheses of [the rank-one theorem](#thm-s1),

$$
M\succeq0\quad\Longleftrightarrow\quad
\begin{cases}A\succeq0,&\Delta>0,\\n_-(A)=1,&\Delta<0.\end{cases}
$$

For diagonal $A=\operatorname{diag}(d_i)$ in the negative branch, this is equivalent to exactly one $d_j<0$ and all $d_i\ge0$ for $i\ne j$. Zeros among the other entries are allowed.
:::

::: {.proof #pf-s2}
A real symmetric matrix is positive semidefinite exactly when its negative index is zero. Insert the negative counts of the pinned `inertia_downdate` declaration. A diagonal matrix has its entries as eigenvalues. This proves manuscript Corollary 2.
:::

::: {.corollary #thm-s3 title="Removal of a nondegenerate block" status="written-proof" proof="pf-s3" doi="10.5281/zenodo.23920598" source="Corollary 3" request="https://github.com/the-omega-institute/trureturing-requests/issues/171" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s3"}
Let $A$ be real symmetric, $X\in\mathbb R^{n\times k}$, and $G=X^{\mathsf T}AX$ invertible. Set $N=A-AXG^{-1}X^{\mathsf T}A$. Then

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
If $Xc=0$, then $Gc=0$, so $c=0$; thus $X$ has rank $k$. Let $H=\ker(X^{\mathsf T}A)$. Every $v$ has the decomposition

$$
v=(v-XG^{-1}X^{\mathsf T}Av)+XG^{-1}X^{\mathsf T}Av.
$$

The first term lies in $H$. If $Xc\in H$, then $Gc=0$, so the sum $H+\operatorname{im}X$ is direct. In a basis $P=[Z\ X]$ adapted to it,

$$
\begin{gathered}
P^{\mathsf T}AP=\operatorname{diag}(Z^{\mathsf T}AZ,G)\\
P^{\mathsf T}NP=\operatorname{diag}(Z^{\mathsf T}AZ,0_k).
\end{gathered}
$$

Indeed, $Z^{\mathsf T}AX=0$ and $NX=0$. Sylvester's law gives the inertia. If $Nv=0$, then $A(v-XG^{-1}X^{\mathsf T}Av)=0$. Conversely $N$ kills both $\ker A$ and $\operatorname{im}X$. Their intersection is zero because $AXc=0$ implies $Gc=0$. Rank-nullity finishes manuscript Corollary 3. The case $k=0$, with the usual empty-block convention, gives $N=A$.
:::

::: {.corollary #thm-s4 title="Changing the coefficient" status="written-proof" proof="pf-s4" doi="10.5281/zenodo.23920598" source="Corollary 4" request="https://github.com/the-omega-institute/trureturing-requests/issues/172" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s4"}
Under [the rank-one hypotheses](#thm-s1), let $t\in\mathbb R$ and $M_t=A-tww^{\mathsf T}/\Delta$. Componentwise,

$$
\operatorname{In}(M_t)=\operatorname{In}(A)-\operatorname{In}([\Delta])+\operatorname{In}([(1-t)\Delta]).
$$

Thus $t<1$ preserves inertia; $t=1$ gives the rank-one theorem; $t>1$ replaces one sign by its opposite and preserves nullity.
:::

::: {.proof #pf-s4}
The same matrix $P$ used in [the rank-one proof](#pf-s1) gives $P^{\mathsf T}M_tP=\operatorname{diag}(C,(1-t)\Delta)$. Subtract the contribution of $[\Delta]$ and add that of $[(1-t)\Delta]$. For $t<1$ its sign agrees with $\Delta$; for $t=1$ it is zero; for $t>1$ it is nonzero with opposite sign. This proves manuscript Corollary 4.
:::

## Continuous families and punctures

For continuous maps $d,x:Y\to\mathbb R^n$, define

$$
\begin{gathered}
D(y)=\operatorname{diag}(d_1(y),\ldots,d_n(y))\\
\Delta(y)=\sum_i d_i(y)x_i(y)^2,
\end{gathered}
$$

$$
M(y)=D(y)-\frac{D(y)x(y)x(y)^{\mathsf T}D(y)}{\Delta(y)}.
$$

::: {.theorem #thm-s5 title="A fixed coordinate on a connected domain" status="written-proof" proof="pf-s5" doi="10.5281/zenodo.23920598" source="Theorem 5" request="https://github.com/the-omega-institute/trureturing-requests/issues/173" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s5"}
Let $Y$ be a nonempty connected topological space. Suppose $d,x:Y\to\mathbb R^n$ are continuous and $\Delta(y)\ne0$, $M(y)\succeq0$ for every $y$. Exactly one alternative holds:

1. For all $y$, $\Delta(y)>0$ and $d_i(y)\ge0$ for every $i$.
2. For all $y$, $\Delta(y)<0$, and there is a unique index $j$ such that $d_j(y)<0$ for every $y$, while $d_i(y)\ge0$ for every $i\ne j$ and every $y$.
:::

::: {.proof #pf-s5}
The continuous function $\Delta$ never vanishes. Its positive and negative inverse images are disjoint open sets covering $Y$. Connectedness and nonemptiness force one to be empty, so its sign is constant. In the positive case apply [the PSD classification](#thm-s2) pointwise. In the negative case that classification says exactly one diagonal entry is negative at each point. Put $U_i=\{y:d_i(y)<0\}$. These sets are open, pairwise disjoint and cover $Y$. The complement of each $U_i$ is the union of the others, so $U_i$ is closed as well. At least one is nonempty; a nonempty subset both open and closed in a connected space is the entire space. Thus one $U_j=Y$ and every other $U_i$ is empty. Nonemptiness also proves uniqueness of $j$. The other entries can vanish. This proves manuscript Theorem 5.
:::

::: {.theorem #lean-path title="Finite-puncture path connectedness" lean="D5/S3/QuadraticForms/StructuredRankOneFamily.punctured_simplex_pathConnected" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s6"}
Let $n\ge3$, let $X$ be homeomorphic to the open $(n-1)$-simplex, and let $F\subset X$ be finite. Then $X\setminus F$ is nonempty and path connected.
:::

::: {.theorem #thm-s6 title="Finite-puncture family theorem" lean="D5/S3/QuadraticForms/StructuredRankOneFamily.continuous_family" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s6"}
Under the domain hypotheses of the pinned `punctured_simplex_pathConnected` declaration, let $d,x:X\setminus F\to\mathbb R^n$ be continuous. If $\Delta\ne0$ and $M\succeq0$ everywhere, then $X\setminus F$ is nonempty and either $\Delta>0$ everywhere, or $\Delta<0$ everywhere with a unique index $j$ such that $d_j<0$ everywhere and every other $d_i\ge0$ everywhere.
:::


Manuscript Corollary 6 applies the full connected-domain theorem [above](#thm-s5) to this finite-puncture domain, including $d_i\ge0$ in the positive branch. The exact family declaration just stated supplies the sign and negative-branch conclusion; the additional positive-branch classification follows from [the written PSD corollary](#thm-s2).

To see the domain property directly, transport it to

$$
S=\{u\in\mathbb R^{n-1}:u_i>0,\ \sum_i u_i<1\}
$$

with deleted set $B$. Given $p,q\in S\setminus B$, consider all lines through $p,b$ or $q,b$ with $b\in B$. Choose a small circle in a two-dimensional affine plane lying in $S$. Each forbidden line meets the circle in at most two points, so a point $z$ of the circle avoids all these lines. Convexity keeps $[p,z]$ and $[z,q]$ in $S$; if either segment met a deleted point, $z$ would lie on a forbidden line. These two segments give the path. The circle also shows that the complement of a finite set is nonempty. Transport back and apply [the connected-domain theorem](#thm-s5).

::: {.corollary #thm-s7 title="Countably many punctures" status="written-proof" proof="pf-s7" doi="10.5281/zenodo.23920598" source="Corollary 7" request="https://github.com/the-omega-institute/trureturing-requests/issues/174" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s7"}
The full finite-puncture conclusion remains true when $F$ is countable: for $n\ge3$, a space $X$ homeomorphic to an open $(n-1)$-simplex has nonempty path-connected $X\setminus F$, and the hypotheses of [the family theorem](#thm-s5) imply its two alternatives there.
:::

::: {.proof #pf-s7}
In the preceding two-segment construction there are now countably many forbidden lines. Their intersections with the small circle form a countable set, whereas the circle is uncountable. A permissible $z$ still exists. The open simplex itself contains that circle, so removing countably many points cannot empty it. Thus the domain is nonempty and path connected, hence connected, and [the family theorem](#thm-s5) applies. This is manuscript Corollary 7. The pinned path-connectedness declaration assumes a finite deleted set; this countable extension is the written argument here.
:::

::: {.corollary #thm-s8 title="Sharp dimension threshold" status="written-proof" proof="pf-s8" doi="10.5281/zenodo.23920598" source="Corollary 8" request="https://github.com/the-omega-institute/trureturing-requests/issues/175" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s8"}
The requirement $n\ge3$ is sharp for a finite-puncture family conclusion uniform over all finite deleted sets. In dimension $n=2$, deleting one point can allow the negative coordinate to switch between components.
:::

::: {.proof #pf-s8}
Let $X=(-1,1)$ and $F=\{0\}$. On $y<0$ set $D=\operatorname{diag}(-1,1)$ and $x=(1,0)^{\mathsf T}$; on $y>0$ set $D=\operatorname{diag}(1,-1)$ and $x=(0,1)^{\mathsf T}$. These maps are continuous on $X\setminus F$, since they are constant on its two open components. In both components $\Delta=-1$. The resulting $M$ is respectively $\operatorname{diag}(0,1)$ and $\operatorname{diag}(1,0)$, both positive semidefinite. But the negative coordinate is respectively the first and the second. The interval is homeomorphic to an open one-simplex, so this meets the domain description for $n=2$ and disproves a uniform extension of the conclusion. It does not contradict the theorem on a connected domain. This proves manuscript Corollary 8.
:::

## Sphere ratios: regularity and the earlier examples

The linked question takes continuous $h:(0,1]\to\mathbb R$ with $h(t)\ge h(1)t>0$ for $0<t\le1$. For a positive unit vector $x\in\mathbb R^d$, set

$$
\begin{gathered}
N=\sum_i x_i h(x_i)\\ D=\sqrt{\sum_i h(x_i)^2}\\ R_h(x)=N/D.
\end{gathered}
$$

Here $D>0$. “Active coordinates” means that zero coordinates are omitted, because a general $h$ has no specified value at zero. For the polynomial below $h(0)=0$, so adding zero coordinates leaves the ratio unchanged.

::: {.corollary #thm-s9 title="Numerator bound and stationarity" status="written-proof" proof="pf-s9" doi="10.5281/zenodo.23920598" source="Corollary 9" request="https://github.com/the-omega-institute/trureturing-requests/issues/176" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s9"}
Under these hypotheses, $N\ge h(1)$. If $h$ is differentiable near every active coordinate of a positive unit vector with $x_i<1$ for all $i$, an interior stationary point satisfies, for some real $\lambda$,

$$
\begin{gathered}
D^2[h(x_i)+x_i h'(x_i)]-N h(x_i)h'(x_i)\\
=2\lambda x_iD^3.
\end{gathered}
$$

for every $i$. Continuity alone does not justify the derivatives.
:::

::: {.proof #pf-s9}
Multiply $h(x_i)\ge h(1)x_i$ by $x_i>0$ and sum: $N\ge h(1)\sum_i x_i^2=h(1)$. This termwise argument is already in Lucid's linked question. Under the differentiability assumption, $\partial_iN=h(x_i)+x_i h'(x_i)$ and $\partial_iD=h(x_i)h'(x_i)/D$. Thus the quotient rule gives $\partial_i(N/D)$ as the left side of the displayed equation divided by $D^3$. The unit-sphere constraint has gradient $2x\ne0$, so the Lagrange multiplier rule yields the equation. The condition $0<x_i<1$ ensures an ordinary neighborhood of each active coordinate is available. This proves manuscript Corollary 9.
:::

::: {.corollary #thm-s10 title="Infima in the earlier examples" status="written-proof" proof="pf-s10" doi="10.5281/zenodo.23920598" source="Corollary 10" request="https://github.com/the-omega-institute/trureturing-requests/issues/177" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s10"}
With active coordinates, $h=1$ has fixed-dimension infimum $1/\sqrt d$ and all-finite-dimension infimum zero; at most two active coordinates give infimum $1/\sqrt2$. For $h(t)=1/t$, the infimum is already zero in dimension two.
:::

::: {.proof #pf-s10}
For $h=1$, $R_h=(\sum_i x_i)/\sqrt d\ge1/\sqrt d$, since $(\sum_i x_i)^2=1+2\sum_{i<j}x_ix_j\ge1$. For $d>1$, take positive unit vectors approaching $(1,0,\ldots,0)$ to approach this bound; for $d=1$ it is attained. Letting $d\to\infty$ gives zero, while taking the smaller infimum for $d=1,2$ gives $1/\sqrt2$. For $h(t)=1/t$ and $d=2$, write $p=x_1^2\in(0,1)$; then $N=2$, $D^2=1/p+1/(1-p)$, and $R_h^2=4p(1-p)\to0$ as $p\to0$. Ratios are positive, so these limiting lower bounds are the infima. Both functions meet the source inequality. The choices $h=1$ and $h=1/t$ are due to daw and Exodd respectively, as credited in [the sources](coverage.md). This proves manuscript Corollary 10.
:::

## The polynomial: a moment identity and a diffuse tail

::: {.theorem #thm-s11 title="A sharp polynomial sphere bound" status="written-proof" proof="pf-s11" doi="10.5281/zenodo.23920598" source="Theorem 11" request="https://github.com/the-omega-institute/trureturing-requests/issues/178" mathesis="collected:mathoverflow-513954-singular-diagonal-downdate-inertia:2:s11"}
Let $h(t)=(3t-t^3)/2$ on $[0,1]$. It is the restriction of an odd polynomial, is strictly increasing, and satisfies $h(1)=1$ and strictly decreasing $h(t)/t=(3-t^2)/2$ on $(0,1]$. For nonnegative unit vectors of arbitrary finite dimension,

$$
\inf R_h(x)^2=\frac{16(17-9\sqrt3)}{23}.
$$

No finite-dimensional vector attains this infimum. With at most two nonzero coordinates, the attained minimum is

$$
\min R_h(x)^2=\frac{80}{81}.
$$

Squared coordinates $(4/5,1/10,1/10)$ give $13689/13885<80/81$. The all-dimension infimum is approached by one squared coordinate $a_*=6-3\sqrt3$ and $m$ squared coordinates $(1-a_*)/m$, as $m\to\infty$.
:::

::: {.proof #pf-s11}
**Polynomial and moment identity.** Since $h'(t)=3(1-t^2)/2>0$ for $0\le t<1$, integration over any nontrivial subinterval proves strict increase, including at the endpoint $1$. The formula for $h(t)/t$ proves its strict decrease and $h(t)\ge t=h(1)t$. Put $p_i=x_i^2$, $s_2=\sum_i p_i^2$, $s_3=\sum_i p_i^3$. Then $p_i\ge0$ and $\sum_i p_i=1$. Expanding gives

$$
\begin{gathered}
\sum_i x_i h(x_i)=\tfrac12(3-s_2)\\
\sum_i h(x_i)^2=\tfrac14(9-6s_2+s_3),
\end{gathered}
$$

hence the moment identity

$$
R_h(x)^2=\frac{(3-s_2)^2}{9-6s_2+s_3}.
$$

The denominator is positive because $s_2\le1$ and $s_3\ge0$, so it is at least $3$.

**Exact two-coordinate gap.** Write the two squared coordinates as $p,1-p$, allowing endpoints for a single active coordinate, and set $u=p(1-p)\in[0,1/4]$. Then $s_2=1-2u$, $s_3=1-3u$, and

$$
\begin{gathered}
R_h(x)^2=\frac{(1+u)^2}{1+9u/4}\\
R_h(x)^2-\frac{80}{81}=\frac{(9u-1)^2}{81(1+9u/4)}.
\end{gathered}
$$

Equality holds precisely when $u=1/9$, feasible at $p=(3+\sqrt5)/6$ or $(3-\sqrt5)/6$. Both coordinates are positive. Endpoints instead give ratio squared $1$.

**Three coordinates already improve the value.** For $(p_1,p_2,p_3)=(4/5,1/10,1/10)$, $s_2=33/50$ and $s_3=257/500$. Substitution gives $R_h^2=13689/13885$, with exact gap

$$
\frac{80}{81}-\frac{13689}{13885}=\frac{1991}{81\cdot13885}>0.
$$

Thus the proposed universal reduction to two coordinates fails even under all the stated polynomial regularity conditions.

**Dimension-free lower bound.** Put $a=\sqrt{s_2}\in(0,1]$. Every $p_i\le a$ since $p_i^2\le s_2$. Thus $s_3\le a s_2=a^3$, and positivity of denominators gives

$$
R_h(x)^2\ge f(a):=\frac{(3-a^2)^2}{9-6a^2+a^3}.
$$

On $[0,1]$ the denominator is at least $3$. Differentiation gives

$$
f'(a)=-\frac{a^2(3-a^2)(a^2-12a+9)}{(9-6a^2+a^3)^2}.
$$

The roots of the last quadratic are $6\pm3\sqrt3$. Only $a_*=6-3\sqrt3$ lies in $(0,1)$. All other displayed factors are positive in the interior; hence $f$ decreases before $a_*$ and increases after it. Its unique minimum is $f(a_*)=16(17-9\sqrt3)/23$.

**Sharpness through a diffuse tail.** For each positive integer $m$, use squared coordinates $a_*,(1-a_*)/m,\ldots,(1-a_*)/m$ with $m$ tail entries. They are positive and sum to one. Their moments are

$$
\begin{gathered}
s_2=a_*^2+\frac{(1-a_*)^2}{m}\\
s_3=a_*^3+\frac{(1-a_*)^3}{m^2}.
\end{gathered}
$$

These converge to $a_*^2,a_*^3$. The limiting denominator is positive, so continuity of the rational expression proves convergence to $f(a_*)$. This proves sharpness over finite vectors whose dimension grows.

**Nonattainment.** Attaining the lower bound would force equality in $s_3\le a s_2$. The nonnegative summands $p_i^2(a-p_i)$ must then all be zero, so every positive $p_i=a$. Consequently $s_2=a\sum_i p_i=a$, while by definition $s_2=a^2$. Since $a>0$, we get $a=1$, exactly one active coordinate and $R_h^2=1$. But $f(a_*)<1$ (for example $f(1/2)<1$ and the minimum is no larger). Hence no finite vector attains the smaller infimum. This completes manuscript Theorem 11.
:::

## What the formal declarations cover

| Mathematical statement | Exact pinned Lean declaration | Remaining written scope |
| --- | --- | --- |
| Both inertia triples for arbitrary real symmetric $A$ | `StructuredRankOneInertia.inertia_downdate` | Full theorem also states rank |
| Kernel direct sum; nullity increase | `kernel_split`; `nullity_downdate` in the same module | Rank-nullity deduction |
| Finite-puncture path connectedness | `StructuredRankOneFamily.punctured_simplex_pathConnected` | Countable punctures and dimension-two boundary |
| Finite-puncture sign and fixed negative index | `StructuredRankOneFamily.continuous_family` | General connected spaces and the positive-branch entry classification |
| Block removal, coefficient changes, sphere results | No matching declaration in the two inspected pinned modules | Complete written proofs above |

The names in this table abbreviate the namespace `D5.S3.QuadraticForms`. [The coverage chapter](coverage.md) links each declaration at the full pinned revision and the existing contribution requests. The broader classification for general $h$, and the source's numerical observation about an unspecified odd polynomial, are not settled here.
