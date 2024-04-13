# 2.3 Functions

1. Why is f not a function from ℝ to ℝ if
- (a) $f(x) = 1/x$
  - undefined for 0
- (b) $f(x) = \sqrt{x}$
  - undefined or ℝ → ℂ
- (c) $f(x) = ±\sqrt{(x² + 1)}$
  - ⭕ ambiguous, two possible values for x (pos./neg. root)

2. Determine whether $f$ is a function from ℤ to ℝ if
- (a) $f(n) = ±n$
  - no, ambiguous
- (b) $f(n) = \sqrt{n² + 1}$
  - yes, principal root
- (c) $f(n) = 1/(n² − 4)$
  - ❌ yes ✅ undefined for 2 and -2

3. Determine whether $f$ is a function from the set of all bit strings to the set of integers if
- (a) $f(S)$ is the position of a 0 bit in $S$.
  - ❌ yes ✅ there may be no or more than one value for $S$
- (b) $f(S)$ is the number of 1 bits in $S$.
  - yes
- (c) $f(S)$ is the smallest integer $i$ such that the ith bit of $S$ is 1 and $f(S) = 0$ when $S$ is the empty string, the string with no bits.
  - ❌ yes ✅ undefined for all-zero strings

4. Find the domain and range of these functions. Note that in each case, to find the domain, determine the set of elements assigned values by the function.
- (a) the function that assigns to each nonnegative integer its last digit
  - $ℤ⁺_0 → \{0,1,2,3,4,5,6,7,8,9\}$.
- (b) the function that assigns the next largest integer to a positive integer
  - $ℤ⁺ → ❌ ℤ⁺ ✅ (n > 1)$
- (c) the function that assigns to a bit string the number of one bits in the string
  - $S → ℤ⁺_0$
- (d) the function that assigns to a bit string the number of bits in the string
  - $S → ℤ⁺_0$

5. Find the domain and range of these functions. Note that in each case, to find the domain, determine the set of elements assigned values by the function.
- (a) the function that assigns to each bit string the number of ones in the string minus the number of zeros in the string
  - $S → ℤ$
- (b) the function that assigns to each bit string twice the number of zeros in that string
  - $S → ℤ⁺_0 $ ⭕ all even n
- (c) the function that assigns the number of bits left over when a bit string is split into bytes (which are blocks of 8 bits)
  - $S → ❌ ℤ⁺_0 ✅ \{0,1,2,3,4,5,6,7\}$
- (d) the function that assigns to each positive integer the largest perfect square not exceeding this integer
  - $ℤ⁺ → ❌ ℤ⁺ ✅ \{1,4,8,16,...\}$

6. Find the domain and range of these functions.
- (a) the function that assigns to each pair of positive integers the first integer of the pair
  - $ℤ⁺ → ℤ⁺$
  - ⭕ $ℤ⁺ \times ℤ⁺ → ℤ⁺$
- (b) the function that assigns to each positive integer its largest decimal digit
  - $ℤ⁺ → \{1,2,3,4,5,6,7,8,9\}$
- (c) the function that assigns to a bit string the number of ones minus the number of zeros in the string
  - $S → ℤ$
- (d) the function that assigns to each positive integer the largest integer not exceeding the square root of the integer
  - $ℤ⁺ → ℤ⁺$
- (e) the function that assigns to a bit string the longest string of ones in the string
  - $S → \{\lambda,1,11,111,...\}$

7. Find the domain and range of these functions.
- (a) the function that assigns to each pair of positive integers the maximum of these two integers
  - $ℤ⁺ \times ℤ⁺ → ℤ⁺$
- (b) the function that assigns to each positive integer the number of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 that do not appear as decimal digits of the integer
  - $ℤ⁺ → \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$
- (c) the function that assigns to a bit string the number of times the block 11 appears
  - $S → ℤ⁺_0$ ✔ $ℕ$
- (d) the function that assigns to a bit string the numerical position of the first 1 in the string and that assigns the value 0 to a bit string consisting of all 0s
  - $S → ℤ⁺_0$ ✔ $ℕ$

8. Find these values.
- (a) ⌊1.1⌋ $1$
- (b) ⌈1.1⌉ $2$
- (c) ⌊−0.1⌋ $-1$
- (d) ⌈−0.1⌉ $0$
- (e) ⌈2.99⌉ $3$
- (f) ⌈−2.99⌉ $-2$
- (g) ⌊1/2 + ⌈1/2⌉⌋ $1$
- (h) ⌈⌊1/2⌋ + ⌈1/2⌉ + 1/2⌉ $2$

9. Find these values.
- (a) ⌈3/4⌉ $1$
- (b) ⌊7/8⌋ $0$
- (c) ⌈−3/4⌉ $0$
- (d) ⌊−7/8⌋ ❌ $1$ ✅ $-1$
- (e) ⌈3⌉ $3$
- (f) ⌊−1⌋ $-1$
- (g) ⌊1/2 + ⌈3/2⌉⌋ ❌ $1$ ✅ $2$
- (h) ⌊1/2 · ⌊5/2⌋⌋ ❌ $2$ ✅ $1$

10. Determine whether each of these functions from {a, b, c, d} to itself is one-to-one.
- (a) $f(a) = b$, $f(b) = a$, $f(c) = c$, $f(d) = d$ **Yes**
- (b) $f(a) = b$, $f(b) = b$, $f(c) = d$, $f(d) = c$ **No f(a), f(b)**
- (c) $f(a) = d$, $f(b) = b$, $f(c) = c$, $f(d) = d$ **No f(a), f(d)**

11. Which functions in Exercise 10 are onto?
    - a

12. Determine whether each of these functions from ℤ to ℤ is one-to-one.
- (a) $f(n) = n − 1$
  - Yes
- (b) $f(n) = n² + 1$
  - No, n and -n result in the same value
- (c) $f(n) = n³$
  - Yes
- (d) $f(n) = ⌈n/2⌉$
  - ❌ Yes ✅ No $f (3) = f (4) = 2$

13. Which functions in Exercise 12 are onto?
    - a, ⭕ d; $f(2x) = ⌈2x/2⌉ = ⌈x⌉ = x \text{ for all } x ∈ ℤ$

14. Determine whether $f : ℤ × ℤ → ℤ$ is onto if
- (a) $f(m,n) = 2m − n$
  - Yes, ⭕ $f(0, -n) = n$
- (b) $f(m,n) = m² − n² $
  - No, ❌ $f(\sqrt{m}, \sqrt{n})$ undefined for negative Integers.
  - ✅ This is not onto, since, for example, 2 is not in the range. To see this, if $m^2 − n^2 = (m − n)(m + n) = 2$, then $m$ and $n$ must have same parity (both even or both odd). In either case, both $m − n$ and $m + n$ are then even, so this expression is divisible by $4$ and hence cannot equal $2$.
- (c) $f(m,n) = m + n + 1$
  - Yes, ❌ $m + n + 1 → m = - n - 1$
  - ✅ $f(0, n - 1) = n$
- (d) $f(m,n) = |m| − |n|$
  - Yes, ❌ let $n = m + 1$ then $|m| − |m + 1| = |m - 1|$
  - ✅ to achieve negative values we set $m = 0$ and to achieve positive values we set $n = 0$
- (e) $f(m,n) = m² − 4$
  - ❎ No, the lowest negative value will be $-4$ for $m = 0$

15. Determine whether the function $f : ℤ × ℤ → ℤ$ is onto if
- (a) $f(m,n) = m + n$
  - Yes, $f(0,n) = n$
- (b) $f(m,n) = m² + n²$
  - No, the range is $ℤ⁺_0$
- (c) $f(m,n) = m$
  - Yes, trivially
- (d) $f(m,n) = |n|$
  - No, the range is $ℤ⁺_0$
- (e) $f(m,n) = m − n$
  - Yes, $f(m,0) = m$

16. Consider these functions from the set of students in a discrete mathematics class. Under what conditions is the function one-to-one if it assigns to a student his or her
- (a) mobile phone number.
  - ❌ If every student as no or 1 number.
  - ✅ If no two students have the same number.
- (b) student identification number.
  - Should be one-to-one unless a mistake has happened when assigning the IDs.
- (c) final grade in the class.
  - ❌ One-to-one.
  - ✅ Not o-t-o, multiple students will probably have the same grade.
- (d) home town.
  - Not o-t-o, multiple students will probably live in the same town.

