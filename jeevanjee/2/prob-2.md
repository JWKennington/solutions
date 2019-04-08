Given $f,g\ \in L^2\left[-a,a\right]$, we need to show that the addition of $f$ and $g$ also is in $L^2\left[-a,a\right]$. 
Specifically, we must show $h(x) = (f+g)(x)\ \in L^2\left[-a,a\right]$.

Begin by using the Triangle Inequality

$$\int_{-a}^{a}\lvert h\rvert ^2dx = \int_{-a}^{a}\lvert f+g \rvert ^2dx \leq \int_{-a}^{a}\left(\lvert f \rvert + \lvert g \rvert\right)^2 dx$$

Using the given inequality $0 \leq \int_{-a}^a\left(\lvert f\rvert + \lambda\lvert g\rvert\right)^2dx$ for all $\lambda \in \mathbb{R}$. 

If we expand the inequality and choose $\lambda=1$, we obtain the fairly general result:

$$0 \leq \int_{-a}^{a}\left(\lvert f\rvert + \lambda\lvert g\rvert\right)^2dx = \int_{-a}^{a}\lvert f\rvert^2dx + \lambda^2\int_{-a}^a\lvert g\rvert^2dx + 2\lambda\int_{-a}^a\lvert f\rvert\lvert g\rvert dx$$

$$2\int_{-a}^a\lvert f\rvert\lvert g\rvert dx \leq \int_{-a}^a\lvert X \rvert ^2dx + \int_{-a}^a\lvert g \rvert ^2dx < \infty$$

Now that we've shown the cross-term is finite, we can establish our original objective:

$$\int_{-a}^a\lvert h\rvert ^2dx = \int_{-a}^a\lvert f\rvert ^2dx + \int_{-a}^a\lvert g\rvert ^2dx + 2\int_{-a}^a\lvert f \rvert \lvert g\rvert dx < \infty$$
