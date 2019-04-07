Given $f,g\ \in \SIF$, we need to show that the addition of $f$ and $g$ also is in $\SIF$. 
Specifically, we must show $h(x) = (f+g)(x)\ \in \SIF$.

Begin by using the Triangle Inequality

$$\int_{-a}^{a}\norm{h}^2dx = \int_{-a}^{a}\norm{f+g}^2dx \leq \int_{-a}^{a}\left(\norm{f} + \norm{g}\right)^2 dx$$

Using the given inequality $0 \leq \int_{-a}^a\left(\norm{f} + \lambda\norm{g}\right)^2dx$ for all $\lambda \in \mathbb{R}$. 

If we expand the inequality and choose $\lambda=1$, we obtain the fairly general result:

$$0 \leq \int_{-a}^{a}\left(\norm{f} + \lambda\norm{g}\right)^2dx = \int_{-a}^{a}\norm{f}^2dx + \lambda^2\int_{-a}^a\norm{g}^2dx + 2\lambda\int_{-a}^a\norm{f}\norm{g}dx$$

$$2\int_{-a}^a\norm{f}\norm{g}dx \leq \int_{-a}^a\norm{f}^2dx + \int_{-a}^a\norm{g}^2dx < \infty$$

Now that we've shown the cross-term is finite, we can establish our original objective:

$$\int_{-a}^a\norm{h}^2dx = \int_{-a}^a\norm{f}^2dx + \int_{-a}^a\norm{g}^2dx + 2\int_{-a}^a\norm{f}\norm{g}dx < \infty$$
