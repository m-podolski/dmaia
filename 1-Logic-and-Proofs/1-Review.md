# 1 Review

1. Parts:
- (a) Define the negation of a proposition.
  - A negation inverts the truth-value of a proposition.
- (b) What is the negation of “This is a boring course”?
  - "This is not a boring course".

2. Parts:
- (a) ❕ Define (using truth tables) the disjunction, conjunction, exclusive or, conditional, and biconditional of the propositions p and q.
- (b) What are the disjunction, conjunction, exclusive or, conditional, and biconditional of the propositions “I’ll go to the movies tonight” and “I’ll finish my discrete mathematics homework”?
  - “I’ll go to the movies tonight”
  - “I’ll finish my discrete mathematics homework”
    - disj.: "I'll go to the movies tonight OR I'll finish..."
    - conj.: "I'll go to the movies tonight AND I'll finish...
    - xor: "EITHER I'll go to the movies OR I'll finish..."
    - cond.: "If I'll go to the movies tonight, then I'll finish..."
    - bicond.: "I'll go to the movies tonight if and only if I'll finish..."

3. Parts:
- (a) Describe at least five different ways to write the conditional statement p → q in English.
  - If p, then q
  - q whenever p
  - p is sufficient for q
  - p, only if q
  - ❌ p is necessary for q
  - ❎ q is necessary for p
- (b) Define the converse and contrapositive of a conditional statement.
  - converse: A conditional with "swapped" hypothesis and conclusion.
  - contrapositive: A conditional statement that hase the negated conclusion of another one as hypothesis and the negated hypothesis as its conclusion.
- (c) State the converse and the contrapositive of the conditional statement “If it is sunny tomorrow, then I will go for a walk in the woods.”
  - converse: "if I go for a walk in the woods, then it will be sunny tomorrow."
  - contrap.: "If i dont go for a walk in the woods, it wont be sunny tomorrow."

4. Parts:
- (a) What does it mean for two propositions to be logically equivalent?
  - ❌ The propositions will have the same truth value for all truth-values of their contained propositions.
  - ❎ The compound propositions p and q are called logically equivalent if p ↔ q is a tautology.
- (b) Describe the different ways to show that two compound propositions are logically equivalent.
  - Constructing truth-tables.
  - Inferring the equivalence stepwise using established equivalences or establishing new ones for intermediary steps.
- (c) Show in at least two different ways that the compound propositions ¬p ∨ (r → ¬q) and ¬p ∨ ¬q ∨ ¬r are equivalent.
  - ❕ Truth tables
  - ⭕ r → ¬q ≡ ¬p ∨ ¬q ∨ ¬r

5. (Depends on the Exercise Set in Section 1.3)
- (a) Given a truth table, explain how to use disjunctive normal form to construct a compound proposition with this truth table.
  - By considering the truth-values of the variables in each row a conjunction of variables or their negations can be obtained. By chaining the compound propositions with disjunctions the resulting proposition covers all cases of truth values.
- (b) Explain why part (a) shows that the operators ∧, ∨, and ¬ are functionally complete.
  - As every possible combination of truth-values can be expressed in DNF (using only the above operators) it follows that every compound-proposition can be expressed with these operator-set.
- (c) Is there an operator such that the set containing just this operator is functionally complete?
  - Yes, the NAND and NOR operators are sufficient as the DNF can be transformed using only OR or AND by DeMorgans laws and the remaining negation and disjunction/conjunction are then equivalent expressions using only NAND/NOR.

6. What are the universal and existential quantifications of a predicate P(x)? What are their negations?
   - $∀x P(x)$: $∃x ¬P(x)$
   - $∃x P(x)$: $∀x ¬P(x)$

7. Parts:
- (a) What is the difference between the quantification $∃x∀yP(x, y)$ and $∀y∃xP(x, y)$, where P(x,y) is a predicate?
  - In $∃x∀yP(x, y)$ the universal quantification is dependend on the existential one: "There exists one x, such that for all y...". In $∀y∃xP(x, y)$ its the other way around: "For all y there exists an x, such that..."
- (b) Give an example of a predicate P(x,y) such that $∃x∀yP(x,y)$ and $∀y∃xP(x,y)$ have different truth values.
  - ❌ P: "Student x has taken course y".
  - ❎ x+y=0 (1.5/Ex.4)

