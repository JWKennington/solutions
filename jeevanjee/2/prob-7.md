#### Problem
Properties of the Hermitian adjoint. This problem will use the tensorial definition of the Hermitian adjoint to derive the commonly-seen, more behavioral, definition. Several properties of the Hermitian adjoint will also be explored. 

Using the metric dual map $L: V\rightarrow V^*$ and definition of $A^T$ from Problem 6, we define the *Hermitian adjoint* $A^{\dagger}$ of the operator $A$ to be:
$$A^{\dagger} \equiv L^{-1} \circ A^T \circ L\ :\ V \rightarrow V$$
If $A = A^{\dagger}$, then $A$ is said to be *self-adjoint* or *Hermitian*. This indicates a certain compatibility between $A$ and $(\cdot\ |\ \cdot)$.

Show the following things about $A$:

1. $(A^{\dagger}v|w) = (v|Aw)$, usually taken as the definition of the adjoint operator. Also show $(A^{\dagger})^{\dagger} = A$, and finally $(Av|w) = (v|A^{\dagger}w)$
2. Given an orthonormal basis $\mathcal{B} = \{e_i\}_{i=1...n}$ that $\left[A^{\dagger}\right] = \left[A\right]^{\dagger}$
3. If $A$ is self-adjoint, then even when $V$ is a complex vector space any eigenvalue of $A$ must be real.
4. Show whether or not the result from Part 2 extends to non-orthonormal bases.

#### Solution
A lot of things to show here! Fortunately, most of this will boil down to keeping the track of the definitions of $A^T$ and $L$. Recall that $L(v) = \tilde{v} = (v|\ \cdot)$ and that $A^T$ is defined by $(A^T(f))(v) \equiv f(Av)$. Now to show (1), using the definition of $A^{\dagger}$:
$$(A^{\dagger}v|w) = L\left(A^{\dagger}v\right)(w) = \left(L^{-1}\circ L \circ A^T \circ L \right)(v)(w)$$
$$= A^T(L(v))(w) \equiv \tilde{v}(Aw) = (v|Aw)$$
Next, we show that evaluating the matrix and the adjoint commute. Specifically, we aim to show that $\left[A^{\dagger}\right] = \left[A\right]^{\dagger}$. Recall that for matrices, the adjoint is the conjugate-transpose. We use this to show:
$$\overline{A_j{}^i} = \overline{e^i(Ae_j)} = \overline{(e_i|Ae_j)}=(Ae_j|e_i)=(e_j|A^{\dagger}e_i) = e^j(A^{\dagger}e_i) = A^{\dagger}_i{}^j$$
Where we used the Hermiticity of the metric, that $\overline{(v|w)} = (w|v)$. Notice that the statement above $A^{\dagger}_i{}^j = \overline{A_j{}^i}$ implies that the matrices are, in fact, conjugate-transpose (element-wise).
For the next piece, we need to show that any eigenvalue $\lambda$ of a self-adjoint operator $A$ has no imaginary component. Showing that $\lambda = \overline{\lambda}$ is sufficient. We begin with the familiar eigenvalue condition $Av=\lambda v$, taking the inner product on both sides yields $(Av|w)=(\lambda v | w)$. Exploiting various properties of conjugation and Hermiticity, the previous equality can be rewritten as $\overline{(\overline{\lambda}w|v)} = \overline{(Aw|v)}$, which implies that $Aw=\overline{\lambda}w$. Therefore we conclude that $\lambda = \overline{\lambda}$, or that $\lambda \in \mathbb{R}$.
Lastly, we show that the result from Part 2 does *not* generalize to non-orthonormal bases. This is easily done with the counterexample suggested by the author, where the basis is $\mathcal{B} = \{(1,0,0), (1,1,0), (0,0,1)\}$ and $V = L^2([-a,a])$ and $A = L_z$. Recall that $L_z = -i\left(x\frac{d}{dy} - y\frac{d}{dx}\right)$. We compute the columns $[L_z]_i$ by evaluating $L_z$ on the basis vectors:
$$[L_z]_1 = L_z(e_1) = L_z(x) = iy = (0, i, 0)$$
$$[L_z]_2 = L_z(e_2) = L_z(x + y) = -i(x-y) = -i(2x - (x+y)) = (-2i, i, 0)$$
$$[L_z]_3 = L_z(e_3) = L_z(z) = (0, 0, 0)$$
Thus, the resulting matrix is clearly not adjoint - transposing the factor of 2 will cause inconsistencies.
$$[L_z]_{\mathcal{B}} = \begin{pmatrix}
0 & -2i & 0 \\
-i & i & 0 \\
0 & 0 & 0 \\
\end{pmatrix}$$