# One direction leaves one zero direction

Can a matrix that already has zero directions still lose exactly one positive or negative direction? Haobo Ma and Wenlin Zhang’s revision-two paper answers yes. When a chosen direction has nonzero quadratic value, a special rank-one modification creates exactly one new zero direction. Continuity turns this local fact into a global restriction: the unique negative coordinate cannot switch places in a connected diagonal family. A linked sphere problem gives another surprise: even a very regular cubic odd polynomial does not always allow the worst case to be compressed to two coordinates.

The questions come from Lucid’s MathOverflow 513954 revision two and its linked discussion. The earlier proof of the inertia formula is credited to user1551. Ma and Zhang give a self-contained proof, the family argument and extensions, and an exact polynomial sphere infimum. We start with school algebra; the [next chapter](statements.md) contains complete precise statements and proofs.

## First calculate an example with a zero direction

A measurement assigns $-2u^2+3w^2$ to $(u,v,w)$. It is negative along the first axis, positive along the third, and unaffected by the second. Write
$$
A=\operatorname{diag}(-2,0,3),\qquad x=(1,0,0)^{\mathsf T}.
$$
The superscript $\mathsf T$ means transpose. Then $\Delta=x^{\mathsf T}Ax=-2$, $Ax=(-2,0,0)^{\mathsf T}$, and
$$
M=A-\frac{(Ax)(Ax)^{\mathsf T}}{\Delta}=\operatorname{diag}(0,0,3).
$$
The old zero direction survives, and $x$ becomes an independent new one. The denominator is the number $\Delta$; we never invert $A$. The original matrix is singular, yet the calculation works.

A real symmetric matrix assigns the quadratic value $v^{\mathsf T}Av$. Suitable coordinates split it into positive, negative and zero terms. Their eigenvalue counts, including multiplicity, form the **inertia** $(n_+,n_-,n_0)$. This does not count every vector with zero measurement. For example $u^2-v^2$ vanishes at $(1,1)$ although the matrix has zero kernel. The **kernel** requires $Av=0$, stronger than one quadratic value being zero.

