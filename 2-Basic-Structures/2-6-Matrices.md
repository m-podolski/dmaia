# Matrices

  $A = \left[ \begin{array}{ccc}
  x & x & x \\
  x & x & x \\
  \end{array} \right] $

1. Let $A$ = $ \left[ \begin{array}{cccc}
1 & 1 & 1 & 3 \\
2 & 0 & 4 & 6 \\
1 & 1 & 3 & 7 \\
\end{array} \right] $

- (a) What size is $A$?
  - ❌ $4 × 3$ ✅ $3 × 4$
- (b) What is the third column of $A$?
  - $[1 ~ 4 ~ 3]$
- (c) What is the second row of $A$?
  - $[2 \ 0 \ 4 \ 6]$
- (d) What is the element of $A$ in the $(3, 2)$th position?
  - $1$
- (e) What is $A^t$ ?
  - $
\left[ \begin{array}{ccc}
1 & 2 & 1 \\
1 & 0 & 1 \\
1 & 4 & 3 \\
3 & 6 & 7 \\
\end{array} \right] $

2. Find $A + B$, where
- (a)
  $A = \left[ \begin{array}{ccc}
  1 & 0 & 4 \\
  -1 & 2 & 2 \\
  0 & -2 & -3 \\
  \end{array} \right] $

  $B = \left[ \begin{array}{ccc}
  -1 & 3 & 5 \\
  2 & 2 & -3 \\
  2 & -3 & 0 \\
  \end{array} \right] $

  $A + B = \left[ \begin{array}{ccc}
  0 & 3 & 9 \\
  1 & 4 & -1 \\
  2 & -5 & -3 \\
  \end{array} \right]$

- (b)
  $A = \left[ \begin{array}{cccc}
  -1 & 0 & 5 & 6 \\
  -4 & -3 & 5 & -2 \\
  \end{array} \right] $

  $B = \left[ \begin{array}{cccc}
  -3 & 9 & -3 & 4 \\
  0 & -2 & -1 & 2 \\
  \end{array} \right] $

  $A + B =\left[\begin{array}{cccc}
  -4 & 9 & 2 & 10 \\
  -4 & -5 & 4 & 0 \\
  \end{array} \right] $

3. Find $AB$ if
- (a)
  $A = \left[\begin{array}{cc}
  2 & 1 \\
  3 & 2 \\
  \end{array} \right]$

  $B = \left[ \begin{array}{cc}
  0 & 4 \\
  1 & 3 \\
  \end{array} \right] $

  $AB = \left[ \begin{array}{cc}
  1 & 11 \\
  2 & 18 \\
  \end{array} \right] $
- (b)
  $A = \left[ \begin{array}{cc}
  1 & -1 \\
  0 & 1 \\
  2 & 3 \\
  \end{array} \right] $

  $B = \left[ \begin{array}{ccc}
  3 & -2 & -1 \\
  1 & 0 & 2 \\
  \end{array} \right] $

  $AB = \left[ \begin{array}{ccc}
  2 & -2 & -3 \\
  1 & 0 & 2 \\
  9 & -4 & 4 \\
  \end{array} \right] $
- (c)
  $A = \left[ \begin{array}{cc}
  4 & -3 \\
  3 & -1 \\
  0 & -2 \\
  -1 & 5 \\
  \end{array} \right] $

  $B = \left[ \begin{array}{cc}
  -1 & 3 & 2 & -2 \\
  0 & -1 & 4 & -3 \\
  \end{array} \right] $

  $AB = \left[ \begin{array}{cccc}
  -4 & 15 & -4 & 1 \\
  -3 & 10 & 2 & -3 \\
  0 & -2 & -8 & 6 \\
  1 & -8 & 18 & -13 \\
  \end{array} \right] $

4. ❕ Find the product $AB$, where

