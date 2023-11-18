# 1.3 Propositional-Equivalences

1. Use truth tables to verify these equivalences.
- (a) p ∧ 𝐓 ≡ p
$$
\begin{array}{|c c|c|}
p & p ∧ 𝐓 & p ∧ 𝐓 ≡ p\\
\hline
T & T & T\\
F & F & T\\
\end{array}
$$
- (b) p ∨ 𝐅 ≡ p
- (c) p ∧ 𝐅 ≡ 𝐅
- (d) p ∨ 𝐓 ≡ 𝐓
- (e) p ∨ p ≡ p
- (f) p ∧ p ≡ p

3. Use truth tables to verify the commutative laws
- (a) p ∨ q ≡ q ∨ p
- (b) p ∧ q ≡ q ∧ p
$$
\begin{array}{|c c|c c|c c|}
p & q & p ∨ q & q ∨ p & p ∧ q & q ∧ p\\
\hline
T & T & T & T & T & T\\
T & F & T & T & F & F\\
F & T & T & T & F & F\\
F & F & F & F & F & F\\
\end{array}
$$

4. Use truth tables to verify the associative laws
- (a) (p ∨ q) ∨ r ≡ p ∨ (q ∨ r).
- (b) (p ∧ q) ∧ r ≡ p ∧ (q ∧ r).
$$
\begin{array}{|c c c|c|c|}
p & q & r & (p ∧ q) ∧ r & p ∧ (q ∧ r)\\
\hline
T & T & T & T & T\\
T & T & F & F & F\\
T & F & T & F & F\\
T & F & F & F & F\\
F & T & T & F & F\\
F & T & F & F & F\\
F & F & T & F & F\\
F & F & F & F & F\\
\end{array}
$$

5. Use a truth table to verify the distributive law p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r).
$$
\begin{array}{|c c c|c|c|}
p & q & r & p ∧ (q ∨ r) & (p ∧ q) ∨ (p ∧ r)\\
\hline
T & T & T & T & T\\
T & T & F & T & T\\
T & F & T & T & T\\
T & F & F & F & F\\
F & T & T & F & F\\
F & T & F & F & F\\
F & F & T & F & F\\
F & F & F & F & F\\
\end{array}
$$

6. Use a truth table to verify the first De Morgan law
¬(p ∧ q) ≡ ¬p ∨ ¬q.
$$
\begin{array}{|c c|c|c|}
p & q & ¬(p ∧ q) & ¬p ∨ ¬q\\
\hline
T & T & F & F\\
T & F & T & T\\
F & T & T & T\\
F & F & T & T\\
\end{array}
$$

7. Use De Morgan’s laws to find the negation of each of the following statements.
- **(a) Jan is rich and happy.**
  - Jan is not poor and not unhappy
  - It is not true that Jan is poor or unhappy
- (b) Carlos will bicycle or run tomorrow.
  - Carlos will not bicycle and not run
- (c) Mei walks or takes the bus to class.
  - Mei does not walk and does not take the bus
- (d) Ibrahim is smart and hard working.
  - Ibrahim is not smart or not hard working

8. Use De Morgan’s laws to find the negation of each of the following statements.
- (a) Kwame will take a job in industry or go to graduate school.
  - Kwame will not take a job and not go to graduate school
- (b) Yoshiko knows Java and calculus.
  - Yoshiko does not know Java or calculus
- (c) James is young and strong.
  - James is not young or not strong
- (d) Rita will move to Oregon or Washington.
  - Rita will not move to Oregon and not to Washington.

