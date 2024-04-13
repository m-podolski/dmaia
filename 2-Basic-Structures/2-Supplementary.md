# 2 Supplementary

1. Let $A$ be the set of English words that contain the letter $x$, and let $B$ be the set of English words that contain the letter $q$. Express each of these sets as a combination of $A$ and $B$.
- (a) The set of English words that do not contain the letter $x$.
  - ❌ $B - A$ ✅ $\overline{A}$
- (b) The set of English words that contain both an $x$ and a $q$.
  - $A ∩ B$
- (c) The set of English words that contain an $x$ but not a $q$.
  - $A - B$
- (d) The set of English words that do not contain either an $x$ or a $q$.
  - $\overline{A ∪ B}$
- (e) The set of English words that contain an $x$ or a $q$, but not both.
  - $A ⊕ B$

2. Show that if A is a subset of B, then the power set of A is a subset of the power set of B.
    - As any element of A must be in B the powerset of B must at least be contain all subsets of A.

3. Suppose that A and B are sets such that the power set of A is a subset of the power set of B. Does it follow that A is a subset of B?
    - Yes. ✔ We must show that every element of A is also an element of B. So suppose a is an arbitrary element of A. Then {a} is a subset of A, so it is an element of the power set of A. Since the power set of A is a subset of the power set of B, it follows that {a} is an element of the power set of B, which means that {a} is a subset of B. But this means that the element of {a}, namely a, is an element of B, as desired.

4. Let E denote the set of even integers and O denote the set of odd integers. As usual, let ℤ denote the set of all integers. Determine each of these sets.
- (a) $E ∪ O = ℤ$
- (b) $E ∩ O = ∅$
- (c) $ℤ − E = O$
- (d) $ℤ − O = E$

5. Show that if A and B are sets, then $A − (A − B) = A ∩ B$.
    - If $x ∈ A − (A − B)$ then $x ∈ A$ but $x ∉ (A − B)$ so $x$ must be in $A$ and $B$ which bd. is $A ∩ B$. Conversely if $x ∈ A ∩ B$ then $x ∈ A$ and $x ∈ B$ so ⭕ **$x ∉ A - B$** and $x ∈ A − (A − B)$.

6. Let A and B be sets. Show that $A ⊆ B$ if and only if $A ∩ B = A$.
   - Btdo. subsets we know that $x ∈ A → x ∈ B$ so $x ∈ A ∩ B$. Conversely, if $A ∩ B = A$ then all $x ∈ A ∩ B$ must be in $B$. Therefore $A ⊆ B$.

7. Let A, B, and C be sets. Show that $(A − B) − C$ is not necessarily equal to $A − (B − C)$.
   - ❎ $(A − B) − C ≠ A − (B − C)$ because if we assume an element $x ∈ A ∩ C$ then this is not in $(A − B) − C$ but in $A − (B − C)$. This is because in $(A − B) − C$ the intersection of $C$ is subtraced from $A$ but in $A − (B − C)$ only elements that are in $A ∩ B$ but not in $C$ are subtracted.
   - ✅ We need only provide a counterexample to show that $(A - B) - C$ is not necessarily equal to $A - (B - C)$. Let $A = C = \{1\}$, and let $B = ∅$. Then $(A - B) - C = (\{1\} - ∅) - \{1\} = \{1\} - \{1\} = ∅$, whereas $A- (B-C) = \{1\}- (∅- \{1\}) = \{1\}-∅ = \{1\}$.

8. Suppose that A, B, and C are sets. Prove or disprove that $(A − B) − C = (A − C) − B$.
    - Assuming $x ∈ (A − B) − C$ this element is in $A$ but not in $B$ and not in $C$. ⭕ Therefore $x ∈ A − C$, and therefore $x ∈ (A − C) − B$. The converse is proved in exactly the same way.

9. Suppose that A, B, C, and D are sets. Prove or disprove that $(A − B) − (C − D) = (A − C) − (B − D)$.
    - This is not true. If $A = B = D = \{1\}$ and $C = ∅$ then $(A − B) − (C − D) = (\{1\} - \{1\}) - (∅ - \{1\}) = ∅ - ∅ = ∅$ but $(A − C) − (B − D) = (\{1\} - ∅) - (\{1\} - \{1\}) = \{1\} - ∅ = \{1\}$.

