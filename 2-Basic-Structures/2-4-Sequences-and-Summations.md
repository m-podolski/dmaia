# Sequences and Summations

1. Find these terms of the sequence $\{a_n\}$, where $a_n = 2 · (−3)^n + 5^n$.
- (a) $a_0 = 3$
- (b) $a_1 = -1$
- (c) $a_4 = 787$
- (d) $a_5 = 2639$

2. What is the term $a_8$ of the sequence $\{a_n\}$ if $a_n$ equals
- (a) $2^{n−1}: 128$
- (b) $7 : 7$
- (c) $1 + (−1)^n : 0$
- (d) $−(−2)^n : -256$

3. What are the terms $a_0$ , $a_1$, $a_2$, and $a_3$ of the sequence $\{a_n\}$, where $a_n$ equals
- (a) $2^n + 1$
  - $a_0 = 2, a_1 = 3, a_2 = 5, a_3 = 9$
- (b) $(n + 1)^{n+1}$
  - $a_0 = 1, a_1 = 4, ❌ a_2 = 9, a_3 = 16$
  - ✅ $a_2 = 27, a_3 = 256$
- (c) $⌊n/2⌋$
  - $a_0 = 0, a_1 = 0, a_2 = 1, a_3 = 1$
- (d) $⌊n/2⌋ + ⌈n/2⌉$
  - $a_0 = 0, a_1 = 1, a_2 = 2, a_3 = 3$

4. What are the terms $a_0$ , $a_1$, $a_2$, and $a_3$ of the sequence $\{a_n\}$, where $a_n$ equals
- (a) $(−2)^n$
  - $a_0 = 1, a_1 = -2, a_2 = 4, a_3 = -8$
- (b) $3$
  - $3$
- (c) $7 + 4^n$
  - $a_0 = 8, a_1 = 11, a_2 = 23, a_3 = 71$
- (d) $2^n + (−2)^n$
  - $a_0 = 2, a_1 = 0, a_2 = 8, a_3 = 0$

5. List the first 10 terms of each of these sequences.
- (a) the sequence that begins with 2 and in which each successive term is 3 more than the preceding term
  - $\{2, 5, 8, 11, 14, 17 ,20, 23, 26, 29\}$
- (b) the sequence that lists each positive integer three times, in increasing order
  - $\{1, 1, 1, 2, 2, 2, 3, 3, 3, 4\}$
- (c) the sequence that lists the odd positive integers in increasing order, listing each odd integer twice
  - $\{1, 1, 3, 3, 5, 5, 7, 7, 9, 9\}$
- (d) the sequence whose nth term is $n! − 2^n$
  - $\{-1, -2, -2, 8, 88, 656, 4912, 40064, 362368, 3627776\}$
- (e) the sequence that begins with 3, where each succeeding term is twice the preceding term
  - $\{3, 6, 12, 24, 48, 96, 192, 384, 768, 1536\}$
- (f) the sequence whose first term is 2, second term is 4, and each succeeding term is the sum of the two preceding terms
  - $\{2, 4, 6, 10, 16, 26, 42, 68, 110, 178\}$
- (g) the sequence whose $n$ th term is the number of bits in the binary expansion of the number $n$ (defined in Section 4.2)
  - $\{\}$
  - ✔ For $n = 1$, the binary expansion is $1$, which has one bit, so the first term of the sequence is $1$. For $n = 2$, the binary expansion is $10$, which has two bits, so the second term of the sequence is $2$. Continuing in this way we see that the first ten terms are $1,2,2,3,3,3,3,4,4,4$. Note that the sequence has one 1, two 2's, four 3's, eight 4's, as so on, with $2^{k-1}$ copies of $k$.
- (h) the sequence where the $n$ th term is the number of letters in the English word for the index $n$
  - ❕ $\{\}$

6. List the first 10 terms of each of these sequences.
- (a) the sequence obtained by starting with 10 and obtaining each term by subtracting 3 from the previous term
  - ❕ $\{\}$
- (b) the sequence whose nth term is the sum of the first $n$ positive integers
  - $\{1, 3, 6, 10, 15, 21, 28, 36, 45, 55\}$
- (c) the sequence whose nth term is $3^n − 2^n$
  - $\{1, 5, 19, 65, 211, 665, 2059, 6305, 19171, 58025\}$
- (d) the sequence whose nth term is $⌊\sqrt{n}⌋$
  - $\{1, 1, 1, 2, 2, 2, 2, 2, 3, 3\}$
- (e) the sequence whose first two terms are 1 and 5 and each succeeding term is the sum of the two previous terms
  - $\{1, 5, 6, 11, 17, 28, 45, 73, 118, 191\}$
- (f) the sequence whose nth term is the largest integer whose binary expansion (defined in Section 4.2) has $n$ bits (Write your answer in decimal notation.)
  - $\{\}$
  - ✔ The largest number whose binary expansion has $n$ bits is $(11 . . . 1)_2$, which is $2n − 1$. So the sequence is $1, 3, 7, 15, 31, 63, 127, 255, 511, 1023$.
- (g) the sequence whose terms are constructed sequentially as follows: start with 1, then add 1, then multiply by 1, then add 2, then multiply by 2, and so on
  - $\{1, 2, 2, 4, ❌ 16, 19, 57, 61, 244, 249\}$
  - $\{1, 2, 2, 4, ✅ 8, 11, 33, 37, 148, 153\}$
- (h) the sequence whose nth term is the largest integer $k$ such that $k! ≤ n$
  - $\{1, 2, 2, 2, 2, 3, 3, 3, 3, 3\}$

7. Find at least three different sequences beginning with the terms $1, 2, 4$.
   - $a_n = 2^n$
   - $a_n = 2a_{n-1}$
   - $a_n = a_{n-1} + n$

8. Find at least three different sequences beginning with the terms $3, 5, 7$.
   - odd integers starting from 3.
   - $a_n = a_{n-1} + 2$
   - prime numbers starting from 3.

9. Find the first five terms of the sequence defined by each of these recurrence relations and initial conditions.
- (a) $a_n = 6a_{n−1} , a_0 = 2$
  - $\{2, 12, 72, 432, 2592\}$
- (b) $a_n = a²_{n−1}, a_1  = 2$
  - $\{2, 4, 16, 256, 65536\}$
- (c) $a_n = a_{n−1} + 3a_{n−2} , a_0 = 1, a_1 = 2$
  - $\{1, 2, 5, 11, 26\}$
- (d) $a_n = na_{n−1} + n² a_{n−2} , a_0 = 1, a_1 = 1$
  - $\{1, 1, 6, ❌ 54, 312\}$
  - $\{1, 1, 6, ✅ 27, 204\}$
- (e) $a_n = a_{n−1} + a_{n−3} , a_0 = 1, a_1 = 2, a_2 = 0$
  - $\{1, 2, 0, 1, 3\}$

10. Find the first six terms of the sequence defined by each of these recurrence relations and initial conditions.
- (a) $a_n = −2a_{n−1}, a_0 = −1$
  - $\{-1, 2, -4, 8, -16, 32\}$
