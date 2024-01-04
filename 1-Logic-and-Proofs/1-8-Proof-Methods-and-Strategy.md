# 1.8 Proof Methods and Strategy

1. Prove that $n² + 1 ≥ 2^n$ when n is a positive integer with 1 ≤ n ≤ 4.
    - proof by exhaustion
    - $n=1, 2 ≥ 2$
    - $n=2, 5 ≥ 4$
    - $n=3, 10 ≥ 8$
    - $n=4, 17 ≥ 16$

2. Prove that there are no positive perfect cubes less than 1000 that are the sum of the cubes of two positive integers.
    - $1, 8, 27, 64, 125, 216, 343, 512, 729$
    - $1$ cannot be expressed as a sum
    - $8$ cannot be expressed as a sum
    - $1+8=9 < 27$
    - $8+27=35 < 64$
    - $27+64=91 < 125$
    - $64+125=189 < 216$
    - $125+216=341 < 343$
    - $216+343=559 > 512$
    - $343+512=855 > 729$
    - ⭕ to be truly exhaustive all 45 permutations need to be tried

3. Prove that if x and y are real numbers, then $max(x, y) + min(x, y) = x + y$. [Hint: Use a proof by cases, with the two cases corresponding to $x ≥ y$ and $x < y$, respectively.]
    - Case $x ≥ y$: $max(x,y) = x, min(x,y) = y$ so $x + y$
    - Case $x < y$: $max(x,y) = y, min(x,y) = x$ so $y + x$

4. ❌ Use a proof by cases to show that $min(a, min(b, c)) = min(min(a, b), c)$ whenever a, b, and c are real numbers.
    - Case $a ≥ b ≥ c$: $min(a, min(b, c)) = c = min(min(a, b), c) = c$
    - Case $a ≥ c ≥ b$: ...
    - Case $b ≥ c ≥ a$:
    - Case $b ≥ a ≥ c$:
    - Case $c ≥ a ≥ b$:
    - Case $c ≥ b ≥ a$:
    - ❎ 3 cases: a, b or c are smallest (or tied for smallest)

5. Prove using the notion of without loss of generality that $min(x, y) = (x + y − |x − y|)/2$ and $max(x, y) = (x + y + |x − y|)/2$ whenever x and y are real numbers.
    - ❌ Case $x ≥ y$: $x − y ≥ 0, |x - y| = x - y$
      - $min(x, y) = y$
      - $(x + y − x + y)/2$
      - $max(x, y) = x$
      - $(x + y + x - y)/2$
    - ❌ Case $x < y$: $x − y < 0, |x - y| = -(x - y)$
    - ❎ Because $|x - y| = |y - x|$, the values of x and y are interchangeable. Therefore WLOG we can assume that $x ≥ y$ and $|x - y| = x - y$.

6. Prove using the notion of without loss of generality that 5x + 5y is an odd integer when x and y are integers of opposite parity.
    - As ~~$5x + 5y$ is commutative and~~ x and y are of opposite parity, we assume WLOG that x is even and y is odd. This gives us $5(2a) + 5(2b + 1) = 10a + 10b + 1 = 2(5a + 5b) + 1$

7. Prove the triangle inequality, which states that if x and y are real numbers, then $|x| + |y| ≥ |x + y|$ (where |x| represents the absolute value of x, which equals x if x ≥ 0 and equals −x if x < 0).
    - (i) x and y both nonnegative, (ii) x nonnegative and y is negative, (iii) x negative and y nonnegative, and (iv) x negative and y negative.
    ❌ 1. $|x + y|$ is nonnegative, so $x + y ≥ x + y$
    ❌ 2. $|x + y|$ is , so $x - y ≥ x + y$
    - ❎ (i), then $|x|+|y| = x+y = |x+y|$
    - (iv), then $|x|+|y| = (-x)+(-y) = -(x+y) = |x+y|$ since x+y is negative.
    - (ii,iii) aussume WLOG that $x≥0$ and $y<0$ because of the commutativity of addition.
    - two subcases depending on the relative sizes of x and -y
      1. $x≥-y$, then $x+y≥0$. Therefore $|x+y|=x+y$ which is a nonnegative number smaller than x (since y is negative). On the other hand $|x|+|y|=x+|y|$ is a positve number bigger than x. Therefore we have $|x+y|<x<|x|+|y|$
      2. ⚠️ $x<-y$, then $|x+y|=-(x+y)=(-x)+(-y)$ is a positive number less than or equal to -y (since -x is nonpositive). On the other hand $|x|+|y|=|x|+(-y)$ is a positive number greater than or equal to -y. Therefore we have $|x+y|≤-y≤|x|+|y|$

