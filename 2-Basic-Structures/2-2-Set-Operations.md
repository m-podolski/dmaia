# 2.2 Set Operations

1. Let A be the set of students who live within one mile of school and let B be the set of students who walk to classes. Describe the students in each of these sets.
- (a) A ∩ B
  - Students who live within one mile and walk.
- (b) A ∪ B
  - Students who live within one mile or walk (or both).
- (c) A − B
  - Students who live within one mile but do not walk.
- (d) B − A
  - Students who walk but do not live within one mile.

2. Suppose that A is the set of *sophomores* at your school and B is the set of *students in discrete mathematics* at your school. Express each of these sets in terms of A and B.
- (a) the set of sophomores taking discrete mathematics in your school
  - $A ∩ B$
- (b) the set of sophomores at your school who are not taking discrete mathematics
  - $A - B$
- (c) the set of students at your school who either are sophomores or are taking discrete mathematics
  - $A ∪ B$
- (d) the set of students at your school who either are not sophomores or are not taking discrete mathematics
  - $\overline{A} ∪ \overline{B}$

3. Let A = {1, 2, 3, 4, 5} and B = {0, 3, 6}. Find
- (a) A ∪ B.
  - {0,1,2,3,4,5,6}
- (b) A ∩ B.
  - {3}
- (c) A − B.
  - {1,2,4,5}
- (d) B − A.
  - {0,6}

4. ❕ Let A = {a, b, c, d, e} and B = {a, b, c, d, e, f, g, h}. Find
- (a) A ∪ B.
- (b) A ∩ B.
- (c) A − B.
- (d) B − A.

In Exercises 5–10 assume that A is a subset of some underlying universal set U .

5. Prove the complementation law in Table 1 by showing that $\overline{(\overline{A})} = A$.
   - ❌ As $\overline{A} = U - A$, $\overline{(\overline{A})} = U - (U - A) = A$.
   - ✅ $\overline{\overline{A}} = \{x|¬x∈\overline{A}\} = \{x|¬¬x∈\overline{A}\} = \{x|x∈\overline{A}\}$

6. Prove the identity laws in Table 1 by showing that
- (a) $A ∪ ∅ = A$.
  - $\{x|x ∈ ∅ ∨ x ∈ A\}$. As $x ∈ ∅$ is always false $x ∈ A$ remains.
  - ✔ $A ∪ Ø = \{ x | x ∈ A ∨ x ∈ Ø \} = \{ x | x ∈ A ∨ F \} = \{ x | x ∈ A \} = A$
- (b) $A ∩ U = A$.
  - As $A ⊆ U$ for all $x ∈ A$, $x ∈ U$ is true.
  - ✔ $A ∩ U = \{ x | x ∈ A ∧ x ∈ U \} = \{ x | x ∈ A ∧ T \} = \{ x | x ∈ A \} = A$

7. Prove the domination laws in Table 1 by showing that
- (a) $A ∪ U = U$.
  - $A ∪ U = \{x|x ∈ A ∨ x ∈ U\} = \{x|x ∈ A ∨ T\} = \{x|T\} = U$
- (b) $A ∩ ∅ = ∅$.
  - $A ∩ ∅ = \{x|x ∈ A ∧ x ∈ ∅\} = \{x|x ∈ A ∧ F\} = \{x|F\} = ∅$

8. Prove the idempotent laws in Table 1 by showing that
- (a) $A ∪ A = A$.
  - $A ∪ A = \{x|x ∈ A ∨ x ∈ A\} = \{x|x ∈ A\} = A$
- (b) $A ∩ A = A$.
  - $A ∪ A = \{x|x ∈ A ∧ x ∈ A\} = \{x|x ∈ A\} = A$

9. Prove the complement laws in Table 1 by showing that
- (a) $A ∪ \overline{A} = U$.
  - ❎ $A ∪ \overline{A} = \{x ∈ U|x ∈ A ∨ x ∉ A\} = U$
- (b) $A ∩ \overline{A} = ∅$.
  - ❎ $A ∩ \overline{A} = \{x ∈ U|x ∈ A ∧ x ∉ A\} = \{x|F\} = ∅$

10. Show that
- (a) $A − ∅ = A$.
  - $\{x|x ∈ A ∧ x ∉ ∅\} = \{x|x ∈ A ∧ T\} = \{x|x ∈ A\} = A$
- (b) $∅ − A = ∅$.
  - $\{x|x ∈ ∅ ∧ x ∉ A\} = \{x|F ∧ x ∈ A\} = \{x|F\} = ∅$

11. Let A and B be sets. Prove the commutative laws from Table 1 by showing that
- (a) A ∪ B = B ∪ A.
  - $A ∪ B = \{x|x ∈ A ∨ x ∈ B\} = \{x|x ∈ B ∨ x ∈ A\} = B ∪ A$
- (b) A ∩ B = B ∩ A.
  - $A ∩ B = \{x|x ∈ A ∧ x ∈ B\} = \{x|x ∈ B ∧ x ∈ A\} = B ∩ A$

12. Prove the first absorption law from Table 1 by showing that if A and B are sets, then A ∪ (A ∩ B) = A.
    - ✔ Prove equality by showing both sides are subsets of each other.
    - ❎ $A ∪ (A ∩ B) = \{x|x ∈ A ∨ (x ∈ A ∧ x ∈ B)\}$ so $x ∈ A$.
    - ⭕ Conversely, let x ∈ A. Then by the definition of union, x ∈ A ∪ (A ∩ B) as well. Thus we have shown that the right-hand side is a subset of the left-hand side.

