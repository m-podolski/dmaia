# 1.7 Introduction to Proofs

1. ❓ Use a direct proof to show that the sum of two odd integers is even.
   - ❎ If two integers are summed, then their result is even.
   - $n + n = 2k$ where $n = 2m + 1$

2. Use a direct proof to show that the sum of two even integers is even.
   - Suppose a and b are two even integers such that $a=2s$ and $b=2t$. Then the sum is $a+b = 2s+2t = 2(s+t)$. So the sum of a and b is two times the integer $s+t$ and therefore even.

3. Show that the square of an even number is an even number using a direct proof.
   - Assuming $a = 2m$ then $a² = 2n$. By squaring a we obtain $a² = (2m)² = 2m * 2m = 4m² = 2(2m²)$. So a² is two times 2m² and therefore even.

4. Show that the additive inverse, or negative, of an even number is an even number using a direct proof.
   - The assertion is "If an even number is inverted, the the result is also even". Assuming that $n = 2k$ then $-n = -1(2k) = -2k ⭕ = 2(-k)$

5. Prove that if m + n and n + p are even integers, where m, n, and p are integers, then m + p is even. What kind of proof did you use?
   - If $m+n = 2k$ and $n+p = 2j$, then $m+p = 2l$.
   - ✅ $m = 2k-n$ and $p = 2j-n$ then $m+p = (2k-n)+(2j-n)$.
   - $m+p = 2(k-\frac{1}{2}n)+2(j-\frac{1}{2}n) = 2((k-\frac{1}{2}n)+(j-\frac{1}{2}n))$
   - Therefore m + p is even, proven directly.

6. Use a direct proof to show that the product of two odd numbers is odd.
    - Assuming $a = 2k + 1$ and $b = 2j + 1$
    - Then $ab = (2k + 1)(2j + 1) = 4kj + 2k + 2j + 1$
    - $= 2(2kj + k + j) + 1$

7. ❓ Use a direct proof to show that every odd integer is the difference of two squares.
   - Assuming $a = 2k + 1$, then $a = i² - j²$
   - ❎ the difference of two squares can be factored: $a² - a² = (a + b)(a - b)$
   - if we can arrange for our given integer to equal a + b and for a - b to equal 1, we are done.
   - letting a and b be the integers that straddle $n/2$ (i.e. 6 + 5 = 11)
   - if $n = 2k + 1$, then we let $a = k + 1$ and $b = k$
   - then $(k + 1)² - k² = k² + 2k + 1 - k² = 2k + 1 = n$

8. ❓ Prove that if n is a perfect square, then n + 2 is not a perfect square.
    - If $n = m²$, then $n+2 ≠ o²$.
    - ❎ Let n = m². If m = 0, then n + 2 = 2, which is not a perfect square, so we can assume that m ≥ 1. The smallest perfect square greater than n is (m+1)², and we have $(m + 1)² = m² + 2m + 1 = n + 2m + 1 > n + 2 * 1 + 1 > n + 2$. Therefore n + 2 cannot be a perfect square.

9. ❓ Use a proof by contradiction to prove that the sum of an irrational number and a rational number is irrational.
    - ❎ If r is rational and i is irrational, then $s = r + i$ is irrational
    - Then, by example 7 the sum of s and -r must be rational
    - But $s + (-r) = r + i + (-r) = i$, so i must be rational
    - Therefore the assumption that s was rational was incorrect and it must be irrational

10. Use a direct proof to show that the product of two rational numbers is rational.
    - If $r = \frac{p}{q} ∧ q ≠ 0$ and $ s = \frac{t}{u} ∧ u ≠ 0$, then $rs = \frac{a}{b}$
    - $rs = \frac{pt}{qu}$

11. ❌ Prove or disprove that the product of two irrational numbers is irrational.
    - If $r ≠ \frac{a}{b}∧ s ≠ \frac{c}{d}$, then $rs ≠ \frac{e}{f}$
    - Contraposition: If $rs = \frac{e}{f}$, then $r = \frac{a}{b} ∨ s = \frac{c}{d}$
    - $rs = \frac{e}{f}$
    - $r = \frac{e}{fs} ∨ s = \frac{e}{fr}$
    - Therefore this is true.
    - ❎ $\sqrt{2}\sqrt{2} = 2$; disproved by counterexample