8. ❌ Prove that there is a positive integer that equals the sum of the positive integers not exceeding it. Is your proof constructive or nonconstructive?
    - $1 + 2 = 3$, constructive
    - ❎ 1

9. Prove that there are 100 consecutive positive integers that are not perfect squares. Is your proof constructive or nonconstructive?
    - ❌ nonconstructive
    - ❎ by looking at large enough numbers such a sequence can be found, for example $100²=10000$ and $101²=10201$ so between them are 201 consecutive numbers of which the first 100 satisfy the exercise. The proof is constructive.

10. Prove that either $2·10^{500} + 15$ or $2·10^{500} + 16$ is not a perfect square. Is your proof constructive or nonconstructive?
    - let $x=2·10^{500} + 15$, then $x+1=2·10^{500} + 16$
    - ❌ $(10^{250})^{2}=10^{500}$
    - ❎ The only perfect squares that differ by 1 are 0 and 1. This is a nonconstructive proof (in fact neither is a perfect square).

11. Prove that there exists a pair of consecutive integers such that one of these integers is a perfect square and the other is a perfect cube.
    - $n = x² ∧ (n+1 = y³ ∨ n-1 = y³)$.
    - $1, 4, 9, 16, 25, 36, 49, 64, 81, 100$
    - $1, 8, 27, 64, 125, 216, 343, 512, 729$
    - $8=2³$ and $9=3²$ satisfy the exercise.

12. Show that the product of two of the numbers $65^{1000} − 8^{2001} + 3^{177}$ , $79^{1212} − 9^{2399} + 2^{2001}$ , and $24^{4493} − 5^{8192} + 7^{1777}$ is nonnegative. Is your proof constructive or nonconstructive? [Hint: Do not try to evaluate these numbers!]
    - For the product(s) of two arbitrarily chosen numbers to be nonnegative both have to have the same sign. ❌ So all numbers must be nonnegative or all must be negative.
    - ❎ For any three numbers at least two must have the same sign, so for these the product will be nonnegative. This is a nonconstructive proof.

13. ❓ Prove or disprove that there is a rational number x and an irrational number y such that $x^y$ is irrational.
    - ❎ let $x=2$ and $y=\sqrt{2}$. If $x^y=2^{\sqrt{2}}$ is irrational, we are done.
    - If not the let  $x=2^{\sqrt{2}}$ and  $y=\sqrt{2}/4$; x is rational by assumption and y is irrational (if it were rational, then $\sqrt{2}$ would be rational). But now $x² = (2^{\sqrt{2}})^{\sqrt{2}/4} = 2^{\sqrt{2}\sqrt{2}/4} = 2^{1/2} = \sqrt{2}$, which is irrational.

14. Prove or disprove that if a and b are rational numbers, then $a^b$ is also rational.
    - if $a = \frac{m}{n}$ and $b = \frac{o}{p}$, then $a^b = \frac{q}{r}$
    - ❌ $\frac{m}{n}^\frac{o}{p} = \frac{q}{r}$
    - $\frac{m^\frac{o}{p}}{n^\frac{o}{p}}$
    - ❎ disprove by counterexample: $a^b = 2^{1/2} = \sqrt{2}$

15. Show that each of these statements can be used to express the fact that there is a unique element x such that P(x) is true. [Note that we can also write this statement as $∃!xP(x)$.]
- (a) $∃x∀y(P(y) ↔ x = y)$
  - ✅ This statement says that there exists an element x such that for all elements y if P is true then its element equals x; leaving open the possibility that P might not be true in some cases where x=y. This is ruled out by the converse implication that if x=y (is unique), then P will be true.
- (b) $∃xP(x) ∧ ∀x∀y(P(x) ∧ P(y) → x = y)$
  - Here the first part of the conjunction states the existence and the second the uniqueness, where for all two elements (not necessarily dsitinct) from the domain P is only true for both, if the elements are the same.