17. Consider these functions from the set of teachers in a school. Under what conditions is the function one-to-one if it assigns to a teacher his or her
- (a) office.
  - If no two teacher share an office.
- (b) assigned bus to chaperone in a group of buses taking students on a field trip.
  - If each bus is chaperoned by only one teacher.
- (c) salary.
  - Considering that teachers in public schools have fixed salary categories, probably not one-to-one.
- (d) social security number.
  - Must be one-to-one.

18. Specify a codomain for each of the functions in Exercise 16. Under what conditions is each of these functions with the codomain you specified onto?
- (a) mobile phone number.
  - All numbers available from all service providers.
  - If all (possible) numbers are assigned
- (b) student identification number.
  - All n-digit numbers, depending on the encoding scheme.
  - Very unlikely to be onto.
- (c) final grade in the class.
  - Grade range.
  - May or may not be onto.
- (d) home town.
  - ❎ All home towns of students at the school.
  - ❎ Unlikely to be onto, as the subset of students in the class is small.

19. ❕ Specify a codomain for each of the functions in Exercise 17. Under what conditions is each of the functions with the codomain you specified onto?

20. Give an example of a function from ℕ to ℕ that is
- (a) one-to-one but not onto.
  - $f(x) = x²$ ✔ $f(x) = n + 17$
- (b) onto but not one-to-one.
  - ⭕ $f(n) = ⌈n/2⌉$
- (c) both onto and one-to-one (but different from the identity function).
  - ⭕ We let $f (n) = n − 1$ for even values of $n$, and $f (n) = n + 1$ for odd values of $n$.
- (d) neither one-to-one nor onto.
  - $f(n) = ⌈n/2⌉ + 1$ ✔ $f(x) = 17$

21. Give an explicit formula for a function from ℤ to ℤ⁺ that is
- (a) one-to-one, but not onto.
  - ❎ $$
    f(x) =
      \begin{cases}
        x + 2 & \text{if x ≥ 0} \\
        0 & \text{if x < 0}
      \end{cases}
    $$
  - ✅ $$
    f(x) =
      \begin{cases}
        3x + 3 & \text{if x ≥ 0} \\
        3|x| + 1 & \text{if x < 0}
      \end{cases}
    $$
- (b) onto, but not one-to-one.
  - $f(x) = |x| + 1$
- (c) one-to-one and onto.
  - ❌ $$
    f(x) =
      \begin{cases}
        2x + 2 & \text{if x ≥ 0} \\
        |x| + (|x| - 1) & \text{if x < 0}
      \end{cases}
    $$
  - ✅ $$
    f(x) =
      \begin{cases}
        2x + 1 & \text{if x ≥ 0} \\
        2|x| & \text{if x < 0}
      \end{cases}
    $$
- (d) neither one-to-one nor onto.
  - $f(n) = n²$
22. Determine whether each of these functions is a bijection from ℝ to ℝ.
- (a) $f(x) = −3x + 4$
  - ❌ No; not onto. ✅ Inverse is $f^{−1} (x) = (4 − x)/3$
- (b) $f(x) = −3x² + 7$
  - No, it is not one-to-one because $y = ±\sqrt{-1/3(x - 7)}$ where $y$ is in the domain.
- (c) $f(x) = (x + 1)/(x + 2)$
  - Not onto because discontinuity at $f(-2)=u.$
  - ✔  This function is a bijection, but not from ℝ to ℝ. To see that the domain and range are not ℝ, note that $x = −2$ is not in the domain, and $x = 1$ is not in the range. On the other hand, $f$ is a bijection from ℝ − {−2} to ℝ − {1} , since its inverse is $f^{−1}(x) = (1 − 2x)/(x − 1)$
- (d) $f(x) = x⁵ + 1$
  - $x = y⁵ + 1$
  - $f^{−1}(x) = \sqrt[5]{x - 1}$
  - Yes, fifth-root keeps sign.

23. Determine whether each of these functions is a bijection from ℝ to ℝ.
- (a) $f(x) = 2x + 1$
  - Yes; $f^{−1}(y) = (y - 1)/2$.
  - ✔ Alternatively, we can argue directly. To show that the function is one-to-one, note that if $2x + 1 = 2x' + 1$, then $x = x'$. To show that the function is onto, note that $2( (y - 1) /2) + 1 = y$, so every number is in the range.
- (b) $f(x) = x² + 1$
  - No, not one-to-one; $f(-1) = 2$, $f(1) = 2$.
  - ✔ not surjective either: range is $[1, ∞)$
- (c) $f(x) = x³$
  - Yes; $f^{−1}(y) = \sqrt[3]{y}$.
- (d) $f(x) = (x² + 1)/(x² + 2)$
  - Not one-to-one; $ℝ⁻$ not in the range. ✔  $\{ y \mid 0.5 ≤ y < 1\} = [0.5, 1)$

24. Let $f : ℝ → ℝ$ and let $f(x) > 0$ for all $x ∈ ℝ$. Show that $f(x)$ is strictly increasing if and only if the function $g(x) = 1/f(x)$ is strictly decreasing.
    - We must show that if $f(x) < f(y)$, whenever $x < y$, then $g(x) > g(y)$, whenever $x > y$ and vice versa.
    - Assuming $f(x) < f(y)$, ⭕ **To show that g is strictly decreasing, suppose that x < y**. then $1/f(x) > 1/f(y)$ because both sides will be positive (and not undefined) according to the hypothesis $f(x) > 0$. So $g(x) > g(y)$.
    - Assuming $g(x) > g(y)$ then $1/f(x) > 1/f(y)$ wich by multiplication gives $f(y) > f(x)$.

25. Let $f : ℝ → ℝ$ and let $f(x) > 0$ for all $x ∈ ℝ$. Show that $f(x)$ is strictly decreasing if and only if the function $g(x) = 1/f(x)$ is strictly increasing.
    - see above wlog.

26. Parts:
- (a) Prove that a strictly increasing function from ℝ to itself is one-to-one.
  - We must show that if $f(x) < f(y)$, whenever $x < y$, then if $f(x) = f(y)$, whenever $x = y$.
  - Suppose that $x < y$, then $x ≠ y$. ⭕
  - ✅ Let $f : ℝ → ℝ$ be the given function. We are told that $f (x) < f (y)$ whenever $x < y$. We need to show that $f(x) ≠ f (y)$ whenever $x ≠ y$. This follows immediately from the given conditions, because without loss of generality, we may assume that $x < y$.
- (b) Give an example of an increasing function from ℝ to itself that is not one-to-one.
  - $f(x) = ⌈x⌉$ (not strictly increasing)
  - ✔ We could take the trivial function $f(x) = 17$. If we want the range to be all of ℝ, we could define $f$ in parts this way: $f (x) = x$ for $x < 0$; $f (x) = 0$ for $0 ≤ x ≤ 1$; and $f (x) = x − 1$ for $x > 1$.

27. Parts:
- (a) Prove that a strictly decreasing function from ℝ to itself is one-to-one.
  - Let $f : ℝ → ℝ$ be the given function. We know that $f(x) > f(y)$ whenever $x < y$. We must show that $f(x) ≠ f(y)$ when $x ≠ y$ which follows from the condition that $x < y$. ⭕ The second case is that $x > y$, then $f(x) < f(y)$. So $x ≠ y$ in both cases.
- (b) Give an example of a decreasing function from ℝ to itself that is not one-to-one.
  - ❌ A multipart-function could be $f(x) = x - 1$ for $x > 1$, $f(x) = 0$ for $1 ≥ x ≥ 0$ and $f(x) = x - 1$ for $x < 0$.
  - $f(x) = -x - 1$ for $x < -1$, $f(x) = 0$ for $1 ≤ x ≤ 0$ and $f(x) = -x + 1$ for $x < 0$

28. ❓ Show that the function $f(x) = e^x$ from the set of real numbers to the set of real numbers is not invertible, but if the codomain is restricted to the set of positive real numbers, the resulting function is invertible.
    - ✅ For the function to be invertible, it must be a one-to-one correspondence. This means that it has to be one-to-one, which it is, and onto, which it is not, because, its range is the set of positive real numbers, rather than the set of all real numbers. When we restrict the codomain to be the set of positive real numbers, we get an invertible function. In fact, there is a well-known name for the inverse function in this case—the natural logarithm function $g(x) = ln x$.