13. Prove the second absorption law from Table 1 by showing that if A and B are sets, then A ∩ (A ∪ B) = A.
    - Again taking the subset-approach; if $x ∈ A ∩ (A ∪ B)$ then $x ∈ A$ by the definition of intersection. Conversely if $x ∈ A$, then $x ∈ A ∪ B$ by the defintion of union and also $x ∈ A ∩ (A ∪ B)$ again by the defintion of intersection.

14. Find the sets A and B if $A − B = {1, 5, 7, 8}$, $B − A = {2, 10}$, and $A ∩ B = {3, 6, 9}$.
    - A = {1, 3, 5, 6, 7, 8, 9}
    - B = {2, 3, 6, 9, 10}

15. Prove the second De Morgan law in Table 1 by showing that if A and B are sets, then $\overline{A ∪ B} = \overline{A} ∩ \overline{B}$
- (a) by showing each side is a subset of the other side.
  - If $x ∈ \overline{A ∪ B}$ then $x ∉ A ∪ B$ by the definition of complement. So ~~¬((x ∈ A) ∨ (x ∈ B)) by the defintion of union and~~ $x ∉ A ∧ x ∉ B$ ~~by applying De Morgans law and the definition of negation of propositions~~ which is equal to $\overline{A} ∩ \overline{B}$ by the definition of intersection and complement.
  - If $x ∈ \overline{A} ∩ \overline{B}$ then btd. of intersection and complement $x ∉ A ∧ x ∉ B$. ~~Btd. of negation of propositions this is ¬(x ∈ A) ∧ ¬(x ∈ B) and the application of De Morgans law results in ¬((x ∈ A) ∨ (x ∈ B)).~~ ⭕ So x cannot be in the union of A and B. Since $x ∉ A ∪ B$, Btd. of union and complement this is $\overline{A ∪ B}$
- (b) using a membership table.
  $$
  \begin{array}{|c|c|c|c|c|c|c|}
  A & B & A ∪ B & \overline{A ∪ B} & \overline{A} & \overline{B} & \overline{A} ∩ \overline{B} \\
  \hline
  1 & 1 & 1 & 0 & 0 & 0 & 0 \\
  1 & 0 & 1 & 0 & 0 & 1 & 0 \\
  0 & 1 & 1 & 0 & 1 & 0 & 0 \\
  0 & 0 & 0 & 1 & 1 & 1 & 1 \\
  \end{array}
  $$

16. Let A and B be sets. Show that
- (a) (A ∩ B) ⊆ A.
  - Btd. of intersection x is a member of A ∩ B only if it is a member of A.
- (b) A ⊆ (A ∪ B).
  - Btd. of union any x in A is in A ∪ B.
- (c) A − B ⊆ A.
  - As the difference A − B can at a maximum include any x in A (if B is empty), it is a subset of A.
- (d) A ∩ (B − A) = ∅.
  - As B − A does not include any x of A, this must be empty.
- (e) A ∪ (B − A) = A ∪ B.
  - If x ∈ A then x ∉ B - A but btd. of union it can be in A or B.

17. Show that if A, B, and C are sets, then $\overline{A ∩ B ∩ C} = \overline{A} ∪ \overline{B} ∪ \overline{C}$
- (a) by showing each side is a subset of the other side.
  - If $x ∈ \overline{A ∩ B ∩ C}$ then $x ∉ A ∩ B ∩ C$. By De Morgans law this is equal to $x ∉ A ∨ x ∉ B ∨ x ∉ C$ which is $\overline{A} ∪ \overline{B} ∪ \overline{C}$ btdo. union.
  - If $x ∈ \overline{A} ∪ \overline{B} ∪ \overline{C}$ then $x ∉ A ∨ x ∉ B ∨ x ∉ C$ ❎ which is $¬(x ∈ A ∧ x ∈ B ∧ x ∈ C)$ according to De Morgans law, so $\overline{A ∩ B ∩ C}$ btdo. union and complement.
- (b) ❕ using a membership table.

18. Let A, B, and C be sets. Show that
- (a) $(A ∪ B) ⊆ (A ∪ B ∪ C)$.
  - ❌ If $x ∈ A ∪ B ∪ C$ then $x ∈ A ∪ B$ or $x ∈ C$.
  - ✅  Suppose that $x ∈ A ∪ B$. Then either $x ∈ A$ or $x ∈ B$. In either case, certainly $x ∈ A ∪ B ∪ C$. This establishes the desired inclusion.
- (b) $(A ∩ B ∩ C) ⊆ (A ∩ B)$.
  - If $x ∈ A ∩ B ∩ C$ then $x ∈ A ∩ B$ and $x ∈ C$.
- (c) $(A − B) − C ⊆ A − C$.
  - ❎ As $A − B$ must be a subset of $A$, $(A − B) − C$ must be a subset of $A − C$.
  - ✅ Suppose that $x ∈ (A − B) − C$. Then x is in $A − B$ but not in $C$. Since $x ∈ A − B$, we know that $x ∈ A$. Since we have established that $x ∈ A$ but $x ∉ C$ , we have proved that $x ∈ A − C$.