10. Show that if A and B are finite sets, then $|A ∩ B| ≤ |A ∪ B|$. Determine when this relationship is an equality.
    - If $A = B$ then $|A ∩ B| = |A ∪ B|$ because $A ∩ B = A ∪ B$. If $A ≠ B$ then bd. intersection $A ∩ B$ is at least one element smaller than $A ∪ B$. ✔ This follows from the fact that $A ∩ B ⊆ A ∪ B$.

11. Let A and B be sets in a finite universal set U . List the following in order of increasing size.
- (a) $|A|, |A ∪ B|, |A ∩ B|, |U|, |∅|$
  - $|∅|, ❌|A|, |A ∩ B|, |A ∪ B|, |U|$
  - $|∅|, ✅|A ∩ B|, |A|, |A ∪ B|, |U|$
- (b) $|A − B|, |A ⊕ B|, |A| + |B|, |A ∪ B|, |∅|$
  - $|∅|, |A − B|, |A ⊕ B|, |A ∪ B|, |A| + |B|$

12. Let A and B be subsets of the finite universal set U . Show that $|\overline{A} ∩ \overline{B}| = |U| − |A| − |B| + |A ∩ B|$.
    - If we subtract both $|A|$ and $|B|$ from $|U|$, we have subtracted $|A ∩ B|$ twice so we need to add it again.

13. Let $f$ and $g$ be functions from $\{1, 2, 3, 4\}$ to $\{a, b, c, d\}$ and from $\{a, b, c, d\}$ to $\{1, 2, 3, 4\}$, respectively, with $f (1) = d$, $f (2) = c$, $f (3) = a$, and $f (4) = b$, and $g(a) = 2$, $g(b) = 1$, $g(c) = 3$, and $g(d) = 2$.
- (a) Is $f$ one-to-one? Is $g$ one-to-one?
  - Yes, No
- (b) Is $f$ onto? Is $g$ onto?
  - Yes, No
- (c) Does either $f$ or $g$ have an inverse? If so, find this inverse.
  - $f$ has; $f(x)^{-1} = f(a) = 3, f(b) = 4, f(c) = 2, f(d) = 1$.

14. Suppose that f is a function from A to B where A and B are finite sets. Explain why $|f(S)| ≤ |S|$ for all subsets S of A.
    - ❌ If $f$ is a bijection we have $|f(S)| = |S|$, if it is only onto, we have $|f(S)| < |S|$. It cannot be that $|f(S)| > |S|$ because then $f$ would not be a function (as it sends at least one element to two different images).
    - ✅⚠️ Define a function $g : f (S) → S$ by choosing, for each element $x$ in $f (S)$, an element $g(x) ∈ S$ such that $f (g(x)) = x$. Clearly $g$ is one-to-one, so $|f (S)| ≤ |S|$. Note that we do not need the hypothesis that A and B are finite.

15. ❓ Suppose that f is a function from A to B where A and B are finite sets. Explain why $|f(S)| = |S|$ for all subsets S of A if and only if f is one-to-one.
    - ✅ If $f$ is one-to-one, then $f$ provides a bijection between $S$ and $f(S)$, so they have the same cardinality by definition. If $f$ is not one-to-one, then there exist elements $x$ and $y$ in $S$ such that $f(x) = f(y)$. Let $S = \{x,y\}$. Then $|S| = 2$ but $|f(S)| = 1$. Note that we do not need the hypothesis that A and B are finite.

Suppose that $f$ is a function from $A$ to $B$. We define the function $S_f$ from $𝒫(A) to 𝒫(B)$ by the rule $S_f (X) = f (X)$ for each subset $X$ of $A$. Similarly, we define the function $S_{f−1}$ from $𝒫(B)$ to $𝒫(A)$ by the rule $S_{f−1} (Y ) = f^{−1} (Y )$ for each subset $Y$ of $B$. Here, we are using Definition 4, and the definition of the inverse image of a set found in the preamble to Exercise 42, both in Section 2.3.

16. (∗) Suppose that $f$ is a function from the set $A$ to the set $B$. Prove that
- (a) ❓ if $f$ is one-to-one, then $S_f$ is a one-to-one function from $𝒫(A)$ to $𝒫(B)$.
  - ✅⚠️ We are given that $f$ is one-to-one, and we must show that $S_f$ is one-to-one. So suppose that $X_1 ≠ X_2$, where these are subsets of $A$. We have to show that $S_f (X_1) ≠ S_f (X_2 )$. Without loss of generality there is an element $a ∈ X_1 − X_2$. This means that $f(a) ∈ S_f (X_1)$. If $f(a)$ were also an element of $S_f (X_2)$, then we would need an element $a' ∈ X_2$ such that $f(a') = f(a)$. But since $f$ is one-to-one, this forces $a' = a$, which is impossible, because $a ∉ X_2$. Therefore $f(a) ∈ S_f (X_1 ) − S_f (X_2)$, so $S_f (X_1) ≠ S_f (X_2)$.