- (b) $a_n = a_{n−1} − a_{n−2}, a_0 = 2, a_1 = −1$
  - $\{2, -1, -3, -2, 1, 3\}$
- (c) $a_n = 3a²_{n−1}, a_0  = 1$
  - $\{1, 3, 27, 2187, 14348907, 6.17673396\times10^{14}\}$
- (d) $a_n = na_{n−1} + a²_{n−2}, a_0  = −1, a_1  = 0$
  - $\{-1, 0, 1, 3, ❌ 21, 546\}$
  - $\{-1, 0, 1, 3, ✅ 13, 74\}$
- (e) $a_n = a_{n−1} − a_{n−2} + a_{n−3}, a_0 = 1, a_1 = 1, a_2 = 2$
  - $\{1, 1, 2, 2, 1, 1\}$

11. Let $a_n = 2^n + 5 · 3^n$ for $n = 0, 1, 2, ...$.
- (a) Find $a_0$, $a_1$, $a_2$, $a_3$, and $a_4$.
  - $\{6, 17, 49, 143, 421\}$
- (b) Show that
- $a_2 = 5a_1 − 6a_0,$
- $a_3 = 5a_2 − 6a_1$, and
- $a_4 = 5a_3 − 6a_2$.
  - $a_2 = 5(17) − 6(6) = 85 - 36 = 49$
  - $a_3 = 5(49) − 6(17) = 245 - 102 = 143$
- (c) Show that $a_n = 5a_{n−1} − 6a_{n−2}$ for all integers $n$ with $n ≥ 2$.
  - $5a_{n−1} − 6a_{n−2}$
  - $5(2^{n-1} + 5 · 3^{n-1}) − 6(2^{n-2} + 5 · 3^{n-2})$
  - ❌ $(10^{n-1} + 75^{n-1}) + (- 12^{n-2} - 90^{n-2})$
  - $85^{n-1} − 102^{n-2}$
  - ✅ $5(2^{n-1} + 5 · 3^{n-1}) − 6(2^{n-2} + 5 · 3^{n-2})$
  - ⚠️ $2^{n-2}(10 - 6) + 3^{n-2}(75 - 30)$
  - $2^{n-2}(4) + 3^{n-2}(9)(5)$
  - $2^{n} + 3^{n}(5)$

12. Show that the sequence $\{a_n\}$ is a solution of the recurrence relation $a_n = −3a_{n−1} + 4a_{n−2}$ if
- (a) $a_n = 0$
  - $−3a_{n−1} + 4a_{n−2} = -3(0) + 4(0) = 0 = a_n$
- (b) $a_n = 1$
  - $−3 + 4 = 1$
- (c) $a_n = (−4)^n $
  - $−3(−4)^{n−1} + 4(−4)^{n−2}$
  - $−3(−4)^{n−2}(-4) + 4(−4)^{n−2}$
  - $(−4)^{n−2}(12 + 4)$
  - $(−4)^{n−2}(-4)(-4)$
  - $(−4)^{n}$
- (d) $a_n = 2(−4)^n + 3$
  - $−3(2(−4)^{n−1} + 3) + 4(2(−4)^{n−2} + 3)$
  - $(-6(−4)^{n−1} - 9) + (8(−4)^{n−2} + 12)$
  - $(-6(−4)^{n−2}(-4) - 9) + (8(−4)^{n−2} + 12)$
  - ❌ $(−4)^{n−2}((24 - ?) + (8 + (-3)))$
  - ✅ $(−4)^{n−2}((-6)(-4) + (4 * 2)) - 9 + 12$
  - $(−4)^{n−2} * 32 + 3$
  - $(−4)^{n−2}(−4)² * 2 + 3$
  - $2(−4)^{n} + 3$

13. Is the sequence $\{a_n\}$ a solution of the recurrence relation
$a_n = 8a_{n−1} − 16a_{n−2}$ if
- (a) $a_n = 0$
  - $8(0) − 16(0) = 0$ **Yes**
- (b) $a_n = 1$
  - $8 − 16 = -8$ **No**
- (c) $a_n = 2^n $
  - $8(2^{n−1}) − 16(2^{n−2})$
  - $(2^{n−1})(2)(2²) − (2^{n−2})(2²)(4)$
  - $(2^n)(4) − (2^n)(4)$
  - $(2^n)(4) − (2^n)(4) = 0$ **No**
- (d) $a_n = 4^n $
  - $(2)(4)(4^{n−1}) − (4)²(4^{n−2})$
  - $(2)(4^{n}) − (4^{n})$
  - $4^{n}$ **Yes**
- (e) $a_n = n4^n $
  - $(2)(4)(n-1)(4^{n−1}) − (4)²(n-2)(4^{n−2})$
  - $(2)(n-1)(4^{n}) − (n-2)(4^{n})$
  - $(2n-2)(4^{n}) − (n-2)(4^{n})$
  - $n4^{n}$ **Yes**
- (f) $a_n = 2(4^n) + 3n(4^n)$
  - $(16(4^{n−1}) + 24(n - 1)(4^{n−1})) − (32(4^{n-2}) + 48(n - 2)(4^{n-2}))$
  - $16(4^{n−2})(4) + 24(n - 1)(4^{n−2})(4) − 32(4^{n-2}) + 48(n - 2)(4^{n-2})$
  - $4^{n−2}(144n - 160)$
  - $4^{n−2}(4²)(9n - 10)$
  - ❌ $- 10(4^{n}) + 9n(4^{n})$ **No**
  - ✅ $a_n = 8(2(4^{n−1}) + 3(n-1)(4^{n−1})) − 16(2(4^{n−2}) + 3(n-2)(4^{n−2}))$
  - $4^{n−2}(8 * 2 * 4 + 8 * 3(n-1) * 4 - 16 * 2 - 16 * 3(n-2))$
  - $4^{n−2}(64 + 96n - 96 - 32 - 48n + 96)$
  - $4^{n−2}(48n + 32)$
  - $4^{n−2}(4²)(3n + 2)$
  - $(2 + 3n)(4^{n})$
- (g) $a_n = (−4)^n$
  - $8(−4)^{n−1} − 16(−4)^{n−2}$
  - ❌ $2(−4)^{n} − (−4)^{n}$
  - $(−4)^{n}$ Yes
  - ✅ $(−4)^{n−2}(8 * (−4) − 16)$
  - $(−4)^{n−2}(-48)$
  - $(-3)(−4)^{n}$ **No**
- (h) $a_n = n^2 * 4^n$
  - $8((n-1)^2 * 4^{n−1}) − 16((n-2)^2 * 4^{n−2})$
  - $4^{n−2}(8 * (n-1)^2 * 4 − 16 * (n-2)^2)$
  - $4^{n−2}(8 * (n² - 2n + 1) * 4 − 16 * (n² - 4n + 4))$
  - $4^{n−2}(32n² - 64n + 32 − 16n² ❌ - 64n + 64)$
  - $4^{n−2}(32n² - 64n + 32 − 16n² ✅ + 64n - 64)$
  - $4^{n−2}(16n² - 128n + 96)$
  - $(n² - 8n + 6)4^{n}$ **No**