- (c) $∃x(P(x) ∧ ∀y(P(y) → x = y))$
  - ✅ This follows the same principle as (b) in that we have a conjunction stating existence first and then uniqueness but existentially quantified as one expression. So the scope of ∃x extends into the second part and P(x) constrains it as needed.

16. Show that if a, b, and c are real numbers and a ≠ 0, then there is a unique solution of the equation ax + b = c.
    - 1: A solution exists:
      - $ax + b = c$, solve to $x = (c-b)/a$
    - 2: This solution is unique:
      - as there were no even/even fractional exponents involed this x is unique.

17. Suppose that a and b are odd integers with a ≠ b. Show there is a unique integer c such that |a − c| = |b − c|.
    - ❌ $|(2k+1) − c| = |(2j+1) − c|$
    - ❎ c exists/c is unique: $|a − c| = |b − c|$ is equivalent to $a − c = b − c ∨ a − c = -b + c$. The first of these is equivalent to $a=b$ which contradicts our assumptions, so the original equation is equivalent to $a − c = -b + c$, solving for c gives $c=(a+b)/2$. Thus there is a unique solution.
    - c is an integer: the sum of the odd integers a and b is even.

18. Show that if r is an irrational number, there is a unique integer n such that the distance between r and n is less than 1/2.
    - ❌ $|\sqrt{2}-n| < 1/2$
    - $\sqrt{(\sqrt{2}-n)²} < 1/2$
    - $(\sqrt{2}-n)² < (1/2)²$
    - $n +n² > (-1/4+2)/2\sqrt{2}$
    - ❎ Let a be the closest integer to r less than r and b be the closest integer to r greater than r. Then $b = a+1$. Clearly the distance between r and any integer other than a or b is greater than 1. Furthermore, since r is irrational, it cannot be exactly halfway between a and b, so exactly one of $r-a < 1/2$ and $b-r < 1/2$ holds.

19. Show that if n is an odd integer, then there is a unique integer k such that n is the sum of k − 2 and k + 3.
    - $n = 2j+1$
    - ❌ $n = (k-2)+(k+3) = 2k+1$
    - ❎ $k = (n-1)/2$; since n is odd, $n-1$ is even, so k is an integer.

20. ❓ Prove that given a real number x there exist unique numbers n and e such that x = n + e, n is an integer, and 0 ≤ e < 1.
    - ❎ Given x, let n be the greatest integer less that or equal to x, and let $e = x-n$. Clearly $0 ≤ e < 1$, and e is unique for this n. Any other choice wuld cause the required e to be less than 0 or greater than or equal to 1, so n is unique as well.

21. Prove that given a real number x there exist unique numbers n and e such that $x = n − e$, n is an integer, and $0 ≤ e < 1$.
    - Let n be the smallest integer number greater than or equal to x. Then $0 ≤ e < 1$ and e is unique. Any other choice of n would make $0 ≤ e < 1$ false.
    - ⭕ If x is itself an integer, then we can take $n=x$ and $e=0$. No other solution is possible in this case, since if the integer n is greater than x, then n is at least $x+1$, which would make $e≥1$.

22. Use forward reasoning to show that if x is a nonzero real number, then $x² + 1/x² ≥ 2$. [Hint: Start with the inequality $(x − 1/x)² ≥ 0$ which holds for all nonzero real numbers x.]
    - $x ≠ 0 → x² + 1/x² ≥ 2$
    - $(x − 1/x)² ≥ 0$
    - $x²-2x(1/x)+(1/x²) ≥ 0$
    - $x²+(1/x²) ≥ 2$

