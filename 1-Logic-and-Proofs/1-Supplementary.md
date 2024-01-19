# 1 Supplementary

1. Let p be the proposition “I will do every exercise in this book” and q be the proposition “I will get an “A” in this course.” Express each of these as a combination of p and q.
- (a) I will get an “A” in this course only if I do every exercise in this book.
  - ❌ $p→q$
  - ❎ $q→p$
- (b) I will get an “A” in this course and I will do every exercise in this book.
  - $q∧p$
- (c) Either I will not get an “A” in this course or I will not do every exercise in this book.
  - $¬q∨¬p$
- (d) For me to get an “A” in this course it is necessary and sufficient that I do every exercise in this book.
  - $p↔q$

2. ❕ Find the truth table of the compound proposition $(p ∨ q) → (p ∧ ¬r)$.

3. Show that these compound propositions are tautologies.
- (a) $(¬q ∧ (p → q)) → ¬p$
  - ✅ As this proposition can only be false, if the condition is true and p is true, this must be shown to be a contradiction. Assuming the above for the conjunction to be true p → q has to be and therefore q. But this contradicts the initial assumption.
  - ❎ Since q is false but the conditional statement p → q is true, we must concludie that p is also false.
- (b) $((p ∨ q) ∧ ¬p) → q$
  - For (p ∨ q) ∧ ¬p to be true, q must be, therefore the conclusion is the same as the hypothesis.

4. Give the converse, the contrapositive, and the inverse of these conditional statements.
- (a) If it rains today, then I will drive to work.
  - Conv.: If I drive to work, it will rain today.
  - Contr.: If dont I drive to work, it will not rain today.
  - Inv.: If it does not rain today, then I will not drive to work.
- (b) If |x| = x, then x ≥ 0.
  - Conv.: If x ≥ 0, then |x| = x
  - Contr.: If x < 0, then |x| ≠ x
  - Inv.: If |x| ≠ x, then x < 0
- (c) If n is greater than 3, then n² is greater than 9.
  - Conv.: If n² is greater than 9, then n is greater than 3
  - Contr.: If n² is <= 9, then n is <= 3
  - Inv.: If n is <= 3, then n² is <= 9

5. Given a conditional statement p → q, find the converse of its inverse, the converse of its converse, and the converse of its contrapositive.
   - $¬q → ¬p$
   - $p → q$
   - $¬p → ¬q$

6. ❕ Given a conditional statement p → q, find the inverse of its inverse, the inverse of its converse, and the inverse of its contrapositive.

7. Find a compound proposition involving the propositional variables p, q, r, and s that is true when exactly three of these propositional variables are true and is false otherwise.
   - $(¬p∧q∧r∧s) ∨ (p∧¬q∧r∧s) ∨ (p∧q∧¬r∧s) ∨ (p∧q∧r∧¬s)$

8. Show that these statements are inconsistent: “If (t)Sergei takes the job offer then he will (b) get a signing bonus.” “If Sergei takes the job offer, then (h) he will receive a higher salary.” “If Sergei gets a signing bonus, then he will not receive a higher salary.” “Sergei takes the job offer.”
   - $t$
   - $t→b$ b must be true
   - ✅ $b→¬h$ h must be false
   - ✅ $t→h$ t must be false (contradiction)

9. Show that these statements are inconsistent: “If (t) Miranda does not take a course in discrete mathematics, then (g) she will not graduate.” “If Miranda does not graduate, then (q) she is not qualified for the job.” “If (r) Miranda reads this book, then she is qualified for the job.” “Miranda does not take a course in discrete mathematics but she reads this book.”
    - $¬t ∧ r$
    - $¬t → ¬g$ g must be false
    - ✅ $¬g → ¬q$ q must be false
    - ✅ $r → q$ contradiction

Teachers in the Middle Ages supposedly tested the realtime propositional logic ability of a student via a technique known as an obligato game. In an obligato game, a number of rounds is set and in each round the teacher gives the student successive assertions that the student must either accept or reject as they are given. When the student accepts an assertion, it is added as a commitment; when the student rejects an assertion its negation is added as a commitment. The student passes the test if the consistency of all commitments is maintained throughout the test.

10. Suppose that in a three-round obligato game, the teacher first gives the student the proposition $p → q$, then the proposition $¬(p ∨ r) ∨ q$, and finally the proposition $q$. For which of the eight possible sequences of three answers will the student pass the test?
    - $p → q$
    - $¬(p ∨ r) ∨ q$ / $(¬p ∧ ¬r) ∨ q$
    - $q$
    - ❌ (misunderstood excercise) YNY, NYN
    - ❎⚠️ (via truth-table)