Set $\Delta=x^{\mathsf T}Ax\ne0$, $w=Ax$, and $M=A-ww^{\mathsf T}/\Delta$. The [inertia result](statements.md#lean-inertia) says that $\Delta>0$ removes one positive eigenvalue, whereas $\Delta<0$ removes one negative eigenvalue. The other nonzero count stays unchanged and the zero count rises by one. The [complete result](statements.md#thm-s1) says the new kernel is the direct sum of the old kernel and the line through $x$, so rank falls by one. The sign counts are controlled; the other eigenvalues need not retain their numerical values.

## Why does just one block change?

Let $H=\{z:(Ax)^{\mathsf T}z=0\}$. Since $(Ax)^{\mathsf T}x=\Delta\ne0$, $x$ lies outside this hyperplane, and
$$
v=\left(v-\frac{(Ax)^{\mathsf T}v}{\Delta}x\right)
+\frac{(Ax)^{\mathsf T}v}{\Delta}x.
$$
The first part lies in $H$, the second along $x$. The spaces meet only at zero, making the split unique. It is like moving along $x$ until landing in the hyperplane. The hyperplane is perpendicular to $Ax$, not necessarily to $x$.

Symmetry eliminates cross terms. Use a basis of $H$ followed by $x$:
$$
A\longleftrightarrow\begin{pmatrix}C&0\\0&\Delta\end{pmatrix},
\qquad M\longleftrightarrow\begin{pmatrix}C&0\\0&0\end{pmatrix}.
$$
The block $C$ may have its own zero directions; all of it survives. Replacing $[\Delta]$ by zero explains the answer. Invertible coordinate changes preserve inertia, a fact called Sylvester’s law. The [proof](statements.md#pf-s1) explains why singular matrices are included.

::: {.film src="001-one-direction"}
The same mathematical story in motion: a scalar block becomes zero, connectedness fixes the negative coordinate, and a diffuse tail defeats two-coordinate reduction.
:::

## Why can the negative coordinate not hand over?

Positive semidefinite means every $v^{\mathsf T}Mv\ge0$, or no negative eigenvalues. The inertia formula says that when $\Delta<0$ and $M$ is positive semidefinite, the original diagonal matrix has exactly one negative entry; the others may vanish. The [positive branch](statements.md#thm-s2) requires the original matrix itself to be positive semidefinite.

Let the diagonal entries and $x$ vary continuously over a nonempty connected parameter space, keeping $\Delta\ne0$ and $M$ positive semidefinite. A continuous nonzero real function cannot change sign. In the negative branch, let $U_j$ be the parameters where entry $j$ is negative. These sets are open, disjoint and cover the space. Each complement is the union of the other $U_i$, so each is closed too. Connectedness forces one such region to be the whole space: the same coordinate stays negative. This is the [continuous-family theorem](statements.md#thm-s5).

An open triangle with a few points removed still permits two-segment paths around them; higher dimensions work too, even with countably many punctures. But removing an interval’s midpoint disconnects it. Coordinate one can be negative on the left and coordinate two on the right, continuously on the punctured space. The simplex dimension threshold of two is essential.

## Two-coordinate intuition fails on the sphere

A unit vector satisfies $\sum_i x_i^2=1$. Apply $h$ to every coordinate and define
$$
R_h(x)=\frac{\sum_i x_i h(x_i)}{\sqrt{\sum_i h(x_i)^2}}.
$$
The numerator is a dot product; the denominator removes the transformed vector’s length. Since $\|x\|_2=1$, this is the cosine of the angle between the vectors. The source assumes continuous $h:(0,1]\to\mathbb R$ with $h(t)\ge h(1)t>0$ and asks whether the all-finite-dimension infimum needs at most two positive coordinates. When $h(0)$ is unspecified, zero coordinates are omitted. For the polynomial below $h(0)=0$, so either convention agrees.

daw had proposed $h=1$: its infimum with $d$ positive coordinates is $1/\sqrt d$, tending to zero with dimension, while at most two coordinates give $1/\sqrt2$. Exodd’s $h(t)=1/t$ already tends to zero in dimension two. The paper uses
$$
h(t)=\frac{3t-t^3}{2}.
$$
It is odd, strictly increasing on $[0,1]$, and $h(t)/t=(3-t^2)/2$ strictly decreases. Even so, the [polynomial theorem](statements.md#thm-s11) gives
$$
\inf_{\text{arbitrary finite dimension}}R_h(x)^2=\frac{16(17-9\sqrt3)}{23},
$$
$$
\min_{\text{at most two nonzero coordinates}}R_h(x)^2=\frac{80}{81}.
$$
These are approximately $0.981943$ and $0.987654$: a small but strict gap. Squared coordinates $(4/5,1/10,1/10)$ already give $13689/13885<80/81$, so three coordinates beat every two-coordinate vector.

## One large coordinate and an increasingly diffuse tail

Put $p_i=x_i^2$, distributing mass one. With $s_2=\sum_i p_i^2$ and $s_3=\sum_i p_i^3$, expansion gives
$$
R_h(x)^2=\frac{(3-s_2)^2}{9-6s_2+s_3}.
$$
Let $a=\sqrt{s_2}$. Every $p_i\le a$, so $s_3\le a^3$. Increasing the denominator decreases the fraction; hence
$$
R_h(x)^2\ge f(a)=\frac{(3-a^2)^2}{9-6a^2+a^3}.
$$
This one-variable function is minimized at $a_*=6-3\sqrt3$. Take one squared coordinate $a_*$ and divide the remaining $1-a_*$ equally among $m$ coordinates. As $m$ grows, the tail’s contributions to the square and cube sums disappear, leaving $a_*^2$ and $a_*^3$. The ratio approaches the exact constant. This is a sequence of finite vectors, not a finite-dimensional minimizer.

Finite equality $s_3=a^3$ forces every positive $p_i=a$; their total being one then gives $s_2=a$. Together with $s_2=a^2$, this forces $a=1$ and squared ratio one, above the optimal constant. The diffuse tail is the approximation mechanism, not disposable noise.

The matrix lesson is “isolate a nonzero block and replace it by zero.” The family lesson is “local uniqueness plus connectedness gives global uniqueness.” The sphere lesson is “moments give a uniform bound and a diffuse tail approaches it.” Block removal, coefficient changes and all boundary cases are in the [proof chapter](statements.md). A classification for general $h$, and the source’s observation about an unspecified polynomial, lie outside this paper’s settlement.

::: {.slides src="seminar"}
The aligned Chinese and English academic Beamer deck and speaker notes develop this same story.
:::

Authors: Haobo Ma (Chrono AI, Singapore); Wenlin Zhang (National University of Singapore and Chrono AI, Singapore). Version 2, CC BY 4.0, version DOI: [10.5281/zenodo.23920598](https://doi.org/10.5281/zenodo.23920598). Original questions, earlier proofs and exact formalization scope appear in the [sources chapter](coverage.md).