14. For each of these sequences find a recurrence relation satisfied by this sequence. (The answers are not unique because there are infinitely many different recurrence relations satisfied by any sequence.)
- ❓ (a) $a_n = 3$
  - ✅ (answers are not unique) $a_n = a_{n-1}$
- ❓ (b) $a_n = 2n$
  - ✅ Note that $a_n − a_{n−1} = 2n − (2n − 2) = 2$. Therefore we have $a_n = a_{n−1} + 2$ as one possible answer.
- ❓ (c) $a_n = 2n + 3$
  - ✅ Just as in part (b), we have $a_n = a_{n−1} + 2$.
- ❓ (d) $a_n = 5^n$
  - ✅ Probably the simplest answer is $a_n = 5a_{n−1}$.
- (e) $a_n = n^2$
  - ❌ $a_{n−1}²$
  - $(n−1)² = n² - 2n + 1$
  - ✅ Since $a_n - a_{n-1} = n² - (n - 1)² = 2n - 1$, we have $a_n = a_{n−1} + 2n - 1$
- (f) $a_n = n^2 + n$
  - $a_n - a_{n-1} = n² + n - ((n - 1)² + (n - 1))$
  - $a_n - a_{n-1} = n² + n - n² + 2n - 1 - n + 1$
  - $a_n= 2n$
  - $a_n =  a_{n-1} + 2n$
- (g) $a_n = n + (−1)^n$
  - $a_n - a_{n-1} = (n + (−1)^n) - (n - 1 + (−1)^{n - 1})$
  - $a_n - a_{n-1} = (n + (-1)(−1)^{n - 1}) - (n - 1 + (−1)^{n - 1})$
  - $a_n - a_{n-1} = (−1)^{n - 1}((-1) + 1) + n - n + 1$
  - ❌ $a_n - a_{n-1} = (−1)^{n - 1} + 1$
  - ✅ $a_n - a_{n-1} = n + (−1)^n - (n - 1) - (−1)^{n - 1}$
  - $a_n - a_{n-1} = 1 + 2(−1)^n$
- (h) $a_n = n!$
  - $a_n = na_{n-1}$

15. Show that the sequence $\{a_n\}$ is a solution of the recurrence relation $a_n = a_{n−1} + 2a_{n−2} + 2n − 9$ if
- (a) $a_n = − n + 2$
  - $a_n = ((- (n - 1)) + 2) + 2((- (n - 2)) + 2) + 2n − 9$
  - $a_n = (- n + 1 + 2) + (- 2n + 4 + 4) + 2n − 9$
  - $a_n = - n - 2n + 2n − 9 + 1 + 2  + 4 + 4$
  - $a_n = - n + 2$
- (b) $a_n = 5(−1)^n − n + 2$
  - $a_n = (5(−1)^{n-1} − (n - 1) + 2) + 2(5(−1)^{n-2} − (n - 2) + 2) + 2n − 9$
  - $a_n = (5(−1)^{n-1} − n + 3) + (10(−1)^{n-2} − 2n + 8) + 2n − 9$
  - $a_n = (−1)^{n-2}(10 - 5) + (− n + 3) + (− 2n + 8) + 2n − 9$
  - $a_n = 5(−1)^{n-2} − n + 2$
  - ✔ $(−1)^{n-2} = (−1)^{n}$ since $(−1)^{2} = 1$
- (c) $a_n = 3(−1)^n + 2^n − n + 2$
  - $a_n = (3(−1)^{n−1} + 2^{n−1} − n + 3) + (6(−1)^{n−2} + (2)2^{n−2} − 2n + 8) + 2n − 9$
  - $a_n = (−1)^{n−2}(- 3 + 6) + ((2)2^{n−2} − n + 3) + ((2)2^{n−2} − 2n + 8) + 2n − 9$
  - ❌ $a_n = (−1)^{n−2}(- 3 + 6) + 2^{n−2}(2 + 2) + (− n + 3) + (− 2n + 8) + 2n − 9$
  - $a_n = (3)(−1)^{n−2} + (4)2^{n−2} − n - 4$
  - ✅ $a_n = 3(−1)^{n−1} + 2^{n−1} − (n - 1) + 2 + 2(3(−1)^{n−2} + 2^{n−2} − (n - 2) + 2) + 2n − 9$
  - ✅ $a_n = 3(−1)^{n−2}(- 1 + 2) + 2^{n−2}(2 + 2) − n + 2$
- (d) $a_n = 7 * 2^n − n + 2$
  - $a_n = 7 * 2^{n−1} − (n - 1) + 2 + 2(7 * 2^{n−2} − (n - 2) + 2) + 2n − 9$
  - $a_n = 2^{n−2}(7 * 2 − n + 1 + 2) + 2(7 * 2 − n + 2 + 2) + 2n − 9$
  - $a_n = 7 * 2^{n−2}(2 − n + 1 + 2) + 2(2 − n + 2 + 2) + 2n − 9$
  - ❌ $a_n = 7 * 2^{n−2}(− n + 5) + 4$
  - ✅ $a_n = 2^{n−2}(7 * 2 + 2 * 7) - n + 2$

16. Find the solution to each of these recurrence relations with the given initial conditions. Use an iterative approach such as that used in Example 10.
- (a) $a_n = −a_{n−1}, a_0 = 5$
  - $a_0 = 5$
  - $a_1 = 5 * (- 1)$
  - ❌ $a_2 = 5 * 2 * (- 1)$
  - $a_n = 5 * (n * (-1))$
  - ✅ $a_n = − a_{n−1} = (-1)^2a_{n-2} = ... = (-1)^na_{n-n} = (-1)^na_0 = 5 * (-1)^n$
- (b) $a_n = a_{n−1} + 3, a_0 = 1$
  - $a_1 = 1 + (3 * 1)$
  - $a_2 = 1 + (3 * 2)$
  - $a_n = 1 + 3n$
- (c) $a_n = a_{n−1} − n, a_0 = 4$
  - $a_1 = 4 - 1$
  - $a_2 = 4 - 1 - 1$
  - $a_3 = 4 - (3 * 1)$
  - ❌ $a_n = 4 - n$
  - ✅ $a_n =  − n + a_{n−1}$
  - ✅ $a_n =  − n + (- (n - 1) + a_{n−2}) = - (n + (n - 1)) + a_{n-2}$
  - ✅ $a_n =  − (n + (n - 1)) + (- (n - 2) + a_{n−3}) = - (n + (n - 1)) + (n - 2) + a_{n−3}$
  - ✅ $a_n = - (n + (n - 1) + (n - 2) + \dotsb + (n - (n - 1))) + a_{n−n}$
  - ✅ $a_n = - (n + (n - 1) + (n - 2) + \dotsb + 1) + a_0$
  - ✅ $a_n = - \frac{n(n + 1)}{2} + 4$
  - ✅ $a_n = \frac{n² - n + 8}{2}$
