# 1.1 Propositional Logic

1. Which of these sentences are propositions? What are the
truth values of those that are propositions?

    - (a) Boston is the capital of Massachusetts.
        - Yes, T
    - (b) Miami is the capital of Florida.
        - Yes, F
    - (c) 2 + 3 = 5.
        - T
    - (d) 5 + 7 = 10.
        - F
    - (e) x + 2 = 11.
        - No
    - (f) Answer this question.
        - No

3. What is the negation of each of these propositions?
    - (a) Mei has an MP3 player. -> does not have
    - (b) There is no pollution in New Jersey. -> there is pollution
    - (c) 2 + 1 = 3. -> $2 +1 \ne 3$
    - (d) The summer in Maine is hot and sunny. -> is not

5. What is the negation of each of these propositions?
    - (a) Steve has more than 100 GB free disk space on his laptop.
        - does not have
    - (b) Zach blocks e-mails and texts from Jennifer.
        - Zach does not block emails and texts...; Zach does not block emails OR does not block texts...
    - (c) 7 · 11 · 13 = 999.
        - $7 · 11 · 13 \ne 999$
    - (d) Diane rode her bicycle 100 miles on Sunday.
        - did not ride...; Diane did not ride it at 100 miles OR not on Sunday

7. Suppose that during the most recent fiscal year, the an-
nual revenue of Acme Computer was 138 billion dollars
and its net profit was 8 billion dollars, the annual revenue
of Nadir Software was 87 billion dollars and its net profit
was 5 billion dollars, and the annual revenue of Quixote
Media was 111 billion dollars and its net profit was
13 billion dollars. Determine the truth value of each of
these propositions for the most recent fiscal year.
**Acme: r=138, p=8
Nadir: r=87, p=5
Quixote: r=111, p=13**

- (a) Quixote Media had the largest annual revenue.
  - F
- (b) Nadir Software had the lowest net profit and Acme Computer had the largest annual revenue.
  - T
- (c) Acme Computer had the largest net profit or Quixote Media had the largest net profit.
  - T
- (d) If Quixote Media had the smallest net profit, then Acme Computer had the largest annual revenue.
  - T
- (e) Nadir Software had the smallest net profit if and only if Acme Computer had the largest annual revenue.
  - $T \iff T$ is T

9. Let p and q be the propositions “Swimming at the New
Jersey shore is allowed” and “Sharks have been spotted
near the shore,” respectively. Express each of these com-
pound propositions as an English sentence.

- (a) ¬q
  - No sharks have been spotted
- (b) p ∧ q
  - Swimming is allowed and sharks have been spotted
- (c) ¬p ∨ q
  - Swimming is not allowed or sharks have been spotted
- (d) p → ¬q
  - If Swimming is allowed, then no sharks have been spotted
- (e) ¬q → p
  - If sharks have not been spotted near the shore, then swimming at the New Jersey shore is allowed.
- (f) ¬p → ¬q
  - If swimming is not allowed, then no sharks have been spotted
- (g) p ↔ ¬q
  - Only if Swimming is allowed no sharks have been spotted
- (h) ¬p ∧ (p ∨ ¬q)
  - Swimming is not allowed and either swimming is or no sharks have been spotted

11. Let p and q be the propositions
p : It is below freezing.
q : It is snowing.
Write these propositions using p and q and logical con- nectives (including negations).

- (a) It is below freezing and snowing.
  - $p \land q$
- (b) It is below freezing but not snowing.
  - $p \land \neg q$
- (c) It is not below freezing and it is not snowing.
  - $\neg p \land \neg q$
- (d) It is either snowing or below freezing (or both).
  - $p \lor q$
- (e) If it is below freezing, it is also snowing.
  - $p \implies q$
- (f) Either it is below freezing or it is snowing, but it is not snowing if it is below freezing.
  - $(p \lor q) \land (p \implies \neg q)$
- (g) That it is below freezing is necessary and sufficient for it to be snowing.
  - $p \iff q$

