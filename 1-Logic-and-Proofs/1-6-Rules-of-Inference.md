# 1.6 Rules of Inference

1. Find the argument form for the following argument and determine whether it is valid. Can we conclude that the conclusion is true if the premises are true?

    - Yes, it is the modus ponens

$$
\begin{align*}
    & && \text{If Socrates is human, then Socrates is mortal.} \\
    & && \text{Socrates is human.} \\
    & && \rule[0.5ex]{7cm}{0.5pt} \\
    & ∴ && \text{Socrates is mortal.}
\end{align*}
$$

$$
\begin{align*}
    & && h → m \\
    & && h \\
    & ∴ && m
\end{align*}
$$

2. Find the argument form for the following argument and determine whether it is valid. Can we conclude that the conclusion is true if the premises are true?

    - $(¬l → ¬s) ∧ s → l$
    - ❎ Yes, it is a tautology.

$$
\begin{align*}
    & && \text{If George does not have eight legs, then he is not a spider.} \\
    & && \text{George is a spider.} \\
    & && \rule[0.5ex]{7cm}{0.5pt} \\
    & ∴ && \text{George has eight legs.}
\end{align*}
$$

$$
\begin{align*}
    & && ¬l → ¬s \\
    & && s \\
    & ∴ && l
\end{align*}
$$

3. What rule of inference is used in each of these arguments?
- (a) Alice is a mathematics major. Therefore, Alice is either a mathematics major or a computer science major.
  - Addition
- (b) Jerry is a mathematics major and a computer science major. Therefore, Jerry is a mathematics major.
  - Simplification
- (c) If it is rainy, then the pool will be closed. It is rainy. Therefore, the pool is closed.
  - Modus ponens
- (d) If it snows today, the university will close. The university is not closed today. Therefore, it did not snow today.
  - Modus tollens
- (e) If I go swimming, then I will stay in the sun too long. If I stay in the sun too long, then I will sunburn. Therefore, if I go swimming, then I will sunburn.
  - Hypothetical syllogism

4. What rule of inference is used in each of these arguments?
- (a) Kangaroos live in Australia and are marsupials. Therefore, kangaroos are marsupials.
  - Simplification
- (b) It is either hotter than 100 degrees today or the pollution is dangerous. It is less than 100 degrees outside today. Therefore, the pollution is dangerous.
  - Disjunctive syllogism
- (c) Linda is an excellent swimmer. If Linda is an excellent swimmer, then she can work as a lifeguard. Therefore, Linda can work as a lifeguard.
  - Modus ponens
- (d) Steve will work at a computer company this summer. Therefore, this summer Steve will work at a computer company or he will be a beach bum.
  - Addition
- (e) If I work all night on this homework, then I can answer all the exercises. If I answer all the exercises, I will understand the material. Therefore, if I work all night on this homework, then I will understand the material.
  - Hypothetical syllogism

5. Use rules of inference to show that the hypotheses “Randy works hard,” “If Randy works hard, then he is a dull boy,” and “If Randy is a dull boy, then he will not get the job” imply the conclusion “Randy will not get the job.”
    - $w ∧ (w → d) ∧ (d → ¬j) → ¬j$
    - $w ∧ (w → d) → d$ modus ponens
    - $d ∧ (d → ¬j) → ¬j$ modus ponens

6. Use rules of inference to show that the hypotheses “If it does not rain or if it is not foggy, then the sailing race will be held and the lifesaving demonstration will go on,” “If the sailing race is held, then the trophy will be awarded,” and “The trophy was not awarded” imply the conclusion “It rained.”
    1. $s → t$
    1. $¬t$
    1. $¬s$ modus tollens
    1. $(¬r ∨ ¬f) → (s ∧ l)$
    1. ❎ $¬(s ∧ l)$ 3
    1. ❎ $¬(¬r ∨ ¬f)$ modus tollens
    1. $r ∧ f$ De Morgans law
    1. $r$ simplification

7. What rules of inference are used in this famous argument? “All men are mortal. Socrates is a man. Therefore, Socrates is mortal.”
   - universal instantiation