- (d) $a_n = 2a_{n−1} − 3, a_0 = −1$
  - $− 3 + 2a_{n−1}$
  - $− 3 + 2(2 * a_{n−2} - 3)$
  - ❌ $−3 + 2(2 * (2 * a_{n−3} - 3) - 3)$
  - ✅ $−3 + 2(- 3 + 2a_{n−2}) = - 3 + 2(-3) + 4a_{n−2}$
  - ✅ $−3 + 2(-3) + 4(- 3 + 2a_{n−3}) $
  - $= - 3 + 2(-3) + 4a_{n−2} = - 3 + 2(-3) +(-3) + 8a_{n-3}$
  - ✅ $−3 + 2(−3) + 4(−3) + 8(−3 + 2a_{n−4}) $
  - $= −3 + 2(−3) + 4(−3) + 8(−3) + 16a_{n−4}$
  - $\ddots$
  - ✅ $−3(1 + 2 + 4 + \dotsb + 2^{n-1}) + 2^na_{n-n} $
  - $= −3(2^n - 1) + 2^n(-1) = -2^n{n+2} + 3$
- (e) $a_n = (n + 1)a_{n − 1} , a_0 = 2$
  - $(n + 1)a_{n − 1}$
  - $((n - 1) + 1)((n + 1)a_{n − 2}) = (n + 1)na_{n − 2}$
  - $((n - 1) + 1)(n - 1)(n + 1)a_{n − 3}$
  - $(n + 1)n(n - 1)a_{n − 3}$
  - $((n - 1) + 1)(n - 1)((n - 1) - 1)(n + 1)a_{n − 4}$
  - $(n + 1)n(n - 1)(n - 2)a_{n − 4}$
  - $\ddots$
  - ⭕ $(n + 1)n(n - 1)(n - 2)(n - 3) ... (n - (n -2)) a_{n − n}$
  - ⭕ $(n + 1)n(n - 1)(n - 2)(n - 3) ... 2 * a_0$
  - ⭕ $(n + 1)! * 2 = 2(n + 1)!$
- (f) $a_n = 2na_{n − 1}, a_0 = 3$
  - $2na_{n − 1}$
  - ❌ $2(n - 1)2(n - 1)a_{n − 2} = 4(n - 1)²a_{n − 2}$
  - ✅ $2n(2(n - 1)a_{n − 2}) = 2²(n(n - 1))a_{n − 2}$
  - $2²(n(n - 1))2(n - 2)a_{n − 3} = 2³(n(n - 1)(n - 2))a_{n − 3}$
  - $\ddots$
  - $2^n n(n - 1)(n - 2) \dotsb (n - (n - 1))a_{n − n}$
  - $2^n n(n - 1)(n - 2) \dotsb 1 * a_0$
  - $2^n n(n - 1)(n - 2) \dotsb 3$
  - $3 * 2^n n!$
- (g) $a_n = n − 1 − a_{n − 1}, a_0 = 7$
  - $(n − 1) − a_{n − 1}$
  - $(n − 1) − ((n - 1) - 1 − a_{n − 2})$
  - $(n − 1) − (n - 2) + a_{n − 2}$
  - $(n − 1) − (n - 2) + ((n − 2) - 1 − a_{n − 3})$
  - $(n − 1) − (n - 2) + (n − 3) − a_{n − 3}$
  - $\ddots$
  - ❌ $(n − 1) − (n - 2) + (n − 3) - \dots ((n - (n - 1)) − 1 - a_{n − n})$
  - ✅ $(n − 1) − (n - 2) + \dots + (- 1)^{n- 1}(n - n) + (-1)^n a_{n − n}$
  - $\frac{2n - 1 + (-1)^n}{4} + (-1)^n * 7$

17. Find the solution to each of these recurrence relations and initial conditions. Use an iterative approach such as that used in Example 10.
- (a) $a_n = 3a_{n−1} , a_0 = 2$
  - $a_n = 3²a_{n−2}$
  - $a_n = 3³a_{n−3}$
  - $\dotsb$
  - $a_n = 3^{n}a_{n−n}$
  - $a_n = 3^{n} · 2$
- (b) $a_n = a_{n−1} + 2, a_0 = 3$
  - $a_n = 2 + a_{n−1}$
  - $a_n = 2 + (2 + a_{n−2}) = (2 · 2) + a_{n−2}$
  - $a_n = (2 · 2) + (2 + a_{n−3}) = (3 · 2) + a_{n−3}$
  - $\dotsb$
  - $a_n = 2n + a_{n−n} = 2n + 3$
- (c) $a_n = a_{n−1} + n, a_0 = 1$
  - $a_n = n + a_{n−1}$
  - $a_n = n + ((n - 1) + a_{n−2}) = (n + (n - 1)) + a_{n-2}$
  - $a_n = (n + (n - 1)) + ((n - 2) + a_{n-3}) = (n + (n - 1) + (n - 2)) + a_{n-3}$
  - $\dotsb$
  - $a_n = (n + (n - 1) + (n - 2) + \dotsb + (n - (n - 1))) + a_{n-n}$
  - $a_n = (n + (n - 1) + (n - 2) + \dotsb + 1) + a_{0}$
  - ❌ $a_n = \frac{n²(n + 1)}{2} + 1$
  - $a_n = \frac{n²(n + 1) + 2}{2}$
  - ✅ $a_n = \frac{n(n + 1)}{2} + 1$
  - $a_n = \frac{n² + n + 2}{2}$
- (d) $a_n = a_{n−1} + 2n + 3, a_0 = 4$
  - $a_n = 3 + 2n + a_{n−1}$
  - $a_n = 3 + 2n + (3 + 2(n - 1) + a_{n−2})$
  - $a_n = 2 · 3 + 2(n + (n - 1)) + a_{n−2}$
  - $a_n = 2 · 3 + 2(n + (n - 1)) + (3 + 2(n - 2) + a_{n−3})$
  - $a_n = 3 · 3 + 2(n + (n - 1) + (n - 2)) + a_{n−3}$
  - $\dotsb$
  - $a_n = 3n + 2(n + (n - 1) + (n - 2) + \dots + (n - (n - 1))) + a_{n−n}$
  - $a_n = 3n + 2(n + (n - 1) + (n - 2) + \dots + 1) + a_{0}$
  - $a_n = 3n + 2(\frac{n(n + 1)}{2}) + 4$
  - $a_n = 3n + n(n + 1) + 4 = n² + 4n + 4$

- (e) $a_n = 2a_{n−1} − 1, a_0 = 1$
  - $a_n = − 1 + 2a_{n−1}$
  - $a_n = − 1 + 2(− 1 + 2a_{n−2})$
  - ❌ $a_n = 2 · (− 1) + 2^{2}a_{n−2}$
  - $a_n = 3 · (− 1) + 2^{3}a_{n−3}$
  - $\dots$
  - $a_n = n · (− 1) + 2^{n}a_{n−n}$
  - $a_n = − 1n + 2^{n}$
  - ✅ $a_n = - 1 + 2(- 1 + 2a_{n−2}) = - 3 + 4a_{n−2}$
  - ✅ $a_n = - 3 + 2^{2}(- 1 + 2a_{n−3}) = - 7 + 8a_{n−3}$
  - ✅ $a_n = - 7 + 2^{3}(- 1 + 2a_{n−4}) = - 15 + 16a_{n−4}$
  - $\dots$
  - ✅ $a_n = - (2^n - 1) + 2^{n}a_{n−n} = - 2^n + 1 + 2^n · 1 = 1$