13. Let p and q be the propositions
p : You drive over 65 miles per hour.
q : You get a speeding ticket.
Write these propositions using p and q and logical con-
nectives (including negations).

- (a) You do not drive over 65 miles per hour.
  - $\neg p$
- (b) You drive over 65 miles per hour, but you do not get a speeding ticket.
  - $p \land \neg q$
- (c) You will get a speeding ticket if you drive over 65 miles per hour.
  - $p \implies q$
- (d) If you do not drive over 65 miles per hour, then you will not get a speeding ticket.
  - $\neg p \implies \neg q$
- (e) Driving over 65 miles per hour is sufficient for getting a speeding ticket.
  - $p \implies q$
- (f ) You get a speeding ticket, but you do not drive over 65 miles per hour.
  - $q \land \neg p$
- (g) Whenever you get a speeding ticket, you are driving over 65 miles per hour.
  - $q \implies p$

15. Let p, q, and r be the propositions
p : Grizzly bears have been seen in the area.
q : Hiking is safe on the trail.
r : Berries are ripe along the trail.
Write these propositions using p, q, and r and logical
connectives (including negations).

- (a) Berries are ripe along the trail, but grizzly bears have not been seen in the area.
  - $r \land \neg p$
- (b) Grizzly bears have not been seen in the area and hik- ing on the trail is safe, but berries are ripe along the trail.
  - $\neg p \land q \land r$
- (c) If berries are ripe along the trail, hiking is safe if and only if grizzly bears have not been seen in the area.
  - $r \implies (q \iff \neg p)$
- (d) It is not safe to hike on the trail, but grizzly bears have not been seen in the area and the berries along the trail are ripe.
  - $\neg q \land \neg p \land r$
- (e) For hiking on the trail to be safe, it is necessary but not sufficient that berries not be ripe along the trail and for grizzly bears not to have been seen in the area.
  - !!! $(\neg r \land \neg p) \implies q$
  - $(q \implies (\neg r \land \neg p)) \land \neg((\neg r \land \neg p) \implies q)$
- (f) Hiking is not safe on the trail whenever grizzly bears have been seen in the area and berries are ripe along the trail.
  - $(p \land r) \implies \neg q$

17. Determine whether each of these conditional statements
is true or false.

- (a) If 1 + 1 = 2, then 2 + 2 = 5.
  - F: $T \implies F$
- (b) If 1 + 1 = 3, then 2 + 2 = 4.
  - T: $F \implies T$
- (c) If 1 + 1 = 3, then 2 + 2 = 5.
  - T: $F \implies F$
- (d) If monkeys can fly, then 1 + 1 = 3.
  - T: $F \implies F$

19. For each of these sentences, determine whether an inclusive or, or an exclusive or, is intended. Explain your answer.

- (a) Coffee or tea comes with dinner.
  - XOR: dinner comes with one beverage
- (b) A password must have at least three digits or be at least eight characters long.
  - OR: two conditions which enable security by themselves
- (c) The prerequisite for the course is a course in number theory or a course in cryptography.
  - OR: one course is sufficient
- (d) You can pay using U.S. dollars or euros.
  - XOR/OR: payment in two currencies doesnt make sense

21. For each of these sentences, state what the sentence means if the logical connective or is an inclusive or (that is, a dis- junction) versus an exclusive or. Which of these meanings of or do you think is intended?

- (a) To take discrete mathematics, you must have taken calculus or a course in computer science.
  - OR: both parts are suffient conditions, otherwise students which have taken both would be excluded
- (b) When you buy a new car from Acme Motor Company, you get $2000 back in cash or a 2% car loan.
  - XOR: the customer gets either one benefit or the other but certainly not both
- (c) Dinner for two includes two items from column A or three items from column B.
  - XOR: as the choice is limited for the customer, otherwise the customer wouldnt know which selection he gets
- (d) School is closed if more than 2 feet of snow falls or if the wind chill is below −100.
  - OR: two separateely sufficent conditions, otherwise both occuring at the same time would not cause the school to be closed

23. Write each of these statements in the form “if p, then q” in English. [Hint: Refer to the list of common ways to express conditional statements.]