8. What rules of inference are used in this argument? “No man is an island. Manhattan is an island. Therefore, Manhattan is not a man.”
    - ❎ First a negatated existential instatiation; "There is no x that is an island". It follows that if something is an island, then it is not a man. Combining this by modus ponens with "Manhattan is an island" the conclusion is "Manhattan is not a man"

9. For each of these collections of premises, what relevant conclusion or conclusions can be drawn? Explain the rules of inference used to obtain each conclusion from the premises.
- **(a) “If I take the day off, it either rains or snows.” “I took Tuesday off or I took Thursday off.” “It was sunny on Tuesday.” “It did not snow on Thursday.”**
- (b) “If I eat spicy foods, then I have strange dreams.” “I have strange dreams if there is thunder while I sleep.” “I did not have strange dreams.”
  - By using modus tollens on both conditionals we can conclude that neither I ate spicy foods nor there was thunder.
- (c) “I am either clever or lucky.” “I am not lucky.” “If I am lucky, then I will win the lottery.”
  - First a disjunctive syllogism tells us that "I am clever" *Secondly, the second conditional is equivalent to "I am not lucky or I will win the lottery".*
- (d) “Every computer science major has a personal computer.” “Ralph does not have a personal computer.” “Ann has a personal computer.”
  - First universal instantiation of the given conditional gives us "If Ralph/Ann is a CS major, then he has a PC". Combining the case "Ralph" with the second statement by modus tollens, it follows that "Ralph is not a CS major". For "Ann" no definite conclusion can be drawn.
- (e) “What is good for corporations is good for the United States.” “What is good for the United States is good for you.” “What is good for corporations is for you to buy lots of stuff.”
  - The first statement equals the universally quantified conditional "If x is good for corporations, then it is good for the US". The second equals "If x is good for the US, then it is good for you." The third can be used to instantiate the first conditional as "If you buying lots of stuff is good for corporations, buying lots of stuff is good for the US". ❎ Extending this by a hypothetical syllogism to the second statement, the conclusion is "If you buying lots of stuff is good for corporations, then it is good for you."
- (f) “All rodents gnaw their food.” “Mice are rodents.” “Rabbits do not gnaw their food.” “Bats are not rodents.”
  - "If x is a rodent, then x gnaws its food",
  - instantiate with "Mice" -> "Mice gnaw their food"
  - ❌ instantiate with "bats" -> "Bats dont gnaw their food"
  - instantiate with "rabbits" -> modus tollens -> "rabbits are not rodents"

10. For each of these sets of premises, what relevant conclusion or conclusions can be drawn? Explain the rules of inference used to obtain each conclusion from the premises.
- (a) “If I play hockey, then I am sore the next day.” “I use the whirlpool if I am sore.” “I did not use the whirlpool.”
  - modus tollens: "I am not sore (today)"
  - ❌ universal instantiation: "If I play(ed) hockey (yesterday), then I am sore (today)"
  - modus tollens: "I did not play hockey (yesterday)"
- (b) “If I work, it is either sunny or partly sunny.” “I worked last Monday or I worked last Friday.” “It was not sunny on Tuesday.” “It was not partly sunny on Friday.”
  - no conclusions
- (c) “All insects have six legs.”
“Dragonflies are insects.”
“Spiders do not have six legs.”
“Spiders eat dragonflies.”
  - universal instatiation, modus ponens: "Dragonflies have six legs"
  - univ. inst., mod. tollens: "Spiders are not insects"
  - ⭕ existential generalization: "there exists a non-six-legged creature that eats a six-legged creature, and that there exists a non-insect that eats an insect"
- (d) “Every student has an Internet account.”
“Homer does not have an Internet account.”
“Maggie has an Internet account.”
  - univ. inst., modus tollens: "Homer is not a student"
  - ❌ univ. inst., modus ponens: "Maggie is a student"
- (e)
“All foods that are healthy to eat do not taste good.”
“Tofu is healthy to eat.”
“Cheeseburgers are not healthy to eat.”
“You only eat what tastes good.”
“You do not eat tofu.”
  - univ. inst., modus ponens: "Tofu does not taste good" (other way possible)