29. Show that the function $f(x) = |x|$ from the set of real numbers to the set of nonnegative real numbers is not invertible, but if the domain is restricted to the set of nonnegative real numbers, the resulting function is invertible.
    - Assuming $f: ℝ → ℝ⁺_0$ then the inverse would be $|f(x)| = x$ which means $f(x)^{-1} = x$ for $f(x) ≥ 0$ and $f(x)^{-1} = -x$ for $f(x) < 0$. But as the codomain is $ℝ⁺_0$ the second case does not apply so no negative values can be reached in the domain. By restricting the latter to nonnegative values we get $f(x)^{-1} = f(x) = x$.
    - ✔ The function is not one-to-one (for example, $f(2) = 2 = f(-2)$), so it is not invertible. On the restricted domain, the function is the identity function from the set of nonnegative real numbers to itself, $f(x) = x$, so it is one-to-one and onto and therefore invertible; in fact, it is its own inverse.

30. Let $S = \{−1, 0, 2, 4, 7\}$. Find $f(S)$ if
- (a) $f(x) = 1$
  - $\{1\}$
- (b) $f(x) = 2x + 1$
  - $\{-1, 1, 5, 9, 15\}$
- (c) $f(x) = ⌈x/5⌉$
  - $\{0, 1, 2\}$
- (d) $f(x) = ⌊(x² + 1)/3⌋$
  - $\{0, 1, 5, 16 \}$

31. Let $f(x) = ⌊x²/3⌋$. Find $f(S)$ if
- (a) $S = \{−2, −1, 0, 1, 2, 3\}$
  - $\{0, 1, 3\}$
- (b) $S = \{0, 1, 2, 3, 4, 5\}$
  - $\{0, 1, 3, 5, 8\}$
- (c) $S = \{1, 5, 7, 11\}$
  - $\{0, 8, 16, 40\}$
- (d) $S = \{2, 6, 10, 14\}$
  - $\{1, 12, 33, 65\}$

32. Let $f(x) = 2x$ where the domain is the set of real numbers. What is
- (a) $f(ℤ)$?
  - $\{x ∈ ℤ \mid x = 2k\}$
- (b) $f(ℕ)$?
  - the set of even natural numbers
- (c) $f(ℝ)$?
  - ⭕ the set of real numbers

 -->
33. Suppose that $g$ is a function from $A$ to $B$ and $f$ is a function from $B$ to $C$.
- (a) Show that if both $f$ and $g$ are one-to-one functions, then $f ◦ g$ is also one-to-one.
  - ❎ First note that $f ◦ g$ is defined as the range of $g$ is a subset of the domain of $f$. To show that $f(g(x))$ is one-to-one when $f$ and $g$ are, we must show that $f(g(x_1)) = f(g(x_2))$ whenever $x_1 = x_2$. Assuming $x_1 = x_2$ then by the hypothesis $g(x_1) = g(x_2)$. So $f(g(x_1)) = f(g(x_2))$, again by the hypothesis.
  - ✅ Assume that both f and g are one-to-one. We need to show that $f ◦ g$ is one-to-one. This means that we need to show that if $x$ and $y$ are two distinct elements of $A$, then $f(g(x)) ≠ f(g(y))$. First, since $g$ is one-to-one, the definition tells us that $g(x) ≠ g(y)$. Second, since now $g(x)$ and $g(y)$ are distinct elements of $B$, and since $f$ is one-to-one, we conclude that $f(g(x)) ≠ f(g(y))$, as desired.

- (b) Show that if both $f$ and $g$ are onto functions, then $f ◦ g$ is also onto.
  - ❎ To show that $f ◦ g$ is onto, we must show that for any element $y$ of the codomain of $f ◦ g$ ($C$) there is an $x$ in the domain ($A$) of $f ◦ g$ such that $f(g(x)) = y$. Assuming $y ∈ B$ then, as $g$ is onto, we know that there is a $x ∈ A$ such that $g(x) = y$. Assuming $z ∈ C$ as $f$ is also onto, we know that there is a $y ∈ B$ such that $f(y) = z$. So $f(g(x)) = z$.
  - ✅ (Same argumentation but starting with $f$ and then looking at $g$.)

34. (∗) If $f$ and $f ◦ g$ are one-to-one, does it follow that $g$ is one-to-one? Justify your answer.
    - By the definitions we know that $f(x_1) = f(x_2)$ and $f(g(x_1)) = f(g(x_2))$ if $x_1 = x_2$. That means if $g(x_1) = g(x_2)$ then $f(g(x_1)) = f(g(x_2))$. To see that $g(x_1) = g(x_2)$ if $x_1 = x_2$ suppose ❌ $g(x_1) ≠ g(x_2)$. Then $f(g(x_1)) ≠ f(g(x_2))$ which contradicts the hypothesis.
    - ✅ To clarify the setting, suppose that $g : A → B$ and $f : B → C$, so that $f ◦ g: A → C$. We will prove that if $f ◦ g$ is one-to-one, then $g$ is also one-to-one, so not only is the answer to the question “yes,” but part of the hypothesis is not even needed. Suppose that $g$ were not one-to-one. By definition this means that there are distinct elements $a_1$ and $a_2$ in $A$ such that $g(a_1) = g(a_2)$. Then certainly $f(g(a_1)) = f(g(a_2))$, which is the same statement as $(f ◦ g)(a_1) = (f ◦ g)(a_2)$. By definition this means that $f ◦ g$ is not one-to-one, and our proof is complete.

35. (∗) If $f$ and $f ◦ g$ are onto, does it follow that $g$ is onto? Justify your answer.
    - To clarify the setting, suppose that $g : A → B$ and $f : B → C$, so that $f ◦ g: A → C$. We know that for for every $c ∈ C$ there is an $a ∈ A$ such that $(f ◦ g)(a) = c$  and that for every $c ∈ C$ there is an $b ∈ B$ such that $f(b) = c$ . If $g$ is not onto there might still be a $b$ for which there is no $a$ but for which $f(b) = c$ holds. So $g$ might not be onto.
    - ✔ For a simple counterexample, suppose that $A = {a}$, $B = {b_1 ,b_2}$, and $C = {c}$. Let $g(a) = b_1$, and let $f(b_1) = c$ and $f(b_2) = c$. Then clearly $f$ and $f ◦ g$ are onto, but $g$ is not, since $b_2$ is not in its range.

36. Find $f ◦ g$ and $g ◦ f$, where $f(x) = x² + 1$ and $g(x) = x + 2$, are functions from ℝ to ℝ.
    - $(f ◦ g)(x) = (x + 2)² + 1 = x² + 4x + 5$
    - $(g ◦ f)(x) = (x² + 1) + 2 = x² + 3$

37. Find $f + g$ and $fg$ for the functions $f$ and $g$ given in Exercise 36.
    - $(f + g)(x) = (x² + 1) + (x + 2) = x² + x + 3$
    - $(fg)(x) = (x² + 1)(x + 2) = x³ + 2x² + x + 2$

38. Let $f(x) = ax + b$ and $g(x) = cx + d$, where $a$, $b$, $c$, and $d$ are constants. Determine necessary and sufficient conditions on the constants $a$, $b$, $c$, and $d$ so that $f ◦ g = g ◦ f$.
    - $(f ◦ g)(x) = a(cx + d) + b = acx + ad + b$
    - $(g ◦ f)(x) = c(ax + b) + d = cax + cb + d$
    - $ad + b$ has to equal $cb + d$, ❌ so $a$ must equal $c$ and $d$ $c$, or vice versa. Additionally $b$ and $d$ must be equal in any case. Of course these constants could also be $0$.
    - ✅ equality holds for all 4-tuples $(a, b, c, d)$ for which $ad + b = cb + d$

39. Show that the function $f(x) = ax + b$ from ℝ to ℝ is invertible, where $a$ and $b$ are constants, with $a ≠ 0$, and find the inverse of $f$.
    - ❎ To show that $f$ is invertible we must show that it is a one-to-one-correspondence, so it must be injective and surjective.
    - ❎ One-to-one: To be injective, for very two distinct elements of the domain the results in the range must be distinct as well. Assuming $x_1$ and $x_2$ such that $x_1 ≠ x_2$, then $ax_1 + b = ax_2 + b = x_1 + b = x_2 + b = x_1 = x_2$ is false by our assumption. So the values in the range are also distinct.
    - ❎ Onto: To be surjective codomain and range must be identical. So for every real number $y$ there must be a real number $x$ such that $f(x) = y$ which holds iff $y = ax + b$ which is equal to $\frac{y - b}{a} = x$. As we know $a ≠ 0$ this is defined for all ℝ.
    - Inverse: $f(y)^{-1} = (y - b)a$
    - ⭕ Check correctness with the identity-functions $f ◦ f(x)^{-1}$ and $f(x)^{-1} ◦ f$.