- (b) ❓ if $f$ is onto function, then $S_f$ is an onto function from $𝒫(A)$ to $𝒫(B)$.
  - ✅⚠️ We are given that $f$ is onto, and we must show that $S_f$ is onto. So suppose that $Y ⊆ B$. We have to find $X ⊆ A$ such that $S_f (X) = Y$. Let $X = \{ x ∈ A \mid f (x) ∈ Y \}$. We claim that $S_f (X) = Y$. Clearly $S_f (X) ⊆ Y$. To see that $Y ⊆ S_f (X)$, suppose that $b ∈ Y$. Then because $f$ is onto, there is some $a ∈ A$ such that $f (a) = b$. By our definition of $X$, $a ∈ X$. Therefore by definition $b ∈ S_f (X)$.
- (c) ❓ if $f$ is onto function, then $S_{f−1}$ is a one-to-one function from $𝒫(B)$ to $𝒫(A)$.
  - ✅⚠️ We are given that $f$ is onto, and we must show that $S_{f−1}$ is one-to-one. So suppose that $Y_1 ≠ Y_2$, where these are subsets of $B$. We have to show that $S_{f−1} (Y_1 ) ≠ S_{f−1} (Y_2 )$. Without loss of generality there is an element $b ∈ Y_1 − Y_2$. Because $f$ is onto, there is an $a ∈ A$ such that $f (a) = b$. Therefore $a ∈ S_{f−1} (Y_1 )$. But we also know that $a ∉ S_{f−1} (Y_2)$, because if a were an element of $S_{f−1} (Y_2)$, then we would have $b = f (a) ∈ Y_2$, contrary to our choice of $b$. The existence of this $a$ shows that $S_{f−1} (Y_1 ) ≠ S_{f−1} (Y_2)$.
- (d) ❓ if $f$ is one-to-one, then $S_{f−1}$ is an onto function from $𝒫(B)$ to $𝒫(A)$.
  - ✅⚠️ We are given that f is one-to-one, and we must show that $S_{f−1}$ is onto. So suppose that $X ⊆ A$. We have to find $Y ⊆ B$ such that $S_{f−1} (Y ) = X$. Let $Y = S_f (X)$. In other words, $Y = \{ f (x) \mid x ∈ X \}$. We must show that $S_{f−1} (Y ) = X$, which means that we must show that $\{ a ∈ A \mid f (a) ∈ \{ f (x) \mid x ∈ X \} \} = X$. That the right-hand side is a subset of the left-hand side is immediate, because if $a ∈ X$, then $f (a)$ is an $f (x)$ for some $x ∈ X$. Conversely, suppose that $a$ is in the left-hand side. Thus $f (a) = f (x_0 )$ for some $x_0 ∈ X$. But because $f$ is one-to-one, we know that $a = x_0$; that is $a ∈ X$.
- (e) ❓ if $f$ is a one-to-one correspondence, then $S_f$ is a one-to-one correspondence from $𝒫(A)$ to $𝒫(B)$ and $S_{f−1}$ is a one-to-one correspondence from $𝒫(B)$ to $𝒫(A)$. [Hint: Use parts (a)-(d).]
  - ✅ This follows immediately from the earlier parts, because to be a one-to-one correspondence means to be one-to-one and onto.

17. ❓ Prove that if $f$ and $g$ are functions from $A$ to $B$ and $S_f = S_g$ (using the definition in the preamble to Exercise 16), then $f(x) = g(x)$ for all $x ∈ A$.
    - ✅ The key is to look at sets with just one element. On these sets, the induced functions act just like the original functions. So let $x$ be an arbitrary element of $A$. Then $\{x\} ∈ P(A)$, and $S_f(\{x\}) = \{f(y)  \mid y ∈ \{x\}\} = \{f(x)\}$. By the same reasoning, $S_g (\{x\}) = \{g(x)\}$. Since $S_f = S_g$, we can conclude that $\{f(x)\} = \{g(x)\}$, and so necessarily $f(x) = g(x)$.

