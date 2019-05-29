#### Problem
Given a finite dimensional vector space $V$ and a map from the space to the dual $J: V\rightarrow V^*$ defined by $J: v \mapsto J_v$ where $J_v (f) \equiv f(v)$, show that $J$ is linear, 1-to-1, and onto. This implies that $|V| = |(V^*)^*|$, that the dual of the dual is the original vector space.

#### Solution
Show $J$ is linear by exploiting the linearity of $f$. 
$$J_v(v_1 +cv_2)(f)\equiv f(v_1 + cv_2) = f(v_1) + c f(v_2) = J(v_1)(f) + cJ(v_2)(f)$$
Show $J$ is injective. Let $a, b \in V$ such that $J_a(f) = J_b(f)$ for all $f$ in $V^*$. This implies that $f(a) = f(b)$ for all $f$, or, in index notation, that $a^if_i=b^if_i$ for all $f$. Therefore $a^i=b^i$, which implies $a=b$. 

Next, show $J$ is surjective. Let $w \in (V^*)^*$ such that $w: V^* \rightarrow C$ and $w(f) \equiv f(w)$. Realize that $f(w) \equiv J_w(f)$, and therefore we have a map $w\mapsto J_w$, which gives us surjectivity!

Lastly, we conclude that $J$ is bijective, and that $V = (V^*)^*$.