- (a) It snows whenever the wind blows from the northeast.
  - if the wind blows ... , then it snows
- (b) The apple trees will bloom if it stays warm for a week.
  - if it stays warm ... , then the trees bloom
- **(c) That the Pistons win the championship implies that they beat the Lakers.**
  - !!! if they beat the Lakers ... the Pistons win
  - If the Pistons win ...
- **(d) It is necessary to walk 8 miles to get to the top of Long’s Peak.**
  - !!! If you walk 8 miles, then you get to the top ...
  - If you get to the top ... , then you must have walked ...
- (e) To get tenure as a professor, it is sufficient to be world- famous.
  - If one is world-famous, then one can get a tenure ...
- (f) If you drive more than 400 miles, you will need to buy gasoline.
  - (same)
- **(g) Your guarantee is good only if you bought your CD player less than 90 days ago.**
  - !!! if you baught ... , then your guarantee is good
  - If your guarantee is good ...
- (h) Jan will go swimming unless the water is too cold.
  - If the water is not too cold, then Jan will ...

25. Write each of these propositions in the form “p if and only if q” in English.

- (a) If it is hot outside you buy an ice cream cone, and if you buy an ice cream cone it is hot outside.
  - you buy an ice-cream cone if and only if it is hot outside
- (b) For you to win the contest it is necessary and sufficient that you have the only winning ticket.
  - You win the contest if and only if you have the winning ticket.
- (c) You get promoted only if you have connections, and you have connections only if you get promoted.
  - You get promoted if and only if you have connections
- (d) If you watch television your mind will decay, and con- versely.
  - Your mind will decay if and only if ...
- (e) The trains run late on exactly those days when I take it.
  - The train runs late if and only if I take it

27. State the converse, contrapositive, and inverse of each of
these conditional statements.

- (a) If it snows today, I will ski tomorrow.
  - C: If I will ski tomorrow, it snows today. / *I will ski tomorrow only if it snows today.*
  - CP: If I dont ski tomorrow, it wont have snowed today.
  - I: If it doesnt snow today, I wont ski tomorrow.
- (b) I come to class whenever there is going to be a quiz.
  - C: If I come to class, there is going to be a quiz.
  - CP: If I dont come to class, there isnt going to be a quiz.
  - I: I there isnt going to be a quiz, I dont come to class.
- (c) A positive integer is a prime only if it has no divisors other than 1 and itself.
  - C: If a positive int has no divisors ... , then it is a prime
  - CP: If a positive int has divisors ... , then it is not a prime
  - I: If a positive int is not a prime, then it has divisors ...

29. How many rows appear in a truth table for each of these compound propositions?

- (a) p → ¬p
- (b) (p ∨ ¬r) ∧ (q ∨ ¬s)
- (c) q ∨ p ∨ ¬s ∨ ¬r ∨ ¬t ∨ u
- (d) (p ∧ r ∧ t) ↔ (q ∧ t)

31. Construct a truth table for each of these compound propositions.

- **(a) p ∧ ¬p**
$$
\begin{array}{|c|c|}
p & p \lor \neg p\\
\hline
T & F\\
F & F\\
\end{array}
$$
- **(b) p ∨ ¬p**
$$
\begin{array}{|c|c|}
p & p \lor \neg p\\
\hline
T & T\\
F & T\\
\end{array}
$$
- (c) (p ∨ ¬q) → q
$$
\begin{array}{|c c|c|}
p & q & (p \lor \neg q) \implies q\\
\hline
T & T & T\\
T & F & F\\
F & T & T\\
F & F & F\\
\end{array}
$$
- (d) (p ∨ q) → (p ∧ q)
$$
\begin{array}{|c c|c|}
p & q & (p \lor q) \implies (p \land q)\\
\hline
T & T & T\\
T & F & F\\
F & T & F\\
F & F & T\\
\end{array}
$$
- (e) (p → q) ↔ (¬q → ¬p)
$$
\begin{array}{|c c|c|}
p & q & (p \implies q) \iff (\neg q \implies \neg p)\\
\hline
T & T & T\\
T & F & T\\
F & T & T\\
F & F & T\\
\end{array}
$$
- (f) (p → q) → (q → p)
$$
\begin{array}{|c c|c|}
p & q & (p \implies q) \implies (q \implies p)\\
\hline
T & T & T\\
T & F & T\\
F & T & F\\
F & F & T\\
\end{array}
$$