11. ⚠️ Suppose that in a four-round obligato game, the teacher first gives the student the proposition ¬(p → (q ∧ r)), then the proposition p ∨ ¬q, then the proposition ¬r, and finally, the proposition (p ∧ r) ∨ (q → p). For which of the 16 possible sequences of four answers will the student pass the test?

12. Explain why every obligato game has a winning strategy.
    - ❌ As every compound proposition, however complex, reduces to a binary truth value and the player is supposed to give a binary answer, every proposition can be matched.
    - ❎⚠️ As we saw from the examples in the previous exercises, one winning strategy is just to assume that all the variables are true and answer "accept" or "reject" according to wether the given prop. is true or false.

Exercises 13 and 14 are set on the island of knights and knaves described in Example 7 in Section 1.2.

13. Suppose that you meet three people Aaron, Bohan, and Crystal. Can you determine what Aaron, Bohan, and Crystal are if Aaron says “All of us are knaves” and Bohan says “Exactly one of us is a knave.”?
    - a: $¬a ∧ ¬b ∧ ¬c$
      - if a is a knave, not all are knaves
      - if a were a knight, this would be a contradiction
    - b: $(¬a ∧ b ∧ c) ∨ (a ∧ ¬b ∧ c) ∨ (a ∧ b ∧ ¬c)$
      - at least a is a knave
      - if b is a knight, then $¬a ∧ b ∧ c$
      - if b is a knave, then $¬a ∧ ¬b ∧ c$
    - cannot be determined

14. Suppose that you meet three people, Anita, Boris, and Carmen. What are Anita, Boris, and Carmen if Anita says “I am a knave and Boris is a knight” and Boris says “Exactly one of the three of us is a knight”?
    - a: $¬a ∧ b$
      - a must be a knave
      - b must also be a knave
    - b: $(a ∧ ¬b ∧ ¬c) ∨ (¬a ∧ b ∧ ¬c) ∨ (¬a ∧ ¬b ∧ c)$
      - ⭕ c is also a knave

15. (Adapted from [Sm78]) Suppose that on an island there are three types of people, knights, knaves, and normals (also known as spies). Knights always tell the truth, knaves always lie, and normals sometimes lie and sometimes tell the truth. Detectives questioned three inhabitants of the island—Amy, Brenda, and Claire—as part of the investigation of a crime. The detectives knew that one of the three committed the crime, but not which one. They also knew that the criminal was a knight, and that the other two were not. Additionally, the detectives recorded these statements: Amy: “I am innocent.” Brenda: “What Amy says is true.” Claire: “Brenda is not a normal.” After analyzing their information, the detectives positively identified the guilty party. Who was it?
    - crime: $(a ∧ ¬b ∧ ¬c) ∨ (¬a ∧ b ∧ ¬c) ∨ (¬a ∧ ¬b ∧ c)$
    - criminal is knight
    - others are knave or normal
    - a: i am innocent
      - a cannot be a knight
      - a cannot be a knave
      - a is a spy
    - b: a is true
      - b is knight or spy
    - c: b is knight or knave
      - c is knave or spy
      - b is the knight (there must be one knight)
      - (c is a spy)

16. Show that if S is a proposition, where S is the conditional statement “If S is true, then unicorns live,” then “Unicorns live” is true. Show that it follows that S cannot be a proposition. (This paradox is known as Löb’s paradox.)
    - $s = (s → u) → u$
    - ❌ this creates endless recursion through the definition of s as it never hits a base case.
    - ❎ If S is a proposition, then it is either true or false. If S is false, then the statement "If S is true, then unicorns live' is vacuously true; but this IS S, so we would have a contradiction. Therefore S is true, so the statement "If S is true, then unicorns live" is true and has a true hypothesis. Hence it has a true conclusion, and so unicorns live. But we know that unicorns do not live. It follows that S cannot be a proposition.

17. Show that the argument with premises “The tooth fairy is a real person” and “The tooth fairy is not a real person” and conclusion “You can find gold at the end of the rainbow” is a valid argument. Does this show that the conclusion is true?
    - ❎ It is vacuously true that whenever both of the (contradictory) premises are true the conclusion is as well but because the premises are not both true we cannot conclude anything.