23. The **harmonic mean** of two real numbers x and y equals $2xy/(x + y)$. By computing the harmonic and geometric means of different pairs of positive real numbers, formulate a conjecture about their relative sizes and prove your conjecture.
$$
\begin{array}{|c|c|c|c|c|c|c|}
x & y & 2xy/(x + y) & \sqrt[2]{xy} & HM & GM & HM/GM\\
\hline
1/4 & 1/4 & 1/4 & 1/4 & 0,25 & 0,25 & 1\\
1/2 & 1/2 & 1/2 & 1/2 & 0,5 & 0,5 & 1\\
1 & 1 & 1 & 1 & 1 & 1 & 1\\
2 & 2 & 2 & 2 & 2 & 2 & 1\\
1/4 & 1/3 & 2/7 & \sqrt{1/12} & 0,2857 & 0,2886 & 0,9897\\
1/4 & 1/2 & 1/3 & \sqrt{1/8} & 0,3333 & 0,3535 & 0,9428\\
1/2 & 1 & 2/3 & \sqrt{1/2} & 0,6666 & 0,7071 & 0,9428\\
1 & 2 & 4/3 & \sqrt{2} & 1,3333 & 1,4142 & 0,9428\\
2 & 4 & 8/3 & 2\sqrt{2} & 2,6666 & 2,8284 & 0,9428\\
2 & 8 & 16/5 & 4 & 3,2000 & 4,000 & 0,8000\\
2 & 10 & 10/3 & 2\sqrt{5} & 3,3333 & 4,4721 & 0,7453\\
3 & 400 & 2400/403 & \sqrt{1200} & 5,9553 & 34,641 & 0,1719\\
\end{array}
$$
- ❌ Conjecture: The ratio of the harmonic mean over the geometric mean r is $0 < r ≤ 1$ and it is the same for all x and y where $o = x/y$ is the same. Additionally it decreases when $xy$ increases.
- ❎ Conjecture: HM of x and y is always less than GM if x and y are distinct positive real numbers. So we want to verify the inequality $2xy/(x + y) < \sqrt{xy}$. Multiplying both sides by $(x+y)/(2\sqrt{xy})$ gives us the equivalent inequality $\sqrt{xy} < (x + y)/2$, which is proved in example 14.

24. The **quadratic  mean**  mean of two real numbers x and y equals $(x^2 + y^2 )/2$. By computing the arithmetic and quadratic means of different pairs of positive real numbers, formulate a conjecture about their relative sizes and prove your conjecture.
    - $\sqrt{(x^2 + y^2 )/2}$
      - 1,2: $5/2 ≈ 1.58$
      - 2,3: $13/2 ≈ 2.55$
      - 3,4: $25/2 ≈ 3.54$
    - $(x + y)/2$
      - 1,2: $3/2 ≈ 1.5$
      - 2,3: $5/2 ≈ 2.5$
      - 3,4: $7/2 ≈ 3.5$
    - Conjecture: $\sqrt{(x^2 + y^2 )/2} ❌ > (x + y)/2$
    - Conjecture: $\sqrt{(x^2 + y^2 )/2} ❎ ≥ (x + y)/2$
    - $\sqrt{(x^2 + y^2 )/2} > (x + y)/2$ | square
    - $(x^2 + y^2 )/2 > (x + y)²/4$ | *4
    - $2(x^2 + y^2 ) > (x + y)²$ | -(x + y)²
    - $2(x^2 + y^2) - (x + y)² > 0$ | exp.
    - $2x² + 2y² - x² - 2xy - y² > 0$ | simp.
    - $x² - 2xy + y² > 0$ | factor
    - ⭕ $(x - y)² > 0$

25. (∗) Write the numbers 1, 2, . . . , 2n on a blackboard, where n is an odd integer. Pick any two of the numbers, j and k, write |j − k| on the board and erase j and k. Continue this process until only one integer is written on the board. Prove that this integer must be odd.
    - ❌ (did not add the absolute value to the original list)
    - ❎ The key point here is that the parity of the sum of the numbers written on the board never changes. If j and k are both even or both odd, then their sum and their difference are both even and we are replacing the even sum $j+k$ by the even difference $|j-k|$, leaving the parity of the total unchanged. If j and k have different parities, then erasing them changes the parity of the total, but hteir difference $|j-k|$ is odd, so adding this difference restores the parity of the total. Therefore the integer we end up with at the end of the process must have the same parity as $1+2+...+2n$. It is easy to compute this sum. If we add the first and last terms we get $2n+1$; if we add the second and next-to-last terms we get $2+(2n-1) = 2n+1$; and so on. In all we get n sums of 2n+1, so th total sum is $n(2n+1)$. If n is odd, this is the product of two odd numbers and therefore odd, as desired.