9. Show that each of these conditional statements is a tautology by using truth tables.
- (a) (p ∧ q) → p
$$
\begin{array}{|c c|c|}
p & q & (p ∧ q) → p\\
\hline
T & T & T\\
T & F & T\\
F & T & T\\
F & F & T\\
\end{array}
$$
- (b) p → (p ∨ q)
$$
\begin{array}{|c c|c|}
p & q & p → (p ∨ q)\\
\hline
T & T & T\\
T & F & T\\
F & T & T\\
F & F & T\\
\end{array}
$$
- (c) ¬p → (p → q)
$$
\begin{array}{|c c|c|}
p & q & ¬p → (p → q)\\
\hline
T & T & T\\
T & F & T\\
F & T & T\\
F & F & T\\
\end{array}
$$
- (d) (p ∧ q) → (p → q)
$$
\begin{array}{|c c|c|}
p & q & (p ∧ q) → (p → q)\\
\hline
T & T & T\\
T & F & T\\
F & T & T\\
F & F & T\\
\end{array}
$$
- (e) ¬(p → q) → p
$$
\begin{array}{|c c|c|}
p & q & ¬(p → q) → p\\
\hline
T & T & T\\
T & F & T\\
F & T & T\\
F & F & T\\
\end{array}
$$
- (f) ¬(p → q) → ¬q
$$
\begin{array}{|c c|c|}
p & q & ¬(p → q) → ¬q\\
\hline
T & T & T\\
T & F & T\\
F & T & T\\
F & F & T\\
\end{array}
$$

