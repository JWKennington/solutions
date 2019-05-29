#### Problem
Properties of the transpose of a linear operator. Given a linear operator $A\in\mathcal{L}(V)$, define a linear operator on $V^*$  called the _transpose_ of $A$ denoted $A^T$ as follows:
$$(A^T(f))(v) \equiv f(Av)$$ where $v\in V$ and $f \in V^*$. Show that (a) this definition corresponds to the matrix transpose under basis transformation, $[A^T]_{\mathcal{B}^*} = [A]^T_{\mathcal{B}}$. Also show that (b) the Dirac delta functional $\delta \in L^2([-a, a])^*$ may be differentiated by the transpose of the linear operator $\frac{d}{dx}$ on $L^2([-a, a])$. Specifically, this amounts to showing
$$\left(\frac{d}{dx}^T\delta\right)(f) = \frac{df}{dx}(0)\ \forall f \in L^2([-a, a])$$

#### Solution
First, we show that the transpose of the operator $A$ evaluated in the dual basis represents the transpose of the matrix of $A$ evaluated in the original basis. In index notation, this amounts to showing that ${A^T}_i{}^j = A^I{}_j$. This is relatively simple:
$${A^T}_i{}^j = e_i(A^T e^j) = (A^T e^j)(e_i) \equiv e^i(Ae_j) = A^i{}_j$$
Next, we show that the Dirac delta functional can be properly used with the dual of the derivative operator. First, recall that
$$\delta(f)(x)\equiv f(0)$$
Now combine that with the above expression for the derivative of the delta functional to show the conventional result:
$$\left({\frac{d}{dx}}^T \delta\right)(f) \equiv \delta\left(\frac{d}{dx}(f)\right) = \delta\left(\frac{df}{dx}\right) = \frac{df}{dx}(0)$$