26. (∗) Suppose that five ones and four zeros are arranged around a circle. Between any two equal bits you insert a 0 and between any two unequal bits you insert a 1 to produce nine new bits. Then you erase the nine original bits. Show that when you iterate this procedure, you can never get nine zeros. [Hint: Work backward, assuming that you did end up with nine zeros.]
    - Assuming that the result is a circle with only zeros, it is obvious that its predecessor must have consisted of only equal pairs of bits.(*) But because we have two distinct values there will be at least two unequal pairs (when all 1s are stringed together and all 0s are stringed together) where the strings are connected.
    - ⭕* Thus if we are to start with something other than nine 0s and yet end up with nine 0s, we must have had nine 1s at some point. But in the step before that each adjacent pair of bits must have bee different; in other words, they must have alternated. This is impossible with an odd number of bits.

27. Formulate a conjecture about the decimal digits that appear as the final decimal digit of the fourth power of an integer. Prove your conjecture using a proof by cases.
    - $0^4 = 0$
    - $1^4 = 1$
    - $2^4 = 16$
    - $3^4 = 81$
    - $4^4 = 256$
    - $5^4 = 625$
    - $6^4 = 1296$
    - $7^4 = 2401$
    - $8^4 = 4096$
    - $9^4 = 6561$
    - Conjecture: The final decimal digit is either 0,1,5 or 6.
    - According to example 5 we express the result of a fourth power (always positive) as $10a + b$, where a and b are positive integers and b is 0, 1, 2, 3, 4, 5, 6, 7, 8, or 9.
    - Then $n⁴ = (10a + b)⁴ = 10a^4+40a^3b+60a^2b^2+40ab^3+b^4 = 10(a⁴+4a³b+6a²b²+4ab³) + b⁴$ so that the final decimal digit of n⁴ is the same as the final decimal digit of b⁴.
    ❌
    1. final digit of $n = 2k = 0 ∨ 6$
    1. final digit of $n = 2k+1 = 5 ∨ 1$
    - ❎ Because $(10a + b)⁴$ where $b=0..9$ yields the above numbers as values of b⁴ (the last part of the resulting polynomial, where the other parts are divisible by 10 and therefore irrelevant to the argument), the ones digits are always 0,1,5 or 6.

28. Formulate a conjecture about the final two decimal digits of the square of an integer. Prove your conjecture using a proof by cases.
    - ❌
    - $10^2 = 100$
    - $11^2 = 121$
    - $12^2 = 144$
    - $13^2 = 169$
    - $14^2 = 196$
    - $15^2 = 225$
    - $16^2 = 256$
    - $17^2 = 289$
    - $18^2 = 324$
    - $19^2 = 361$
    - ❎ Clearly only the last two digits of n contribute to the last two digits of n². so we can compute 0²,1²,...,99². We obtain  00 , 01 , 04 , 09 , 16 , 25 , 36 , 49 , 64, 81 , 21, 44, 69, 96, 56, 89, 24, 61, 41 , 84, 29, 76. From that point on, the list repeats in reverse order (as we take the squares from 25² to 49², and then it repeats again as we take the squares from 50² to 99²). The reason for these last two statements are that $(50-n)² = 2500-100n+n²$, so $(50-n)²$ and n² have the same two final digits, and $(50+n)² = 2500+100n+n²$, so $(50+n)²$ and n² have the same two final digits. Thus our list (which contains 22 numbers) is complete.

29. Prove that there is no positive integer n such that $n^2 + n^3 = 100$.
    - A result x ≤ 100 is impossible if one summand is > 100, so the only possible cases are 1..4 as 5³ = 125. The closest of which is n = 4 and its result is 80.

30. Prove that there are no solutions in integers x and y to the equation $2x^2 + 5y^2 = 14$.
    - ❌:
    - solve for x:
    - $2x² + 5y² = 14$
    - $x² = (14 - 5y²)/2$
    - $x = \sqrt{(14 - 5y²)/2}$
    - solve for y:
    - $y = \sqrt{(14 - 2x²)/5}$
    - ❎  If $|y| ≥ 2$, then $2x² + 5y² ≥ 2x² + 20 ≥ 20$, so the only possible values of y to try are 0 and ±1 . In the former case we would be looking for solutions to $2x² = 14$ and in the latter case to $2x² = 9$. Clearly there are no integer solutions to these equations, so there are no solutions to the original equation.