5. Find a matrix $A$ such that
    $\left[ \begin{array}{cc}
    2 & 3 \\
    1 & 4 \\
    \end{array} \right]
    A =
    \left[ \begin{array}{cc}
    3 & 0 \\
    1 & 2 \\
    \end{array} \right]$

    $\left[ \begin{array}{cc}
    2 & 3 \\
    1 & 4 \\
    \end{array} \right]
    ❌ \left[ \begin{array}{c}
    x \\
    y \\
    \end{array} \right] =
    \left[ \begin{array}{cc}
    3 & 0 \\
    1 & 2 \\
    \end{array} \right]$

    $\
    \begin{array}{ccc}
    2x + 3y &=& z \\
    x + 4y &=& z \\
    \end{array}
    $

    $\left[ \begin{array}{cc}
    2 & 3 \\
    1 & 4 \\
    \end{array} \right]
    ✅ \left[a_{ij}\right] =
    \left[ \begin{array}{cc}
    3 & 0 \\
    1 & 2 \\
    \end{array} \right]$

    $\
    \begin{array}{ccc}
    2a_{11} + 3a_{21} &=& 3 \\
    2a_{12} + 3a_{22} &=& 0 \\
    1a_{11} + 4a_{21} &=& 1 \\
    1a_{12} + 4a_{22} &=& 2 \\
    \end{array}
    $
[Hint: Finding $A$ requires that you solve systems of linear equations.]

6. ❌ Find a matrix A such that
    $\left[ \begin{array}{ccc}
    1 & 3 & 2 \\
    2 & 1 & 1 \\
    4 & 0 & 3 \\
    \end{array} \right]
    A =
    \left[ \begin{array}{ccc}
    7 & 1 & 3 \\
    1 & 0 & 3 \\
    -1 & -3 & 7 \\
    \end{array} \right]$

    $ ✅ A =
    \left[ \begin{array}{ccc}
    -1 & 0 & 1 \\
    2 & 1 & 0 \\
    1 & -1 & 1 \\
    \end{array} \right]$

 ⚠️ **(cant find solution algebraically)**

7. Let $A$ be an $m × n$ matrix and let $0$ be the $m × n$ matrix that has all entries equal to zero. Show that $A = 0 + A = A + 0$.
   - As matrix addition is commutative ($a_{ij} + b_{ij}$) and defined in this case (same dimensions) and the second matrix is all zeros, we see in every case the values of $A$ are not changed.

8. Show that matrix addition is commutative; that is, show that if $A$ and $B$ are both $m × n$ matrices, then $A + B = B + A$.
   - As the resulting matrix bd. has $a_{ij} + b_{ij}$ in the (i,j)th position where $a$ and $b$ are the element of two matrices with equal dimensions, the rules of additon apply, which is commutative.
   - ✔ rules of additon of **real numbers**.

9. Show that matrix addition is associative; that is, show that if $A$, $B$, and $C$ are all $m × n$ matrices, then $A + (B + C) = (A + B) + C$.
    - As stated in Ex. 8, commutativity applies to any matrix-addition, so the order of addition does not matter as is true for the associative arithmetic operation.

10. Let $A$ be a $3 × 4$ matrix, $B$ be a $4 × 5$ matrix, and $C$ be a $4 × 4$ matrix. Determine which of the following products are defined and find the size of those that are defined.
- (a) AB : 3 × 5
- (b) BA : n. d.
- (c) AC : 3 × 4
- (d) CA : n. d.
- (e) BC : n. d.
- (f) CB : 4 × 5

11. What do we know about the sizes of the matrices A and B if both of the products AB and BA are defined?
    - ❌ As the number of columns of the first factor must equal the number of rows of the second one, in this case both must be squares.
    - ✅  In order for AB to be defined, the number of columns of A must equal the number of rows of B. In order for BA to be defined, the number of columns of B must equal the number of rows of A. Thus for some positive integers m and n, it must be the case that $A$ is an $m × n$ matrix and $B$ is an $n × m$ matrix. Another way to say this is to say that A must have the same size as Bt (and/or vice versa).