12. ❌ Prove or disprove that the product of a nonzero rational number and an irrational number is irrational.
    - If $x = \frac{a}{b}$ and $y ≠ \frac{c}{d}$ then $z = xy ≠ \frac{e}{f}$
    - $x = \frac{z}{y}$
    - This is false, as the quotient of the two irrational numbers equals the rational x
    - ❎ This is true; suppose a/b is a non-zero rational and x is irrational, then xa/b must be irrational
    - Proof by contradiction: suppose xa/b were rational
    - since a/b ≠ 0, b/a is rational
    - multiply b/a by the assumed rational xa/b
    - the result is (b/a)(xa/b) = x which is irrational by hypothesis
    - this is a contradiction so xa/b must be irrational

13. Prove that if x is irrational, then 1/x is irrational.
    - If $x ≠ \frac{a}{b}$ then $\frac{1}{x} ≠ \frac{c}{d}$
    - Contraposition: If $\frac{1}{x} = \frac{c}{d}$ then $x = \frac{a}{b}$
    - $\frac{1}{x} = \frac{c}{d}$
    - ⭕ $x ≠ 0 ∧ 1/x ≠ 0 ∧ c ≠ 0$
    - $1 = \frac{c}{d}x$
    - $\frac{d}{c} = x$
    - True

14. Prove that if x is rational and x ≠ 0, then 1/x is rational.
    - If $x = \frac{a}{b}$ and $x ≠ 0$ then $\frac{1}{x} = \frac{c}{d}$
    - By definition $b ≠ 0$ and $d ≠ 0$
    - By the hypothesis $a ≠ 0$
    - $x = \frac{a}{b}$
    - $\frac{b}{a} = \frac{1}{x}$
    - True

15. Use a proof by contraposition to show that if x + y ≥ 2, where x and y are real numbers, then x ≥ 1 or y ≥ 1.
    - If $x + y ≥ 2$ then $x ≥ 1 ∨ y ≥ 1$
    - Contrapos.: If $x < 1 ∧ y < 1$ then $x + y < 2$
    - $x + y < 1 + 1$

16. ✅ Prove that if m and n are integers and mn is even, then m is even or n is even.
    - $mn = 2a → m = 2b ∨ n = 2c$
    - $mn = 2a$
    - $m = 2\frac{a}{n} ∨ n = 2\frac{a}{m}$
    - ❎ Contraposition: m and n are odd
    - By ex. 6, this tells us that mn is odd

17. Show that if n is an integer and n³ + 5 is odd, then n is even using
- $n³ + 5 = 2a + 1 → n = 2b$
- (a) a proof by contraposition.
  - $n = 2b + 1 → n³ + 5 = 2a$
  - $n³ + 5 = (2b + 1)³ + 5$
  - ❌ $n³ + 5 = 2b³ + 6$
  - ❌ $n³ + 5 = 2(b³ + 3)$
  - ❎ $n 3 +5 = (2k+1)^3 +5 = 8k^3 +12k^2 +6k+6 = 2(4k^3 +6k^2 +3k+3)$
  - True
- (b) a proof by contradiction.
  - ❌ $n³ + 5 = 2a → F$
  - $n³ = 2a - 5$
  - $n = \frac{2a - 5}{n²}$
  - n is a rational number, thus contradicting the hypothesis that it is an integer.
  - True
  - ❎ $n³ + 5 = 2a + 1$
  - As the product of odd numbers is odd, n³ is odd.
  - Subtracting 5 results in an even number, which is false.

18. Prove that if n is an integer and 3n + 2 is even, then n is even using
- $3n + 2 = 2a → n = 2b$
- (a) a proof by contraposition.
  - $n = 2b + 1 → 3n + 2 = 2a + 1$
  - $n = 2b + 1$
  - $3n + 2 = 6b + 5$
  - $3n + 2 = 2(3b + 2) + 1$; valid
- (b) a proof by contradiction.
  - $(3n + 2 = 2a) ∧ ¬(n = 2b)$
  - $3n + 2 = 2a ∧ n = 2b + 1$
  - ✅ $n = \frac{2a - 2}{3}$
  - $n = 2\frac{a - 1}{3}$; n is even, contradicting $n = 2b + 1$

19. Prove the proposition P(0), where P(n) is the proposition “If n is a positive integer greater than 1, then n² > n.” What kind of proof did you use?
    - $0 > 1 → 0² > 0$
    - $0 > 1$ is false, therefore the proposition is vacuously true (direct proof)