- (f) $a_n = 3a_{n−1} + 1, a_0 = 1$
  - $a_n = 1 + 3a_{n−1}$
  - $a_n = 1 + 3(1 + 3a_{n−2}) = 4 + 3^{2}a_{n−2}$
  - $a_n = 4 + 3^{2}(1 + 3a_{n−3}) = 13 + 3^{3}a_{n−3}$
  - $a_n = 13 + 3^{3}(1 + 3a_{n−4}) = 40 + 3^{4}a_{n−4}$
  - $\dots$
  - ❌ $a_n = 3^{n} + 3^{n-1} + 3^{n} · 1$
  - ✅ $a_n = (1 + 3 + 3^{2} + \dots + 3^{n-1}) + 3^{n}a_{n−n}$
  - ✅ $a_n = \frac{3^{n-1} - 1}{3 - 1} = \frac{3^{n-1} - 1}{2}$
- (g) $a_n = na_{n−1}, a_0 = 5$
  - $a_n = na_{n−1}$
  - ❌ $a_n = n(na_{n−2}) = n²a_{n−2}$
  - $a_n = n²(na_{n−3}) = n^{3}a_{n−3}$
  - $\dots$
  - $a_n = n^{n}a_{n−n} = 5n^{n}$
  - ✅ $a_n = n(n - 1)a_{n−2}$
  - ✅ $a_n = n(n - 1)(n - 2)a_{n−3}$
  - $\dots$
  - ✅ $a_n = n(n - 1)(n - 2)(n - 3) \dots (n - (n - 1))a_{n−n}$
  - ✅ $a_n = n(n - 1)(n - 2)(n - 3) \dots 1a_{0}$
  - ✅ $a_n = 5n!$
- (h) $a_n = 2na_{n−1}, a_0 = 1$
  - $a_n = 2na_{n−1}$
  - $a_n = 2n(2(n - 1)a_{n−2}) = 2²n(n - 1)a_{n−2}$
  - $a_n = 2²n(n - 1)(2(n - 2)a_{n−3}) = 2³n(n - 1)(n - 2)a_{n−3}$
  - $\dots$
  - $2^{n}n(n - 1)(n - 2) \dots (n - (n - 1))a_{n−n}$
  - $2^{n}n(n - 1)(n - 2) \dots 1 · 1$
  - ❌ $\frac{1 · (n + 1)^{n+1} - 1}{(n + 1) - 1}$
  - $\frac{(n + 1)^{n+1} - 1}{n}$
  - ✅ $2^{n}n!$

18. A person deposits $1000 in an account that yields 9% interest compounded annually.
- (a) Set up a recurrence relation for the amount in the account at the end of $n$ years.
- (b) Find a formula for the amount in the account at the end of $n$ years.
- (c) How much money will the account contain after 100 years?
  - (a) $a_n = (9/100)a_{n-1}, a_0 = 1000$
    - ✔ $a_n = 1.09a_{n-1}$
  - (b) $a_n = 1.09a_{n-1}$
    - $a_n = 1.09a_{n-1}$
    - $a_n = 1.09(1.09a_{n-2}) = 1.09²a_{n-2}$
    - $a_n = 1.09²(1.09a_{n-3}) = 1.09³a_{n-3}$
    - $\dots$
    - $a_n = 1.09^{n} ·1000$
  - (c) $5 529 040.792$

19. Suppose that the number of bacteria in a colony triples every hour.
- (a) Set up a recurrence relation for the number of bacteria after $n$ hours have elapsed.
- (b) If 100 bacteria are used to begin a new colony, how many bacteria will be in the colony in 10 hours?
  - (a) $a_n = 3a_{n-1}$
  - (b) $a_0 = 100$
    - $a_n = 3(3a_{n-2}) = 3²a_{n-2}$
    - $\dots$
    - $a_n = 3^{n}a_{n-n} = 3^{n} · 100$
    - $3^{10} · 100 = 5 904 900$

20. ❕ Assume that the population of the world in 2010 was 6.9 billion and is growing at the rate of 1.1% a year.
- (a) Set up a recurrence relation for the population of the world $n$ years after 2010.
- (b) Find a formula for the population of the world $n$ years after 2010.
- (c) What will the population of the world be in 2030?

21. A factory makes custom sports cars at an increasing rate. In the first month only one car is made, in the second month two cars are made, and so on, with $n$ cars made in the nth month.
- (a) Set up a recurrence relation for the number of cars produced in the first n months by this factory.
  - $a_n = c_{n-1} + n, a_0 = 0$
- (b) How many cars are produced in the first year?
  - $\frac{12^2 + 12}{2} = 78$
- (c) Find an explicit formula for the number of cars produced in the first $n$ months by this factory.
  - $a_n = n + a_{n-1}$
  - $a_n = n + ((n - 1) + a_{n-2}) = n + (n - 1) + a_{n-2}$
  - $a_n = n + (n - 1) + (n - 2) + a_{n-3}$
  - $\dots$
  - $a_n = n + (n - 1) + (n - 2) + \dots + (n - (n - 1)) + a_{n-n}$
  - $a_n = n + (n - 1) + (n - 2) + \dots + 1 + 0$
  - $\frac{n(n + 1)}{2} = \frac{n^2 + n}{2}$

22. An employee joined a company in 2009 with a starting salary of \$50,000. Every year this employee receives a raise of \$1000 plus 5% of the salary of the previous year.
- (a) Set up a recurrence relation for the salary of this employee n years after 2009.
  - $a_n = 1 + 1.05a_{n-1}, a_0 = 50$ (in thousands of dollars)
- (b) What will the salary of this employee be in 2017?
  - $70 · (1.05)^8 - 20 ≈ 83.421$
- (c) Find an explicit formula for the salary of this employee n years after 2009.
  - $a_n = 1 + 1.05a_{n-1}$
  - $a_n = 1 + 1.05(1 + 1.05a_{n-2})$
  - $a_n = 1 + (1 · 1.05) + 1.05^{2}a_{n-2}$
  - $a_n = 1 + (1 · 1.05) + 1.05^{3}(1 + 1.05a_{n-3})$
  - $a_n = 1 + (1 · 1.05) + 1.05^{3}a_{n-3}$
  - $a_n = 1 + (1 · 1.05) + (1 · 1.05 · 1.05) + 1.05^{4}a_{n-4}$
  - $\dots$
  - $a_n = 1 + (1 · 1.05) + (1 · 1.05 · 1.05) + \dots + (1 · (n - 1) · 1.05) + 1.05^{n}a_{n-n}$
  - $a_n = 1 + (1.05) + (1.05 · 1.05) + \dots + ((n - 1) · 1.05) + 1.05^{n}a_{0}$
  - $\frac{1 · (1.05)^{n+1} - 1}{1.05 - 1} · 1.05^n · 50$
  - ✔ $70 · (1.05)^n - 20$