31. Prove that there are no solutions in positive integers x and y to the equation $x^4 + y^4 = 625$.
    - Because $5^4 = 625$, y must be ≤ 4 and no sum of 1,2,3 and 4 is equal to 625.

32. Prove that there are infinitely many solutions in positive integers x, y, and z to the equation $x^2 + y^2 = z^2$ . [Hint: Let $x = m^2 − n^2 , y = 2mn$, and $z = m^2 + n^2$, where m and n are integers.]
    - $(m^2 − n^2)^2 + (2mn)^2 = (m^2 + n^2)^2$
    - $(m^4 − 2m²n² + n^4) + (4m²n²) = (m^4 + 2m²n² + n^4)$
    - $0 = 0$

33. Adapt the proof in Example 4 in Section 1.7 to prove that if $n =  abc$, where  a, b, and  c are positive integers, then $a ≤ \sqrt[3]{n}$, $b ≤ \sqrt[3]{n}$, or $c ≤ \sqrt[3]{n}$.
    - By contraposition we get the hypothesis $a > \sqrt[3]{n}$ ∧ $b > \sqrt[3]{n}$ ∧ $c > \sqrt[3]{n}$
    - Multiplying the inequalities results in $abc > (\sqrt[3]{n})³ = n$, which contradicts the original hypothesis.

34. Prove that $\sqrt[3]{2}$ is irrational.
    - Using contradiction, suppose $\sqrt[3]{2}$ is rational, then there exist integers a and b with $\sqrt[3]{2} = \frac{a}{b}$, where $b ≠ 0$ and a and b are in lowest terms.
    - Raising to the 3rd power: $2 = \frac{a³}{b³}$
    - Hence $2b³ = a³$
    - By the defintion of an even integer it follows that a³ is even (because 2b³ is). By extending the result of 1.7/16 (if abc is even then a or b or c must be even) we see that a is even. Thus,
    - $2b³ = (2c)³ = 8c³$
    - Dividing by 2/factoring: $b³ = 2(2c³)$
    - By the same reasoning as above this shows that b must be even as well. So 2 divides a and b which contradicts the initial constraint of a and b being in lowest terms.

35. Prove that between every two rational numbers there is an irrational number.
    - $\frac{a}{b} + c < \frac{d}{e}$, where c is irrational, b and e ≠ 0 and the fractions are in lowest terms.
    - ⭕ Because we know that $\sqrt{2}$ is irrational, we can use a small multiple of it.
    - By finding a common denominator, we can assume that the given rational numbers are $\frac{a}{b}$ and $\frac{c}{b}$, where b is a positive integer and a and c are integers with a < c.
    - In particular $(a+1)/b ≤ c/b$. Thus $x = (a+\frac{1}{2}\sqrt{2})/b$ is between the two given rational numbers, because $0 < \sqrt{2} < 2$. Furthermore, x is irrational because if x were rational, then $2(bx-a) = \sqrt{2}$ would be as well, in violation of 1.7/Example 10.

36. Prove that between every rational number and every irrational number there is an irrational number.
    - ❌ Considering the numbers $\frac{a}{b} < \frac{a + 1/c\sqrt{2}}{b}$ where the first one is rational and the second one irrational because if $x = \frac{a + 1/c\sqrt{2}}{b}$ were rational then $c(xb-a) = \sqrt{2}$ would be, too. As c can be any integer there is an irrational number between any rational and irrational number.
    - ❎ The average of a rational number x and an irrational number y must be irrational, because the equation $a = (x+y)/2$ leads to $y = 2a-x$, which would be rational if a were rational.