18. Show that if $n$ is an integer, then $n = ⌈n/2⌉ + ⌊n/2⌋$.
    - If $n$ is even, then $⌈n/2⌉ = ⌊n/2⌋ = n/2$ and therefore $⌈n/2⌉ + ⌊n/2⌋ = n/2 + n/2 = n$ If it is odd, ❎ then $⌈n/2⌉ = n/2 + 1/2$ and $⌊n/2⌋ = n/2 - 1/2$ therefore $⌈n/2⌉ + ⌊n/2⌋ = n/2 + 1/2 + n/2 - 1/2 = n$.

19. For which real numbers $x$ and $y$ is it true that $⌊x + y⌋ = ⌊x⌋ + ⌊y⌋$?
    - Letting $x = m + d$ and $y = n + e$ where $d$ and $e$ are the fractional part with $0 ≤ d < 1$ and $0 ≤ e < 1$ we have three possible cases. (1) $d$ and $e$ $< 1/2$; (2) and wlog. (3) $d$ or $e$ $> 1/2$ and the other $< 1/2$; (4) both are $> 1/2$. If (1) or (3), we have $⌊x + y⌋ = m + n = ⌊x⌋ + ⌊y⌋$ because $d + e < 1$, if (4) we have $⌊x + y⌋ = m + n + 1 ≠ ⌊x⌋ + ⌊y⌋$ because $d + e ≥ 1$.

20. For which real numbers $x$ and $y$ is it true that $⌈x + y⌉ = ⌈x⌉ + ⌈y⌉$?
    - Similar to the above there are two possible outcomes; If $d + e ≤ 1$ we have $⌈x + y⌉ = m + n + 1 and ⌈x⌉ + ⌈y⌉ = m + n + 2$, if $d + e ≥ 1$, we have $⌈x + y⌉ = m + n + 2 = ⌈x⌉ + ⌈y⌉$

21. For which real numbers $x$ and $y$ is it true that $⌈x + y⌉ = ⌈x⌉ + ⌊y⌋$?
    - $⌈x + y⌉ = ⌈x⌉ + ⌊y⌋$
    - (0.4, 0.4) $1 = 1 + 0$
    - (0.5, 0.5) $1 = 1 + 0$
    - (0.6, 0.6) $2 = 1 + 0$
    - Similar to the above. If $d + e ≤ 1$ then both side are equal and if $d + e > 1$ the lhs. is $1$ larger than the rhs..

22. Prove that $⌊n/2⌋⌈n/2⌉ = ⌊n^2/4⌋$ for all integers $n$.
    - If $n = 2k$ then $⌊n/2⌋⌈n/2⌉ = (2k/2)² = (2k)^2/4 = ⌊n^2/4⌋$.
    - If $n = 2k + 1$ then $⌊n/2⌋⌈n/2⌉ = ⭕ (((2k + 1) - 1)/2)(((2k + 1) + 1)/2)= (2k/2)((2k + 2)/2)$.
    - ✅ If $n = 2k + 1$ then $n/2 = k + 1/2$. Therefore the lhs. gives us $k(k + 1) = k² + k$, since we have to round down for the first factor and round up for the second. For the rhs. $n² = (2k + 1)² = 4k² + 4k + 1$, so $n²/4 = k² + k + 1/4$. Therefore the floor function gives us $k² + k$, and the proof is complete.

23. Prove that if $m$ is an integer, then $⌊x⌋ + ⌊m − x⌋ = m − 1$, unless $x$ is an integer, in which case, it equals $m$.
    - If both $m$ and $x$ are integers, the floor functions are obsolete and we have simply $x + m - x = m$. If $x$ is not an integer, we can divide it such that $x = n + d$ where $0 ≤ d < 1$. Then we have $⌊n + d⌋ + ⌊m − (n + d)⌋ = n + (m - (n + 1)) = m - 1$.