- **(f) “I am either dreaming or hallucinating.” “I am not dreaming.” “If I am hallucinating, I see elephants running down the road.”**
  - ❌ simplification: "I am not hallucinating"
  - ❌ equiv.: "I am not hallucinating or I see elephants"
  - ❌ simplification: "I see elephants"
  - simplification: "I am hallucinating"
  - mod. ponens: "I see elephants"

11. Show that the argument form with premises p1 , p2 , . . . , pn and conclusion q → r is valid if the argument form with premises p1 , p2 , . . . , pn , q, and conclusion r is valid.

12. Show that the argument form with premises (p ∧ t) → (r ∨ s), q → (u ∧ t), u → p, and ¬s and conclusion q → r is valid by first using Exercise 11 and then using rules of inference from Table 1.
    - according to ex. 11 conclusion r is valid when q is added to the premises. Which gives us:
    1. $q → (u ∧ t)$ Premise
    1. $q$ Premise
    1. $u ∧ t$ modus ponens i,ii
    1. $u$ simplification iii
    1. $u → p$ Premise
    1. $p$ modus ponens iv,v
    1. $(p ∧ t) → (r ∨ s)$ Premise
    1. $r ∨ s$ simplification iii, modus ponens vi,vii
    1. $¬s$ Premise
    1. $r$ disjunctive syll. viii,ix

13. For each of these arguments, explain which rules of inference are used for each step.
- (a) ❓ “Doug, a student in this class, knows how to write programs in JAVA. Everyone who knows how to write programs in JAVA can get a high-paying job. Therefore, someone in this class can get a high-paying job.”

- (b)
Somebody in this class enjoys whale watching.
Every person who enjoys whale watching cares about ocean pollution.
Therefore, there is a person in this class who cares about ocean pollution.
  1. $∃x(C(x) ∧ W(x))$  Premise
  1. $C(a) ∧ W(a)$      exist. inst.
  1. $W(a)$             simplification ii
  1. $∀x(W(x) → P(x))$  Premise
  1. $W(a) → P(a)$      univ. inst.
  1. $P(a)$             modus ponens iii, iv
  1. $C(a)$             simplification ii
  1. $C(a) ∧ P(a)$      conjunction vi, vii
  1. $∃x(C(x) ∧ P(x))$  exist. gen. Conclusion

- (c) ❎ “Each of the 93 students in this class owns a personal computer. Everyone who owns a personal computer can use a word processing program. Therefore, Zeke, a student in this class, can use a word processing program.”
  1. $∀x(C(x) → P(x))$    Premise
  1. $C(a) → P(a)$        univ. inst i
  1. $∀x(P(x) → W(x))$    Premise
  1. $P(a) → W(a)$        univ. inst iii
  1. $C(a) → W(a)$        hypoth. syll. ii, iv
  1. $C(a)$               Premise
  1. $W(a)$               Conclusion mod. ponens

- (d) ❎ “Everyone in New Jersey lives within 50 miles of the ocean. Someone in New Jersey has never seen the ocean. Therefore, someone who lives within 50 miles of the ocean has never seen the ocean.”
  1. $∀x(J(x) → F(x))$    Premise
  1. $J(a) → F(a)$        univ. inst. i
  1. $∃x(J(x) ∧ ¬S(x))$   Premise
  1. $J(a) ∧ ¬S(a)$       exist. inst. iii
  1. $J(a)$               simp. iv
  1. $F(a)$               mod. pon. ii, v
  1. $F(a) ∧ ¬S(a)$       simp. iv; conjunction vi
  1. $∃x(F(x) ∧ ¬S(x))$   Conclusion exist. gen.