20. Prove the proposition P(1), where P(n) is the proposition “If n is a positive integer, then n² ≥ n.” What kind of proof did you use?
    - $1 > 0 → 1² ≥ 1$
    - ❌ direct;  as the condition is true the conclusion must be as well, which it is.
    - ❎ trivial proof; condition is not needed

21. Let P(n) be the proposition “If a and b are positive real numbers, then $(a + b)^n ≥ a^n + b^n$ .” Prove that P(1) is true. What kind of proof did you use?
    - $(a + b)^n ≥ a^n + b^n$
    - $a + b ≥ a + b$
    - ❎ $(a + b = a + b) ∨ (a + b > a + b)$
    - Trivial proof ❌ as both expressions are exactly the same.
    - ❎ direct or trivial proof; condition is not needed

22. ❓ Show that if you pick three socks from a drawer containing just blue socks and black socks, you must get either a pair of blue socks or a pair of black socks.

23. Show that at least ten of any 64 days chosen must fall on the same day of the week.
    - Proving by contradiction we assume that at most 9 days fall on the same day of the week. As 7 * 9 = 63 a maximum of 63 days could have been chosen which is a contradiction.

24. Show that at least three of any 25 days chosen must fall in the same month of the year.
    - Assuming ¬p, at most two of 25 chosen days fall in the same month. As 2 * 12 = 24 a maximum of 2 days could have been chosen.

25. Use a proof by contradiction to show that there is no rational number r for which $r^3 + r + 1 = 0$. [Hint: Assume that $r = a/b$ is a root, where a and b are integers and a/b is in lowest terms. Obtain an equation involving integers by multiplying by $b^3$. Then look at whether a and b are each odd or even.]
    - $¬(r = \frac{a}{b} → r^3 + r + 1 = 0)$
    - $r = \frac{a}{b} ∧ r^3 + r + 1 ≠ 0$
    - assuming $\frac{a}{b} = 0$
    - ❌ $\frac{a}{b}^3 + \frac{a}{b} + 1 ≠ \frac{a}{b}$
    - $(\frac{a}{b})^3b^3 + \frac{a}{b}b^3 + 1b^3 ≠ \frac{a}{b}b^3$
    - $a^3 + ab^2 + b^3 ≠ ab^2$
    - $a^3 + b^3 ≠ 0$; as $\frac{a}{b} = 0$, $a = 0$
    - $b^3 ≠ 0$
    - ❎ $\frac{a}{b}^3 + \frac{a}{b} + 1 = 0$
    - $a^3 + ab^2 + b^3 = 0$
    - as a and b cannot both be even (a/b is in lowest terms) the left-hand-side will always be odd and therefore cannot be 0.

26. Prove that if n is a positive integer, then n is even if and only if 7n + 4 is even.
    - ❌ $n > 0 → (n = 2k ↔ 7n + 4 = 2j)$
    - ❎ $n = 2k ↔ 7n + 4 = 2j$
    - Contraposition: $(n = 2k ↔ 7n + 4 = 2j + 1) → n ≤ 0$
    - $(n = 2k → 7n + 4 = 2j + 1) ∧ (7n + 4 = 2j + 1 → n = 2k)$
    - Cond. 1: $n = 2k → 7n + 4 = 2j + 1$
    - Cond. 1: $14k + 4 = ❌ 2(7k + 3/2) + 1$ T
    - Cond. 2: $7n + 4 = 2j + 1$
    - Cond. 2: $7n = 2j - 3$
    - Cond. 2: $n = \frac{2j - 3}{7} = 2\frac{j - 3/2}{7}$ F
    - condition1 is true, 2 is false
    - ❌ $(n = 2k ↔ 7n + 4 = 2j + 1)$ is false, so $n ≤ 0$ is vacuously true

27. Prove that if n is a positive integer, then n is odd if and only if 5n + 6 is odd.
    - $n = 2k + 1 ↔ 5n + 6 = 2j + 1$
    - 1: $n = 2k + 1 → 5n + 6 = 2j + 1$
    - $5(2k + 1) + 6 = 10k + 10 + 1 = 2(5k + 5) + 1$; true
    - 2: $5n + 6 = 2j + 1 → n = 2k + 1$
    - Contraposition: $n = 2k → 5n + 6 = 2j$
    - $10k + 6 = 2(5k + 3)$; true