40. Let $f$ be a function from the set $A$ to the set $B$. Let $S$ and $T$ be subsets of $A$. Show that
- (a) $f(S ∪ T) = f(S) ∪ f(T)$
  - As the codomain for $f$ is known to be $B$ it is sufficient to show the equality of the domain-sets, so we show both sides of the equation are a subset of the other.
  - ⭕ For $f(S ∪ T) = b$ we know $a ∈ S ∪ T$. Either $a ∈ S$ or $a ∈ T$ which is equivalent to $f(S)$ or $f(T)$ which btdo. union is $f(S) ∪ f(T)$.
  - ⭕ Starting from $f(S) ∪ f(T)$ we see that if $f(S) = b_1$ and $f(T) = b_2$, then $a_1 ∈ S$ and $a_2 ∈ T$. Combining into a union we get $S ∪ T$ which shows that $f(S ∪ T)$ is indeed equal.
  - ✅ This really has two parts. First suppose that $b$ is in $f(S ∪ T)$. Thus $b = f(a)$ for some $a ∈ S ∪ T$. Either $a ∈ S$, in which case $b ∈ f(S)$, or $a ∈ T$, in which case $b ∈ f(T)$. Thus in either case $b ∈ f(S) ∪ f(T)$. This shows that $f(S ∪ T) ⊆ f(S) ∪ f(T)$.
  - Conversely, suppose $b ∈ f(S) ∪ f(T)$. Then either $b ∈ f(S)$ or $b ∈ f(T)$. This means either that $b = f(a)$ for some $a ∈ S$ or that $b = f(a)$ for some $a ∈ T$. In either case, $b = f(a)$ for some $a ∈ S ∪ T$, so $b ∈ f(S ∪ T)$. This shows that $f(S) ∪ f(T) ⊆ f(S ∪ T)$, and our proof is complete.
- (b) $f(S ∩ T) ⊆ f(S) ∩ f(T)$
  - Assuming $b ∈ f(S ∩ T)$ then $b = f(a)$ for some $a ∈ S ∩ T$, then this $a$ is in both $S$ and $T$. So $b = f(a)$ for $a ∈ S$ and $a ∈ T$, so we have ⭕ **$b ∈ f (S)$ and $b ∈ f (T)$** which gives us $f(S) ∩ f(T)$.

41. Parts:
- (a) Give an example to show that the inclusion in part (b) in Exercise 40 may be proper.
  - ❌ As $f(S) ∩ f(T)$ is a (improper) subset of $S ∩ T$ there may be elements not within $f(S) ∩ f(T)$ but within $S ∩ T$. $f(S ∩ T)$ on the other hand is also a subset of $S ∩ T$ where some elements may be not in $f(S ∩ T)$. But there is no evidence to suggest that these cases are the same.
  - ✅  Let us arrange for $S$ and $T$ to be nonempty sets that have empty intersection. Then the left-hand side will be $f(∅)$, which is the empty set. If we can make the right-hand side nonempty, then we will be done. We can make the right-hand side nonempty by making the codomain consist of just one element, so that $f(S)$ and $f(T)$ will both be the set consisting of that one element. The simplest example is as follows. Let $A = \{1, 2\}$ and $B = \{3\}$. Let f be the unique function from $A$ to $B$ (namely $f(1) = f(2) = 3$). Let $S = \{1\}$ and $T = \{2\}$. Then $f(S ∩ T) = f(∅) = ∅$, which is a proper subset of $f(S) ∩ f(T) = \{3\} ∩ \{3\} = \{3\}$.
- (b) Show that if $f$ is one-to-one, the inclusion in part (b) in Exercise 40 is an equality. ($f(S ∩ T) = f(S) ∩ f(T)$)
  - ❌ Assuming that $f$ is one-to-one $f(a) = f(b)$ whenever $a = b$ where $a$ and $b$ are in $S ∩ T$. Thus
  - ✅ Assume that f is one-to-one. We must show that every element of $f(S) ∩ f(T)$ is an element of $f(S ∩ T)$. Let $y ∈ B$ be an element of $f(S) ∩ f(T)$. Then $y ∈ f(S)$, so $y = f(x_1)$ for some $x_1 ∈ S$. Similarly, $y ∈ f(T)$, so $y = f(x_2)$ for some $x_2 ∈ T$. Because $f$ is one-to-one, it follows that $x_1 = x_2$. This element is therefore in $S ∩ T$, so $y ∈ f(S ∩ T)$.

Let $f$ be a function from the set $A$ to the set $B$. Let $S$ be a subset of $B$. We define the **inverse image** of $S$ to be the subset of $A$ whose elements are precisely all pre-images of all elements of $S$. We denote the inverse image of $S$ by $f^{−1}(S)$, so $f^{−1}(S) = \{a ∈ A \mid f(a) ∈ S\}$.

42. Let $f$ be the function from ℝ to ℝ defined by $f(x) = x²$. Find
- (a) $f^{−1} (\{1\})$
  - $\{-1,1\}$
- (b) $f^{−1} (\{x \mid 0 < x < 1\})$
  - $\{x \mid -1 < x < 0 ∨ 0 < x < 1\}$
- (c) $f^{−1} (\{x \mid x > 4\})$
  - $\{x \mid x < -2 ∨ 2 < x\}$

43. Let $g(x) = ⌊x⌋$. Find
- (a) $g^{−1} (\{0\})$
  - $\{x \mid 0 ≤ x < 1\} = [0,1)$
- (b) $g^{−1} (\{−1, 0, 1\})$
  - $\{-1 ≤ x < 2\}$
- (c) $g^{−1} (\{x \mid 0 < x < 1\})$
  - $∅$

44. Let $f$ be a function from $A$ to $B$. Let $S$ and $T$ be subsets of $B$. Show that
- (a) ❓ $f^{−1}(S ∪ T) = f^{−1} (S) ∪ f^{−1}(T)$
  - ✅ We need to prove two things. First suppose $x ∈ f^{−1} (S ∪ T)$. This means that $f (x) ∈ S ∪ T$. Therefore either $f (x) ∈ S$ or $f (x) ∈ T$. In the first case $x ∈ f^{−1}(S)$, and in the second case $x ∈ f^{−1}(T)$. In either case, then, $x ∈ f^{−1} (S) ∪ f^{−1}(T)$. Thus we have shown that $f^{−1} (S ∪ T) ⊆ f^{−1}(S) ∪ f^{−1}(T)$. Conversely, suppose that $x ∈ f^{−1}(S) ∪ f^{−1} (T)$. Then either $x ∈ f^{−1}(S)$ or $x ∈ f^{−1} (T)$, so either $f (x) ∈ S$ or $f (x) ∈ T$. Thus we know that $f (x) ∈ S ∪ T$, so by definition $x ∈ f^{−1} (S ∪ T)$. This shows that $f^{−1} (S) ∪ f^{−1} (T) ⊆ f^{−1} (S ∪ T)$, as desired.
- (b) ❓ $f^{−1}(S ∩ T) = f^{−1} (S) ∩ f^{−1}(T)$
  - ✅ This is similar to part (a). We have $x ∈ f^{−1} (S ∩ T)$ if and only if $f (x) ∈ S ∩ T$, if and only if $f (x) ∈ S$ and $f (x) ∈ T$, if and only if $x ∈ f^{−1} (S)$ and $x ∈ f^{−1} (T)$, if and only if $x ∈ f^{−1} (S) ∩ f^{−1} (T)$.

45. Let $f$ be a function from $A$ to $B$. Let $S$ be a subset of $B$. Show that $f^{−1}(\overline{S}) = \overline{f^{−1}(S)}$.
    - ✔  Note that the complementation here is with respect to the relevant universal set. Thus $\overline{S} = B - S$ and $\overline{f^{−1} (S)} =A - f^{−1}(S)$.
    - $x ∈ f^{−1}(\overline{S})$ iff $f(x) = \overline{S}$ iff $f(x) ∉ S$. Thus $x ∉ f^{−1}(S)$ which means $\overline{f^{−1}(S)}$.
    - Conversely, $x ∈ \overline{f^{−1}(S)}$ iff $x ∉ f^{−1}(S)$ iff $f(x) ≠ S$ iff $f(x) = \overline{S}$. Thus bdto. inverse image $x ∈ f^{−1}(\overline{S})$.