23. Find a recurrence relation for the balance $B(k)$ owed at the end of $k$ months on a loan of **5000 dollar** at a rate of **7%** if a payment of **100** is made each month. [Hint: Express $B(k)$ in terms of $B(k − 1)$; the monthly interest is $(0.07/12)B(k − 1)$.]
    - ❌ $b_k = - 0.1 + (0.07/12)b_{k-1}, b_0 = 5$
    - ✅ $b_k = b_{k-1} - (0.1 - (0.07/12)b_{k-1}), b_0 = 5$
    - $b_k = b_{k-2} - (0.1 + 0.1 · (0.07/12) - (0.07/12)^{2}b_{k-2})$
    - $b_k = b_{k-3} - (0.1 + 0.1 · (0.07/12) + 0.1 · (0.07/12)^{2} - (0.07/12)^{3}b_{k-3})$
    - $\dots$
    - $b_k = b_{k-k} - (0.1 + 0.1 · (0.07/12) + 0.1 · (0.07/12)^{2} + \dots + 0.1 · (0.07/12)^{k-1} - (0.07/12)^{k}b_{k-k})$

24. Parts:
- (a) Find a recurrence relation for the balance $B(k)$ owed at the end of $k$ months on a loan at a rate of $r$ if a payment $P$ is made on the loan each month. [Hint: Express $B(k)$ in terms of $B(k − 1)$ and note that the monthly interest rate is $r/12$.]
  - $B(k) = B(k - 1) - (P - \frac{r}{12}B(k - 1))$
  - ✔ $B(k) = (1 + \frac{r}{12})B(k - 1) - P$
- (b) ❓ Determine what the monthly payment $P$ should be so that the loan is paid off after $T$ months.
  - ✅ Iteration: $B(k) = (1 + (r/12))^{k}(B(0) - 12P/r) + 12Pr$
  - ✅ Set $B(k) = 0$: $T = \frac{log(-12P/(B(0)r - 12P))}{log(1 + (r/12))}$

25. For each of these lists of integers, provide a simple formula or rule that generates the terms of an integer sequence that begins with the given list. Assuming that your formula or rule is correct, determine the next three terms of the sequence.
- (a) $1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, . . .$
  - 0 and 1 alternate, while their number or places in the sequnce is incremented each time.
  - $+3 = \{1,1,1\}$
- (b) $1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, . . .$
  - Each odd number occurs once each even number twice.
  - $+3 = \{9,10,10\}$
- (c) $1, 0, 2, 0, 4, 0, 8, 0, 16, 0, . . .$
  - 0 alternates with powers of 2.
  - $+3 = \{32,0,64\}$
  - ✔ The nth term is $0$ if $n$ is even and $2^{(n-1)/2}$ if it is odd.
- (d) $3, 6, 12, 24, 48, 96, 192, . . .$
  - $a_n = 2a_{n-1}$, $a_0 = 3$
  - ⭕ $a_n = 3 · 2a_{n-1}$$
  - $\{384,768,1536\}$
- (e) $15, 8, 1, −6, −13, −20, −27, . . .$
  - $a_n = 15 - 7(n - 1)$
  - ✔ $a_n = 22 - 7n$
  - $\{-34, -41, -48\}$
- (f) $3, 5, 8, 12, 17, 23, 30, 38, 47, . . .$
  - ❌ $a_n = (n + 1) + a_{n-1}, a_0 = 3$
  - $a_n = (n + 1) + n + a_{n-2}$
  - $a_n = (n + 1) + n + (n - 1) + a_{n-3}$
  - $\dots$
  - $a_n = (n + 1) + n + (n - 1) + \dots + (n - (n - 1)) + a_{n-n}$
  - $a_n = (n + 1) + n + (n - 1) + \dots + 2 + 3$
  - $\frac{n² + 2n}{2} + 3$
  - ✅ $(n² + n + 4)/2$
  - ✅ $a_n = 3 + 2 + 3 + 4 + 5 \dots + n = n(n + 1)/2$
  - ✅ $a_n = (n(n + 1)/2) + 2$ (adding the difference of 1 and the initial term 3)
  - $\{57, 68, 80\}$
- (g) ⭕ $2, 16, 54, 128, 250, 432, 686, . . .$
  - $2$
  - $2·8 = 16$
  - $3·16 = 3·2·8 = 54$
  - $16·8 = 128$
  - $54·8 = 432$
  - ✅ $\{1024, 1458, 2000\}$
  - $a_n = 2n³$
- (h) ⭕ $2, 3, 7, 25, 121, 721, 5041, 40321, . . .$
  - ✅ $a_n = n! + 1$.

26. For each of these lists of integers, provide a simple formula or rule that generates the terms of an integer sequence that begins with the given list. Assuming that your formula or rule is correct, determine the next three terms of the sequence.
- (a) $3, 6, 11, 18, 27, 38, 51, 66, 83, 102, . . .$
  - $\{123, 146, 171\}$
  - $a_n = n² + 2, a_0 = 1$
  - ✔ $a_n = 2n - 1, a_0 = 3$
- (b) $7, 11, 15, 19, 23, 27, 31, 35, 39, 43, . . .$
  - $a_n = 4n - 1, a_0 = 2$
  - $\{47, 51, 55\}$
  - ✔ $a_n = 7 + 4(n - 1) = 4n + 3$
- (c) $1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, . .$
  - $\{1100, 1101, 1110\}$
  - ⭕ binary expansion of $n$
- (d) $1, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, . . .$
  - The next prime is added n times, where n is the next odd number.
  - $\{9,9,9,9,9,9,9\}$
  - ✔ Start at 1, increse of 2 and n is the sum of the two previous values.
- (e) $0, 2, 8, 26, 80, 242, 728, 2186, 6560, 19682, . . .$
  - $3^n - 1$ and $a_0 = 0$
  - $\{59048, 177146, 531440\}$
- (f) ⭕ $1, 3, 15, 105, 945, 10395, 135135, 2027025, 34459425, . . .$
  - each term evenly divides the next; the multipliers are $3,5,7,9,...$
  - ✅ $a_n = (2n - 1)!!$
  - $\{ 654729075, 13749310575, 316234143225\}$
- (g) $1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, . . .$
  - 1 and 0 are added alternatingly and the number of terms increases by one each time.
  - $\{0, 0, 0\}$
- (h) $2, 4, 16, 256, 65536, 4294967296, . . .$
  - ✅ $a_n = a_{n-1}², a_0 = 2$
  - $\{1.84467441\times10^{19}, 3.40282368\times10^{38}, 1.1579209\times10^{77}\}$
27. ❓ (∗∗) Show that if $a_n$ denotes the nth positive integer that is not a perfect square, then $a_n = n + \{\sqrt{n}\}$, where $\{x\}$ denotes the integer closest to the real number $x$.
- ✅⚠️ (see SSG)

28. ❓ (∗) Let $a_n$ be the nth term of the sequence $1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, . . . $, constructed by including the integer $k$ exactly $k$ times. Show that $a_n = ⌊\sqrt{2n} + 1/2⌋$.
- ✅⚠️ (see SSG)

29. What are the values of these sums?
- (a) $\sum_{i=1}^{5} (i + 1)$
  - $20$
- (b) $\sum_{i=0}^{4} (-2)i$
  - $-20$