37. (∗) Let S = $x_1y_1 + x_2y_2 + · · · + x_ny_n$, where $x1, x2 , . . . , xn$ and $y1 , y2 , . . . , yn$ are orderings of two different sequences of positive real numbers, each containing n elements.
- (a) ❓ Show that S takes its maximum value over all orderings of the two sequences when both sequences are sorted (so that the elements in each sequence are in nondecreasing order).
  - ❎ WLOG, we may assume that the x sequence is already sorted, since we can relabel indices. There are only a finite number of possible orderings for the y sequence, so if we can show that we increase the sum (or at least keep it the same) whenever we find $y_i$ and $y_j$ that are out of order (i.e. $i<j$ but $y_i>y_j$) by switching them, then we will have shown that the sum is largest when the y sequence is in nondecreasing order. Indeed, if we perform the swap, then we have added $x_iy_j+x_jy_i$ to the sum and subtracted $x_iy_i+x_jy_j$. The net effect, then, is to have added $x_iy_j+x_jy_i - x_iy_i-x_jy_j = (x_j-x_i)(y_i-y_j)$, which is nonnegative by our ordering assumptions.
- (b) Show that S takes its minimum value over all orderings of the two sequences when one sequence is sorted into nondecreasing order and the other is sorted into nonincreasing order.
  - Again assuming the x sequence is sorted, if we can show that we decrease the sum whenever we find $y_i$ and $y_j$ so that $i<j$ but $y_i<y_j$ by switching them, then the proof is complete. If we perform the swap we have $x_iy_j+x_jy_i - x_iy_i-x_jy_j = (x_j-x_i)(y_i-y_j)$, which is nonpositive by our ordering assumptions.

38. Prove or disprove that if you have an 8-gallon jug of water and two empty jugs with capacities of 5 gallons and 3 gallons, respectively, then you can measure 4 gallons by successively pouring some of or all of the water in a jug into another jug.
    - $4 = 2(5-3)$
    - ❌ Not possible: (8,0,0), (3,5,0), (3,2,3), (6,2,0). So now the measured 2gal cannot be stored outside of the needed 5 and 3gal jugs.
    - ❎ (8,0,0), (3,5,0), (3,2,3), (6,2,0), (6,0,2), (1,5,2), (1,4,3)

39. Verify the 3x + 1 conjecture for these integers.
- (a) $6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1$
- (b) $7 → 22 → 11 → 34 → 17 → 52 → 26 → 13 → 40 → 20 → 10 → ...$ (s.a.)
- (c) $17 → ...$ (s.a.)
- (d) $21 → 64 → 32 → 16 → ...$ (s.a.)

40. Verify the 3x + 1 conjecture for these integers.
- (a) $16 → ...$ (s.a.)
- (b) $11 → ...$ (s.a.)
- (c) $35 → 106 → ❌54 → 27 → 82 → 41 → 124 → 62 → 31 → 94 → 47 → 142 → 71 → 214 → 107 → 322 → 161 → 484 → 242 → 121 → 364 → 182 → 91 → 274 → 137 → 412 → 206 → 103 → 310 → 155 → 466 → 233 → ...$
- (d) $113 → 340 → 170 → ❌511 → 1534 → 767 → ...$

41. Prove or disprove that you can use dominoes to tile the standard checkerboard with two adjacent corners removed (that is, corners that are not opposite).
    - Constructive Existence Proof: The removal of two adjacent corners results in a row between them of 6 squares with 3 black and 3 white, so this can be tiled. Building upon the proof of 1.8/Example 18 the rest of the board can be tiled horizontally.

42. Prove or disprove that you can use dominoes to tile a standard checkerboard with all four corners removed.
    - Extending the proof given in 41 to two rows connecting two corners each, a tiling is possible, if both rows are on oppsite sides of the board.

43. Prove that you can use dominoes to tile a rectangular checkerboard with an even number of squares.
    - As every domino covers an even number of squares and every recangular grid with an even number of squares must have at least one side with an even number of squares any of those boards can be tiled by aligning the dominoes with their longer side to the even sides of the rectangle.

44. Prove or disprove that you can use dominoes to tile a 5 × 5 checkerboard with three corners removed.
    - ✅ A board with both sides odd will always have the same colour in all corners. Therefore we assume WLOG that the rsulting board has 10 black and 12 white squares (3 black ones being removed), so a tiling with dominoes covering two adjacent squares is impossible.