12. In this exercise we show that matrix multiplication is distributive over matrix addition.
- (a) Suppose that $A$ and $B$ are $m × k$ matrices and that $C$ is a $k × n$ matrix. Show that $(A + B)C = AC + BC$.
  - ❎ First, note that the addition of $A$ and $B$ is defined and results in a matrix $m × k$-matrix $X$ with its (i,j)th element $x_{ij} = a_{ij} + b_{ij}$. Multiplication with $C$ is also defined and results in a $m × n$ matrix with $c_{ij} = x_{i1}c_{1j} + x_{i2}c_{2j} + \dots + x_{ik}c_{kj}$.
  - Conversely starting from the rhs. the two summands have elements $x_{ij} = a_{i1}c_{1j} + a_{i2}c_{2j} + \dots + a_{ik}c_{kj}$ (wlog. for $BC$ as $A$ and $B$ have the same dimensions).
  - ✅  $(A + B)C$
  - $= \sum_{j=1}^{k} (a_{iq} + b_{iq})c_{qj}$
  - $= \sum_{j=1}^{k} a_{iq}c_{qj} + \sum_{j=1}^{k} b_{iq}c_{qj}$
  - $= AC + BC$
- (b) ⭕ Suppose that $C$ is an $m × k$ matrix and that $A$ and $B$ are $k × n$ matrices. Show that $C(A + B) = CA + CB$.
  - ✅  $C(A + B) = \sum_{j=1}^{k} c_{iq}(a_{qj} + b_{qj}) = \sum_{j=1}^{k} c_{iq}a_{qj} + \sum_{j=1}^{k} c_{iq}b_{qj} = CA + CB$

13. ❓ In this exercise we show that matrix multiplication is associative. Suppose that $A$ is an $m × p$ matrix, $B$ is a $p × k$ matrix, and $C$ is a $k × n$ matrix. Show that $A(BC) = (AB)C$.
    - ✅  Let us begin with the left-hand side and find its $(i, j)$th entry. First we need to find the entries of $BC$. By definition, the $(q, j)$th entry of $BC$ is $\sum_{r=1}^{k} b_{qr}c_{rj}$. Therefore the $(i,j)$th entry of $A(BC)$ is $\sum_{q=1}^{p} a_{iq}(\sum_{r=1}^{k} b_{qr}c_{rj})$. By distributing multiplication over addition (for real numbers), we can move the term $a_{iq}$ inside the inner summation, to obtain $\sum_{q=1}^{p}\sum_{r=1}^{k} a_{iq}b_{qr}c_{rj}$. (We are also implicitly using associativity of multiplication of real numbers here, to avoid putting parentheses in the product.)
    - A similar analysis with the right-hand side shows that the $(i, j)$ th entry there is equal to $\sum_{r=1}^{k}\sum_{q=1}^{p} a_{iq}b_{qr}c_{rj}$. Now by the commutativity of addition, the order of summation (whether we sum over $r$ first and then $q$, or over $q$ first and then $r$) does not matter, so these two expressions are equal, and the proof is complete.

14. ❓ The $n × n$ matrix $A = [a_{ij}]$ is called a diagonal matrix if $a_{ij} = 0$ when $i ≠ j$. Show that the product of two $n × n$ diagonal matrices is again a diagonal matrix. Give a simple rule for determining this product.
    - ✅ Let $A$ and $B$ be two diagonal $n × n$ matrices. Let $C = [c_{ij}]$ be the product $AB$. From the definition of matrix  multiplication, $c_{ij} = \sum_{q=1}^{k} a_{iq}b_{qj}$. Now all the terms $a_{iq}$ in this expression are $0$ except for $q = i$, so $c_{ij} = a_{ii}b_{ij}$. But $b_{ij} = 0$ unless $i = j$, so the only nonzero entries of $C$ are the diagonal entries $c_{ii} = a_{ii}b_{ii}$.

15. ❓ Let
  $A = \left[\begin{array}{cc}
  1 & 1 \\
  0 & 1 \\
  \end{array} \right]$
  Find a formula for $A^n$, whenever $n$ is a positive integer.
- ✅  Let us begin by computing An for the first few values of $n$.
    $A¹ = \left[\begin{array}{cc}
    1 & 1 \\
    0 & 1 \\
    \end{array} \right]$
    $A² = \left[\begin{array}{cc}
    1 & 2 \\
    0 & 1 \\
    \end{array} \right]$
    $A³ = \left[\begin{array}{cc}
    1 & 3 \\
    0 & 1 \\
    \end{array} \right]$
    It seems clear from this pattern, then, that
    $A^n = \left[\begin{array}{cc}
    1 & n \\
    0 & 1 \\
    \end{array} \right]$