14. For each of these arguments, explain which rules of inference are used for each step.
- (a) “Linda, a student in this class, owns a red convertible. Everyone who owns a red convertible has gotten at least one speeding ticket. Therefore, someone in this class has gotten a speeding ticket.”
  1. $S(l) ∧ C(l)$        Premise
  1. $∀x(C(x) → T(x))$    Premise
  1. $C(l) → T(l)$        univ. inst. ii
  1. $T(l)$               simp. i; mod. pon. iii
  1. $T(l) ∧ C(l)$        simp. i; conj iv
  1. ❌ $∃x(C(x) ∧ T(x))$    Conclusion; exist. gen.

- (b) “Each of five roommates, Melissa, Aaron, Ralph, Veneesha, and Keeshawn, has taken a course in discrete mathematics. Every student who has taken a course in discrete mathematics can take a course in algorithms. Therefore, all five roommates can take a course in algorithms next year.”
  <!-- 1. ❌ $∀x(d(x))$           Premise -->
  1. $∀x(r(x) → d(x))$       Premise
  1. $r(a) → d(a)$           univ. inst. i
  1. $∀x(d(x) → a(x))$       Premise
  1. $d(a) → a(a)$           univ. inst. iii
  1. $r(a) → a(a)$           hypoth. syll. ii, iv
  1. $∀x(r(x) → a(x))$       Conclusion; univ. gen. v

- (c) “All movies produced by John Sayles are wonderful. John Sayles produced a movie about coal miners. Therefore, there is a wonderful movie about coal miners.”
  1. $∀x(s(x) → w(x))$    Premise
  1. $s(m) → w(m)$        univ. inst. i
  1. $∃x(s(x) ∧ c(x))$    Premise
  1. $s(m) ∧ c(m)$        exist. inst. iii
  1. $w(m)$               simp. iv; mod. pon. ii
  1. $w(m) ∧ c(m)$        simp. iv; conj. v
  1. $∃x(w(x) ∧ c(x))$    Conclusion; exist. gen.

- (d) ❕ “There is someone in this class who has been to France. Everyone who goes to France visits the Louvre. Therefore, someone in this class has visited the Louvre.”
  1. $∃x(c(x) ∧ f(x))$    Premise
  1. $∀x(f(x) → l(x))$    Premise
  1. $∃x(c(x) ∧ l(x))$    Premise

15. For each of these arguments determine whether the argument is correct or incorrect and explain why.
- (a) ❓All students in this class understand logic. Xavier is a student in this class. Therefore, Xavier understands logic.
- (b) Every computer science major takes discrete mathematics. Natasha is taking discrete mathematics. Therefore, Natasha is a computer science major.
  - Incorrect, The second statement cannot be used to draw a conclusion from the universal instatntiation of the first one.
- (c) All parrots like fruit. My pet bird is not a parrot. Therefore, my pet bird does not like fruit.
  - Incorrect, fallacy of denying the hypothesis.
- (d) Everyone who eats granola every day is healthy. Linda is not healthy. Therefore, Linda does not eat granola every day.
  - Correct, first univ. inst, then modus tollens

16. For each of these arguments determine whether the argument is correct or incorrect and explain why.
- (a) Everyone enrolled in the university has lived in a dormitory. Mia has never lived in a dormitory. Therefore, Mia is not enrolled in the university.
  - Correct by univ. inst. and modus tollens.
- (b) A convertible car is fun to drive. Isaac’s car is not a convertible. Therefore, Isaac’s car is not fun to drive.
  - Incorrect, fallcy of denying the hypothesis.
- (c) Quincy likes all action movies. Quincy likes the movie Eight Men Out. Therefore, Eight Men Out is an action movie.
  - Incorrect, fallacy of affirming the conclusion.
- (d) All lobstermen set at least a dozen traps. Hamilton is a lobsterman. Therefore, Hamilton sets at least a dozen traps.
  - Correct by univ. inst. and modus ponens.

17. What is wrong with this argument? Let $H(x)$ be “x is happy.” Given the premise $∃xH(x)$, we conclude that $H(Lola)$. Therefore, Lola is happy.
    - There is no way of knowing that the existing happy person is indeed Lola and not anyone else.