8. Describe what is meant by a valid argument in propositional logic and show that the argument “If the earth is flat, then you can sail off the edge of the earth,” “You cannot sail off the edge of the earth,” therefore, “The earth is not flat” is a valid argument.
   - ⭕ An argument is valid if and only if it is impossible for its conclusion to be false if all the premises are true.
   - The first statement establishes a conclusion that is negated by the second one. So by modus tollens the last statement being the negation of the hypothesis of the first one, must be true.

9. Use rules of inference to show that if the premises “All zebras have stripes” and “Mark is a zebra” are true, then the conclusion “Mark has stripes” is true.
    - By universal instantiation the first statement becomes "If someone is a zebra, he or she has stripes". The second statement confirms the hypothesis, therefore, by modus ponens, the third statement is true.

10. Parts:
- (a) Describe what is meant by a direct proof, a proof by contraposition, and a proof by contradiction of a conditional statement p → q.
  - A direct proof starts from the given propositions/hypothesis and constructs inferences until the desired conlusion is reached.
  - A proof by contraposition tries to prove the contraposed original hypothesis and conclusion, therefore starting with the negated conclusion as hypothesis.
  - A proof by contradiction negates the original statement and then works toward the conclusion, trying to find a contradictory statement that shows that the negated statement must have been true.
- (b) Give a direct proof, a proof by contraposition and a proof by contradiction of the statement: “If n is even, then n + 4 is even.”
  - direct: $n = 2k$ and $n+4 = 2k+4 = 2(k+2)$
  - contrapos.: $n+4 = 2k+1$, then $n = 2k-3 = 2(k-2)+1$
  - contradic.: $n = 2k$, then $2k+4 = 2j+1$, ❌ $2k = 2j-3 = 2(j-2)+1$ ⭕ $4 = 2(j-k)+1$

11. Parts:
- (a) Describe a way to prove the biconditional p ↔ q.
  - $p ↔ q ≡ (p→q) ∧ (q→p)$
- (b) Prove the statement: “The integer 3n + 2 is odd if and only if the integer 9n + 5 is even, where n is an integer.”
  - p→q: if $3n+2 = 2k+1$, then $9n+5 = 2l$
    - $9n+6 = 6k+3$
    - $9n+5 = 6k+2 = 2(3k+1)$
  - q→p: ❌ if $9n+5 = 2l$, then $3n+2 = 2k+1$
    - $3n+5/3 = 2/3l$
    - $3n+2 = 2/3l+1/3 = 2(1/3l)+1/3$
    - ❎ use contraposition of converse: $3n+2 = 2k$, then  $9n+5 = 6k-1 = 2(3k-1)+1$

12. To prove that the statements p1, p2, p3, and p4 are equivalent, is it sufficient to show that the conditional statements p4 → p2, p3 → p1, and p1 → p2 are valid? If not, provide another collection of conditional statements that can be used to show that the four statements are equivalent.
    - No, but by swapping p1 → p2 for p2 → p3 and adding p1 → p4 a complete proof would be possible.

13. Parts:
- (a) Suppose that a statement of the form ∀xP(x) is false. How can this be proved?
  - By finding a counterexample/using a constructive existence-proof for ¬P(x).
- (b) Show that the statement “For every positive integer n, $n² ≥ 2n$” is false.
  - 1 is a counterexample.

14. What is the difference between a constructive and nonconstructive existence proof? Give an example of each.
    - A constructive existence proof finds an object for which a proposition is true. An example would be the found counterexample from 13 above.
    - A nonconstructive EP shows that one of two (or more) possibilities must be true where each one fulfills the proposition. ⭕ P.97/Example 11.

15. What are the elements of a proof that there is a unique element x such that P(x), where P(x) is a propositional function?
    - showing the existence of x such that P(x)
    - showing that there is only one x such that P(x)

16. Explain how a proof by cases can be used to prove a result about absolute values, such as the fact that |xy| = |x||y| for all real numbers x and y.
    - A proof by cases woul consider the numbers x and y with regard to them being nonnegative or not as this
    - ⭕ P.94/Example 4