16. Show that $(A^t)^t = A$.
    - Bd. $(A^t) = b_{ij}$ if $A =  a_{ji}$, so $(A^t)^t = c_{ij}$.
17. Let $A$ and $B$ be two $n × n$ matrices. Show that
- (a) $(A + B)^t = A^t + B^t$.
  - Btdo. matrix addition if $A$ (and wlog. $B$) is $[a_{ij}]$, then $A + B = [c_{ij}]$, thus $(A + B)^t = [t_{ji}]$. For the rhs. (wlog. for $B$) If $A = [a_{ij}]$, then $A^t = [a_{ji}]$ and adding $[b_{ji}]$, again, is $[t_{ji}]$.
- (b) $(AB)^t = B^t A^t$.
  - $AB = [c_{ij}] = \sum_{k=1}^{n} a_{ik}b_{kj}$ s bd. $(AB)^t = [c_{ji}] = \sum_{k=1}^{n} a_{jk}b_{ki}$.
  - For the rhs. The $(i,j)$ th entry of $B^t$ is the $(j,i)$ th entry of $B$ (wlog. for $A$).
  ✔ The $(i,j)$ th entry of $(AB)^t$ is the $(j,i)$ th entry of $AB $, namely $\sum_{k=1}^{n} a_{jk}b_{ki}$. On the other hand, the $(i,j)$ th entry of $B^tA^t$ is ⭕ $\sum_{k=1}^{n} a_{ki}b_{jk}$ (since the $(i,k)$th entry of $B^t$ is $b_{ki}$ and the $(k,j)$ th entry of $A^t$ is $a_{jk}$). By the commutativity of multiplication of real numbers, these two values are the same, so the matrices are equal.

If $A$ and $B$ are $n × n$ matrices with $AB = BA = I_n$, then $B$ is called the **inverse** of $A$ (this terminology is appropriate because such a matrix $B$ is unique) and $A$ is said to be **invertible**. The notation $B = A^{−1}$ denotes that $B$ is the inverse of $A$.

18. Show that
  $A^{-1} = \left[ \begin{array}{ccc}
  2 & 3 & -1 \\
  1 & 2 & 1 \\
  -1 & -1 & 3 \\
  \end{array} \right] $
  is the inverse of
  $A = \left[ \begin{array}{ccc}
  7 & -8 & 5 \\
  -4 & 5 & -3 \\
  1 & -1 & 1 \\
  \end{array} \right] $

  $A^{-1}A = \left[ \begin{array}{ccc}
  1 & 0 & 0 \\
  0 & 1 & 0 \\
  0 & 0 & 1 \\
  \end{array} \right] = I_3$

⭕ need to multiply in both directions.

19. ❓ Let $A$ be the $2 × 2$ matrix
  $A = \left[\begin{array}{cc}
  a & b \\
  c & d \\
  \end{array} \right]$
  Show that if $ad − bc ≠ 0$, then
  $A^{-1} = \left[\begin{array}{cc}
  \frac{d}{ad - bc} & \frac{-b}{ad - bc} \\
  \frac{-c}{ad - bc} & \frac{a}{ad - bc} \\
  \end{array} \right]$
- ✅ All we have to do is form the products $AA^{-1}$ and $A^{-1} A$, using the purported $A^{-1}$ , and see that both of them are the $2 × 2$ identity matrix. It is easy to see that the upper left and lower right entries in each case are $(ad - bc)/ (ad - bc) = 1$, and the upper right and lower left entries are all $0$.

20. Let
  $A = \left[\begin{array}{cc}
  -1 & 2 \\
  1 & 3 \\
  \end{array} \right]$
- (a) Find $A^{-1}$. [Hint: Use Exercise 19.]
  - Because $AA^{-1} = A^{-1}A = I$.
  $A^{-1} = \left[\begin{array}{cc}
  \frac{3}{-5} & \frac{-2}{-5} \\
  \frac{-1}{-5} & \frac{-1}{-5} \\
  \end{array} \right]
   = \left[\begin{array}{cc}
  -\frac{3}{5} & \frac{2}{5} \\
  \frac{1}{5} & \frac{1}{5} \\
  \end{array} \right]$
- (b) Find $A^3$.
  $A^3 = \left[\begin{array}{cc}
  1 & 18 \\
  9 & 37 \\
  \end{array} \right]$