10. Show that each of these conditional statements is a tau- tology by using truth tables.
- (a) [¬p ∧ (p ∨ q)] → q
- (b) [(p → q) ∧ (q → r)] → (p → r)
- (c) [p ∧ (p → q)] → q
- (d) [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r

11. Show that each conditional statement in Exercise 9 is a
tautology without using truth tables.
- (a) (p ∧ q) → p
  - For p to be the true conclusion p must already be true in the antecedent.
- (b) p → (p ∨ q)
  - If the condition holds, the disjunction in the conclusion will already be proven to be true.
- (c) ¬p → (p → q)
  - The conclusion can only be false as the condition p has to be false.
- (d) (p ∧ q) → (p → q)
  - As both p and q have to be true in the first place, the conclusion is irrelevant.
- (e) ¬(p → q) → p
  - The only way this can be true is p being true and q being false, therefore the conclusion is superfluous.
- (f) ¬(p → q) → ¬q
  - As above, q is already proven to be false in the antecedent.

12. Show that each conditional statement in Exercise 10 is a tautology without using truth tables.
- **(a) [¬p ∧ (p ∨ q)] → q**
$$
¬p ∧ (p ∨ q) → q \\
≡ ¬(¬p ∧ (p ∨ q)) ∨ q \\
≡ ❌ (p ∧ ¬(p ∨ q)) ∨ q \\
≡ ❌ (p ∧ ¬p ∧ ¬q) ∨ q \\
≡ ❌ (F ∧ ¬q) ∨ q \\
≡ ❌ ¬q ∨ q \\
≡ ❌ T \\
≡ p ∨ ¬(p ∨ q) ∨ q \\
≡ (p ∨ q) ∨ ¬(p ∨ q) \\
≡ T \\
$$

- **(b) [(p → q) ∧ (q → r)] → (p → r)**
$$
[(p → q) ∧ (q → r)] → (p → r) \\
≡ (¬p ∨ q) ∧ (¬q ∨ r) → (p ∨ r) \\
≡ ¬((¬p ∨ q) ∧ (¬q ∨ r)) ∨ (p ∨ r) \\
≡ ¬(¬p ∨ q) ∨ ¬(¬q ∨ r) ∨ (p ∨ r) \\
≡ (p ∧ ¬q) ∨ (q ∧ ¬r) ∨ (p ∨ r) \\
≡ ((p ∧ ¬q) ∨ (q ∧ ¬r)) ∨ (p ∨ r) \\
$$

- (c) [p ∧ (p → q)] → q
  - The condition can only be true, if p is true, which also means q must be true. Therefore the conclusion is already known to be true.
$$
p ∧ (p → q) → q \\
≡ ¬(p ∧ (¬p ∨ q)) ∨ q \\
≡ (¬p ∨ ¬(¬p ∨ q)) ∨ q \\
≡ ¬p ∨ ((p ∧ ¬q) ∨ q) \\
≡ ¬p ∨ ((q ∨ p) ∧ (q ∨ ¬q)) \\
≡ ¬p ∨ ((q ∨ p) ∧ T) \\
≡ ¬p ∨ q ∨ p \\
≡ T ∨ q \\
≡ T \\
$$

- (d) [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r
  - First, from te first part of the condition, either p or q mus be true. So at least one of the two other parts must have a true conclusion. As r is the conclusion in both cases it must be true and the conclusion is tautologic.

13. Use truth tables to verify the absorption laws.
- (a) p ∨ (p ∧ q) ≡ p
$$
\begin{array}{|c c|c|c|}
p & q & p ∧ q & p ∨ (p ∧ q)\\
\hline
T & T & T & T\\
T & F & F & T\\
F & T & F & F\\
F & F & F & F\\
\end{array}
$$

- (b) p ∧ (p ∨ q) ≡ p
$$
\begin{array}{|c c|c|c|}
p & q & p ∨ q & p ∧ (p ∨ q)\\
\hline
T & T & T & T\\
T & F & T & T\\
F & T & T & F\\
F & F & F & F\\
\end{array}
$$

14. **- Determine whether (¬p ∧ (p → q)) → ¬q is a tautology**
    - ❌ p has to be false
    - ❌ if p is false, q could either be true or false
    - This says that if q is the conclusion of p and p is false, then q is false. But if p is false, q could either be true or false to render the antecedent true.

15. Determine whether (¬q ∧ (p → q)) → ¬p is a tautology.

    - this says that when the conclusion of an implication is false, then the condition is also false, which is not true

    - for this to be false p has to be true
    - then the 2nd part of the condition says that q would have to be true to render the conjunction true
    - however, q is negated in the conjunction, so it will always be false

16. Show that p ↔ q and (p ∧ q) ∨ (¬p ∧ ¬q) are logically equivalent.

17. **+Show that ¬(p ↔ q) and p ↔ ¬q are logically equivalent.**
    - ❌ The first biconditional will be true if p and q are false and false if they are true. The second implies that p and q have to have different values.
    - as a biconditional is true whenever both values are the same, a biconditional with one negated side will only be true, whenever both sides are different, which is the same as negating a complete biconditional.

18. Show that p → q and ¬q → ¬p are logically equivalent.
    - p → q is false only if p is true and q is false. the same is true for ¬q → ¬p.

19. Show that ¬p ↔ q and p ↔ ¬q are logically equivalent.
    - Inverting the truth values of p and q between these statements keeps the bicondotional true.

20. Show that ¬(p ⊕ q) and p ↔ q are logically equivalent.
    - The first statement says that p and q cannot have different values which is the defintion of a biconditional.

21. Show that ¬(p ↔ q) and ¬p ↔ q are logically equivalent.
    - The first proposition is true only if p and q have different values which is also the case in the second proposition.

22. Show that (p → q) ∧ (p → r) and p → (q ∧ r) are logically equivalent.
    - The first proposition essentially means that q and r are true if p is true which is exactly what the second one says.

23. **+ Show that (p → r) ∧ (q → r) and (p ∨ q) → r are logically equivalent.**
    - ❌ Assuming (p → r) ∧ (q → r) to be true we want to show that (p ∨ q) → r is true which means r is true whenever p OR q is true OR both are true. Applying this to the first proposition with p, q and are being true we can see that this holds.
    - The first part will be true if either p and q are false or if p and q are true as well as r. Both applies to the second part.

24. **+ Show that (p → q) ∨ (p → r) and p → (q ∨ r) are logically equivalent.**
    - ❌ As p → (q ∨ r) is only false if p is true and q ∨ r is false, it follows that q and r would be false. Applying this to the first proposition it is rendered false as well. If either q or r are are true both propositions are true.
    - p → (q ∨ r) is only true if p is false or if it is true and at least one of q and r is true.

25. Show that (p → r) ∨ (q → r) and (p ∧ q) → r are logically equivalent.
    - As the first proposition is a disjunction, we show that it is false in the same cases as the second is. This means p → r and q → r have to be false which is true only if p and q are true and r is false. This holds for the second propositon. If either p or q are false, both propositions are true.

26. Show that ¬p → (q → r) and q → (p ∨ r) are logically equivalent.
    - q → (p ∨ r) is true whenever q is false or q is true and either p or r are true. Applying the cases to ¬p → (q → r) you can see that this is true for p being true as well as for p being false and q and r being true.

27. Show that p ↔ q and (p → q) ∧ (q → p) are logically equivalent.
    - Here (p → q) ∧ (q → p) has to be true whenever p and q have the same value but not otherwise. This is true for both being false as both implications fail and true for both being true as the conclusion is the other proposition respectively.

28. Show that p ↔ q and ¬p ↔ ¬q are logically equivalent.
    - As both propositions are negated together their sameness is still given.

29. **- Show that (p → q) ∧ (q → r) → (p → r) is a tautology.**
    - ❌ This would be a tautology if the top-level-conditional cannot be false. So (p → q) ∧ (q → r) cannot be true while (p → r) is false. p → r will be false if p is true and r is false. Applying this to the antecedent we see that it must be false for any q.

30. **+ Show that (p ∨ q) ∧ (¬p ∨ r) → (q ∨ r) is a tautology**
    - We will show that if p ∨ q and ¬p ∨ r are true, q ∨ r will be true. Because p is negated in one part of the antecedent one of p ∨ q and ¬p ∨ r will always be true. Therefore it is sufficient for either q or r to be true.

31. Show that (p → q) → r and p → (q → r) are not logically equivalent.
    - (¬p ∨ q) → r will be false only if r is false and either p is false or q is true or both. Applying this to p → (¬q ∨ r), shows that it is true if p is true, therefore they are not equivalent.

32. Show that (p ∧ q) → r and (p → r) ∧ (q → r) are not logically equivalent.
    - This is not the same for p = true and q and r = false.

33. **~ Show that (p → q) → (r → s) and (p → r) → (q → s) are not logically equivalent.**
    - ❌ For both statements to be false r → s and q → s have to be false. This means s has to be false and both r and q have to be true. Applying this to (p → q) → (r → s) this gives a false proposition only if p is false. Applying this to (p → r) → (q → s) gives
    - Assuming the first part to be false p → q would have to be true and r → s would have to be false. This implies r is true and s is false.

34. Find the dual of each of these compound propositions.
- (a) p ∨ ¬q
  - p ∧ ¬q
- (b) p ∧ (q ∨ (r ∧ T))
  - p ∨ (q ∧ (r ∨ T))
- (c) (p ∧ ¬q) ∨ (q ∧ F)
  - (p ∨ ¬q) ∧ (q ∨ T)

36. **+ When does s∗ = s, where s is a compound proposition?**
    - ❌ p ∧ T (Identity), p ∨ p (Idempotence), p ∨ (p ∧ q) (Absorption)
    - (~) p ∧ T = p ∨ F

37. Show that (s∗ )∗ = s when s is a compound proposition.
    - As all changes in the dual will be reverted, this is clearly the same.

38. Show that the logical equivalences in Table 6, except for the double negation law, come in pairs, where each pair contains compound propositions that are duals of each other.
    - Considering that (s*)* = s, it follows that you can go from one case of each law to the other by by writing the dual.

40. Find a compound proposition involving the propositional variables p, q, and r that is true when p and q are true and r is false, but is false otherwise. [Hint: Use a conjunction of each propositional variable or its negation.]
    - p ∧ q ∧ ¬r

41. Find a compound proposition involving the propositional variables p, q, and r that is true when exactly two of p, q, and r are true and is false otherwise. [Hint: Form a disjunction of conjunctions. Include a conjunction for each combination of values for which the compound proposition is true. Each conjunction should include each of the three propositional variables or its negations.]
    - (¬p ∧ q ∧ r) ∨ (p ∧ ¬q ∧ r) ∨ (p ∧ q ∧ ¬r)

42. Suppose that a truth table in n propositional variables is specified. Show that a compound proposition with this truth table can be formed by taking the disjunction of conjunctions of the variables or their negations, with one conjunction included for each combination of values for which the compound proposition is true. The resulting compound proposition is said to be in disjunctive normal form.

43. Show that ¬, ∧, and ∨ form a functionally complete collection of logical operators. [Hint: Use the fact that every compound proposition is logically equivalent to one in disjunctive normal form, as shown in Exercise 42.]
    - As for every possible compound proposition using ¬, ∧, and ∨ and n statements, the disjunctive normal form for every possible combination of truth valus can be created, this is then equivalent to the initial form.

44. (*) Show that ¬ and ∧ form a functionally complete collection of logical operators. [Hint: First use a De Morgan law to show that p ∨ q is logically equivalent to ¬(¬p ∧ ¬q).]
    - De Morgans law shows that the negation of ¬(¬p ∧ ¬q) is p ∨ q and vice versa. Each occurrence of ∨ can therefore be expressed with ¬ and ∧. Applying this to the disjunctive normal form which can be used to express any compund proposition gives us
    - p1 ∨ p2 ∨ ··· ∨ pn
    - ¬(¬p1 ∧ ¬p2 ∧ ··· ∧ ¬pn)
    - therefore ¬ and ∧ are sufficient to express any compound proposition.

45. (*) Show that ¬ and ∨ form a functionally complete collection of logical operators.
    - Similar to 44 we now apply De Morgans law to each proposition of the disjunctive normal form rather than to the whole. Therefore every p1 ∨ p2 ∨ ··· ∨ pn now only uses ¬ and ∨.

46. Construct a truth table for the logical operator NAND.
$$
\begin{array}{|c c|c|}
p & q & p \uparrow q\\
\hline
T & T & F\\
T & F & T\\
F & T & T\\
F & F & T\\
\end{array}
$$

47. Show that p | q is logically equivalent to ¬(p ∧ q).
    - As ¬(p ∧ q) is false only for p and q being true this is esxactly what NAND means.

48. Construct a truth table for the logical operator NOR.
$$
\begin{array}{|c c|c|}
p & q & p \downarrow q\\
\hline
T & T & F\\
T & F & F\\
F & T & F\\
F & F & T\\
\end{array}
$$

49. Show that p ↓ q is logically equivalent to ¬(p ∨ q).
    - ¬(p ∨ q) is true only if neither p nor q are true, which is the definition of NOR.

50. In this exercise we will show that {↓} is a functionally complete collection of logical operators.
- (a) Show that p ↓ p is logically equivalent to ¬p.
  - As p ↓ p is only true if both sides are false, p must be false.

- *(b) Show that (p ↓ q) ↓ (p ↓ q) is logically equivalent to p ∨ q.*
  - ! As p ∨ q is only false, if both p and q are false, this has to be true for (p ↓ q) ↓ (p ↓ q) as well, which it is.

  - The proposition (p ↓ q) ↓ (p ↓ q) is equivalent, by part (a), to ¬(p ↓ q), which from the definition (or truth table or Exercise 49) is clearly equivalent to p ∨ q .

- (c) Conclude from parts (a) and (b), and Exercise 49, that {↓} is a functionally complete collection of logical operators.
  - As we know the disjunctive normal form can be expressed with only ¬ and ∨, we need to show that both of these operators have equivalences which use only use ↓. Part (a) shows that ¬p is logically equivalent to p ↓ p and part (b) shows that p ∨ q is equivalent to (p ↓ q) ↓ (p ↓ q).

51. **(*) Find a compound proposition logically equivalent to p → q using only the logical operator ↓.**
    - p → q
    - ❌ ¬(p ∨ q) **must be ¬ p ∨ q**
    - ❌ ((p ↓ q) ↓ (p ↓ q)) ↓ ((p ↓ q) ↓ (p ↓ q))

52. Show that {|} is a functionally complete collection of logical operators.
    - As we know the disjunctive normal form can be expressed with only ¬ and ∧, we need to show that both of these operators have equivalences which only use ↑.
    - ¬p ≡ p ↑ p
    - p ↑ q ≡ ¬(p ∧ q) [From 47]
    - ¬(p ↑ q) ≡ p ∧ q
    - p ∧ q ≡ (p ↑ q) ↑ (p ↑ q)

53. Show that p ↑ q and q ↑ p are equivalent.
    - Both are false only if p and q are true.

54. Show that p ↑ (q ↑ r) and (p ↑ q) ↑ r are not equivalent, so that the logical operator ↑ is not associative.
    - F ↑ (T ↑ T)
    - (F ↑ T) ↑ T
    - p = T, q = F and r = F give T for the first part and F for the second

55. **(*) How many different truth tables of compound propositions are there that involve the propositional variables p and q?**
    - ❌ To find the number of unique truth tables for all possible compound propositions, one first has to list all compound propositions involving ¬, ∧, ∨, ↑, ↓, → and ↔ and then eliminate all equivalents. The number of the remaining propositions is the solution.

56. Show that if p, q, and r are compound propositions such that p and q are logically equivalent and q and r are logically equivalent, then p and r are logically equivalent.
    - By the definition of logical equivalence this must be true.

57. The following sentence is taken from the specification of a telephone system: “If the directory database is opened, then the monitor is put in a closed state, if the system is not in its initial state.” This specification is hard to understand because it involves two conditional statements. Find an equivalent, easier-to-understand specification that in- volves disjunctions and negations but not conditional statements.
    - do: the directory database is opened
    - mc: the monitor is put in a closed state
    - in: the system is in its initial state
    - ❌ do → (¬in → mc)
    - ¬in → (do → mc)
    - do → (¬in → mc)
    - do → (in ∨ mc)
    - in ∨ ¬do ∨ mc
    - Either the system is in its initial state or the directory database is not opened or the monitor is put in a closed state.

58. How many of the disjunctions p ∨ ¬q, ¬p ∨ q, q ∨ r, q ∨ ¬r, and ¬q ∨ ¬r can be made simultaneously true by an assignment of truth values to p, q, and r?
    - (p ∨ ¬q), (¬p ∨ q), (q ∨ r), (q ∨ ¬r), (¬q ∨ ¬r)
    - p: 1, q: 23, ¬r: 45
    - p = T, q = T and r = F renders all true

59. How many of the disjunctions p ∨ ¬q ∨ s, ¬p ∨ ¬r ∨ s, ¬p ∨ ¬r ∨ ¬s, ¬p ∨ q ∨ ¬s, q ∨ r ∨ ¬s, q ∨ ¬r ∨ ¬s, ¬p ∨ ¬q ∨ ¬s, p ∨ r ∨ s, and p ∨ r ∨¬s can be made simultaneously true by an assignment of truth values to p, q, r, and s?
    - p ∨ ¬q ∨ s
    - ¬p ∨ ¬r ∨ s
    - ¬p ∨ ¬r ∨ ¬s
    - ¬p ∨ q ∨ ¬s
    - q ∨ r ∨ ¬s
    - q ∨ ¬r ∨ ¬s
    - ¬p ∨ ¬q ∨ ¬s
    - p ∨ r ∨ s
    - p ∨ r ∨¬s
    - p=F: 2,3,4,7
    - q=T: 6
    - r=T: 5,8,9
    - s=T: 1

60. Show that the negation of an unsatisfiable compound proposition is a tautology and the negation of a compound proposition that is a tautology is unsatisfiable.
    - a unsatisfiable compound proposition is in effect a contradiction, which resolves to false for all possible values. Negating this makes the result true for all values and is therefore a tautology.

61. Determine whether each of these compound propositions is satisfiable.
- **(a) (p ∨ ¬q) ∧ (¬p ∨ q) ∧ (¬p ∨ ¬q)**
  - ❌ Yes, if p and q have different values
- (b) (p → q) ∧ (p → ¬q) ∧ (¬p → q) ∧ (¬p → ¬q)
  - No, first p and q cannot both be true as this would create false conditionals. p and q having different values also doesnt work, as all permutations of values and negated values exist inside the conditonals, so one of them will always be false.
- (c) (p ↔ q) ∧ (¬p ↔ q)
  - No, p and q would have to have the same truth values but p is negated in the second part

62. Determine whether each of these compound propositions
is satisfiable.
- (a) (p ∨ q ∨ ¬r) ∧ (p ∨ ¬q ∨ ¬s) ∧ (p ∨ ¬r ∨ ¬s) ∧ (¬p ∨ ¬q ∨ ¬s) ∧ (p ∨ q ∨ ¬s)
  - Yes, for p=T, q=T and either r/s=F
- (b) (¬p ∨ ¬q ∨ r) ∧ (¬p ∨ q ∨ ¬s) ∧ (p ∨ ¬q ∨ ¬s) ∧ (¬p ∨ ¬r ∨ ¬s) ∧ (p ∨ q ∨ ¬r) ∧ (p ∨ ¬r ∨ ¬s)
  - Yes, p=T, q=T, r=T, s=F
- (c) (p ∨ q ∨ r) ∧ (p ∨ ¬q ∨ ¬s) ∧ (q ∨ ¬r ∨ s) ∧ (¬p ∨ r ∨ s) ∧ (¬p ∨ q ∨ ¬s) ∧ (p ∨ ¬q ∨ ¬r) ∧ (¬p ∨ ¬q ∨ s) ∧ (¬p ∨ ¬r ∨ ¬s)
  - Yes, p=F, q=F, r=T, s=T

63. **Show how the solution of a given 4 × 4 Sudoku puzzle can be found by solving a satisfiability problem.**
    - ❌ p(i, j, n): the proposition that each number n is positioned at row i, column j with all variables ranging from 1 to 4.
    - ❌ by creating a conjunction of the propositions denoting the given values, the propositions that every cell can only contain one number, that every row must contain every number, that every column must contain every number, that every subgrid must contain every number and the 64 possible position-propositions the solution can be found by determining the satisfiability of the resulting compound proposition.
    - $\bigwedge_{r=0}^{1}\bigwedge_{s=0}^{1}\bigwedge_{n=1}^{4}\bigvee_{i=1}^{2}\bigvee_{j=1}^{2} p(2r + i, 2s + j, n)$

64. **Construct a compound proposition that asserts that every cell of a 9 × 9 Sudoku puzzle contains at least one number.**
    - ❌ $\bigwedge_{i=1}^{9}\bigwedge_{j=1}^{9}p(i,j,n)$

65. Explain the steps in the construction of the compound proposition given in the text that asserts that every column of a 9 × 9 Sudoku puzzle contains every number.
    - $\bigvee_{i=1}^{9}p(i,j,n)$: Every column j contains number n

    - $\bigwedge_{n=1}^{9}\bigvee_{i=1}^{9}p(i,j,n)$: Every column j contains all n numbers

    - $\bigwedge_{j=1}^{9}\bigwedge_{n=1}^{9}\bigvee_{i=1}^{9}p(i,j,n)$: Every column contains all numbers

66. (*) Explain the steps in the construction of the compound proposition given in the text that asserts that each of the nine 3 × 3 blocks of a 9 × 9 Sudoku puzzle contains every number.
    - $p(3r+i, 3s+j,n)$: Every cell i,j where i is offset by 3r and j is offset by 3s contains number n. This defines subgrids by moving their upper and left edge inwards together. This also means that i and j must range from 1 to 3 for the expression to cover only the subgrid and that r and s must range from 0 to 2 to not 'push' the subgrids over the edge.

    - $\bigvee_{j=1}^{3}p(3r+i, 3s+j,n)$: Every row of the subgrid contains number n

    - $\bigvee_{i=1}^{3}\bigvee_{j=1}^{3}p(3r+i, 3s+j,n)$: Every cell of the subgrid contains number n

    - $\bigwedge_{n=1}^{9}\bigvee_{i=1}^{3}\bigvee_{j=1}^{3}p(3r+i, 3s+j,n)$: Every cell of the subgrid contains all n numbers

    - $\bigwedge_{s=0}^{2}\bigwedge_{n=1}^{9}\bigvee_{i=1}^{3}\bigvee_{j=1}^{3}p(3r+i, 3s+j,n)$: Every cell of the subgrid offset by 3s from the left contains all n numbers

    - $\bigwedge_{r=0}^{2}\bigwedge_{s=0}^{2}\bigwedge_{n=1}^{9}\bigvee_{i=1}^{3}\bigvee_{j=1}^{3}p(3r+i, 3s+j,n)$: Every cell of the subgrid offset by 3s from the left and offset by 3r from the top contains all n numbers