18. What is wrong with this argument? Let $S(x, y)$ be “x is shorter than y.” Given the premise $∃sS(s, Max)$, it follows that $S(Max, Max)$. Then by existential generalization it follows that $∃xS(x, x)$, so that someone is shorter than himself.
    - Exist. gen. of $∃sS(s, Max)$ would produce $S(x, Max)$ rather than $S(Max, Max)$.

19. Determine whether each of these arguments is valid. If an argument is correct, what rule of inference is being used? If it is not, what logical error occurs?
- (a) If n is a real number such that n > 1, then n2 > 1. Suppose that n2 > 1. Then n > 1.
  - Incorrect; affirming the conclusion.
- (b) If n is a real number with n > 3, then n2 > 9. Suppose that n2 ≤ 9. Then n ≤ 3.
  - True, by modus tollens.
- (c) If n is a real number with n > 2, then n2 > 4. Suppose that n ≤ 2. Then n2 ≤ 4.
  - Incorrect, denying the hypothesis.

20. Determine whether these are valid arguments.
- (a) If x is a positive real number, then x² is a positive real number. Therefore, if a² is positive, where a is a real number, then a is a positive real number.
  - $∀x(x > 0) → (x² > 0)$
  - $(a² > 0) → (a > 0)$
  - Incorrect, affirming the conclusion
- (b) If $x^2 ≠ 0$, where $x$ is a real number, then $x ≠ 0$. Let $a$ be a real number with $a^2 ≠ 0$; then $a ≠ 0$.
  - Correct; modus ponens.

21. Which rules of inference are used to establish the conclusion of Lewis Carroll’s argument described in Example 26 of Section 1.4?
    - univ. inst.
    - exist. inst. (particular lion does not drink coffee)
    - mod. pon. (part. lion is fierce)
    - conjunction (part. fierce creature doean not drink coffee)
    - exist. gen.

22. ❌ Which rules of inference are used to establish the conclusion of Lewis Carroll’s argument described in Example 27 of Section 1.4?
    - P: x is a hummingbird
    - Q: x is large
    - R: x lives on honey
    - S: x is richly coloured
    1. $¬∃x(Q(x) ∧ R(x))$      Premise
    1. $¬Q(h) ∨ ¬R(h)$         dml i; univ. inst.
    1. $¬R(h) → ¬S(h)$         Premise; univ. inst.
    1. $R(h) ∨ ¬S(h)$          equiv. iii
    1. $¬Q(h) ∨ ¬S(h)$         resolution ii, iv
    1. $P(h) → S(h)$           Premise; univ. inst.
    1. $¬P(h) ∨ S(h)$          equiv. vi
    1. $¬P(h) ∨ ¬Q(h)$         resolution v, vii
    1. $∀x(P(x) → ¬Q(x))$      Conclusion; equiv. vii

23. Identify the error or errors in this argument that supposedly shows that if ∃xP(x) ∧ ∃xQ(x) is true then ∃x(P(x) ∧ Q(x)) is true.

    1. ∃xP(x) ∨ ∃xQ(x)   Premise: *disj. instead of conj.*
    2. ∃xP(x)            **Simplification from (1): *simpl. on disj.***
    3. P(c)              Existential instantiation from (2)
    4. ∃xQ(x)            **Simplification from (1): *simpl. on disj.***
    5. Q(c)              Existential instantiation from (4)
    6. P(c) ∧ Q(c)       Conjunction from (3) and (5)
    7. ∃x(P(x) ∧ Q(x))   Existential generalization

24. Identify the error or errors in this argument that supposedly shows that if ∀x(P(x) ∨ Q(x)) is true then ∀xP(x) ∨ ∀xQ(x) is true.

    1. ∀x(P(x) ∨ Q(x))    Premise
    2. P(c) ∨ Q(c)        Universal instantiation from (1)
    3. P(c)               Simplification from (2) *simpl. on disj.*
    4. ∀xP(x)             Universal generalization from (3)
    5. Q(c)               Simplification from (2) *simpl. on disj.*
    6. ∀xQ(x)             Universal generalization from (5)
    7. ∀xP(x) ∨ ∀xQ(x)    Conjunction from (4) and (6) *disj. instead of conj.*