18. Suppose that the truth value of the proposition pi is T whenever i is an odd positive integer and is F whenever i is an even positive integer. Find the truth values of $\bigvee^{100}_{i=1} (p_i ∧ p_i+1)$ and $\bigwedge^{100}_{i=1} (p_i ∨ p_i+1 )$.
    - $\bigvee^{100}_{i=1} (p_i ∧ p_i+1)$
    - $(p_1 ∧ p_1+1) ∨ (p_2 ∧ p_2+1) ∨ (p_3 ∧ p_3+1) ...$
    - $(T ∧ F) ∨ (F ∧ T) ∨ (T ∧ F) ...$
    - F
    - $\bigwedge^{100}_{i=1} (p_i ∨ p_i+1 )$
    - $(T ∨ F) ∧ (F ∨ T) ∧ (T ∨ F) ...$
    - T

19. ❕ (∗) Model 16 × 16 Sudoku puzzles (with 4 × 4 blocks) as satisfiability problems.
    - ✅ same as for the 9x9 (1.3), just change the indexes

20. Let P(x) be the statement “Student x knows calculus” and let Q(y) be the statement “Class y contains a student who knows calculus.” Express each of these as quantifications of P(x) and Q(y).
- (a) Some students know calculus.
  - $∃x∃y(x≠y ∧ P(x) ∧ P(y))$
- (b) Not every student knows calculus.
  - $∃x¬P(x)$
- (c) Every class has a student in it who knows calculus.
  - $∀yQ(y)$
- (d) Every student in every class knows calculus.
  - $∀x∀y(P(x) ∧ Q(y))$
  - ❎ $∀xP(x)$
- (e) There is at least one class with no students who know calculus.
  - $∃y¬Q(y)$

21. Let P(m, n) be the statement “m divides n,” where the domain for both variables consists of all positive integers. (By “m divides n” we mean that n = km for some integer k.) Determine the truth values of each of these statements.
- (a) $P(4,5)$ F
- (b) $P(2,4)$ T
- (c) $∀m∀n P(m,n)$ F
- (d) $∃m∀n P(m,n)$ T (1)
- (e) $∃n∀m P(m,n)$ F
- (f) $∀n P(1,n)$ T

22. Find a domain for the quantifiers in $∃x∃y(x ≠ y ∧ ∀z((z = x) ∨ (z = y)))$ such that this statement is true.
    - The set of black shoes I own.

23. Find a domain for the quantifiers in $∃x∃y(x ≠ y ∧ ∀z((z = x) ∨ (z = y)))$ such that this statement is false.
    - The set of all shoes I own.

24. Use existential and universal quantifiers to express the statement “No one has more than three grandmothers” using the propositional function G(x,y), which represents “x is the grandmother of y.”
    - ❌ (does not allow 0 grandmothers) $∀y∃x_1∃x_2∃x_3((G(y,x_1) ∨ G(y,x_2) ∨ G(y,x_3)) ∧ ∀z(z=x_1 ∨ z=x_2 ∨ z=x_3))$
    - ❎ $∀x¬∃a∃b∃c∃d(a≠b ∧ a≠c ∧ a≠d ∧ b≠c ∧ b≠d ∧ c≠d ∧ G(a, y) ∧ G(b, y) ∧ G(c, y) ∧ G(d, y))$

25. Use existential and universal quantifiers to express the statement “Everyone has exactly two biological parents” using the propositional function P(x, y), which represents “x is the biological parent of y.”
    - ✅ $∀x∃y∃z(y≠z ∧ P(y,x) ∧ P(z,x) ∧ ∀w(w=y ∨ w=z))$
    - ❎ $∀x∃y∃z(y≠z ∧ ∀w(P(w,x) ↔ (w=y ∨ w=z)))$

26. The quantifier ∃n denotes “there exists exactly n,” so that ∃n xP(x) means there exist exactly n values in the domain such that P(x) is true. Determine the true value of these statements where the domain consists of all real numbers.
- (a) $∃_0 x(x² = −1)$ T
- (b) $∃_1x(|x| = 0)$ T
- (c) $∃_2 x(x² = 2)$ T
- (d) $∃_3x(x = |x|)$ F

27. Express each of these statements using existential and universal quantifiers and propositional logic where ∃n is defined in Exercise 26.
- (a) $∃_0xP(x)$
  - $¬∃xP(x)$