28. Prove that m² = n² if and only if m = n or m = −n.
    - $m² = n² ↔ m = n ∨ m = −n$
    - 1: $m² = n² → m = n ∨ m = −n$
    - 1: ❌ $\plusmn m = \plusmn n$
    - 1: ❎ $(m + n)(m − n) = 0$
    - 1: $m = \plusmn n = n ∨ -n$
    - 2: $m = n ∨ m = −n → m² = n²$
    - 2: $n² = n² ∨ (-n)² = n² = T ∨ T$

29. ❓ Prove or disprove that if m and n are integers such that mn = 1, then either m = 1 and n = 1, or else m = −1 and n = −1.
    - $mn = 1 → (m = 1 ∧ n = 1) ∨ (m = −1 ∧ n = −1)$
    - ❎ Proof by contradiction: m is neither 1 nor -1
    - then $mn$ has a factor $|m| > 1$, but $mn = 1$ so this is false
    - therefore $m = 1 ∨ m = -1$ and $n = 1 ∨ n = -1$ because $mn = 1$ implies $n = 1/m$

30. Show that these three statements are equivalent, where a and b are real numbers: (i) a is less than b, (ii) the average of a and b is greater than a, and (iii) the average of a and b is less than b.
    - $a < b ↔ \frac{a + b}{2} > a ↔ \frac{a + b}{2} < b$
    - 1: $a < b → \frac{a + b}{2} > a$
    - 1: $a < b → b > a$
    - 2: $\frac{a + b}{2} > a → \frac{a + b}{2} < b$
    - 2: $b > a → a < b$
    - 3: $\frac{a + b}{2} < b → a < b$
    - 3: $a < b → a < b$

31. ✅ Show that these statements about the integer x are equivalent: (i) 3x + 2 is even, (ii) x + 5 is odd, (iii) x² is even.
    - 1: $3x + 2 = 2k ↔ x + 5 = 2k + 1$
    - 1: $3x + 2 = 2k ↔ x = 2k + 6$
    - 1: $3x + 2 = 2k ↔ 3x + 2 = 6k + 20 = 2(3k + 10)$
    - 2: $x + 5 = 2k + 1 ↔ x² = 2k$
    - 2: $x² = (2k + 6)² = 4k² + 24k + 36 = 2(2k² + 12k + 18) ↔ x² = 2k$
    - 3: $x² = 2k ↔ 3x + 2 = 2k$
    - 3: $x² = 2k ↔ x² = (\frac{2k - 2}{3})²$
    - $x² = 2(\frac{2k²-4k+2}{9})$

32. Show that these statements about the real number x are equivalent: (i) x is rational, (ii) x/2 is rational, (iii) 3x − 1 is rational.
    - **1: $x = \frac{a}{b}, b ≠ 0$**
    - **2: $\frac{x}{2} = \frac{a}{b}, b ≠ 0$**
    - **3: $3x - 1 = \frac{a}{b}, b ≠ 0$**
    - ✅ p1 → p2: $\frac{x}{2} = \frac{a/b}{2}: x = \frac{a}{b}$
    - p2 → p3: $x = \frac{2a}{b}: \frac{6a}{b} - 1 = \frac{6a - b}{b}$
    - p3 → p1: $3x - 1 = \frac{a}{b} : x = \frac{a/b + 1}{3b}$

33. Show that these statements about the real number x are equivalent: (i) x is irrational, (ii) 3x + 2 is irrational, (iii) x/2 is irrational.
    - p1: $x ≠ a/b, b ≠ 0$
    - p2: $3x + 2 ≠ c/d, d ≠ 0$
    - p3: $x/2 ≠ e/f, f ≠ 0$
    - Contraposition:
    - ¬p2 → ¬p1: $3x + 2 = c/d → x = a/b$
    - $x = \frac{c/d - 2}{3}, a = c/d - 2, b = 3$
    - ⭕ $\frac{c/d - 2}{3} = \frac{c - 2d}{3d}$
    - ¬p3 → ¬p2: $x/2 = e/f → 3x + 2 = c/d$
    - $3x + 2 = \frac{6e + 2f}{f}$
    - ¬p1 → ¬p3: $x = a/b → x/2 = e/f$
    - $x = 2a/b$

34. Is this reasoning for finding the  solutions of the equation √2x2 − 1 = x correct?
- (1) $\sqrt{2x^2 − 1} = x$ is given;
- (2) $2x^2 − 1 = x^2$ , obtained by squaring both sides of (1);
- (3) $x^2 − 1 = 0$, obtained by subtracting x² from both sides of (2)
- (4) $(x − 1)(x + 1) = 0$, obtained by factoring the left-hand side of x² − 1
- (5) $x = 1 or x = −1$, which follows because $ab = 0$ implies that $a = 0$ or $b = 0$.
  - ❌ Yes
  - ❎ No, not all steps (especially squaring) are reversible. Therefore the **possible** solutions must be substituted back into the equation.