- (c) Find $(A^{-1})^3$.
  $(A^{-1})^3 = \left[\begin{array}{cc}
  \frac{-37}{125} & \frac{❌ 16 ✅ 18}{125} \\
  \frac{9}{125} & \frac{❌ -2 ✅ -1}{125} \\
  \end{array} \right]$
- (d) Use your answers to (b) and (c) to show that $(A^{-1})^3$ is the inverse of $A^3$.
  - ❎ Because $AA^{-1} = A^{-1}A = I$, $A³(A^{-1})³ = (A^{-1})³A³ = I$.
  - **omitted $(A^{-1})^3A^3$**
  $A^3(A^{-1})^3 = \left[\begin{array}{cc}
  -33/125 + 162/125 = 1 & 18/125 - 18/125 = 0 \\
  -333/125 + 333/125 = 0 & 162/125 - 37/125 = 1 \\
  \end{array} \right]$
  - ✅  Applying the method of Exercise 19 for obtaining inverses to the answer in part (b), we obtain the answer in part (c). Therefore $(A^3)^{-1} = (A^{-1})^3$.

21. ❓ Let $A$ be an invertible matrix. Show that $(A^n)^{−1} = (A^{-1})^n$ whenever $n$ is a positive integer.
    - ✅ We must show that $A^n(A^{−1})^n = I$, where $I$ is the $n × n$ identity matrix. Since matrix multiplication is associative, we can write this product as. $$A^n(A^{−1})^n = A(A \dots (A(AA^{−1})A^{−1}) \dots A^{−1})A^{−1}$$
    - By dropping each $AA^{−1} = I$ from the center as it is obtained, this product reduces to $I$. Similarly $((A^{−1})^n)A^n =I$. Therefore by definition $(A^n)^{−1} = (A^{−1})^n$. (A more formal proof requires mathematical induction; see Section 5.1.)

22. ❓ Let $A$ be a matrix. Show that the matrix $AA^t$ is symmetric. [Hint: Show that this matrix equals its transpose with the help of Exercise 17b.]
    - ✅ A matrix is symmetric if and only if it equals its transpose. So let us compute the transpose of $AA^t$ and see as if we get this matrix back. Using Exercise 17b and then Exercise 16, we have ⚠️ $(AA^t)^t = ((A^t)^t)A^t = AA^t$ as desired.

23. ❓ Suppose that $A$ is an $n × n$ matrix where $n$ is a positive integer. Show that $A + A^t$ is symmetric.
    - ✅ By definition, the $(i,j)$ th entry of $A + A^t$ is $a_{ij} + a_{ji}$ Similarly, the $(j, i)$ th entry of $A + A^t$ is $a_{ji} + a_{ij}$. By the commutativity of addition, these are equal, so $A + A^t$ is symmetric by the definition of symmetric matrices.

24. Parts:

- (a) Show that the system of linear equations
    $\ \begin{array}{ccc}
    a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &=& b_1 \\
    a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &=& b_2 \\
    &\vdots& \\
    a_{n1}x_1 + a_{n2}x_2 + \dots + a_{nn}x_n &=& b_n \\
    \end{array} $
in the variables $x_1 , x_2 , . . . , x_n$ can be expressed as $AX = B$, where $A = [a_{ij}]$, $X$ is an $n × 1$ matrix with $x_i$ the entry in its $i$th row, and $B$ is an $n × 1$ matrix with $b_i$ the entry in its $i$th row
  - By putting all values $a_{ij}$ for one equation into one row of $A$ and all variables $x_n$ into the only column of $X$ such that its number of rows equals the occurences of $x$ in the equation, the equations can be obtained by multiplying $AX$ and their results are contained in $B$.

- (b) Show that if the matrix $A = [a_{ij}]$ is invertible (as defined in the preamble to Exercise 18), then the solution of the system in part (a) can be found using the equation $X = A^{-1}B$.
  - We can multiply the equation with $A^{-1}$ and get $I_nX = A^{-1}B$, which btdo. inverse is simply $X$.

