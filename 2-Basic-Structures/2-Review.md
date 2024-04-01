# 2 Review

1. Explain what it means for one set to be a subset of another set. How do you prove that one set is a subset of another set?
   - By showing that  every element of the subset is also in the superset.

2. What is the empty set? Show that the empty set is a subset of every set.
   - The empty set is the set that has no elements. As there are no elements in the empty set all of them are (vacuously) members of every other set.

3. Parts:
- (a) Define $|S|$, the cardinality of the set $S$.
  - For finite sets it is the number of the elements that it contains; for infinite ones it is the size relative to the size of the set of natural numbers.
- (b) Give a formula for $|A ∪ B|$, where A and B are sets.
  - ❌ $|A| + (|B| - |A|)$.
  - ✅ $|A ∪ B| = |A| + |B| − |A ∩ B|$.

4. Parts:
- (a) Define the power set of a set $S$.
  - The power set is the set of all possible subsets of a given (finite) set.
- (b) When is the empty set in the power set of a set $S$?
  - always.
- (c) How many elements does the power set of a set $S$ with $n$ elements have?
  - $2^n$.

5. Parts:
- (a) Define the union, intersection, difference, and symmetric difference of two sets.
  - union: $\{x \mid x ∈ A ∨ x ∈ B\}$
  - intersection: $\{x \mid x ∈ A ∧ x ∈ B\}$
  - difference: $\{x \mid x ∈ A ∧ x ∉ B\}$
  - sym. diff.: $\{x \mid x ∈ A ∨ x ∈ B ∧ x ∉ A ∩ B\}$
- (b) What are the union, intersection, difference, and symmetric difference of the set of positive integers and the set of odd integers?
  - union: the integers that are positive or odd
  - intersection: the odd positive integers
  - difference: the even positive integers
  - sym. diff.: ❌ the even negative integers ✅ even positive integers together with odd negative integers

6. Parts:
- (a) Explain what it means for two sets to be equal.
  - ❌ They contain the same elements (quantity and quality)
  - ✅ $A = B =(A ⊆ B ∧ B ⊆ A)= ∀x(x ∈ A ↔ x ∈ B)$
- (b) Describe as many of the ways as you can to show that two sets are equal.
  - By showing that an arbitrary element is in both sets and that neither of that sets contains elements that are not in the other.
  - ✔ using identity-laws / algebraically, using membership tables, venn diagrams
- (c) Show in at least two different ways that the sets $A − (B ∩ C)$ and $(A − B) ∪ (A − C)$ are equal.
  - ❌ First we show that $A − (B ∩ C)$ is a subset of $(A − B) ∪ (A − C)$. If $x ∈ A − (B ∩ C)$ then $x ∈ A$ and $x ∉ B ∩ C$. Btdo. intersection it follows that $x ∈ A$ and $x ∉ B ∩ C$
  - Secondly we show that $(A − B) ∪ (A − C)$ is a subset of $A − (B ∩ C)$.
  - ✅ $A − (B ∩ C) = A ∩ \overline{B ∩ C} = A ∩ (\overline{B} ∪ \overline{C}) = (A ∩ \overline{B}) ∪ (A ∩ \overline{C}) = (A − B) ∪ (A − C)$

7. Explain the relationship between logical equivalences and set identities.
- As an element can be thought of having a binary truth-value (being in a set or not), all logical operations have equivalents in set theory.

8. Parts:
- (a) Define the domain, codomain, and range of a function.
  - domain: the set of values (✔ preimages) which the function assigns to their images.
  - codomain: the set of possible images.
  - range: the actual set of images.
- (b) Let $f (n)$ be the function from the set of integers to the set of integers such that $f (n) = n^2 + 1$. What are the domain, codomain, and range of this function?
  - domain: integers.
  - codomain: integers.
  - range: positive integers greater or equal to 1.

9. Parts:
- (a) Define what it means for a function from the set of positive integers to the set of positive integers to be one-to-one.
  - for every value in the domain there is a unique image.
- (b) Define what it means for a function from the set of positive integers to the set of positive integers to be onto.
  - for every value in the codomain there is a preimage in the domain.
- (c) Give an example of a function from the set of positive integers to the set of positive integers that is both one-to-one and onto.
  - $f(n) = n$
- (d) Give an example of a function from the set of positive integers to the set of positive integers that is one-to-one but not onto.
  - ❎ $f(n) = n + 1$
  - ✅ $f(n) = 2n$
- (e) Give an example of a function from the set of positive integers to the set of positive integers that is not one-to-one but is onto.
  - ❎ $f(n) = 1 \text{ if n ≤ 10, else } n - 10$
  - ✅ $f(n) = ⌈n/2⌉$
- (f) Give an example of a function from the set of positive integers to the set of positive integers that is neither one-to-one nor onto.
  - $f(n) = 42$

10. Parts:
- (a) Define the inverse of a function.
  - The inverse is the function from the range to the domain of the original.
- (b) When does a function have an inverse?
  - Only when it is a bijection.
- (c) Does the function $f(n) = 10 − n$ from the set of integers to the set of integers have an inverse? If so, what is it?
  - $f(n) = 10 - n$

11. Parts:
- (a) Define the floor and ceiling functions from the set of real numbers to the set of integers.
  - Ceiling round to the next greater integer, floor to the next smaller integer.
- (b) For which real numbers $x$ is it true that $⌊x⌋ = ⌈x⌉$?
  - integers

12. Conjecture a formula for the terms of the sequence that begins $8, 14, 32, 86, 248$ and find the next three terms of your sequence.
    - ⭕ $3, 9, 27, 81: a_n = 3^n + 5$

13. Suppose that $a_n = a_{n−1} − 5$ for $n = 1, 2, \dots$. Find a formula for $a_n$.
    - $a_0 - 5n$

14. What is the sum of the terms of the geometric progression $a + ar + \dots + ar^n$ when $r ≠ 1$?
    - $\frac{ar^{n+1} - a}{r  -1}$

15. Show that the set of odd integers is countable.
    - ❌ **(read odd positive ints instead of odd ints)** By letting $f(n) = n + (n - 1)$ we have a bijection from the natural numbers to the odd integers.
    - ✅ $1 ↔ 1, 2 ↔ -1, 3 ↔ 3, 4 ↔ -3, 5 ↔ 5, 6 ↔ -5$

16. Give an example of an uncountable set.
    - The real numbers between 0 and 1.

17. Define the product of two matrices A and B. When is this product defined?
    - When $A$ is a $m × k$ matrix and B is a $k × n$.

18. Show that matrix multiplication is not commutative
    $$
    \left[ \begin{array}{ccc}
    1 & 2 \\
    2 & 1 \\
    \end{array} \right]
    × \left[ \begin{array}{ccc}
    1 & 2 \\
    3 & 4 \\
    \end{array} \right]
    = \left[ \begin{array}{ccc}
    7 & 10 \\
    5 & 8 \\
    \end{array} \right]
    $$
    $$
    \left[ \begin{array}{ccc}
    1 & 2 \\
    3 & 4 \\
    \end{array} \right]
    × \left[ \begin{array}{ccc}
    1 & 2 \\
    2 & 1 \\
    \end{array} \right]
    = \left[ \begin{array}{ccc}
    5 & 4 \\
    11 & 10 \\
    \end{array} \right]
    $$