25. ❌ Justify the rule of universal modus tollens by showing that the premises $∀x(P(x) → Q(x))$ and $¬Q(a)$ for a particular element a in the domain, imply $¬P(a)$.
    - **By using universal instantiation of the first statement and conjunction with the second we obtain $P(a) → Q(a)$ which allows us to use modus tollens to conclude $¬P(a)$.**

26. ❎ Justify the rule of universal transitivity, which states that if $∀x(P(x) → Q(x))$ and $∀x(Q(x) → R(x))$ are true, then $∀x(P(x) → R(x))$ is true, where the domains of all quantifiers are the same.
    - $∀x(P(x) → Q(x))$
    - $∀x(Q(x) → R(x))$
    - $∀x(P(x) → R(x))$ Conclusion
    - **Using universal instantiation on the premises and the conclusion those form a hypothetical syllogism where the conclusion of the first premise is the condition of the second.**
    - We want to show that the conditional statement P (a) → R(a) is true for all a in the domain; the desired conclusion then follows by universal generalization. Thus we want to show that if P (a) is true for a particu- lar a, then R(a) is also true. For such an a, by universal modus ponens from the first premise we have Q(a), and then by universal modus ponens from the second premise we have R(a), as desired.

27. Use rules of inference to show that if ∀x(P(x) → (Q(x) ∧ S(x))) and ∀x(P(x) ∧ R(x)) are true, then ∀x(R(x) ∧ S(x)) is true.
    1. $∀x(P(x) ∧ R(x))$            Premise
    1. $P(a)$                       univ. inst., simpl. i
    1. $∀x(P(x) → (Q(x) ∧ S(x)))$   Premise
    1. $Q(a) ∧ S(a)$                univ. inst iii, mod. pon. ii,iii
    1. $R(a)$                       univ. inst., simpl. i
    1. $R(a) ∧ S(a)$                simpl. iv, conj. iv,v
    1. $∀x(R(x) ∧ S(x))$            Conclusion; univ. gen.

28. ❌ Use rules of inference to show that if $∀x(P(x) ∨ Q(x))$ and $∀x((¬P(x) ∧ Q(x)) → R(x))$ are true, then $∀x(¬R(x) → P(x))$ is also true, where the domains of all quantifiers are the same.
    - We want to show that $¬R(a) → P(a)$. This can then be generalized. **Using equivalence on the instantiation of the second statement gives us $(P(a) ∨ ¬Q(a) ∨ R(a)) ∧ (P(a) ∨ Q(a))$ in conjunction with the second statement. Resolution on $Q(a)$ gives us $(P(a) ∨ R(a)) ∧ P(a)$ and simplificaion shows that $P(a)$ is true.**

29. ❎ Use rules of inference to show that if $∀x(P(x) ∨ Q(x))$, $∀x(¬Q(x) ∨ S(x))$, $∀x(R(x) → ¬S(x))$, and $∃x¬P(x)$ are true, then $∃x¬R(x)$ is true.
    1. $∀x(¬Q(x) ∨ S(x))$     Premise
    1. $∀x(P(x) ∨ Q(x))$      Premise
    1. $P(a) ∨ S(a)$          univ. inst., resoltuion i,ii
    1. $∀x(R(x) → ¬S(x))$     Premise
    1. $¬R(a) ∨ ¬S(a)$        univ. inst., equiv. iv
    1. $P(a) ∨ ¬R(a)$         resolution iii,v
    1. $∃x¬P(x)$              Premise
    1. $¬R(a)$                exist. inst. vii, equiv. vi,vii
    1. $∃x¬R(x)$              Conclusion, exist. gen.

30. Use resolution to show the hypotheses “Allen is a bad boy or Hillary is a good girl” and “Allen is a good boy or David is happy” imply the conclusion “Hillary is a good girl or David is happy.”
    - As both statements contain the proposition "Allen is a good boy (or bad boy respectively)" one of these being false will require the other proposition in the same disjunction to be true. Therefore, if both statements are to be true, it reduces to the other propositions in a disjunction.