- (b) $∃_1xP(x)$
  - ❌ $∃x∀y(P(x) ↔ x=y)$
  - ❎ $∃x(P(x) ∧ ∀y(P(y) → x=y))$
- (c) $∃_2xP(x)$
  - ❌ $∃x∃y(x≠y ∧ ∀z(P(y) → (z=x ∨ z=y)))$
  - ❎ $∃x_1∃x_2(P(x_1) ∧ P(x_2) ∧ x_1≠x_2 ∧ ∀y(P(y) → (y=x_1 ∨ y=x_2)))$
- (d) $∃_3xP(x)$
  - $∃x_1∃_x2∃_x3(P(x_1) ∧ P(x_2) ∧ P(x_3) ∧ x_1≠x_2 ∧ x_2≠x_3 ∧ x_1≠x_3 ∧ ∀y(P(y) → (y=x_1 ∨ y=x_2 ∨ y=x_3)))$

28. Let P(x, y) be a propositional function. Show that
$∃x∀yP(x, y) → ∀y∃xP(x,y)$ is a tautology.
    - The hypothesis says that there exists one element such that P is true for all elements. Then of course for all elements there exists one other such that P is true, namely the initial element.

29. Let P(x) and Q(x) be propositional functions. Show that $∃x(P(x) → Q(x))$ and $∀xP(x) → ∃xQ(x)$ always have the same truth value.
    - $∃x(P(x) → Q(x))$
    - $∀xP(x) → ∃xQ(x)$
    - ❌ The first statement means that there exists at least one element for that Q is true if P is. If this is true then stating that P is true for all x must make Q true for at least one x. If the first statement is false, which means that there is no x for which P being true implies Q, then rendering P true for all x will make the conclusion of the second statement false.
    - ❎ Suppose that $∃x(P(x) → Q(x))$ is true. Then for some x either Q(x) is true or P(x) is false. If Q(x) is true for some x, then the conditional statement $∀xP(x) → ∃xQ(x)$ is true (having true conclusion). If P(x) is false for some x, then again $∀xP(x) → ∃xQ(x)$ is true (having false hypothesis). Conversely, suppose that $∃x(P(x) → Q(x))$ is false. That means that for every x, $P(x) → Q(x)$ is false, in other words, P(x) is true and Q(x) is false. The latter implies that $∃xQ(x)$ is false. Thus $∀xP(x) → ∃xQ(x)$ has a truew hypothesis and a false conclusion and is therefore false.

30. If $∀y∃xP(x,y)$ is true, does it necessarily follow that $∃x ∀yP(x,y)$ is true?
    - $∀y∃xP(x,y)$
    - $∃x∀yP(x,y)$
    - No, as in the first statement x depends on y so x could be different for every y. The second statement means all y being the same for a given x.

31. If $∀x∃yP(x,y)$ is true, does it necessarily follow that $∃x ∀yP(x,y)$ is true?
    - $∀x∃yP(x,y)$
    - $∃x∀yP(x,y)$
    - No, the first statement says that for all x there is one y but that does not mean that there is an x for which all y make P true.

32. Find the negations of these statements.
- (a) If it snows today, then I will go skiing tomorrow.
  - ❌ If it snows today, then I wont go skiing tomorrow.
  - ❎ It will snow today, but I will not go skiing tomorrow.
- (b) Every person in this class understands mathematical induction.
  - There is a person in this class who does not understand...
- (c) Some students in this class do not like discrete mathematics.
  - All students like DM.
- (d) In every mathematics class there is some student who falls asleep during lectures.
  - There is a class in which all students stay awake.

33. Express this statement using quantifiers: “Every student in this class has taken some course in every department in the school of mathematical sciences.”
    - $∀s∀d∃cC(s,c,d)$

34. Express this statement using quantifiers: “There is a building on the campus of some college in the United States in which every room is painted white.”
    - ❌ $∃c∃b∀rW(r,b,c)$
    - ❎ W(r) room r is painted white; I(r,b) room r is in building b; L(b,u) building b is on campus of uni u
    - $∃u∃b(L(b,u) ∧ ∀r(I(r,b) → W(r)))$

35. Express the statement “There is exactly one student in this class who has taken exactly one mathematics class at this school” using the uniqueness quantifier. Then express this statement using quantifiers, without using the uniqueness quantifier.
    - $∃!x∃!yT(x,y)$
    - ❌ $∃x∃y(T(x,y) ∧ ∀a∀b(T(a,b) → a=x ∧ b=y))$
    - ❎ $∃x∀z((∃y∀w(T(z,w) ↔ w=y)) ↔ z=x)$