35. Are these steps for finding the solutions of x + 3 = 3 − x correct?
- (1) $\sqrt{x + 3} = 3 − x$ is given;
- (2) $x + 3 = x^2 − 6x + 9$, obtained by squaring both sides of (1);
- (3) $0 = x^2 − 7x + 6$, obtained by subtracting x + 3 from both sides of (2);
- (4) $0 = (x − 1)(x − 6)$, obtained by factoring the right-hand side of (3);
- (5) $x = 1$ or $x = 6$, which follows from (4) because ab = 0 implies that a = 0 or b = 0.
  - (like 34) solutions must be substituted
  - ❎ x = 1, is the only solution

36. Show that the propositions p1 , p2 , p3, and p4 can be shown to be equivalent by showing that p1 ↔ p4 , p2 ↔ p3 , and p1 ↔ p3 .
    - ❌ It is possible to create proofs going from one proposition to the next including all in the argument. I. e. p4 to p1 to p3 to p2.
    - ❎ The missing conditional statements follow with intermediate steps. I.e. p1 ↔ p2 from p1 ↔ p3 and p2 ↔ p3.

37. Show that the propositions p1, p2 , p3 , p4, and p5 can be shown to be equivalent by proving that the conditional statements p1 → p4, p3 → p1 , p4 → p2 , p2 → p5 , and p5 → p3 are true.
    - It is possible to create proofs going from one proposition to the next including all in the argument.
    - ❎ using hypothetical syllogism repeatedly.

38. ❌ Find a counterexample to the statement that every positive integer can be written as the sum of the squares of three integers.
    - $a > 0 → a = b² + c² + d²$
    - 1 = 3 = T → F
    - ❎ b, c and d should denote **different** integers than a. So 7 would be the smallest counterexample.

39. Prove that at least one of the real numbers a1 , a2 ,..., an is greater than or equal to the average of these numbers. What kind of proof did you use?
    - ❌ $\frac{a_1 + a_2 + ... + a_n}{n} = A → (a_1 ∨ a_2 ∨ ... ∨ a_n) ≥ A$
    - ❎ Contradiction: $$a_n < A$$ and $$a_1 + a_2 + ... + a_n < nA$$ considering $$\frac{a_1 + a_2 + ... + a_n}{n} = A$$ this implies $nA < nA$

40. ❓ Use Exercise 39 to show that if the first 10 positive integers are placed around a circle, in any order, there exist three integers in consecutive locations around the circle that have a sum greater than or equal to 17.
    - ❎ Looking at ten groups of thre consecutive numbers each, which overlap so every number occurs in three different groups. So the sums of the ten groups must equal three times the sum of 1 to 10, namely 165. Therefore the average sum is 16.5. By Ex. 39 at least one of the sums must be greater than 16.5.

41. Prove that if n is an integer, these four statements are equivalent: (i) n is even, (ii) n + 1 is odd, (iii) 3n + 1 is odd, (iv) 3n is even.
    1. n = 2k$
    1. n + 1 = 2k + 1$
    1. 3n + 1 = 2k + 1$
    1. 3n = 2k$
    - ❌ iv must be equivalent to i as an even number multiplied will result in another even number. By the same logic ii and iii are equivalent as and even number plus 1 is odd and finally i and ii are equivalent for the same reason.
    - ❎ circular proof (i → ii → iii → iv → i), using contraposition for the last one.

42. Prove that these four statements about the integer n are equivalent: (i) n2 is odd, (ii) 1 − n is even, (iii) n3 is odd, (iv) n2 + 1 is even.
    - p1: $n² = 2k + 1$
    - p2: $1 - n = 2k$
    - p3: $n³ = 2k + 1$
    - p4: $n² + 1 = 2k$
    - ❌ p1 → p2 → p3 → p4 → p1
    - ❎ show that each is equivalent to $n = 2k + 1$ (p5)
    - p1 → p5 and p5 → p1 (by examples 1 and 8)
    - p5 → p2 and p2 → p5
    - p5 → p3 and p3 → p5
    - p5 → p4 and p4 → p5
    - from p5 to x directly and from x to p5 per contraposition