24. Prove that if $x$ is a real number, then $⌊⌊x/2⌋/2⌋ = ⌊x/4⌋$.
    - If we separate the fractional part of $x$ like above, then ❌ $x/2 = (n + d)/2$ and $⌊x/2⌋ = n/2$ so $⌊⌊x/2⌋/2⌋ = (n/2)/2$.
    - ✅  Since we are dividing by $4$, let us write $x = 4n − k$, where $0 ≤ k < 4$. In other words, write $x$ in terms of how much it is less than the smallest multiple of $4$ not less than it. There are three cases. If $k = 0$, then $x$ is already a multiple of $4$, so both sides equal $n$. If $0 < k ≤ 2$, then $⌊x/2⌋ = 2n − 1$, so the left-hand side is $⌊n - 1/2⌋ = n − 1$. Of course the right-hand side is $n − 1$ as well, so again the two sides agree. Finally, suppose that $2 < k < 4$. Then $⌊x/2⌋ = 2n − 2$, and the left-hand side is $⌊n - 1⌋ = n − 1$; of course the right-hand side is still $n − 1$, as well. Since we proved that the two sides are equal in all cases, the proof is complete.

25. Prove that if $n$ is an odd integer, then $⌈n^2/4⌉ = (n^2 + 3)/4$.
    - Letting $n = 2k + 1$, we have $(2k + 1)^2/4 = (4k² + 4k + 1)/4 = k² + k + 1/4$ so $⌈n^2/4⌉ = k² + k + 1$. Conversely $((2k + 1)^2 + 3)/4 = (4k² + 4k + 1 + 3)/4 = k² + k + 1$.

26. Prove that if $m$ and $n$ are positive integers and $x$ is a real number, then $$\left\lfloor \frac{⌊x⌋ + n}{m} \right\rfloor = \left\lfloor \frac{x + n}{m} \right\rfloor$$
    - Dividing the fractional part of $x$ such that $x = k + e$ and $0 ≤ d < 1$, the lhs. is $⌊(k + n) / m⌋$ and the rhs. is $⌊(k + e + n) / m⌋$.
    - ⭕ are the same, since adding a number strictly between 0 and 1 to the numerator of a fraction whose numerator and denominator are integers cannot cause the fraction to reach the next higher integer value (the numerator cannot reach the next multiple of m).

27. (∗) ❓ Prove that if $m$ is a positive integer and $x$ is a real number, then $$⌊mx⌋ = ⌊x⌋ + \left\lfloor x + \frac{1}{m} \right\rfloor + \left\lfloor x + \frac{2}{m} \right\rfloor + \dotsb + \left\lfloor x + \frac{m - 1}{m} \right\rfloor$$
    - ✅ Let us write $x = n + (r / m) + e$, where $n$ is an integer, $r$ is an nonnegative integer less than $m$, and $e$ is a real number with $0 ≤ e < 1/m$. In other words, we are peeling off the integer part of $x$ (i.e., $n = ⌊x⌋$) and the whole multiples of $1/m$ beyond that. Then the left-hand side is $⌊nm + r + me⌋ =nm + r$. On the right-hand side, ⚠️ the terms $⌊x⌋$ through $⌊x + (m - r - 1)/m⌋$ are all just $n$, and the remaining terms, if any, from $⌊x + (m - r)/m⌋$ through $⌊x + (m - 1)/m⌋$, are all $n + 1$. Therefore the right-hand side is $(m - r)n + r(n + 1) = nm+ r$ as well.

28. (∗) We define the **Ulam numbers** by setting $u_1 = 1$ and $u_2 = 2$. Furthermore, after determining whether the integers less than $n$ are Ulam numbers, we set $n$ equal to the next Ulam number if it can be written uniquely as the sum of two different Ulam numbers. Note that $u_3 = 3, u_4 = 4, u_5 = 6,$ and $u_6 = 8$.
- (a) Find the first 20 Ulam numbers.
  - ❌ $(1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13)$
  - ✅ $(1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69)$
- (b) ❓ Prove that there are infinitely many Ulam numbers.
  - ✅  Suppose there were only a finite set of Ulam numbers, say $u_1 < u_2 < · · · < u_n$. Then it is clear that $u_{n−1} + u_n$ can be written uniquely as the sum of two distinct Ulam numbers, so this is an Ulam number larger than $un$, a contradiction. Therefore there are an infinite number of Ulam numbers.

29. Determine the value of $\prod_{k=1}^{100} \frac{k + 1}{k}$. (The notation used here for products is defined in the preamble to Exercise 43 in Section 2.4.)
    - ❌ (tried solving with faculties)
    - ✅ The numerator in the fraction for $k$ cancels the denominator in the fraction for $k + 1$. So all that remains of the product is the numerator for $k = 100$ and the denominator for $k = 1$, namely $101/1=101$.