31. Use resolution to show that the hypotheses “It is not raining or Yvette has her umbrella,” “Yvette does not have her umbrella or she does not get wet,” and “It is raining or Yvette does not get wet” imply that “Yvette does not get wet.”
    - $¬r ∨ u$  Premise
    - $¬u ∨ ¬w$ Premise
    - $¬r ∨ ¬w$
    - $r ∨ ¬w$  Premise
    - $¬w ∨ ¬w$
    - $¬w$      Conclusion

32. ❌ Show that the equivalence $p ∧ ¬p ≡ F$ can be derived using resolution together with the fact that a conditional statement with a false hypothesis is true. [Hint: Let $q = r = F$ in resolution.]
    - $(q ∨ p) ∧ (r ∨ ¬p)$
    - $(F ∨ p) ∧ (F ∨ ¬p)$
    - $p ∧ ¬p$

33. Use resolution to show that the compound proposition (p ∨ q) ∧ (¬p ∨ q) ∧ (p ∨ ¬q) ∧ (¬p ∨ ¬q) is not satisfiable.
    - $p ∨ q$
    - $¬p ∨ q$
    - $p ∨ ¬q$
    - $¬p ∨ ¬q$
    - Using resolution on the first two statements q has to be true while using it on the last shows it has to be false. **Therefore it is an unsatidfiable contradiction.**

34. (∗) The Logic Problem, taken from WFF’N PROOF, The Game of Logic, has these two assumptions:

    1. “Logic is difficult or not many students like logic.”
    2. “If mathematics is easy, then logic is not difficult.”

    - $d ∨ ¬s$ $s → d$ (1)
    - $e → ¬d$ $d → ¬e$ (2)
    - $s → ¬e$
    - $¬e ∨ ¬s$

By translating these assumptions into statements involving propositional variables and logical connectives, determine whether each of the following are valid conclusions of these assumptions:
- (a) ❎ That mathematics is not easy, if many students like logic.
  - $¬e ∨ ¬s$ (equiv. + resolution)
  - $s → ¬e$.
  - This is true. Using equivalence on 2 and then resolution with 1 gives $¬e ∨ ¬s$. This in turn is equivalent to $s → ¬e$.
- (b) That not many students like logic, if mathematics is not easy.
  - $¬e → ¬s$
  - ❌ True, this is the contrapositive of the hypothetical syllogism of the equivalences of 1 and 2.
- (c) ❎ That mathematics is not easy or logic is difficult.
  - $¬e ∨ d$
  - False, using equivalence on 2 and resolution on 1 and 2 it follows that both evaluate to $¬e ∨ ¬s$ and $d$ is excluded.
- (d) That logic is not difficult or mathematics is not easy.
  - $¬d ∨ ¬e$
  - This is equivalent to $e → ¬d$, our second assumption.
- (e) That if not many students like logic, then either mathematics is not easy or logic is not difficult.
  - $¬s → ¬e ∨ ¬d$
  - This will only be false if s = F and both e and d are true. This renders 1 true and 2 false, ❌ **therefore the conclusion is invalid.**

35. (∗) ❎ Determine whether this argument, taken from Kalish and Montague [KaMo64], is valid. If Superman were able and willing to prevent evil, he would do so. If Superman were unable to prevent evil, he would be impotent; if he were unwilling to prevent evil, he would be malevolent. Superman does not prevent evil. If Superman exists, he is neither impotent nor malevolent. Therefore, Superman does not exist.
    - $(a ∧ w) → p$     Premise (1)
    - $¬a → i$          Premise (2)
    - $¬w → m$          Premise (3)
    - $¬p$              Premise (4)
    - $e → (¬i ∧ ¬m)$   Premise (5)
    - $¬e$              Conclusion
    - First p has to be false. Then for 1 to be true either a or w has to be false. The contrapositive of 5 shows that if i or m are true, then e is false. So considering 2 and 3 if a is false, i must be true and if w is false, m must be true. Therefore e is false and the conclusion valid.