46. Show that $⌊x + 1/2⌋$ is the closest integer to the number $x$, except when $x$ is midway between two integers, when it is the larger of these two integers.
    - ❎ Let $x = n + e$ where $n$ is an integer and $0 ≤ e < 1$. We consider the cases where $e$ is less than or greater than or equal to $1/2$ because they result in the expression being the next smaller or larger integer. First when $0 ≤ e < 1/2$ and $x + 1/2 = n + e + 1/2$, then $⌊x + 1/2⌋ = n$ because $0 ≤ e + 1/2 < 1$. Secondly when $1/2 ≤ e < 1$, then $⌊x + 1/2⌋ = n + 1$ because $1 ≤ e + 1/2 < 3/2$.
    - ✅ There are three cases. Define the “fractional part” of $x$ to be $f(x) = x − ⌊x⌋$. Clearly $f(x)$ is always between 0 and 1 (inclusive at 0, exclusive at 1), and $x = ⌊x⌋ + f(x)$. If $f(x)$ is less than $1/2$, then $x + 1/2$ will have a value slightly less than $⌊x⌋ + 1$, so when we round down, we get $⌊x⌋$. In other words, in this case $⌊x + 1/2⌋ = ⌊x⌋$, and indeed that is the integer closest to $x$. If $f(x)$ is greater than $1/2$, then $x + 1/2$ will have a value slightly greater than $⌊x⌋ + 1$, so when we round down, we get $⌊x⌋ + 1$. In other words, in this case $⌊x + 1/2⌋ = ⌊x⌋ + 1$, and indeed that is the integer closest to $x$ in this case. Finally, if the fractional part is exactly $1/2$, then $x$ is midway between two integers, and $⌊x + 1/2⌋ = ⌊x⌋ + 1$, which is the larger of these two integers.

47. Show that $⌈x − 1/2⌉$ is the closest integer to the number $x$, except when $x$ is midway between two integers, when it is the smaller of these two integers.
    - ❎ We define the 'fractional' part of $x$ to be $f(x) = ⌈x⌉ - x$. It is always between 0 and 1 (inclusive at 0, exclusive at 1), and $x = ⌈x⌉ - f(x)$. If $f(x) ≤ 1/2$ then $x − 1/2$ will be smaller or equal to $⌈x⌉ - 1$ so when we round up, we get $⌊x⌋$. If $f(x) > 1/2$ then $x − 1/2$ will be larger than $⌈x⌉ - 1$ so we get $⌈x⌉$.

48. Show that if $x$ is a real number, then $⌈x⌉ − ⌊x⌋ = 1$ if $x$ is not an integer and $⌈x⌉ − ⌊x⌋ = 0$ if $x$ is an integer.
    - If $x$ is not an integer it must lie between two integers. So $⌈x⌉$ will assign the next largest integer and $⌊x⌋$ the next lowest and the difference of them must be 1. If $x$ is an integer floor and ceiling will be equal to it.

49. Show that if $x$ is a real number, then $x − 1 < ⌊x⌋ ≤ x ≤ ⌈x⌉ < x + 1$.
    - ❌ By definition $⌊x⌋ ≤ x ≤ ⌈x⌉$. As the difference between $x$ and $⌊x⌋$ or $⌈x⌉$ will allways be less than 1 (otherwise it would be an integer and keep its value) the difference between $x$ and $x - 1$ or $x + 1$ will always be larger.
    - ✅ We can write the real number $x$ as $⌊x⌋ + e$, where $e$ is a real number satisfying $0 ≤ e < 1$. Since $e = x - ⌊x⌋$, we have $0 ≤ x - ⌊x⌋ < 1$. The first two inequalities, $x - 1 < ⌊x⌋$ and $⌊x⌋ ≤ x$, follow algebraically. For the other two inequalities, we can write $x = ⌈x⌉ - e$, where again $0 ≤ e < 1$. Then $0 ≤ ⌈x⌉ - x < 1$, and again the desired inequalities follow by algebra.

50. Show that if $x$ is a real number and $m$ is an integer, then $⌈x + m⌉ = ⌈x⌉ + m$.
    - ⭕ As $⌈m⌉ = m$ by assumption and the definition of ceiling, the function can only affect $x$, so $⌈x⌉ + m$.
    - ✅  Write $x = n − e$, where $n$ is an integer and $0 ≤ e < 1$; thus $⌈x⌉ = n$. Then $⌈x + m⌉ = ⌈n - e + m⌉ = n + m = ⌈x⌉ + m$. Alternatively, we could proceed along the lines of the proof of property 4a of Table 1, shown in the text.

51. Show that if $x$ is a real number and $n$ is an integer, then
- (a) ❓ $x < n$ if and only if $⌊x⌋ < n$
  - ✅  One direction (the "only if" part) is obvious: If $x < n$, then since $⌊x⌋ ≤ x$ it follows that $⌊x⌋ < n$. We will prove the other direction (the "if" part) indirectly (we will prove its contrapositive). Suppose that $x ≥ n$. Then "the greatest integer not exceeding $x$" must be at least $n$, since $n$ is an integer not exceeding $x$. That is, $⌊x⌋ ≥ n$.
- (b) $n < x$ if and only if $n < ⌈x⌉$
  - If $n < x$ then $n < ⌈x⌉$ because $x ≤ ⌈x⌉$. Proving the other direction by taking the contrapositive we suppose $n ≥ x$. Then $⌈x⌉$ can be at most $n$. Thus $n ≥ ⌈x⌉$.

52. Show that if $x$ is a real number and $n$ is an integer, then
- (a) $x ≤ n$ if and only if $⌈x⌉ ≤ n$
  - If $x ≤ n$ then $⌈x⌉ ≤ n$ because $x ≤ ⌈x⌉$. If $⌈x⌉ ≤ n$ then $x ≤ n$ because $x ≤ ⌈x⌉$.
- (b) $n ≤ x$ if and only if $n ≤ ⌊x⌋$
  - If $n ≤ x$ then $n ≤ ⌊x⌋$ because $⌊x⌋ ≤ x$. If $n ≤ ⌊x⌋$ then $n ≤ x$ because $⌊x⌋ ≤ x$.

53. Prove that if $n$ is an integer, then $⌊n/2⌋ = n/2$ if $n$ is even and $(n − 1)/2$ if $n$ is odd.
    - ❎ If $n$ is even, then $n/2$ is also an integer so $⌊n/2⌋$ will be exactly that bd. ❌ If $n$ is odd $n − 1$ will be even and $⌊(n − 1)/2⌋$ will be an integer as well. So again bd. $⌊n/2⌋$ will be exactly that.
    - ✅ If $n$ is even, then $n = 2k$ for some integer $k$. Thus $⌊n/2⌋ = ⌊k⌋ = k = n/2$. If $n$ is odd, then $n = 2k + 1$ for some integer $k$. Thus $⌊n/2⌋ = ⌊k + 1/2⌋ = k = (n - 1)/2$.

54. Prove that if $x$ is a real number, then $⌊−x⌋ = −⌈x⌉$ and $⌈−x⌉ = −⌊x⌋$.
    - ❌ As $⌊−x⌋$ is the closest integer smaller than $-x$ and $⌈x⌉$ is the closest integer larger than $x$ we see that $⌊−x⌋ - (-x) = ⌈x⌉ - x$ thus $|⌊−x⌋| = ⌈x⌉$ and $⌊−x⌋ = −⌈x⌉$.
    - ✅ To prove the first equality, write $x = n − e$, where $n$ is an integer and $0 ≤ e < 1$; thus $⌈x⌉ = n$. Therefore, $⌊−x⌋ = ⌊−n + e⌋ = −n = −⌈x⌉$. The second equality is proved in the same manner, writing $x = n + e$, where $n$ is an integer and $0 ≤ e < 1$. This time $⌊x⌋ = n$, and $⌈−x⌉ = ⌈−n - e⌉ = −n = −⌊x⌋$.