45. Use a proof by exhaustion to show that a tiling using dominoes of a 4 × 4 checkerboard with opposite corners removed does not exist. [Hint: First show that you can assume that the squares in the upper left and lower right corners are removed. Number the squares of the original checkerboard from 1 to 16, starting in the first row, moving right in this row, then starting in the leftmost square in the second row and moving right, and so on. Remove squares 1 and 16. To begin the proof, note that square 2 is covered either by a domino laid horizontally, which covers squares 2 and 3, or vertically, which covers squares 2 and 6. Consider each of these cases separately, and work through all the subcases that arise.]
    - WLOG we can assume that when two opposite corners are removed these can be considered the upper left and lower right while the entire board is numbered from 1 to 16 in reading-direction.
    - Considering the fact that the domino at 2 must either also cover 3 or 6 we construct a tiling starting with these cases, looking for a contradiction.
    - ✅ (1) 2-3, 4-5, 11-12, 14-15, 9-13, 6-10: 5 and 7 cannot be tiled.
    - ✅ (2) 2-6, 5-9, 13-14, 11-15: 10 cannot be tiled

46. (*) Prove that when a white square and a black square are removed from an 8 × 8 checkerboard (colored as in the text) you can tile the remaining squares of the checkerboard using dominoes. [Hint: Show that when one black and one white square are removed, each part of the partition of the remaining cells formed by inserting the barriers shown in the figure can be covered by dominoes.]
    - Considering the structure given in the figure,a tiling can be made that covers the entire board in a continuous path of dominoes connected by their shorter sides.
    - By removing two arbitrary squares, one black and one white both parts of the line will have an even number of squares and the same number of black and white squares so both can be tiled.

47. Show that by removing two white squares and two black squares from an 8 × 8 checkerboard (colored as in the text) you can make it impossible to tile the remaining squares using dominoes.
    - By removing squares 2-3 and 9-10 the upper left corner can no longer be tiled.

48. (∗) Find all squares, if they exist, on an 8 × 8 checkerboard such that the board obtained by removing one of these square can be tiled using straight triominoes. [Hint: First use arguments based on coloring and rotations to eliminate as many squares as possible from consideration.]
    - ❌ We assume a checkerboard with three colours. The result is 22 squares of colour a and 21 of b and c (which could be exchanged by rotation). So to make a tiling possible one of the white squares (a) would have to be removed to allow for a tiling with 21 triominoes.
    - ❎ If we study Figure 7, we see that by rotating or reflecting the board, we can make any square nonwhite, with the exception of the squares with coordinates (3,3), (3,6), (6,3), (6,6). Therefore the same argument as was used in Example 22 shows that we cannot tile the board using straight triominoes if any one of those other 60 squares is removed.
    - A tiling with one of those four removed is however possible (see solutions guide).

49. (∗)
- (a) Draw each of the five different tetrominoes, where a tetromino is a polyomino consisting of four squares.
  - ⭕ (forgot the L-shaped one)
- (b) For each of the five different tetrominoes, prove or disprove that you can tile a standard checkerboard using these tetrominoes.
  - Clearly, tilings are possible for the straight and the square shape.
  - Two L-shapes can form a 2 by 4 block which can also be used for a tiling.
  - If the S-shape should cover a corner square one of the adjacent corners will be closed in while the other will be covered by an overhanging tetrominoe, so a tiling is impossible.
  - ⭕ The T-shape can also be used by forming a 4 by 4 block ou of 4 shapes.

50. (∗) Prove or disprove that you can tile a 10 × 10 checkerboard using straight tetrominoes.
    - ❌ Assuming a checkerboard coloured in alternating fashion similar to Figure 7 with four colours the resulting board has 26 squares of colour a, 25 of b, 24 of c and 25 of d. A straight tetrominoe would have to cover one of each colour in any position, so we would need the same number of squares in each colour which is not the case.
    - ❎ Assume that 25 straight tetrominoes can cover the board. Some will be placed horizontally and some vertically. Because there is an odd number of tiles, the number placed horizontally and the number placed vertically cannot both be odd, so assume WLOG that an even number of tiles are placed horizontally. Color the squares in order using four colours in a certain order repeatedly, starting in the upper left corner and proceeding in reading direction. Then it is clear that every horizontally placed tile cover one square of each colour and every vertically placed one cover 0 or 2 squares of each colour. It follows that in this tiling an even number of squares of each colour are covered. But this contradicts the fact that there are 25 squares of each colour. Therefore no such colouring exists.