- (d) $(A − C) ∩ (C − B) = ∅$.
  - If $x ∈ A − C$ then $x ∈ A$ but $x ∉ C$. If $x ∈ C - B$ then it must be in $C$. But now for the left side to be true $x ∉ C ∧ x ∈ C$ must hold, which is a contradiction.
- (e) $(B − A) ∪ (C − A) = (B ∪ C) − A$.
  - If $x ∈ (B − A) ∪ (C − A)$ then $x ∈ B$ or $x ∈ C$ and $x ∉ A$ for both differences (⭕ wlog.). ⭕ So $x ∈ B ∪ C$. By combining into a union we obtain $B ∪ C$ and by subtracting $A$ we get the result $(B ∪ C) − A$.
  - If $(B ∪ C) − A$ we again see that $x ∈ B$ or $x ∈ C$ and $x ∉ A$. By creating two differences, both subtracting $A$, we get $(B − A) ∪ (C − A)$.

19. Show that if A and B are sets, then
- (a) $A − B = A ∩ \overline{B}$.
  - ❎ If $x ∈ A − B$ then $x ∈ A$ and $x ∉ B$. The latter is equivalent to $x ∈ \overline{B}$, so $x ∈ A ∩ \overline{B}$
  - ❎ If $x ∈ A ∩ \overline{B}$ then $x ∈ A$ and $x ∉ B$ which is $A − B$ btdo. difference.
  - ✅ This is clear, since both of these sets are precisely $\{x|x ∈ A ∧ x ∉ B\}$
- (b) $(A ∩ B) ∪ (A ∩ \overline{B}) = A$.
  - If $x ∈ A ∩ B$ or $x ∈ A ∩ \overline{B}$ then $x ∈ A$ in both cases. ~~In the first $x ∈ A ∧ x ∈ B$, in the second $x ∈ A ∧ x ∉ B$, as both of these are complementary the set is equal to $A$.~~
  - ❌ If $x ∈ A$ we can assume a set $B$ and define a union of the intersection and intersection of the complement with $A$ by the logic stated above.
  - ✅ If $x ∈ A$, there are two cases: $x ∈ B$ and $x ∉ B$. In the former case, $x$ is an element of $A ∩ B$ and therefore also an element of $(A ∩ B) ∪ (A ∩ \overline{B})$. In the latter case, $x ∈ \overline{B}$ and therefore $x$ is an element of $A ∩ \overline{B}$ and therefore also an element of $(A ∩ B) ∪ (A ∩ \overline{B})$.

20. Show that if A and B are sets with $A ⊆ B$, then
- (a) $A ∪ B = B$.
  - ❌ As we know any $x ∈ A$ is also in B btdo. of subset, there can be no element in the union that is not in B.
  - ✅ It is always the case that $B ⊆ A ∪ B$, so it remains to show that $A ∪ B ⊆ B$. But this is clear because if $x ∈ A ∪ B$, then either $x ∈ A$, in which case $x ∈ B$ (because we are given $A ⊆ B$ ) or $x ∈ B$; in either case $x ∈ B$.
- (b) $A ∩ B = A$.
  - $A ∩ B$ is always a subset of $A$ bd.. ❌ If on the other hand $x ∈ A ∩ B$ then $x$ will be in $A$ and $B$. As we are given $A ⊆ B$ we know that there is no $x ∈ A$ not within $B$, so $A$ is a subset.
  - ✅ It it remains to show that $A ⊆ A ∩ B$. But this is clear because if $x ∈ A$, then $x ∈ B$ as well (because we are given $A ⊆ B$ ), so $x ∈ A ∩ B$.

21. Prove the first associative law from Table 1 by showing that if A, B, and C are sets, then $A ∪ (B ∪ C) = (A ∪ B) ∪ C$.
    - If $x ∈ A ∪ (B ∪ C)$ then $x$ can be in $A$ or $B ∪ C$.
    - ❌ If it is in $B$, we have $A ∪ B$. For the case that it is in $C$ we construct the union $(A ∪ B) ∪ C$.
    - ✅ In the former case we can conclude that $x ∈ A ∪ B$ and thus $x ∈ (A ∪ B) ∪ C$, btdo. union. In the latter case, $x$ must be in $B$ or $C$. In the former subcase, we can conclude that $x ∈ (A ∪ B) ∪ C$, again using the definition of union.
    - If $x ∈ (A ∪ B) ∪ C$.
    - ⭕ The argument in the other direction is practically identical, with the roles of $A$, $B$ and $C$ switched around.

22. Prove the second associative law from Table 1 by showing that if A, B, and C are sets, then $A ∩ (B ∩ C) = (A ∩ B) ∩ C$.
    - If $x ∈ A ∩ (B ∩ C)$ then $x$ will be in $A$, ❌ thus also in $A ∩ B$. $x$ will also be in $B ∩ C$ and therefore in $C$. So btdo. intersection we have $x ∈ (A ∩ B) ∩ C$.
    - ✅ If $x ∈ A ∩ (B ∩ C)$ then $x$ will be in $A$ and in $B$ and in $C$. Since x is in both $A$ and $B$, we conclude that $x ∈ A ∩ B$. This togeteher with the fact that $x ∈ C$ tells us that $x ∈ (A ∩ B) ∩ C$, as desired.
    - The reverse argument is again very similar.

