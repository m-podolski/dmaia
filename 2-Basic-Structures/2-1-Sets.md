# 2.1 Sets

1. List the members of these sets.
- (a) {x | x is a real number such that x² = 1}
  - {1,-1}
- (b) {x | x is a positive integer less than 12}
  - {1,2,3,4,5,6,7,8,9,10,11}
- (c) {x | x is the square of an integer and x < 100}
  - {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
- (d) {x | x is an integer such that x² = 2}
  - ∅

2. Use set builder notation to give a description of each of these sets.
- (a) {0, 3, 6, 9, 12}
  - $\{ x \mid x ∈ ℕ ∧ x/3=0 ∧ x<13 \}$
- (b) {−3, −2, −1, 0, 1, 2, 3}
  - $\{x \mid -3 ≤ x ≤ 3\}$
- (c) {m, n, o, p}
  - $\{x \mid \text{x is a letter of the alphabet after l and before q}\}$

3. For each of these pairs of sets, determine whether the first is a subset of the second, the second is a subset of the first, or neither is a subset of the other.
- (a) the set of airline flights from New York to New Delhi, the set of nonstop airline flights from New York to New Delhi
  - B ⊆ A
- (b) the set of people who speak English, the set of people who speak Chinese
  - no subsets.
- (c) the set of flying squirrels, the set of living creatures that can fly
  - A ⊆ B (A = ∅)

4. For each of these pairs of sets, determine whether the first is a subset of the second, the second is a subset of the first, or neither is a subset of the other.
- (a) the set of people who speak English, the set of people who speak English with an Australian accent
  - B ⊆ A
- (b) the set of fruits, the set of citrus fruits
  - B ⊆ A
- (c) the set of students studying discrete mathematics, the set of students studying data structures
  - no subsets

5. Determine whether each of these pairs of sets are equal.
- (a) {1, 3, 3, 3, 5, 5, 5, 5, 5}, {5, 3, 1}
  - Yes
- (b) {{1}}, {1, {1}}
  - No
- (c) ∅, {∅}
  - No

6. Suppose that A = {2, 4, 6}, B = {2, 6}, C = {4, 6}, and D = {4, 6, 8}. Determine which of these sets are subsets of which other of these sets.
   - B ⊆ A, C ⊆ A, C ⊆ D

7. For each of the following sets, determine whether 2 is an element of that set.
- (a) {x ∈ R | x is an integer greater than 1} Yes
- (b) {x ∈ R | x is the square of an integer} No
- (c) {2,{2}} Yes
- (d) {{2},{{2}}} No
- (e) {{2},{2,{2}}} No
- (f) {{{2}}} No

8. For each of the sets in Exercise 7, determine whether {2} is an element of that set.
- (a) {x ∈ R | x is an integer greater than 1} No
- (b) {x ∈ R | x is the square of an integer} No
- (c) {2,{2}} Yes
- (d) {{2},{{2}}} Yes
- (e) {{2},{2,{2}}} Yes
- (f) {{{2}}} No

9. Determine whether each of these statements is true or false.
- (a) 0 ∈ ∅ **F**
- (b) ∅ ∈ {0} **F**
- (c) {0} ⊂ ∅ **F**
- (d) ∅ ⊂ {0} ❌**F**
- (e) {0} ∈ {0} **F**
- (f) {0} ⊂ {0} ❌**T**
- (g) {∅} ⊆ {∅} **T**

10. Determine whether these statements are true or false.
- (a) ∅ ∈ {∅} **T**
- (b) ∅ ∈ {∅, {∅}} **T**
- (c) {∅} ∈ {∅} **F**
- (d) {∅} ∈ {{∅}} **T**
- (e) {∅} ⊂ {∅, {∅}} **T**
- (f) {{∅}} ⊂ {∅, {∅}} **T**
- (g) {{∅}} ⊂ {{∅}, {∅}} **F**

11. Determine whether each of these statements is true or false.
- (a) x ∈ {x} **T**
- (b) {x} ⊆ {x} **T**
- (c) {x} ∈ {x} **F**
- (d) {x} ∈ {{x}} **T**
- (f) ∅ ∈ {x} **T**
- (e) ∅ ⊆ {x} ❌**T**

12. Use a Venn diagram to illustrate the subset of odd integers in the set of all positive integers not exceeding 10.
    - (see notes)

13. Use a Venn diagram to illustrate the set of all months of the year whose names do not contain the letter R in the set of all months of the year.
    - (see notes)

14. Use a Venn diagram to illustrate the relationship A ⊆ B and B ⊆ C.
    - (see notes)

15. Use a Venn diagram to illustrate the relationships A ⊂ B and B ⊂ C.
    - (see notes) ❌ missing dots to indicate non-emptiness

16. Use a Venn diagram to illustrate the relationships A ⊂ B and A ⊂ C.
    - (see notes) ❌ assume intersection instead of inclusion (dont add points because it is unknown in which intersection-part they lie)

17. Suppose that A, B, and C are sets such that A ⊆ B and B ⊆ C. Show that A ⊆ C.
    - If all elements of B are in C and all elements of A are in B, A must be a subset of B and C.

18. Find two sets A and B such that A ∈ B and A ⊆ B.
    - A = ∅
    - B = ❌∅ ❎{∅}

19. What is the cardinality of each of these sets?
- (a) {a} **1**
- (b) {{a}} **1**
- (c) {a, {a}} **2**
- (d) {a, {a}, {a, {a}}} **3**

20. What is the cardinality of each of these sets?
- (a) ∅ **0**
- (b) {∅} **❌0 ❎1**
- (c) {∅, {∅}} **❌1 ❎2**
- (d) {∅, {∅}, {∅, {∅}}} **❌2 ❎3**

21. Find the power set of each of these sets, where a and b are distinct elements.
- (a) {a} $\{∅,\{a\}\}$
- (b) {a, b} $\{∅,\{a\},\{b\},\{a,b\}\}$
- (c) {∅, {∅}} $\{∅,\{∅\},⭕\{\{∅\}\},\{∅,\{∅\}\}\}$

22. Can you conclude that A = B if A and B are two sets with the same power set?
    - Yes, as the order of elements doesnt matter.
    - ✔ The union of all the sets in the power set of a set X must be exactly X . In other words, we can recover X from its power set, uniquely. Therefore the answer is yes.

23. How many elements does each of these sets have where a and b are distinct elements? (P = Powerset)
- (a) P({a, b, {a, b}}) **❌6 ❎8**
- (b) P({∅, a, {a}, {{a}}}) **❌12 ❎16**
- (c) P(P(∅)) **❌1 ❎2 {∅, {∅}}**
  - ❎ The power set of the empty set has 2⁰ = 1 element. The power set of this set therefore has 2¹ = 2 elements.

24. Determine whether each of these sets is the power set of a set, where a and b are distinct elements.
- (a) ∅
  - No, see above.
- (b) {∅, {a}}
  - Yes, {a}
- (c) {∅, {a}, {∅, a}}
  - No, 3 is not 2^x
- (d) {∅, {a}, {b}, {a, b}}
  - Yes, {a, b}

25. Prove that P(A) ⊆ P(B) if and only if A ⊆ B. (P = Powerset)
    - If P(A) ⊆ P(B), then we know that P(A) contains all combinations of elements of a set so all elements of A must be in B.
    If A ⊆ B, then P(B) contains all combinations of elements of A as well as those that are unique to B.
    ⭕ (For part 1) We must show that every element of A is also an element of B. So suppose a is an arbitrary element of A. Then {a} is a subset of A, so it is an element of the power set of A. Since the power set of A is a subset of the power set of B, it follows that {a} is an element of the power set of B, which means that {a} is a subset of B. But this means that the element of {a}, namely a, is an element of B, as desired.

26. Show that if A ⊆ C and B ⊆ D, then A × B ⊆ C × D
    - First we can see that all combinations of elements that are possible between A and C are possible between C and D as the former are subsets of the latter. Secondly, the order of the resulting pairs is the same as A/C are in the first position and B/D are in the second.
    - ✔ We need to show that every element of A × B is also an element of C × D . By definition, a typical element of A × B is a pair (a, b) where a ∈ A and b ∈ B . Because A ⊆ C , we know that a ∈ C ; similarly, b ∈ D . Therefore (a, b) ∈ C × D .

27. Let A = {a, b, c, d} and B = {y, z}. Find
- (a) A × B.
  - {(a,y), (b,y), (c,y), (d,y), (a,z), (b,z), (c,z), (d,z)}
- (b) B × A.
  - {(y,a), (y,b), (y,c), (y,d), (z,a), (z,b), (z,c), (z,d)}

28. What is the Cartesian product A × B, where A is the set of courses offered by the mathematics department at a university and B is the set of mathematics professors at this university? Give an example of how this Cartesian product can be used.
    - It is a listing of every course, once for each professor. It could be used for course selection, if any course could be taught by any professor.

29. What is the Cartesian product A × B × C, where A is the set of all airlines and B and C are both the set of all cities in the United States? Give an example of how this Cartesian product can be used.
    - This is the set of ordered triples (a,b,c) as definded above which maps every airline to every combination of cities. It could be used for assigning alternative flights with different airlines.

30. Suppose that A × B = ∅, where A and B are sets. What can you conclude?
    - ❌Both sets ❎at least one of the sets must equal the empty set.

31. Let A be a set. Show that ∅ × A = A × ∅ = ∅.
    - For A × B to contain at least one element (a,b) both sets must have at least one element. This is not the case here (see above).
    - ✔ By definition, ∅ × A consists of all pairs (x, a) such that x ∈ ∅ and a ∈ A. Since there are no elements x ∈ ∅ , there are no such pairs, so ∅ × A = ∅ . Similar reasoning shows that A × ∅ = ∅.

32. Let A = {a, b, c}, B = {x, y}, and C = {0, 1}. Find
- (a) ❕ A × B × C.
- (b) ❕ C × B × A.
- (c) ❕ C × A × B.
- (d) B × B × B.
  - {(x,x,x), (x,x,y), (x,y,x), (x,y,y), (y,x,x), (y,x,y), (y,y,x), (y,y,y)}

33. Find A² if
- (a) A = {0, 1, 3}.
  - {(0,0), (0,1), (0,3), (1,0), (1,1), (1,3), (3,0), (3,1), (3,3)}
- (b) ❕ A = {1, 2, a, b}.

34. Find A³ if
- (a) A = {a}.
  - {(a,a,a)}
- (b) ❕ A = {0, a}.

35. How many different elements does A × B have if A has m elements and B has n elements?
    - $mn$

36. How many different elements does A × B × C have if A has m elements, B has n elements, and C has p elements?
    - $mnp$

37. How many different elements does $A^n$ have when $A$ has $m$ elements and $n$ is a positive integer?
    - $m^n$

38. Show that A × B ≠ B × A, when A and B are nonempty, unless A = B.
    - ✅ Assuming A≠B, a∈A and b∈B, A×B yields ordered pairs (a,b) while A×B yields (b,a). If A=B however (a,b)=(b,a).
    - ❎ Suppose A ≠ B and neither A nor B is empty. We must prove that A × B ≠ B × A. Since A ≠ B , either we can find an element x that is in A but not B , or vice versa. The two cases are similar, so without loss of generality, let us assume that x is in A but not B . Also, since B is not empty, there is some element y ∈ B . Then (x, y) is in A × B by definition, but it is not in B × A since x ∉ B . Therefore A × B ≠ B × A.

39. Explain why A × B × C and (A × B) × C are not the same.
    - As a cartesian product A × B results in a set of ordered tuples a product with these ((A × B) × C) will yield elements of the form ((a,b),c).
    - ✔ To be more precise, there is a natural one-to-one correspondence between A × B × C and (A × B) × C given by (a, b, c) ↔ ((a, b), c).

40. Explain why (A × B) × (C × D) and A × (B × C) × D are not the same.
    - Similiar to the above the two cases result in the tuples ((a,b), (c,d)) and (a, (b,c), d) which are not the same.

41. Translate each of these quantifications into English and determine its truth value.
- (a) ∀x ∈ R (x² ≠ −1)
  - No real number has a square of -1. True.
- (b) ∃x ∈ Z (x² = 2)
  - There is at least one integer whose square is 2. False.
- (c) ∀x ∈ Z (x² > 0)
  - The square of all integers is greater than 0. ❌ True. ❎ 0²=0
- (d) ∃x ∈ R (x² = x)
  - There is a real number whose sqaure is equal to itself. True (1).

42. Translate each of these quantifications into English and determine its truth value.
- (a) ∃x ∈ R (x³ = −1)
  - There is a real number whose cube is -1. True (-1).
- (b) ∃x ∈ Z (x + 1 > x)
  - There is an integer whose sum with 1 is larger than itself. True for all Z.
- (c) ∀x ∈ Z (x − 1 ∈ Z)
  - All integers are still integers when 1 is subtracted. True.
- (d) ∀x ∈ Z (x² ∈ Z)
  - All integers are still integers when squared. True.

43. Find the truth set of each of these predicates where the domain is the set of integers.
- (a) P(x): x² < 3
  - {-1,0,1}
- (b) Q(x): x² > x
  - {x ∈ ℤ | x ∉ {0,1}}
  - ✔ Z-{0,1} = { ... ,-2,-1,2,3,4, ... }
- (c) R(x): 2x + 1 = 0
  - ❌ {-1/2} (not an integer) ❎ ∅

44. Find the truth set of each of these predicates where the domain is the set of integers.
- (a) P(x): x³ ≥ 1
  - ❌ ℤ-{0} ❎ {x ∈ Z | x ≥ 1}
- (b) Q(x): x² = 2
  - ∅
- (c) R(x): x < x²
  - ❌ ℤ-{-1,0,1} ❎ ℤ-{0,1}

45. (∗) The defining property of an ordered pair is that two ordered pairs are equal if and only if their first elements are equal and their second elements are equal. Surprisingly, instead of taking the ordered pair as a primitive concept, we can construct ordered pairs using basic notions from set theory. Show that if we define the ordered pair (a, b) to be {{a}, {a, b}}, then (a, b) = (c, d) if and only if a = c and b = d. [Hint: First show that {{a}, {a, b}} = {{c}, {c, d}} if and only if a = c and b = d.]
    - If a = c and b = d, then {{a}, {a, b}} clearly equals {{c}, {c, d}}. If {{a}, {a, b}} = {{c}, {c, d}}
    - ⭕ We want to show that if {{a},{a,b}} = {{c},{c,d}}, then a = c and b = d. **First consider the case in which a ≠ b**. Then {{a}, {a, b}} has exactly two elements, both of which are sets; exactly **one of them contains one element, and exactly one of them contains two elements**. Thus {{c}, {c, d}} must have the same property; hence c cannot equal d, and so {c} is the element containing one element. Hence {a} = {c}, and so **a = c**. Also in this case the two-element elements {a, b} and {c, d} must be equal, and since b ≠ a = c, we must have **b = d**. **The other possibility is that a = b**. Then {{a},{a,b}} ={{a}}, a set with one element. Hence {{c},{c,d}} must also have only one element, which can only happen when c = d and the set is {{c}} . It then follows that **a = c**, and hence **b = d**, as well.

46. (∗) This exercise presents **Russell’s paradox**. Let S be the set that contains a set x if the set x does not belong to itself, so that S = {x | x ∉ x}.
- (a) Show the assumption that S is a member of S leads to a contradiction.
  - As a member of S cannot be a member of itself by definition, this is a contradiction.
- (b) Show the assumption that S is not a member of S leads to a contradiction.
  - As S has a member only if that member does not belong to itself, S not belonging to itself would imply that it should be a member of itself.
By parts (a) and (b) it follows that the set S cannot be defined as it was. This paradox can be avoided by restricting the types of elements that sets can have.

47. (∗) Describe a procedure for listing all the subsets of a finite set (A).
    - ❌ add the empty set to the list
    - add the whole set A
    - include each element of A into a set and add those
    - if A has more that 1 element, create sets with two elements by combining the first member with all the others
    - do the same with the second member, on each turn checking if the set already has been created
    - repeat the two last steps until the cardinality of the created subsets is one less than As.
    - ❎ We can do this recursively, using the idea from Section 5.4 of reducing a problem to a smaller instance of the same problem. Suppose that the elements of the set in question are listed: $A = \{a_1 , a_2 , a_3 , ... , a_n\}$. First we will write down all the subsets that do not involve $a_n$. This is just the same problem we are talking about all over again, but with a smaller set---one with just n - 1 elements. We do this by the process we are currently describing. Then we write these same subsets down again, but this time adjoin $a_n$ to each one. Each subset of A will have been written down, then - first all those that do not include $a_n$, and then all those that do. For example, using this procedure the subsets of {p, d, q} would be listed in the order ∅, {p} , {d} , {p,d}, {q}, {p,q}, {d,q}, {p,d,q}. An alternative solution is given in the answer key in the back of the textbook.