25. Use Exercises 18 and 24 to solve the system
$$
\begin{align}
  7x_1 − 8x_2 + 5x_3 &= 5 \\
  −4x_1 + 5x_2 − 3x_3 &= −3 \\
  x_1 − x_2 + x_3 &= 0 \\
\end{align}
$$
$$
\left[\begin{array}{cc}
  7 & -8 & 5 \\
  -4 & 5 & -3 \\
  1 & -1 & 1 \\
\end{array} \right]
\left[\begin{array}{cc}
  x_1 \\
  x_2 \\
  x_3 \\
\end{array} \right]
= \left[\begin{array}{cc}
  5 \\
  -3 \\
  0 \\
\end{array} \right]
$$
$$A^{-1} = \left[ \begin{array}{ccc}
  2 & 3 & -1 \\
  1 & 2 & 1 \\
  -1 & -1 & 3 \\
  \end{array} \right]$$
$$\left[\begin{array}{cc}
  x_1 \\
  x_2 \\
  x_3 \\
\end{array} \right]
= \left[\begin{array}{cc}
  1 \\
  -1 \\
  -2 \\
\end{array} \right]$$

26. Let
  $$
  A = \left[ \begin{array}{cc}
  1 & 1 \\
  0 & 1 \\
  \end{array} \right]
  B = \left[ \begin{array}{cc}
  0 & 1 \\
  1 & 0 \\
  \end{array} \right]
  $$
Find
- (a) $A ∨ B = \left[ \begin{array}{cc} 1 & 1 \\ 1 & 1 \\ \end{array} \right]$

- (b) $A ∧ B = \left[ \begin{array}{cc} 0 & 1 \\ 0 & 0 \\ \end{array} \right]$

- (c) $A ⊙ B = \left[ \begin{array}{cc} 1 & 1 \\ 1 & 0 \\ \end{array} \right]$

27. ❕ Let
  $$
  A = \left[ \begin{array}{ccc}
  1 & 0 & 1 \\
  1 & 1 & 0 \\
  0 & 0 & 1 \\
  \end{array} \right]
  B = \left[ \begin{array}{ccc}
  0 & 1 & 1 \\
  1 & 0 & 1 \\
  1 & 0 & 1 \\
  \end{array} \right]
  $$
Find
- (a) A ∨ B.
- (b) A ∧ B.
- (c) A ⊙ B.

28. Find the Boolean product of A and B, where
  $$
  A = \left[ \begin{array}{ccc}
  1 & 0 & 0 & 1 \\
  0 & 1 & 0 & 1 \\
  1 & 1 & 1 & 1 \\
  \end{array} \right]
  B = \left[ \begin{array}{ccc}
  1 & 0 \\
  0 & 1 \\
  1 & 1 \\
  1 & 0 \\
  \end{array} \right]
  A ⊙ B = \left[ \begin{array}{cc}
  1 & 0 \\
  1 & 1 \\
  1 & 1 \\
  \end{array} \right]
  $$

29. Let
$$ A = \left[ \begin{array}{ccc}
  1 & 0 & 0 \\
  1 & 0 & 1 \\
  0 & 1 & 0 \\
  \end{array} \right]
$$
Find

- (a)
  $$ A^{[2]} = \left[ \begin{array}{cc}
  1 & 0 & 0 \\
  1 & 1 & 0 \\
  1 & 0 & 1 \\
  \end{array} \right] $$
- (b)
  $$ A^{[3]} = \left[ \begin{array}{cc}
  1 & 0 & 0 \\
  1 & 0 & 1 \\
  1 & 1 & 0 \\
  \end{array} \right]$$
- (c)
  $$A ∨ A^{[2]} ∨ A^{[3]} = \left[ \begin{array}{cc}
  1 & 0 & 0 \\
  1 & 1 & 1 \\
  1 & 1 & 1 \\
  \end{array} \right]$$

30. Let $A$ be a zero–one matrix. Show that
- (a) $A ∨ A = A$.
  - We consider the $(i,j)^{th}$ entry of A. If it is $0$ then $a_{ij} ∨ a_{ij} = 0$; if it is $1$ $a_{ij} ∨ a_{ij} = 1$;
- (b) $A ∧ A = A$.
  - Similar to part (a); If the $(i,j)^{th}$ entry is 1 $a_{ij} ∧ a_{ij} = 1$, otherwise $0$.