55. The function $INT$ is found on some calculators, where $INT(x) = ⌊x⌋$ when $x$ is a nonnegative real number and $INT(x) = ⌈x⌉$ when $x$ is a negative real number. Show that this INT function satisfies the identity $INT(−x) = −INT(x)$.
    - As $INT(x) = ⌊x⌋$ where $0 ≤ x$ and $INT(x) = ⌈x⌉$ where $x < 0$ there are two cases to prove.
    - ⭕ wlog. we can assume that $0 ≤ x$, since the equation to be proved is equivalent to the same equation with $-x$ substituted for $x$.
    - (1) If $0 ≤ x$ then $-x < 0$ so $INT(−x) = ⌈-x⌉$ and $−INT(x) = -⌊x⌋$. To prove $⌈-x⌉ = -⌊x⌋$ we let $x = n + e$, where $n$ is an integer and $0 ≤ e < 1$. Thus $⌊x⌋ = n$ and $⌈-x⌉ = ⌈-n - e⌉ = ⌈-n⌉ = -n = -⌊x⌋$.
    - ~~(2) If $x < 0$ then $0 ≤ -x$~~

56. ❓ Let $a$ and $b$ be real numbers with $a < b$. Use the floor and/or ceiling functions to express the number of integers $n$ that satisfy the inequality $a ≤ n ≤ b$.
    - ✅  If we round a up and round b down to integers, then we will be looking at the smallest and largest integers just inside the range of integers we want to count, respectively. These values are of course $⌈a⌉$ and $⌊b⌋$, respectively. Then the answer is $⌊b⌋ − ⌈a⌉ + 1$ (just think of counting all the integers between these two values, including both ends—if a row of fenceposts one foot apart extends for $k$ feet, then there are $k + 1$ fenceposts). Note that this even works when, for example, $a = 0.3$ and $b = 0.7$.

57. Let $a$ and $b$ be real numbers with $a < b$. Use the floor and/or ceiling functions to express the number of integers $n$ that satisfy the inequality $a < n < b$.
    - ❌ $⌊b - 1⌋ − ⌈a + 1⌉ + 1$
    - ✅⚠️ $⌈b⌉ − ⌊a⌋ - 1$

58. How many bytes are required to encode $n$ bits of data where $n$ equals
- (a) 4?
  - 1.
- (b) 10?
  - 2.
- (c) 500?
  - 63.
- (d) 3000?
  - 375.

59. How many bytes are required to encode n bits of data where $n$ equals
- (a) 7?
  - 1
- (b) 17?
  - 3
- (c) 1001?
  - 126
- (d) 28,800?
  - 3600

60. How many ATM cells (described in Example 28) can be transmitted in 10 seconds over a link operating at the following rates?
- (a) 128 kilobits per second (1 kilobit = 1000 bits)
  - $⌊10 * 128000 / 53 * 8⌋ =  3018$
- (b) 300 kilobits per second
  - 7075
- (c) 1 megabit per second (1 megabit = 1,000,000 bits)
  - 23584

61. Data are transmitted over a particular Ethernet network in blocks of 1500 octets (blocks of 8 bits). How many blocks are required to transmit the following amounts of data over this Ethernet network? (Note that a byte is a synonym for an octet, a kilobyte is 1000 bytes, and a megabyte is 1,000,000 bytes.)
- (a) 150 kilobytes of data
  - ❌ $⌈⌈150000 / 8⌉ / 1500⌉ = 13$
  - ✅ $⌈150000 / 1500⌉ = 100$
- (b) 384 kilobytes of data
- (c) 1.544 megabytes of data
- (d) 45.3 megabytes of data

(62-68 done on desmos.com)

62. ❔ Draw the graph of the function $f(n) = 1 − n²$ from ℤ to ℤ.

63. ❔ Draw the graph of the function $f(x) = ⌊2x⌋$ from ℝ to ℝ.

64. ❔ Draw the graph of the function $f(x) = ⌊x/2⌋$ from ℝ to ℝ.

65. ❔ Draw the graph of the function $f(x) = ⌊x⌋ + ⌊x/2⌋$ from ℝ to ℝ.

66. ❔ Draw the graph of the function $f(x) = ⌈x⌉ + ⌊x/2⌋$ from ℝ to ℝ.

67. ❔ Draw graphs of each of these functions.
- (a) $f(x) = ⌊x + 1/2⌋$
- (b) $f(x) = ⌊2x + 1⌋$
- (c) $f(x) = ⌈x/3⌉$
- (d) $f(x) = ⌈1/x⌉$
- (e) $f(x) = ⌈x − 2⌉ + ⌊x + 2⌋$
- (f) $f(x) = ⌊2x⌋⌈x/2⌉$
- (g) $f(x) = ⌈⌊x − 1/2⌋ + 1/2⌉$

68. ❔ Draw graphs of each of these functions.
- (a) $f(x) = ⌈3x − 2⌉$
- (b) $f(x) = ⌈0.2x⌉$
- (c) $f(x) = ⌊−1/x⌋$
- (d) $f(x) = ⌊x²⌋$
- (e) $f(x) = ⌈x/2⌉⌊x/2⌋$
- (f) $f(x) = ⌊x/2⌋ + ⌈x/2⌉$
- (g) $f(x) = ⌊2⌈x/2⌉ + 1/2⌋$

69. Find the inverse function of $f(x) = x³ + 1$.
    - $x = y³ + 1$
    - $f(y)^{-1} = (y - 1)^{1/3}$

70. Suppose that $f$ is an invertible function from $Y$ to $Z$ and $g$ is an invertible function from $X$ to $Y$. Show that the inverse of the composition $f ◦ g$ is given by $(f ◦ g)^{−1} = g^{−1} ◦ f^{−1}$.
    - ❎ We must show that $g(f(x)^{−1})^{−1}$ is the inverse of $f ◦ g$. As $f ◦ g$ is a function from $X$ to $Z$, $(f ◦ g)^{−1}$ must be from $Z$ to $X$.
    - Letting $x ∈ X$ then $y = g(x)$ is in $Y$ and $z = f(y)$ is in $Z$. Letting $z ∈ Z$, then $y = f(z)^{−1}$ is in $Y$ and $x = g(y)^{−1}$ is in $X$.
    - ✅ $(f ◦ g) ◦ (g^{−1} ◦ f^{−1} ) (z) = z$ for all $z ∈ Z$
    - $= (f ◦ g)((g^{−1} ◦ f^{−1} ) (z))$
    - $= (f ◦ g)(g^{−1}(f^{−1}(z)))$
    - $= f(g(g^{−1}(f^{−1}(z))))$
    - $= f(f^{−1}(z)) = z$
    - ⭕ $(g^{−1} ◦ f^{−1} ) ◦ (f ◦ g) (x) = x$ for all $x ∈ X$

71. Let $S$ be a subset of a universal set $U$. The **characteristic function** $f_S$ of $S$ is the function from $U$ to the set $\{0, 1\}$ such that $f_S (x) = 1$ if $x$ belongs to $S$ and $f_S (x) = 0$ if $x$ does not belong to $S$. Let $A$ and $B$ be sets. Show that for all $x ∈ U$,
- ✔ We can prove all of these identities by showing that the left-hand side is equal to the right-hand side for all possible values of $x$. In each instance (except part (c), in which there are only two cases), there are four cases to consider, depending on whether $x$ is in $A$ and/or $B$.
- (a) ❓ $f_{A∩B}(x) = f_A(x) · f_B(x)$
  - ✅ If $x$ is in both $A$ and $B$, then $f_{A∩B}(x) = 1$; and the right-hand side is $1 · 1 = 1$ as well. Otherwise $x ∉ A ∩ B$, so the left-hand side is $0$, and the right-hand side is either $0 · 1$ or $1 · 0$ or $0 · 0$, all of which are also $0$.
- (b) $f_{A∪B}(x) = f_A(x) + f_B(x) − f_A(x) · f_B(x)$
  - If $x$ is in $A$, $f_{A∪B}(x) = 1$ and the rhs. is $1 + 0 - 1 * 0 = 1$
  - If $x$ is in $B$, $f_{A∪B}(x) = 1$ and the rhs. is $0 + 1 - 0 * 1 = 1$
  - ⭕ If $x$ is in both $A$ and $B$ ...
  - If $x$ is not in $A$ or $B$, $f_{A∪B}(x) = 0$ and the rhs. is $0 + 0 - 0 * 0 = 0$.
- (c) $f_{\overline{A}}(x) = 1 − f_A(x)$
  - If $x$ is in $\overline{A}$ (meaning it is in $U$ but not in $A$), $f_{\overline{A}}(x) = 1$ and the rhs. is $1 - 0 = 1$.
  - If $x$ is in $A$, $f_{\overline{A}}(x) = 0$ and the rhs. is $1 - 1 = 0$.