- (c) $\sum_{i=1}^{10} 3$
  - $33$
- (d) $\sum_{i=0}^{8} (2^{i+1} - 2^i)$
  - $511$
  - ✔ Folding, Reducing, Cancellation

30. What are the values of these sums, where $S = \{1, 3, 5, 7\}$?
- (a) $\sum_{i ∈ S} i$
  - $16$
- (b) $\sum_{i ∈ S} i²$
  - $84$
- (c) $\sum_{i ∈ S} (1/i)$
  - $176/105$
- (d) $\sum_{i ∈ S} 1$
  - $4$

31. What is the value of each of these sums of terms of a geometric progression?
- (a) $\sum_{i=0}^{8} 3 * 2i$
  - $1533$
- (b) $\sum_{i=1}^{8} 2i$
  - ❌ $72$ ✅ $510$
- (c) $\sum_{i=2}^{8} (-3)^i$
  - $4923$
- (d) $\sum_{i=0}^{8} 2 * (-3)^i$
  - $9842$

32. Find the value of each of these sums.
- (a) $\sum_{i=0}^{8} (1 + (-1)^i)$
  - $\sum_{i=0}^{8} 1 + \sum_{i=0}^{8} (-1)^i$
  - ❌ $9 + (8 + 1)(-1) = 0$
  - ✅ $2 + 0 + \dots + 0 + 2 = 10$
- (b) $\sum_{i=0}^{8} (3^i - 2^i)$
  - $\sum_{i=0}^{8} 3^i - \sum_{i=0}^{8} 2^i$
  - $\frac{3^{8+1} - 1}{2} - \frac{2^{8+1} - 1}{1} = 9330$
- (c) $\sum_{i=0}^{8} (2 · 3^i + 3 · 2^i)$
  - $\sum_{i=0}^{8} 2 · 3^i + \sum_{i=0}^{8} 3 · 2^i$
  - $\frac{2 · 3^{9} - 2}{3 - 1} + \frac{3 · 2^{9} - 3}{2 - 1} = 21215$
- (d) $\sum_{i=0}^{8} (2^{i+1} - 2^i)$
  - ⭕ $\frac{2^{n+1} - 1}{2 - 1} - \frac{2^{8+1} - 1}{2 - 1}$
  - ✅ This could be worked as in part (b), but it is easier to note that the sum reduces (see Exercise 35). Each power of $2$ cancels except for the $−2^0$ when $j = 0$ and the $2^9$ when $j = 8$. Therefore the answer is $2^9 − 2^0 = 511$. (Alternatively, note that $2^{j+1} − 2^j = 2^j$.)

$\frac{ar^{n+1} - a}{r - 1}$
$(n + 1)a$

33. Compute each of these double sums.
- (a) $\sum_{i=1}^{2}\sum_{j=1}^{3} (i + j)$
- $\sum_{i=1}^{2}(i + 1) + (i + 2) + (i + 3)$
- $\sum_{i=1}^{2} 3i + 6$
- $(3·1 + 6) + (3·2 + 6) = 9 + 12 = 21$
- (b) $\sum_{i=0}^{2}\sum_{j=0}^{3} (2i + 3j)$
  - $\sum_{i=0}^{2} (2i + 3·0) + (2i + 3·1) + (2i + 3·2) + (2i + 3·3)$
  - $\sum_{i=0}^{2} (8i + 18)$
  - $(8·0 + 18) + (8·1 + 18) + (8·2 + 18) = 3·8 + 3·18 = 78$
- (c) $\sum_{i=1}^{3}\sum_{j=0}^{2} i$
  - ❌ $1 + 2 + 3 = 6$
  - ✅ $(1 + 1 + 1) + (2 + 2 + 2) + (3 + 3 + 3) = 18$
- (d) $\sum_{i=0}^{2}\sum_{j=1}^{3} ij$
  - $(0·1 + 0·2 + 0·3) + (1·1 + 1·2 + 1·3) + (2·1 + 2·2 + 2·3) = 18$

34. Compute each of these double sums.
- (a) $\sum_{i=1}^{3}\sum_{j=1}^{2} (i - j)$
  - $(1 - 1 + 1 - 2) + (2 - 1 + 2 - 2) + (3 - 1 + 3 - 2) = 3$
- (b) $\sum_{i=0}^{3}\sum_{j=0}^{2} (3i + 2j)$
  - $(3·0 + 2·0 + 3·0 + 2·1 + 3·0 + 2·2) + (3·1 + 2·0 + 3·1 + 2·1 + 3·1 + 2·2) + (3·2 + 2·0 + 3·2 + 2·1 + 3·2 + 2·2) + (3·3 + 2·0 + 3·3 + 2·1 + 3·3 + 2·2) = 6 + 15 + 24 + 33 = 78$
- (c) $\sum_{i=1}^{3}\sum_{j=0}^{2} j$
  - $(0 + 1 + 2) + (1 + 1 + 2) + (0 + 1 + 2) = 9$
- (d) $\sum_{i=0}^{2}\sum_{j=0}^{3} i²j³$
  - $(0^{2}0^{3}) + (0^{2}1^{3}) + (0^{2}2^{3}) + (0^{2}3^{3}) + (1^{2}0^{3}) + (1^{2}1^{3}) + (1^{2}2^{3}) + (1^{2}3^{3}) + (2^{2}0^{3}) + (2^{2}1^{3}) + (2^{2}2^{3}) + (2^{2}3^{3}) = 1 + 8 + 27 + 4 + 32 + 108 = 180$

35. Show that $\sum_{j=1}^{n}(a_j − a_{j−1}) = a_n − a_0$,  where $a_0 , a_1 , . . . , a_n$ is a sequence of real numbers.
    - ❎ Expanding the summation we get $a_n = (a_1 − a_{1−1}) + (a_2 − a_{2−1}) + \dots + (a_n − a_{n−1})$. Then each $a_{j-1}$ cancels out the $a_j$ term of the preceding summand. So the last term,  $a_n$, remains as well as $- a_{1-1}$ of the first summand, which is equal to $a_0$ and the result is $a_n − a_0$.
    - ✅ (write out all terms and note that all execept $a_n$ and  $− a_0$) cancel.

36. Use the identity $1/(k(k + 1)) = 1/k − 1/(k + 1)$ and Exercise 35 to compute $\sum_{k=1}^{n}1/(k(k + 1))$.
    - Using $1/k − 1/(k + 1)$ instead of $1/(k(k + 1))$, we see that $− 1/(k + 1)$ cancels the $1/k$ term of each successive summand. Thus we are left with $1/1$ from the first summand and $- 1/(n + 1)$ from the last, resulting in the sum $1 - 1/(n + 1) = n/(n + 1)$.

37. Sum both sides of the identity $k^2 − (k − 1)^2 = 2k − 1$ from $k = 1$ to $k = n$ and use Exercise 35 to find
- (a) a formula for $\sum_{k=1}^{n}(2k - 1)$ (the sum of the first $n$ odd natural numbers).
  - $\sum_{k=1}^{n}(2k - 1) = \sum_{k=1}^{n}(k^2 − (k − 1)^2)  = n^2 - (1 - 1)^{2} = n^2$