31. In this exercise we show that the meet and join operations are commutative. Let $A$ and $B$ be $m × n$ zero–one matrices. Show that
- (a) $A ∨ B = B ∨ A$
  - $A ∨ B = a_{ij} ∨ b_{ij} = b_{ij} ∨ a_{ij} = B ∨ A$ (By the commutativity of the logical or).
- (b) $B ∧ A = A ∧ B$
  - (analogous to (a))

32. In this exercise we show that the meet and join operations are associative. Let A, B, and C be m × n zero–one matrices. Show that
- (a) $(A ∨ B) ∨ C = A ∨ (B ∨ C)$
  - This follows from the associativity of the logical or as each operand is the $(i,j)^{th}$ entry of the respective matrix containing a binary value.
- (b) $(A ∧ B) ∧ C = A ∧ (B ∧ C)$
  - (analogous to (a))

33. We will establish distributive laws of the meet over the join operation in this exercise. Let A, B, and C be m × n zero–one matrices. Show that
- (a) $A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C)$
  - (for (a) and (b)) like stated in Ex. 32 the same laws apply to boolean values in matrices as to logical true and false.
- (b) $A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C)$

34. ❓ Let $A$ be an $n × n$ zero–one matrix. Let $I$ be the $n × n$ identity matrix. Show that $A ⊙ I = I ⊙ A = A$.
    - ✅  Since the ith row of $I$ consists of all $0$’s except for a $1$ in the $(i,i)$ th position, we have $I ⊙ A = [(0 ∧ a_{1j} ) ∨ \dots ∨ (1 ∧ a_{ij} ) ∨ \dots ∨ (0 ∧ a_{nj} )] = [a_{ij} ] = A$. Similarly, since the jth column of $I$ consists of all $0$’s except for a $1$ in the $(j, j)$ th position, we have $A ⊙ I = [(a_{i1} ∧ 0) ∨ \dots ∨ (a_{ij} ∧ 1) ∨ \dots ∨ (a_{in} ∧ 0)] = [a_{ij} ] = A$.

35. In this exercise we will show that the Boolean product of zero–one matrices is associative. Assume that $A$ is an $m × p$ zero–one matrix, $B$ is a $p × k$ zero–one matrix, and $C$is a $k × n$ zero–one matrix. Show that $A ⊙ (B ⊙ C) = (A ⊙ B) ⊙ C$.
    - ⭕ $B ⊙ C = [w_{ij}] = (b_{i1} ∧ c_{1j}) ∨ (b_{i2} ∧ c_{2j}) ∨ \dots ∨ (b_{ik} ∧ c_{kj})$.
    - $A ⊙ (B ⊙ C) = [x_{ij}] = (a_{i1} ∧ w_{1j}) ∨ (a_{i2} ∧ w_{2j}) ∨ \dots ∨ (a_{ik} ∧ w_{kj})$
    - $A ⊙ B = [y_{ij}] = (a_{i1} ∧ b_{1j}) ∨ (a_{i2} ∧ b_{2j}) ∨ \dots ∨ (a_{ik} ∧ b_{kj})$.
    - $(A ⊙ B) ⊙ C = [z_{ij}] = (y_{i1} ∧ c_{1j}) ∨ (y_{i2} ∧ c_{2j}) ∨ \dots ∨ (y_{ik} ∧ c_{kj})$
    - ✅ The proof is identical to the proof in Exercise 13, except that real number multiplication is replaced by ∧ and real number addition is replaced by ∨. Briefly, in symbols,
    - $A ⊙ (B ⊙ C) = [\bigvee_{q=1}^p a_{iq} ∧ (\bigvee_{r=1}^k b_{qr} ∧ c_{rj})]$
    - $= [\bigvee_{q=1}^p \bigvee_{r=1}^k a_{iq} ∧ b_{qr} ∧ c_{rj}]$
    - $= [\bigvee_{r=1}^k \bigvee_{q=1}^p a_{iq} ∧ b_{qr} ∧ c_{rj}]$
    - $= [\bigvee_{r=1}^k (\bigvee_{q=1}^p a_{iq} ∧ b_{qr}) ∧ c_{rj}] = (A ⊙ B) ⊙ C$