33. Construct a truth table for each of these compound propo- sitions.

- (a) (p ∨ q) → (p ⊕ q)
$$
\begin{array}{|c c|c|c|c|}
p & q & p \lor q & p \oplus q & (p \lor q) \implies (p \oplus q)\\
\hline
T & T & T & F & F\\
T & F & T & T & T\\
F & T & T & T & T\\
F & F & F & F & T\\
\end{array}
$$
- (b) (p ⊕ q) → (p ∧ q)
$$
\begin{array}{|c c|c|}
p & q & (p \oplus q) \implies (p \land q)\\
\hline
T & T & T\\
T & F & F\\
F & T & F\\
F & F & T\\
\end{array}
$$
- (c) (p ∨ q) ⊕ (p ∧ q)
$$
\begin{array}{|c c|c|}
p & q & (p \lor q) \oplus (p \land q)\\
\hline
T & T & F\\
T & F & T\\
F & T & T\\
F & F & F\\
\end{array}
$$
- (d) (p ↔ q) ⊕ (¬p ↔ q)
$$
\begin{array}{|c c|c|}
p & q & (p \iff q) \oplus (\neg p \iff q)\\
\hline
T & T & T\\
T & F & T\\
F & T & T\\
F & F & T\\
\end{array}
$$
- (e) (p ↔ q) ⊕ (¬p ↔ ¬r)
$$
\begin{array}{|c c c|c|}
p & q & r & (p \iff q) \oplus (\neg p \iff \neg r)\\
\hline
T & T & T & F\\
T & T & F & T\\
T & F & T & T\\
T & F & F & F\\
F & T & T & F\\
F & T & F & T\\
F & F & T & T\\
F & F & F & F\\
\end{array}
$$
- (f ) (p ⊕ q) → (p ⊕ ¬q)
$$
\begin{array}{|c c|c|}
p & q & (p \oplus q) \implies (p \oplus \neg q)\\
\hline
T & T & T\\
T & F & F\\
F & T & F\\
F & F & T\\
\end{array}
$$

41. Explain, without using a truth table, why (p ∨ q ∨ r) ∧ (¬p ∨ ¬q ∨ ¬r) is true when at least one of p, q, and r is true and at least one is false, but is false when all three variables have the same truth value.
$(p ∨ q ∨ r) ∧ (¬p ∨ ¬q ∨ ¬r)$
    - As this is an inclusive conjunction, both parens have to be true. Both top-level-propositions are composed of the propositions and their negations connected by inclusive ors. That means using the same truth value for all propositions will lead to either side being false, therefore the top-level-and will be false. By introducing at least one proposition with a different truth-value the failing parens-expression will now have at least one true propositon which is sufficient for it to evaluate to true because it uses inclusive ors.

45. The truth value of the negation of a proposition in fuzzy logic is 1 minus the truth value of the proposition. What are the truth values of the statements “Fred is not happy” and “John is not happy?”
    - 0.2 and 0.6

47. The truth value of the disjunction of two propositions in fuzzy logic is the maximum of the truth values of the two propositions. What are the truth values of the statements “Fred is happy, or John is happy” and “Fred is not happy, or John is not happy?”
    - 0.8 and 0.6

49. **(*) The nth statement in a list of 100 statements is “Exactly n of the statements in this list are false.”**

- (a) What conclusions can you draw from these state- ments?
  - The last statement (n=100) will tell you that all statements in the list are false.
- (b) Answer part (a) if the nth statement is “At least n of the statements in this list are false.”
  - the same as above.
- (c) Answer part (b) assuming that the list contains 99 statements.
  - the same as above.