- (d) $f_{A⊕B}(x) = f_A(x) + f_B(x) − 2f_A(x)f_B(x)$
  - If $x$ is in $A$ but not in $B$, $f_{A⊕B}(x) = 1$ and the rhs is $1 + 0 - 2*1*0 = 1$.
  - Wlog. $x$ is in $B$ but not in $A$.
  - If $x$ is in $B$ and $A$, $f_{A⊕B}(x) = 0$ and the rhs is $1 + 1 - 2*1*1 = 0$.
  - If $x$ is not in $B$ or $A$, $f_{A⊕B}(x) = 0$ and the rhs is $0 + 0 - 2*0*0 = 0$.

72. Suppose that $f$ is a function from $A$ to $B$, where $A$ and $B$ are finite sets with $|A| = |B|$. Show that $f$ is one-to-one if and only if it is onto.
    - If $f$ is one-to-one, for every $a_1 ≠ a_2$ there must be two distinct elements in $B$ such that $f(a_1) ≠ f(a_2)$. This means that there must be at least as many distinct elements in $B$ as there are in $A$. As $|A| = |B|$ we know that there are no elements in $B$ for which there is no $a ∈ A$ such that $f(a) = b$. Therefore $f$ is onto.
    - If $f$ is onto, for every $b ∈ B$ there is an $a ∈ A$ such that $f(a) = b$. As $|A| = |B|$ ❎ **the only way for any $b$ to be equal to $f(a)$ for two distinct $a$ would be that there existed an $a$ for which $f(a) = b_1 ∧ f(a) = b_2$ which is not a function.** So $f$ must be one-to-one.
    - ✅  If two or more elements of $A$ were sent to the same element of $B$, then $|A|$ would be at least one greater than the $|B|$.

73. Prove or disprove each of these statements about the floor and ceiling functions.
- (a) $⌈⌊x⌋⌉ = ⌊x⌋$ for all real numbers $x$.
  - Bd. $⌊x⌋$ is the largest integer not exceeding $x$ and as $⌈x⌉$ is the smallest integer not greater than or equal to $x$ and $⌊x⌋$ being an integer the eaulity holds.
- (b) $⌊2x⌋ = 2⌊x⌋$ whenever $x$ is a real number.
  - Counterexample: Letting $x = 1.5$, $⌊2x⌋ = 3$ and $2⌊x⌋ = 2$.
- (c) ❎ $⌈x⌉ + ⌈y⌉ − ⌈x + y⌉ = 0$ or $1$ whenever $x$ and $y$ are real numbers.
  - Letting $x = n + e$ and $y = m + f$ where $0 ≤ e < 1$ and $0 ≤ f < 1$, there are four cases to prove.
  - (1) $0 ≤ e < 1/2$ and $0 ≤ f < 1/2$, then $(n + 1) + (m + 1) − (n + m + 1) = 1$.
  - (2) $1/2 ≤ e < 1$ and $1/2 ≤ f < 1$, then $(n + 1) + (m + 1) − (n + m + 2) = 0$.
  - (3) $0 ≤ e < 1/2$ and $1/2 ≤ f < 1$, then $(n + 1) + (m + 1) − (n + m + 2) = 0$.
  - (4) $1/2 ≤ e < 1$ and $0 ≤ f < 1/2$, wlog. (3)
  - ✅  If $x$ is an integer, then by identity (4b) in Table 1, we know that $⌈x + y⌉ = x + ⌈y⌉$, and it follows that the difference is 0. The remaining case is ... (see above) ...Then $x + y$ will be greater than $m + n$ but less than $m + n + 2$, so $⌈x + y⌉$ will be either $m + n + 1$ or $m + n + 2$. Therefore the given expression will be either $(n + 1) + (m + 1) - (m + n + 1) = 1$ or $(n + 1) + (m + 1) - (m + n + 2) = 0$, as desired.
- (d) $⌈xy⌉ = ⌈x⌉ ⌈y⌉$ for all real numbers $x$ and $y$.
  - Counterexample: $⌈1.1 * 1.2⌉ ≠ ⌈1.1⌉ ⌈1.2⌉$.
- (e) $⌈\frac{x}{2}⌉ = ⌊\frac{x+1}{2}⌋$ for all real numbers $x$.
  - Counterexample: $⌈(1/2)/2⌉ = ⌊(1/2 + 1)/2⌋ → 1 = 0$.

74. Prove or disprove each of these statements about the floor and ceiling functions.
- (a) $⌊⌈x⌉⌋ = ⌈x⌉$ for all real numbers $x$.
  - As $⌈x⌉$ will be an integer $⌊⌈x⌉⌋$ is that exact same integer.
- (b) $⌊x + y⌋ = ⌊x⌋ + ⌊y⌋$ for all real numbers $x$ and $y$.
  - This is false. $⌊0.5 + 0.6⌋ ≠ ⌊0.5⌋ + ⌊0.6⌋$.
- (c) $⌈⌈x/2⌉ /2⌉ = ⌈x/4⌉$ for all real numbers $x$.
  - $⌈⌈5/2⌉ /2⌉ = ⌈5/4⌉$.
  - Letting $x = n + e$ where $0 ≤ e < 1$, then ❌ $⌈⌈x/2⌉/2⌉ = ⌈(n + 1)/2/2⌉ = ⌈(n + 1)/4⌉ = ⌈x/4⌉$.
  - ✅ Since we are dividing by $4$, let us write $x = 4n + k$, where $0 ≤ k < 4$. In other words, write $x$ in terms of how much it exceeds the largest multiple of $4$ not exceeding it. There are three cases. If $k = 0$, then $x$ is already a multiple of $4$, so both sides equal $n$. If $0 < k ≤ 2$, then $⌈x/2⌉ = 2n + 1$, so the left-hand side is $⌈n + 1/2⌉ = n + 1$. Of course the right-hand side is $n + 1$ as well, so again the two sides agree. Finally, suppose that $2 < k < 4$. Then $⌈x/2⌉ = 2n + 2$, and the left-hand side is $⌈n + 1⌉ = n + 1$; of course the right-hand side is still $n + 1$, as well. Since we proved that the two sides are equal in all cases, the proof is complete.
- (d) $⌊\sqrt{⌈x⌉}⌋ = ⌊\sqrt{x}⌋$ for all positive real numbers $x$.
  - Counterexample $⌊\sqrt{⌈1/2⌉}⌋ ≠ ⌊\sqrt{1/2}⌋$.
- (e) $⌊x⌋ + ⌊y⌋ + ⌊x + y⌋ ≤ ⌊2x⌋ + ⌊2y⌋$ for all real numbers $x$ and $y$.
  - ⭕ **(conflates equality and strict inequality)** We must show that $⌊x⌋ + ⌊y⌋ + ⌊x + y⌋$ cannot be larger than $⌊2x⌋ + ⌊2y⌋$. Letting $x = m + e$ and $y = n + f$ where $m$ and $n$ are the largest integers not exceeding $x$ and $y$ and $0 ≤ e < 1$ and $0 ≤ f < 1$. ❎ We see that $⌊x⌋ + ⌊y⌋$ is always $m + n$. For $⌊x + y⌋$ we will consider only the case where the expression yields the largest possible result. That is, if $e$ and $f$ are between $1/2$ and $1$. Then $⌊x + y⌋ = n + m + 1$ so the lhs. is $2m + 2n + 1$ and the rhs. is $2n + 1 + 2m + 1$ which is larger.
  - ✅ This is true. Write $x = m + e$ and $y = n + f$, where $m$ and $n$ are integers and $e$ and $f$ are nonnegative real numbers less than 1. The left-hand side is $m + n + (m + n)$ or $m + n + (m + n + 1)$, the latter occurring if and only if $e + f ≥ 1$. The right-hand side is the sum of two quantities. The first is either $2m$ (if $e < 1/2$ ) or $2m + 1$ (if $e ≥ 1/2$). The second is either $2n$ (if $f < 1/2$) or $2n + 1$ (if $f ≥ 1/2$). The only way, then, for the left-hand side to exceed the right-hand side is to have the left-hand side be $2m + 2n + 1$ and the right-hand side be $2m + 2n$. This can occur only if $e + f ≥ 1$ while $e < 1/2$ and $f < 1/2$. But that is an impossibility, since the sum of two numbers less than $1/2$ cannot be as large as $1$. Therefore the right-hand side is always at least as large as the left-hand side.