- (b) a formula for $\sum_{k=1}^{n}k$.
  - ❌ $\sum_{k=1}^{n}k = 1 + 2 + 3 + \dots + n$
  - ✅ We can use the distributive law to rewrite $\sum_{k=1}^n (2k - 1)$ (which we know from part (a) equals n²) in terms of the sum we want $S = \sum_{k=1}^{n}k$.
  - $$ n^{2} = \sum\limits_{k=1}^n (2k - 1) = 2\sum\limits_{k=1}^n k - \sum\limits_{k=1}^n 1 = 2S - n$$
  - Now we solve for $S$, obtaining $S = (n² + n) / 2$ which is usually represented as $n(n + 1)/2$

38. (∗) Use the technique given in Exercise 35, together with the  result of Exercise 37b, to derive the formula for $\sum_{k=1}^{n}k²$ given in Table 2. [Hint: Take $a_k = k^3$ in the sum in Exercise 35.]
    - $\sum_{k=1}^n (2k - 1) = \frac{n(n + 1)}{2}$
    - ❌ $S = (2·1 - 1) + (2·2 - 1) + (2·3 - 1) + \dots + (2n - 1)$
    - $S = 2 - 1 + 4 - 1 + 6 - 1 + \dots + 2n - 1$
    - ✅  First we note that $k^3 − (k − 1)^3 = 3k^2 − 3k + 1$. Then we sum this equation for all values of $k$ from $1$ to $n$. On the left, because of reduction, we have just $n^3$ ; on the right we have:
    - $$3\sum_{k=1}^n k^2 − 3\sum_{k=1}^n k + \sum_{k=1}^n 1 = 3\sum_{k=1}^nk² - \frac{3n(n + 1)}{2} + n$$
    - Equating the two sides and solving $\sum_{k=1}^n k^2$, we obtain the desired formula.
    - $$\sum_{k=1}^n k^2 = \frac{1}{3}(n³ + \frac{3n(n + 1)}{2} - n)$$
    - $$= \frac{n}{3} ( \frac{2n² + 3n + 3 - 2}{2} ) $$
    - $$= \frac{n}{3} ( \frac{n(n + 1)(2n + 1)}{6} ) $$

39. Find $\sum_{k=100}^{200}k$. (Use Table 2.)
    - $$\sum_{k=100}^{200}k = \sum_{k=1}^{200}k - \sum_{k=1}^{99}k$$
    - $$= \frac{200(200 + 1)}{2} - \frac{99(99 + 1)}{2}$$
    - $$= 20100 - 4950 = 15150$$

40. Find $\sum_{k=99}^{200}k³$. (Use Table 2.)
    - $$\sum_{k=99}^{200}k³ = \sum_{k=1}^{200}k³ - \sum_{k=1}^{98}k³$$
    - $$= \frac{200²(200 + 1)²}{4} - \frac{99²(99 + 1)²}{4}$$
    - $$= 404010000 - 23532201 = 380 477 799$$

41. (∗) Find a formula for $\sum_{k=0}^{m}⌊\sqrt{k}⌋$, when $m$ is a positive integer.
    - $$\sum_{k=0}^{n}⌊\sqrt{k}⌋ = ⌊\sqrt{0}⌋ + ⌊\sqrt{1}⌋ + ⌊\sqrt{2}⌋ + \dots + ⌊\sqrt{n}⌋$$
    - ⭕  If we write down the first few terms of this sum we notice a pattern. It starts $(1 + 1 + 1) + (2 + 2 + 2 + 2 + 2) + (3 + 3 + 3 + 3 + 3 + 3 + 3) + · · ·$. There are three 1's, then five 2's, then seven 3's, and so on; in general there are $(i + 1)^2 - i^2 = 2i + 1$ copies of $i$. So we need to sum $i(2i + 1)$ for an appropriate range of values for $i$. It gets a little messy at the end if m is such that the sequence stops before a complete range of the last value is present. Let $n = ⌊\sqrt{m}⌋ - 1$. ⚠️ Then there are $n + 1$ blocks, and $(n + 1)^2 - 1$ is where the next-to-last block ends. The sum of those complete blocks is $\sum_{i=1}^{n} i(2i + 1) = \sum_{i=1}^{n} 2i^2 + i = n(n + 1)(2n + 1)/3 + n(n + 1)/2$. The remaining terms in our summation all have the value $n + 1$ and the number of them present is $m - ((n + 1)^2 - 1)$. Our final answer is therefore $n(n + 1)(2n + 1)/3 + n(n + 1)/2 + (n + l)(m - (n + 1)^2 + 1)$.

42. ❓ (∗) Find a formula for $\sum_{k=0}^{n}⌊\sqrt[3]{k}⌋$, when $n$ is a positive integer.
    - ✅  If we write down the first few terms of this sum we notice a pattern. It starts $(1 + 1 + 1 + 1 + 1 + 1 + 1) + (2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2) + (3 + 3 + 3 + 3 + · · · + 3) + · · ·$. There are seven $1$s, then $19$ $2$s, then $37$ $3$s, and so on; in general, the number of $i$’s is $(i + 1)^3 − i^3 = 3i^2 + 3i + 1$. So we need to sum $i(3i^2 + 3i + 1)$ for an appropriate range of values for $i$. It gets a little messy at the end if $m$ is such that the sequence stops before a complete range of the last value is present. Let ⚠️ $n = ⌊\sqrt[3]{m}⌋ - 1$. Then there are $n + 1$ blocks, and $(n + 1)^3 - 1$ is where the next-to-last block ends. The sum of those complete blocks is $\sum_{i=1}^{n} i(3i² + 3i + 1) = \sum_{i=1}^{n} 3i³ + 3i² + i = n(3n + 4)(n + 1)²/4$ (using Table 2). The remaining terms in our summation all have the value $n + 1$ and the number of them is $m − ((n + 1)^3 − 1)$. Our final answer is therefore $n(3n + 4)(n + 1)^2 /4 + (n + 1)(m − (n + 1)^3 + 1)$, where, again, $n = ⌊\sqrt[3]{m}⌋ - 1$.

There is also a special **notation for products**. The product of $a_m , a_{m+1} , . . . , a_n$ is represented by $\prod_{j=m}^{n} a_j$, read as the product from $j = m$ to $j = n$ of $a_j$.

43. What are the values of the following products?
- (a) $\prod_{i=0}^{10} i = 0$
- (b) $\prod_{i=5}^{8} i = 1680$
- (c) $\prod_{i=1}^{100} (-1)^i = ❌ -1 ✅ 1$ (since there are 50 factors that are $-1$)
- (d) $\prod_{i=1}^{10} 2 = 1024$

Recall that the value of the factorial function at a positive integer $n$, denoted by $n!$, is the product of the positive integers from $1$ to $n$, inclusive. Also, we specify that $0! = 1$.

44. Express $n!$ using product notation.
    - $\prod_{i=1}^{n} i$

45. Find $\sum_{j=0}^{4} j! = 34$

46. Find $\prod_{j=0}^{4} j! = 288$