36. ⚠️ Describe a rule of inference that can be used to prove that there are exactly two elements x and y in a domain such that P(x) and P(y) are true. Express this rule of inference as a statement in English.
    - ❎ The hypotheses are that P (x) and P (y) are both true, that x ≠ y , and that every z that satisfies P (z) must be either x or y . The conclusion is that there are exactly two elements that make P true.

37. Use rules of inference to show that if the premises $∀x(P(x) → Q(x))$, $∀x(Q(x) → R(x))$, and $¬R(a)$, where a is in the domain, are true, then the conclusion $¬P(a)$ is true.
    1. $∀x(P(x) → Q(x))$
    1. $∀x(Q(x) → R(x))$
    1. $¬R(a)$
    1. $¬Q(x)$ univ. inst. ii, mod. tol. ii
    1. $∴ ¬P(a)$ univ. inst. i, mod. tol. i

38. Prove that if x³ is irrational, then x is irrational.
    - If $x³ ≠ \frac{a}{b}$ then $x ≠ \frac{c}{d}$
    - Contraposition: If $x = \frac{c}{d}$ then $x³ = \frac{a}{b}$
    - $(x = \frac{c}{d})³$
    - $x³ = \frac{c³}{d³}$

39. Prove that if x is irrational and x ≥ 0, then $\sqrt{x}$ is irrational.
    - $x ≠ \frac{a}{b} → \sqrt{x} ≠ \frac{c}{d}$
    - $\sqrt{x} = \frac{c}{d} → x = \frac{a}{b}$
    - $(\sqrt{x} = \frac{c}{d})²$
    - $x = \frac{c²}{d²}$

40. ❓ Prove that given a nonnegative integer n, there is a unique nonnegative integer m such that $m² ≤ n < (m + 1)²$.
    - ❎  Let m be the square root of n , rounded down if it is not a whole number. We can see that this is the unique solution in a couple of ways. First, clearly the different choices of m correspond to a partition of N , namely into {0} , {1, 2, 3} , {4, 5, 6, 7, 8} , {9, 10, 11, 12, 13, 14, 15} , ... So every n is in exactly one of these sets. Alternatively, take the square root of the given inequalities to give $m ≤ √n < m + 1$. That m is then the floor of √n (and that m is unique) follows from statement (1a) of Table 1 in Section 2.3.

41. Prove that there exists an integer m such that $m² > 10^{1000}$. Is your proof constructive or nonconstructive?
    - $m² > 10^{1000}$
    - $m > 10^{500}$
    - $m = 10^{500} + 1$

42. ❕ Prove that there is a positive integer that can be written as the sum of squares of positive integers in two different ways. (Use a computer or calculator to speed up your work.)
    - ❎ 50 = 5² + 5² = 1² + 7²
    - ❎ 65 = 4² + 7² = 1² + 8²

43. Disprove the statement that every positive integer is the sum of the cubes of eight nonnegative integers.
    - counterexample: ❌1 ❎23
    - ⭕⚠️ We look for a number that is 7 more than a small multiple of 8. Indeed, 23 will do. We can use two 8s but then would have to use seven 1s to reach 23, a total of nine numbers.

44. Disprove the statement that every positive integer is the sum of at most two squares and a cube of nonnegative integers.
    - $1, 4, 9, 16, 25, 36, 49, 64, 81, 100$
    - $1, 8, 27, 64, 125, 216, 343, 512, 729$
    - counterexample: 7

45. Disprove the statement that every positive integer is the sum of 36 fifth powers of nonnegative integers.
    - $1, 32, 243$
    - counterexmaple: ❌2 ❎223
    - ⭕⚠️ We look for a number that is 31 more than a small multiple of 32. Indeed, 23 will do. We can use six 32 but then would have to use 31 1s to reach 223, a total of 37 numbers.

46. Assuming the truth of the theorem that states that $\sqrt{n}$ is irrational whenever n is a positive integer that is not a perfect square, prove that $\sqrt{2} + \sqrt{3}$ is irrational.
    - According to the theorem both summands are clearly irrational.
    - ⭕ Contradiction: If $\sqrt{2} + \sqrt{3}$ were rational, thne so would be its square, which is $5 + 2\sqrt{6}$. Subtracting 5 and dividing by 2, then shows that $\sqrt{6}$ is rational, but this contradicts the theorem.