30. (∗) Determine a rule for generating the terms of the sequence that begins $1, 3, 4, 8, 15, 27, 50, 92, . . .$, and find the next four terms of the sequence.
    - $a_n = n + a_{n-1} + a_{n-2} + a_{n-3}$.
    - $169, 311, 572, 1052$.

31. (∗) Determine a rule for generating the terms of the sequence that begins $2, 3, 3, 5, 10, 13, 39, 43, 172, 177, 885, 891, . . .$, and find the next four terms of the sequence.
    - ⭕ In this sequence, we notice that $10 = 2 · 5, 39 = 3 · 13, 172 = 4 · 43$, and $885 = 5 · 177$. We then also notice that $3 = 1 · 3$ for the second and third terms. So each odd-indexed term (assuming that we call the first term $a_1$) comes from the term before it, by multiplying by successively larger integers. In symbols, this says that $a_{2n+1} = n·a_{2n}$ for all $n > 0$. Then we notice that the even-indexed terms are obtained in a similar way by adding: $a_{2n} = n + a_{2n-1}$ for all $n > 0$. So the next four terms are $a_{13} = 6 · 891 = 5346, a_{14} = 7 + 5346 = 5353, a_{15} = 7 · 5353 = 37471$ and $a_{16} = 8 + 37471=37479$.

32. Show that the set of irrational numbers is an uncountable set.
    - ❌ As irratioal numbers can be expressed as nth roots, where n is a decimal number, the same kind of proof as for the real numbers applies such that between any two roots another one can be found that has different decimal-places.
    - ✅ We know that the set of rational numbers is countable. If the set of irrational numbers were also countable, then the union of these two sets would also be countable by Theorem 1 in Section 2.5. But their union, the set of real numbers, is known to be uncountable. This contradiction tells us that the set of irrational numbers is not countable.

33. Show that the set $S$ is a countable set if there is a function $f$ from $S$ to the positive integers such that $f^{−1}(j)$ is countable whenever $j$ is a positive integer.
    - ❌ As $f^{−1}(j)$ is $S$, where $j$ is a positive integer, then bd. $S$ is countable.
    - ✅ If such a function $f$ exists, then $S$ equals the union of a countable number of countable sets, namely $f^{−1}( 1) ∪ f^{−1}(2) ∪ · · ·$. It follows from Exercise 27 in Section 2.5 that S is countable.

34. Show that the set of all finite subsets of the set of positive integers is a countable set.
    - ❌ We can count by successively creating the powerset of a certain finite subset of ℤ⁺ and then incrementing the subset by one and repeating the procedure (First we have $1$ with $P = \{∅, \{1\}\}$, then $2$ with $P = \{∅, \{1\}, \{2\}, \{1, 2\}\}$ and so on).
    - ✅⚠️  A finite subset of $Z+$ has a largest element and therefore is a subset of $\{1, 2, 3, . . . , n\}$ for some positive integer $n$. Let $S_n$ be the set of subsets of $\{1, 2, 3, . . . , n\}$. It is finite and therefore countable; in fact, $|Sn | = 2n$. The set of all finite subsets of  $Z+$ is the union $\bigcup_{n=1}^{∞} S_n$. Being a countable union of countable sets, it is countable by Exercise 27 in Section 2.5.

35. (∗∗) ❓ Show that $|ℝ × ℝ| = |ℝ|$. [Hint: Use the Schröder-Bernstein theorem to show that $|(0, 1) × (0, 1)| = |(0, 1)|$. To construct an injection from $(0, 1) × (0, 1)$ to $(0, 1)$, suppose that $(x, y) ∈ (0, 1) × (0, 1)$. Map $(x, y)$ to the number with decimal expansion formed by alternating between the digits in the decimal expansions of $x$ and $y$, which do not end with an infinite string of $9s$.]
    - ✅⚠️ (see SSG)

36. (∗∗) ❓ Show that $C$, the set of complex numbers has the same cardinality as $R$, the set of real numbers.
    - ✅ This follows immediately from Exercise 35, because $C$ can be identified with $R × R$ by sending the complex number $a + bi$, where $a$ and $b$ are real numbers, to the ordered pair $(a, b)$.