23. Prove the first distributive law from Table 1 by showing that if A, B, and C are sets, then $A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)$.
    - ❎ If $x ∈ A ∪ (B ∩ C)$ then either $x ∈ A$ or $x ∈ B ∩ C$. If it is in $A$ then it will also be in $A ∪ B$ as well as in $A ∪ C$. If $x ∈ B$ and $x ∈ C$, the same is true. Btdo. intersection we have $x ∈ (A ∪ B) ∩ (A ∪ C)$.
    - ❎ If $x ∈ (A ∪ B) ∩ (A ∪ C)$ then it is in $A ∪ B$ and $A ∪ C$. If it is in $A$ then it is in $A ∪ (B ∩ C)$. If it is in $B$ or $C$
    - Assuming $x ∈ S$ for every proposition in the sets above, we get $(a ∨ b) ∧ (a ∨ c) ≡ a ∨ (b ∧ c)$.
    - If a is true both sides of the conjunction on the left are true, as is the right-hand side. If a is false, both b and c must be true on both sides. If wlog. either b or c is true but the other two variables are false both sides will be false as they are if all three variables are false.
    - ✅ (use membership tables)

24. Let A, B, and C be sets. Show that $(A − B) − C = (A − C) − (B − C)$.
    - If $x ∈ (A − B) − C$ then $x$ must be in $A$ but not in $B$ or $C$. ⭕ Thus $x ∈ A − C$, but $x ∉ B − C$ , so $x$ is in the right-hand side.
    - If $x ∈ (A − C) − (B − C)$ then it is not $B$ or $C$ but in $A - C$. So $x ∈ (A − B) − C$.

25. Let A = {0, 2, 4, 6, 8, 10}, B = {0, 1, 2, 3, 4, 5, 6}, and C = {4, 5, 6, 7, 8, 9, 10}. Find
- (a) $A ∩ B ∩ C$
  - {4, 6}