75. ❓ Prove that if $x$ is a positive real number, then
- (a) $⌊\sqrt{⌊x⌋}⌋ = ⌊\sqrt{x}⌋$
  - ✅  If $x$ is a positive integer, then the two sides are identical. So suppose that $x = n^2 + m + e$, where $n$ is the largest perfect square integer less than $x$, $m$ is a nonnegative integer, and $0 < e < 1$. For example, if $x = 13.2$, then $n = 3$, $m = 4$, and $e = 0.2$. Then both $\sqrt{x}$ and $\sqrt{⌊x⌋} = \sqrt{n^2 + m}$ are between $n$ and $n + 1$. Therefore both sides of the equation equal n.
- (b) $⌈\sqrt{⌈x⌉}⌉ = ⌈\sqrt{x}⌉$
  - ✅  If $x$ is a positive integer, then the two sides are identical. So suppose that $x = n^2 - m - e$, where $n$ is the smallest perfect square integer greater than $x$, $m$ is a nonnegative integer, and $e$ is a real number with $0 < e < 1$. For example, if $x = 13.2$, then $n = 4$, $m = 2$, and $e = 0.8$. Then both $\sqrt{x}$ and $\sqrt{⌈x⌉} = \sqrt{n² - m}$ are between $n - 1$ and $n$. Therefore both sides of the equation equal n.

76. Let $x$ be a real number.
Show that $⌊3x⌋ = ⌊x⌋ + ⌊x + 1/3⌋ + ⌊x + 2/3⌋$.
    - Letting $x = m + e$ where $n$ is the largest integers not exceeding $x$ and $0 ≤ e < 1$, we have three cases depending on the size of $e$.
    - If $0 ≤ e < 1/3$ then $⌊3x⌋ = 3x$ and the lhs. equals $x + x + x = 3x$.
    - If $1/3 ≤ e < 2/3$ then $⌊3x⌋ = 3x + 1$ and the lhs. equals $x + x + (x + 1) = 4x$.
    - If $2/3 ≤ e < 1$ then $⌊3x⌋ = 3x + 2$ and the lhs. equals $x + (x + 1) + (x + 1) = 3x + 2$.
    - ✔ Using interval-notation $x ∈ [n, n + 1/3)$ etc.

77. For each of these partial functions, determine its domain, codomain, domain of definition, and the set of values for which it is undefined. Also, determine whether it is a total function.
- (a) $f : ℤ → ℝ, f(n) = 1/n$
  - dod: $\{n ∈ ℤ \mid n ≠ 0\}$, val: $0$, tot? no
- (b) $f : ℤ → ℤ, f(n) = ⌈n/2⌉$
  - dom: ℤ, cod: ℤ, ❌ dod: $\{n ∈ ℤ \mid n = 2k\}$, val: $n ≠ 2k$, tot? no
  - ✅ dod: ℤ, val: ∅, tot? yes
- (c) $f : ℤ × ℤ → ℚ, f(m, n) = m/n$
  - dod: $\{(m, n) ∈ ℤ × ℤ \mid n ≠ 0\}$, val: $n = 0$, tot? no
  - ✔ dod: $ℤ × (ℤ - \{0\})$, val: $ℤ × 0$
- (d) $f : ℤ × ℤ → ℤ, f(m, n) = mn$
  - dod: ℤ × ℤ, val: ∅, tot? yes
- (e) $f : ℤ × ℤ → ℤ, f(m, n) = m − n \text{ if } m > n$
  - dod: $\{(m, n) ∈ ℤ × ℤ \mid m > n\}$, ❌ val: ∅, tot? yes
  - ✅ val: $\{(m, n) ∈ ℤ × ℤ \mid m ≤ n\}$, tot? no

78. Parts:
- (a) Show that a partial function from $A$ to $B$ can be viewed as a function $f^∗$ from $A$ to $B ∪ \{u\}$, where $u$ is not an element of $B$ and
$$
f^∗(a) =
    \begin{cases}
      f(a) & \text{if a belongs to the domain of definition of f} \\
      u & \text{if f is undefined at a}
    \end{cases}
$$
✔ We merely have to remark that f ∗ is well-defined by the rule given here.

- (b) Using the construction in (a), find the function $f^∗$ corresponding to each partial function in Exercise 77.
- (a) $f : ℤ → ℝ, f(n) = 1/n$
  - $$
    f^∗(n) =
        \begin{cases}
          1/n & \text{if } n ≠ 0 \\
          u & \text{if } n = 0
        \end{cases}
    $$
- (b) $f : ℤ → ℤ, f(n) = ⌈n/2⌉$
  - $$
    f^∗(n) = f(n)
    $$
- (c) $f : ℤ × ℤ → ℚ, f(m, n) = m/n$
  - dod: $ℤ × (ℤ - \{0\})$, val: $ℤ × 0$
  - $$
    f^∗(m, n) =
        \begin{cases}
          m/n & \text{if } n ≠ 0\\
          u & \text{if } n = 0
        \end{cases}
    $$
- (d) $f : ℤ × ℤ → ℤ, f(m, n) = mn$
  - $$
    f^∗(m, n) = mn
    $$
- (e) $f : ℤ × ℤ → ℤ, f(m, n) = m − n \text{ if } m > n$
  - dod: $\{(m, n) ∈ ℤ × ℤ \mid m > n\}$, val: $\{(m, n) ∈ ℤ × ℤ \mid m ≤ n\}$, tot? no
  - $$
    f^∗(m, n) =
        \begin{cases}
          m - n & \text{if } m > n \\
          u & \text{if } m ≤ n
        \end{cases}
    $$

79. Parts:
- (a) Show that if a set $S$ has cardinality $m$, where $m$ is a positive integer, then there is a one-to-one correspondence between $S$ and the set $\{1, 2, . . . , m\}$.
  - ❌ By this definition the sets are identical so a function that is one-to-one and onto assigns a value would be the identity function.
  - ✅ A fuction could enumarate the elements in $S$ (which might be anything).
- (b) Show that if $S$ and $T$ are two sets each with $m$ elements, where $m$ is a positive integer, then there is a one-to-one correspondence between $S$ and $T$.
  - ❌ Similar to the above a bijective function could assign each element of $S$ to a distinct element of $T$ as the cardinalities match up.
  - ✅ By part (a), there is a bijection $f$ from $S$ to $\{1,2, ... ,m\}$ and a bijection $g$ from $T$ to $\{1,2, ... ,m\}$. This tells us that $g^{- 1}$ is a bijection from $\{1, 2, ... , m\}$ to $T$. Then the composition $g^{- 1} ○ f$ is the desired bijection from $S$ to $T$.

80. ❓ (∗) Show that a set $S$ is infinite if and only if there is a proper subset $A$ of $S$ such that there is a one-to-one correspondence between $A$ and $S$.
- ✅ For the “if” direction, we simply need to note that if $S$ is a finite set, with cardinality $m$, then every proper subset of $S$ has cardinality strictly smaller than $m$, so there is no possible one-to-one correspondence between the elements of $S$ and the elements of the proper subset. (This is essentially the pigeonhole principle, to be discussed in Section 6.2.)
- The “only if” direction: Let $S$ be the given infinite set. Clearly $S$ is not empty, because by definition, the empty set has cardinality $0$, a nonnegative integer. Let $a_0$ be one element of $S$, and let $A = S − \{a_0\}$. Clearly $A$ is also infinite (because if it were finite, then we would have $|S| = |A| + 1$, making $S$ finite). We will now construct a one-to-one correspondence between $S$ and $A$; think of this as a one-to-one and onto function $f$ from $S$ to $A$. In order to define $f(a_0)$, we choose an arbitrary element $a_1$ in $A$ (which is possible because $A$ is infinite) and set $f (a_0) = a_1$. Next we define $f$ at $a_1$. To do so, we choose an arbitrary element $a_2$ in $A − \{a_1\}$ (which is possible because $A − {a_1}$ is necessarily infinite) and set $f (a_1) = a_2$. Next we define $f$ at $a_2$. To do so, we choose an arbitrary element $a_3$ in $A − \{a_1 , a_2\}$ (which is possible because $A − \{a_1 , a_2 \}$ is necessarily infinite) and set $f (a_2) = a3$. Finally, we let $f$ be the identity function on $S − \{a_0, a_1 , a_2 , . . .\}$. The function thus defined has $f (a_i) = a_i+1$ for all natural numbers $i$ and $f (x) = x$ for all $x ∈ S − \{a0 , a_1 , a_2 , . . .\}$. So $f$ is one-to-one and onto.