37. Find $A^n$ if $A$ is
- ❌ (see notes)
- ✅ Since $A^4 = I$, the pattern will repeat from here: $A^5 = A^4 A = IA = A, A^6 = A^2 , A^7 = A^3$, and so on.
$$
  A^{4n+1} = \left[ \begin{array}{cc}
  0 & 1 \\
  -1 & 0 \\
  \end{array} \right]
  A^{4n+2} = \left[ \begin{array}{cc}
  -1 & 0 \\
  0 & -1 \\
  \end{array} \right]
  A^{4n+3} = \left[ \begin{array}{cc}
  0 & -1 \\
  1 & 0 \\
  \end{array} \right]
  A^{4n+4} = \left[ \begin{array}{cc}
  1 & 0 \\
  0 & 1 \\
  \end{array} \right]
$$

38. Show that if $A = cI$, where $c$ is a real number and $I$ is the $n × n$ identity matrix, then $AB = BA$ whenever $B$ is an $n × n$ matrix.
    - ⭕ (see notes)
    - ✅ Since A is the matrix defined by $aii = c$ and $aij = 0$ for $i ≠ j$, ⭕ it is easy to see from the definition of multiplication that $AB$ and $BA$ are both the same as $B$ except that every entry has been multiplied by $c$. Therefore these two matrices are equal.

39. ❓ Show that if $A$ is a $2 × 2$ matrix such that $AB = BA$ whenever $B$ is a $2 × 2$ matrix, then $A = cI$, where $c$ is a real number and $I$ is the $2 × 2$ identity matrix.
    - ✅ (The notation $cI$ means the identity matrix $I$ with each entry multiplied by the real number $c$; thus this matrix consists of c's along the main diagonal and 0's elsewhere.) Let $A = \left[ \begin{array}{cc}
    u & v \\
    w & x \\
    \end{array} \right]$ .We will determine what these entries have to be by using the fact that $AB = BA$ for a few judiciously chosen matrices $B$. First let $B = \left[ \begin{array}{cc}
    0 & 1 \\
    0 & 0 \\
    \end{array} \right]$. Then $AB = \left[ \begin{array}{cc}
    0 & u \\
    0 & w \\
    \end{array} \right]$, and $BA = \left[ \begin{array}{cc}
    w & x \\
    0 & 0 \\
    \end{array} \right]$. Since these two must be equal, we know that $0 = w$ and $u = x$. Next choose $B = \left[ \begin{array}{cc}
    0 & 0 \\
    1 & 0 \\
    \end{array} \right]$. Then we get $\left[ \begin{array}{cc}
    v & 0 \\
    x & 0 \\
    \end{array} \right] = \left[ \begin{array}{cc}
    0 & 0 \\
    u & v \\
    \end{array} \right]$, whence $v = 0$. Therefore the matrix $A$ must be in the form $\left[ \begin{array}{cc}
    u & 0 \\
    0 & u \\
    \end{array} \right]$, which is just $u$ times the identity matrix, as desired.

40. ❓ Show that if $A$ and $B$ are invertible matrices and $AB$ exists, then $(AB)^{−1} = B^{−1}A^{−1}$.
    - ✅⚠️ We simply need to show that the alleged inverse of $AB$ has the correct defining property—that its product with $AB$ (on either side) is the identity. Thus we compute $$(AB)(B^{−1} A^{−1} ) = A(BB^{−1} )A^{−1} = AIA^{−1} = AA^{−1} = I ,$$ and similarly $(B^{−1} A^{−1} )(AB) = I$. Therefore $(AB)^{−1} = B^{−1}A^{−1}$. (Note that the indicated matrix multiplications were all defined, since the hypotheses implied that both $A$ and $B$ were $n × n$ matrices for some (and the same) $n$.)

41. Let $A$ be an $n × n$ matrix and let $0$ be the $n × n$ matrix all of whose entries are zero. Show that the following are true.
- (a) $A ⊙ 0 = 0 ⊙ A = 0$
  - $A ⊙ 0 = c_{ij} = (a_{i1} ∧ 0) ∨ (a_{i1} ∧ 0) ∨ ... ∨ (a_{in} ∧ 0) = 0$ (wlog. for $0 ⊙ A$).
- (b) $A ∨ 0 = 0 ∨ A = A$
  - $A ∨ 0 = [c_{ij}] = a_{ij} ∨ 0 = a_{ij}$ (wlog. for $0 ∨ A$).
- (c) $A ∧ 0 = 0 ∧ A = 0$
  - $A ∧ 0 = [c_{ij}] = a_{ij} ∧ 0 = 0$ (wlog. for $0 ∧ A$).