- (b) $A ∪ B ∪ C$
  - {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
- (c) $(A ∪ B) ∩ C$
  - {4, 5, 6, 8, 10}
- (d) $(A ∩ B) ∪ C$
  - {0, 2, 4, 5, 6, 7, 8, 9, 10}

26. Draw the Venn diagrams for each of these combinations of the sets A, B, and C.
- (a) $A ∩ (B ∪ C)$
- (b) $\overline{A} ∩ \overline{B} ∩ \overline{C}$
- (c) $(A − B) ∪ (A − C) ∪ (B − C)$
  - (see notes)

27. Draw the Venn diagrams for each of these combinations of the sets A, B, and C.
- (a) $A ∩ (B − C)$
- (b) $(A ∩ B) ∪ (A ∩ C)$
- (c) $(A ∩ \overline{B}) ∪ (A ∩ \overline{C})$
  - (see notes)

28. ❌ Draw the Venn diagrams for each of these combinations of the sets A, B, C, and D.
- (a) $(A ∩ B) ∪ (C ∩ D)$
- (b) $\overline{A} ∪ \overline{B} ∪ \overline{C} ∪ \overline{D}$
- (c) $A − (B ∩ C ∩ D)$
  - (see notes) ❌ (shapes allow only 14 of 16 possible combinations)

29. What can you say about the sets A and B if we know that
- (a) A ∪ B = A?
  - B ⊆ A
- (b) A ∩ B = A?
  - ❌ B = A ✅ A ⊆ B
- (c) A − B = A?
  - ❌ B = Ø ✅ A and B are disjoint: A ∩ B = Ø
- (d) A ∩ B = B ∩ A?
  - Nothing more specific as the sets are identical.
- (e) A − B = B − A?
  - A = B ⭕ = Ø
  - ✔ Every element in A - B must be in A, and every element in B - A must not be in A. Since no item can be in A and not be in A at the same time, there are no elements in both A - B and B - A. Thus the only way for these two sets to be equal is if **both of them are the empty set**. This means that every element of A must be in B, and every element of B must be in A. Thus we conclude that A = B.

30. Can you conclude that A = B if A, B, and C are sets such that
- (a) A ∪ C = B ∪ C?
  - ❌ Yes; any element in the unions that is not in C is in A or B. Then stating equality means A = B.
  - ✅ No; For instance, if A and B are both subsets of C , then this equation will always hold, and A need not equal B .
- (b) A ∩ C = B ∩ C?
  - ❌ Yes; even if A and B are subsets of C they have to intersect with C over the same elements.
  - ✅ No; let C = ∅
- (c) A ∪ C = B ∪ C and A ∩ C = B ∩ C?
  - ⭕ By putting the two conditions together, we can now conclude that A = B . By symmetry, it suffices to prove that A ⊆ B . Suppose that x ∈ A. There are two cases. If x ∈ C , then x ∈ A ∩ C = B ∩ C , which forces x ∈ B . On the other hand, if x ∉ C , then because x ∈ A ∪ C = B ∪ C , we must have x ∈ B .

31. Let A and B be subsets of a universal set U . Show that $A ⊆ B$ if and only if $\overline{B} ⊆ \overline{A}$.
    - Def: $\overline{A} = \{x ∈ U | x ∉ A\}$
    - Def: $A ⊆ B = ∀x(x ∈ A → x ∈ B)$
    - Given: $A ⊆ U$, $B ⊆ U$
    - ❎ If $A ⊆ B$, then either both sets are equal, which means their difference from $U$ will also be equal ($\overline{B} = \overline{A}$) or there is an $x ∈ B ∧ x ∉ A$ which means $x ∈ B ∩ \overline{A}$. So it is not in $\overline{B}$ but in $\overline{A}$. Therefore $\overline{B} ⊆ \overline{A}$.
    - If $\overline{B} ⊆ \overline{A}$, then they are either equal which makes $A ⊆ B$ true or there is an $x ∈ \overline{A} ∧ x ∉ \overline{B}$ which in the context of $U$ means $x ∉ A ∧ x ∈ B$, therefore $A ⊆ B$.
    - ✅ This is the set-theoretic version of the contrapositive law for logic, which says that $p → q$ is logically equivalent to $¬q → ¬p$. We argue as follows. $A ⊆ B ≡ ∀x(x ∈ A → x ∈ B) ≡ ∀x(x ∉ B→ x ∉ A) ≡ ∀x(x ∈ \overline{B} → x ∈ \overline{A}) ≡ \overline{B} ⊆ \overline{A}$

The **symmetric difference** of $A$ and $B$, denoted by $A ⊕ B$, is the set containing those elements in either $A$ or $B$, but not in both $A$ and $B$.

32. Find the symmetric difference of {1, 3, 5} and {1, 2, 3}.
    - {2, 5}

33. Find the symmetric difference of the set of computer science majors at a school and the set of mathematics majors at this school.
    - The set of students who major either CS or M but not both.

34. Draw a Venn diagram for the symmetric difference of the sets A and B.
    - (see notes)

35. Show that A ⊕ B = (A ∪ B) − (A ∩ B).
    - ❎ If $x ∈ A ⊕ B$ then x cannot be element of both A and B; $x ∉ A ∩ B$. But every x must be in A or B; $A ∪ B$. By writing the difference both conditions are included; $(A ∪ B) − (A ∩ B)$. Conversely if $x ∈ (A ∪ B) − (A ∩ B)$ then $x ∈ A ∪ B$ and $x ∉ A ∩ B$.
    - ✅ This is just a restatement of the definition. An element is in $(A ∪ B) − (A ∩ B)$ if it is in the union, but not in the intersection.

36. Show that A ⊕ B = (A − B) ∪ (B − A).
    - If $x ∈ A ⊕ B$ then $(x ∈ A ∧ x ∉ B) ∨ (x ∉ A ∧ x ∈ B)$. Which bd. is $(A − B) ∪ (B − A)$.

37. Show that if A is a subset of a universal set U , then
- (a) $A ⊕ A = Ø$
  - $A ⊕ A = (A − A) ∪ (A − A) = Ø ∪ Ø$
- (b) $A ⊕ Ø = A$
  - $A ⊕ Ø = (A − Ø) ∪ (Ø − A) = A ∪ Ø = A$
- (c) $A ⊕ U = \overline{A}$
  - $A ⊕ U = (A − U) ∪ (U − A) = Ø ∪ \overline{A} = \overline{A}$
- (d) $A ⊕ \overline{A} = U$
  - $A ⊕ \overline{A} = (A − \overline{A}) ∪ (\overline{A} − A) = A ∪ \overline{A} = U$

38. Show that if A and B are sets, then
- (a) $A ⊕ B = B ⊕ A$
  - ❎ As the logical or is commutative $(x ∈ A ∧ x ∉ B) ∨ (x ∉ A ∧ x ∈ B)$ is the same as $(x ∉ A ∧ x ∈ B) ∨ (x ∈ A ∧ x ∉ B)$
  - ✅ This is clear from the symmetry (between A and B) in the definition of symmetric difference.
- (b) $(A ⊕ B) ⊕ B = A$
  - ❌ If $x ∈ A ⊕ B$, x can be in $B$ but if $x ∈ (A ⊕ B) ⊕ B$, it cannot be in $B$ and $A ⊕ B$, so x must be in $A$.
  - ✅ We prove two things. To show that $A ⊆ (A ⊕ B) ⊕ B$, suppose $x ∈ A$. If $x ∈ B$, then $x ∉ A ⊕ B$, so x is an element of the right-hand side. On the other hand if $x ∉ B$ , then $x ∈ A ⊕ B$, so again x is in the right-hand side. Conversely, suppose x is an element of the right-hand side. There are two cases. If $x ∉ B$, then necessarily $x ∈ A ⊕ B$, whence $x ∈ A$. If $x ∈ B$, then necessarily $x ∉ A ⊕ B$, and the only way for that to happen (since $x ∈ B$) is for x to be in $A$.

39. What can you say about the sets A and B if $A ⊕ B = A$?
    - $A ⊕ Ø = (A − Ø) ∪ (Ø − A) = A ∪ Ø = A$.
    - A is non-empty and B is the empty set.
    - ✔ We can conclude that $B = Ø$. To see this, suppose that $B$ contains some element $b$. If $b ∈ A$, then $b$ is excluded from $A ⊕ B$, so $A ⊕ B$ cannot equal $A$. On the other hand, if $b ∉ A$, then $b$ must be in $A ⊕ B$, so again $A ⊕ B$ cannot equal $A$. Thus in either case, $A ⊕ B ≠ A$. We conclude that $B$ cannot have any elements.

40. (∗) Determine whether the symmetric difference is associative; that is, if A, B, and C are sets, does it follow that A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C?
    - ❎ If $x ∈ A ⊕ (B ⊕ C)$ then $x ∉ A ∩ (B ∩ C)$ which is equivalent to $x ∉ (A ∩ B) ∩ C$, so $x ∈ (A ⊕ B) ⊕ C$.
    - ✅ This is an identity; each side consists of those things that are in an odd number of the sets A, B, and C.

41. (∗) Suppose that A, B, and C are sets such that $A ⊕ C = B ⊕ C$. Must it be the case that $A = B$?
    - Yes; ❌ as the intersection are excluded, no subset-relationships are possible. Additionally if $A ⊕ C = C$ or $B ⊕ C = C$ then A and B are both the empty set.
    - ✅ To show that $A = B$, we need to show that $x ∈ A$ implies $x ∈ B$ and conversely. By symmetry, it will be enough to show one direction of this. So assume that $A ⊕ C = B ⊕ C$, and let $x ∈ A$ be given. There are two cases to consider, depending on whether $x ∈ C$. If $x ∈ C$, then by definition we can conclude that $x ∉ A ⊕ C$. Therefore $x tf: B ⊕ C$. Now if $x$ were not in $B$, then $x$ would be in $B ⊕ C$ (since $x ∈ C$ by assumption). Since this is not true, we conclude that $x ∈ B$, as desired. For the other case, assume that $x ∉ C$. Then $x ∈ A ⊕ C$. Therefore $x ∈ B ⊕ C$ as well. Again, if $x$ were not in $B$, then it could not be in $B ⊕ C$ (since $x ∉ C$ by assumption). Once again we conclude that $x ∈ B$, and the proof is complete.

42. If A, B, C, and D are sets, does it follow that (A ⊕ B) ⊕ (C ⊕ D) = (A ⊕ C) ⊕ (B ⊕ D)?
    - Yes, because every set appears an odd number of times.
    - ✔ This is an identity; **each side consists of those things that are in an odd number of the sets** A, B , C , and D.

43. If A, B, C, and D are sets, does it follow that (A ⊕ B) ⊕ (C ⊕ D) = (A ⊕ D) ⊕ (B ⊕ C)?
    - Yes, see above.

44. Show that if A and B are finite sets, then $A ∪ B$ is a finite set.
    - As $|A|$ and $|B|$ are nonnegative integers and $x ∈ A ∨ x ∈ B$, $|A ∪ B|$ can be no more than $|A| + |B|$.
    - ✔ (it might be less because $A ∩ B$ might be nonempty)

45. Show that if A is an infinite set, then whenever B is a set, A ∪ B is also an infinite set.
    - As $|A ∪ B|$ is at most $|A| + |B|$ where $|A|$ is infinity, it must be infinite.
    - ⭕ We give a proof by contradiction. If $A U B$ is finite, then it has $n$ elements for some natural number $n$. But $A$ already has more than $n$ elements, because it is infinite, and $A U B$ has all the elements that $A$ has, so $A U B$ has more than $n$ elements. This contradiction shows that $A U B$ must be infinite.

46. (∗) Show that if A, B, and C are sets, then $|A ∪ B ∪ C| = |A| + |B| + |C| − |A ∩ B| − |A ∩ C| − |B ∩ C| + |A ∩ B ∩ C|$. (This is a special case of the inclusion–exclusion principle, which will be studied in Chapter 8.)
    - As $|A ∪ B ∪ C|$ will bd. be the total number of unique elements in the union, $|A| + |B| + |C|$ is more than that. In particular, it includes twice $|A ∩ B|$, $|A ∩ C|$ and $|B ∩ C|$ which results in thrice the value of $|A ∩ B ∩ C|$. By subtracting the former three sizes those intersections are counted only once but $|A ∩ B ∩ C|$ is now missing and included again for all to equal $|A ∪ B ∪ C|$.

47. Let $A_i = \{1, 2, 3, ..., i\}$ for $i = 1, 2, 3, ...$ . Find
- (a) ❓ $\bigcup\limits_{i=1}^{n} A_i$
  - ✅ The union of these sets is the set of elements that appear in at least one of them. In this case the sets are "increasing": $A_1 ⊆ A_2 ⊆ · · · ⊆ A_n$. Therefore every element in any of the sets is in $A_n$, so the union is $A_n= \{1,2, ... ,n\}$.
- (b) $\bigcap\limits_{i=1}^{n} A_i$
  - As in the intersection every element must appear in all sets and the sets are "increasing" (see above), $A_1= \{1\}$.

48. Let $A_i = \{. . . , −2, −1, 0, 1, . . . , i\}$. Find
- (a) $\bigcup\limits_{i=1}^{n} A_i$
  - ❌ $A_n = \{. . . , −2, −1, 0, 1\}$.
  - ✅ We note that these sets are increasing, that is, $A_1 ⊆ A_2 ⊆ A_3 ⊆ · · ·$. Therefore, the union of any collection of these sets is just the one with the largest subscript, and the intersection is just the one with the smallest subscript.
  - $A_n = \{. . . , −2, −1, 0, 1, . . . , n\}$.
- (b) $\bigcap\limits_{i=1}^{n} A_i$
  - ⭕✅ $A_1 = \{. . . , −2, −1, 0, 1\}$.

49. Let Ai be the set of all nonempty bit strings (that is, bit strings of length at least one) of length not exceeding $i$. Find
- (a) $\bigcup\limits_{i=1}^{n} A_i$
  - ⭕✅  Here the sets are increasing. A bit string of length not exceeding 1 is also a bit string of length not exceeding 2, so $A_1 ⊆ A_2$. Similarly, $A_2 ⊆ A_3 ⊆ A_4 ⊆ ··· ⊆ A_n$. Therefore the union of the sets $A_1, A_2, ... , A_n$ is just $A_n$ itself.
- (b) $\bigcap\limits_{i=1}^{n} A_i$
  - $A_1 = \{0, 1\}$

50. Find (1) $\bigcup_{i=1}^{∞} A_i$  and (2) $\bigcap_{i=1}^{∞} A_i$ if for every positive integer i,
- (a) $A_i = {i, i + 1, i + 2, . . .}$
  - (1) $ℤ⁺$ ✔ As $i$ increases, the sets get smaller: $· · · ⊂ A_3 ⊂ A_2 ⊂ A_1$. All the sets are subsets of $A_1$, which is the set of positive integers $ℤ⁺$.
  - (2) ❌ $ℤ⁺$ ✅ $Ø$ Every positive integer is excluded from at least one of the sets (in integers, fact from infinitely  many), so $Ø$
- (b) $A_i = {0, i}$
  - (1) $ℕ$
  - (2) $\{0\}$
- (c) $A_i = (0, i)$, that is, the set of real numbers $x$ with $0 < x < i$.
  - (1) $ℝ⁺$
  - (2) ❎ $\{x ∈ ℝ⁺\,|\,0 < x < 1\}$ ✅ $(0,1)$
- (d) $A_i = (i, ∞)$, that is, the set of real numbers $x$ with $x > i$.
  - (1) $(1, ∞)$
  - (2) $Ø$ ✔ Notice that $∞$ is not a real number, so we cannot write $A_i = \{∞\}$

51. Find (1) $\bigcup_{i=1}^{∞} A_i$ and (2) $\bigcap_{i=1}^{∞} A_i$ if for every positive integer $i$,
- (a) $A_i = \{−i, −i + 1, . . . , −1, 0, 1, . . . , i − 1, i\}$
  - (1) $ℤ$
  - (2) $\{−1, 0, 1\}$
- (b) $A_i = \{−i, i\}$
  - (1) ❎ $\{x ∈ ℤ\,|\,x ≠ 0\}$ ✅ $ℤ - \{0\}$
  - (2) ❌ $\{−1, 1\}$ ❎ $Ø$ (all sets are disjoint)
- (c) $A_i = [−i, i]$, that is, the set of real numbers $x$ with $−i ≤ x ≤ i$.
  - (1) $ℝ$
  - (2) $[−1, 1]$
- (d) $A_i = [i, ∞)$, that is, the set of real numbers $x$ with $x ≥ i$.
  - (1) $[1, ∞)$
  - (2) $Ø$

52. Suppose that the universal set is $U = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Express each of these sets with bit strings where the ith bit in the string is 1 if i is in the set and 0 otherwise.
- (a) $\{3, 4, 5\}$ 00 1110 0000
- (b) $\{1, 3, 6, 10\}$ 10 1001 0001
- (c) $\{2, 3, 4, 7, 8, 9\}$ 01 1100 1110

53. Using the same universal set as in the last problem, find the set specified by each of these bit strings.
- (a) 11 1100 1111 $\{1,2,3,4,7,8,9,10\}$
- (b) 01 0111 1000 $\{2,4,5,6,7\}$
- (c) 10 0000 0001 $\{1,10\}$

54. What subsets of a finite universal set do these bit strings represent?
- (a) the string with all zeros $Ø$
- (b) the string with all ones $U$

55. What is the bit string corresponding to the difference of two sets?
    - ❌ all zeros
    - ✅  We are given two bit strings, representing two sets. We want to represent the set of elements that are in the first set but not the second. Thus the bit in the ith position of the bit string for the difference is 1 if the ith bit of the first string is 1 and the ith bit of the second string is 0, and is 0 otherwise.

56. What is the bit string corresponding to the symmetric difference of two sets?
    - The bitstring will have 1 if the bit at the ith position of only one of the sets is 1 and 0 otherwise. ✔ XOR

57. Show how bitwise operations on bit strings can be used to find these combinations of
$A = \{a, b, c, d, e\}$,
$A_B =$ 11 1110 0000 0000 0000 0000 0000
$B = \{b, c, d, g, p, t, v\}$,
$B_B =$ 01 1100 1000 0000 0100 0101 0000
$C = \{c, e, i, o, u, x, y, z\}$, and
$C_B =$ 00 1010 0010 0000 1000 0010 0111
$D = \{d, e, h, i, n, o, t, u, x, y\}$.
$D_B =$ 00 0110 0110 0001 1000 0110 0110
- (a) $A ∪ B$
  - A OR B: 11 1110 1000 0000 0100 0101 0000
- (b) $A ∩ B$
  - A AND B: 01 1100 0000 0000 0000 0000 0000
- (c) ❕ $(A ∪ D) ∩ (B ∪ C)$
- (d) ❕ $A ∪ B ∪ C ∪ D$

58. How can the union and intersection of n sets that all are subsets of the universal set U be found using bit strings?
    - By applying the AND/OR operation successively on pairs of sets $A$ and $B$ where $A$ is either the first of $n$ sets or the result of the previous operation.

The successor of the set $A$ is the set $A ∪ \{A\}$.

59. Find the successors of the following sets.
- (a) $\{1, 2, 3\}$
  - $\{1, 2, 3, \{1, 2, 3\}\}$
- (b) $∅$
  - $\{∅\}$
- (c) $\{∅\}$
  - $\{∅, \{∅\}\}$
- (d) $\{∅, \{∅\}\}$
  - $\{∅, \{∅\}, \{∅, \{∅\}\}\}$

60. How many elements does the successor of a set with n elements have?
    - $n + 1$

Sometimes the number of times that an element occurs in an unordered collection matters. **Multisets** are unordered collections of elements where an element can occur as a member more than once. The notation $\{m_1 · a_1, m_2 · a_2, . . . , m_r · a_r \}$ denotes the multiset with element $a_1$ occurring $m_1$ times, element $a_2$ occurring $m_2$ times, and so on. The numbers $m_i$ , $i = 1, 2, . . .$ , $r$ are called the **multiplicities** of the elements $a_i$ , $i = 1, 2, . . . , r$.
Let $P$ and $Q$ be multisets. The **union** of the multisets $P$ and $Q$ is the multiset where the multiplicity of an element is the maximum of its multiplicities in $P$ and $Q$. The **intersection** of $P$ and $Q$ is the multiset where the multiplicity of an element is the minimum of its multiplicities in $P$ and $Q$. The **difference** of $P$ and $Q$ is the multiset where the multiplicity of an element is the multiplicity of the element in $P$ less its multiplicity in $Q$ unless this difference is negative, in which case the multiplicity is $0$. The **sum** of $P$ and $Q$ is the multiset where the multiplicity of an element is the sum of multiplicities in $P$ and $Q$. The union, intersection, and difference of $P$ and $Q$ are denoted by $P ∪ Q$, $P ∩ Q$, and $P − Q$, respectively (where these operations should not be confused with the analogous operations for sets). The sum of $P$ and $Q$ is denoted by $P + Q$.

61. Let A and B be the multisets $\{3 · a, 2 · b, 1 · c\}$ and $\{2 · a, 3 · b, 4 · d\}$, respectively. Find
- (a) $A ∪ B$ $\{3 · a, 3 · b, 1 · c, 4 · d\}$
- (b) $A ∩ B$ $\{2 · a, 2 · b\}$
- (c) $A − B$ $\{1 · a, 1 · c\}$
- (d) $B − A$ $\{1 · b, 4 · d\}$
- (e) $A + B$ $\{5 · a, 5 · b, 1 · c, 4 · d\}$

62. Suppose that A is the multiset that has as its elements the types of computer equipment needed by one department of a university and the multiplicities are the number of pieces of each type needed, and B is the analogous multiset for a second department of the university. For instance, **A** could be the multiset **{107 · personal computers, 44 · routers, 6 · servers}** and **B** could be the multiset **{14 · personal computers, 6 · routers, 2 · mainframes}**.
- (a) What combination of $A$ and $B$ represents the equipment the university should buy assuming both departments use the same equipment?
  - $A ∪ B$
- (b) What combination of $A$ and $B$ represents the equipment that will be used by both departments if both departments use the same equipment?
  - $A ∩ B$
- (c) What combination of $A$ and $B$ represents the equipment that the second department uses, but the first department does not, if both departments use the same equipment?
  - $B - A$
- (d) What combination of $A$ and $B$ represents the equipment that the university should purchase if the departments do not share equipment?
  - $A + B$

**Fuzzy sets** are used in artificial intelligence. Each element in the universal set $U$ has a **degree of membership**, which is a real number between 0 and 1 (including 0 and 1), in a fuzzy set $S$. The fuzzy set S is denoted by listing the elements with their degrees of membership (elements with 0 degree of membership are not listed). For instance, we write $\{0.6 Alice, 0.9 Brian, 0.4 Fred, 0.1 Oscar, 0.5 Rita\}$ for the set $F$ (of famous people) to indicate that Alice has a 0.6 degree of membership in F , Brian has a 0.9 degree of membership in F , Fred has a 0.4 degree of membership in F , Oscar has a 0.1 degree of membership in F , and Rita has a 0.5 degree of membership in F (so that Brian is the most famous and Oscar is the least famous of these people). Also suppose that R is the set of rich people with $R = \{0.4 Alice, 0.8 Brian, 0.2 Fred, 0.9 Oscar, 0.7 Rita\}$.

63. ❕ The **complement** of a fuzzy set S is the set $\overline{S}$, with the degree of the membership of an element in $\overline{S}$ equal to 1 minus the degree of membership of this element in S. Find $\overline{F}$ (the fuzzy set of people who are not famous) and $\overline{R}$ (the fuzzy set of people who are not rich).

64. ❕ The **union** of two fuzzy sets S and T is the fuzzy set $S ∪ T$, where the degree of membership of an element in S ∪ T is the maximum of the degrees of membership of this element in S and in T . Find the fuzzy set $F ∪ R$ of rich or famous people.

65. ❕ The **intersection** of two fuzzy sets S and T is the fuzzy set $S ∩ T$ , where the degree of membership of an element in S ∩ T is the minimum of the degrees of membership of this element in S and in T . Find the fuzzy set F ∩ R of rich and famous people.
    - {me}
