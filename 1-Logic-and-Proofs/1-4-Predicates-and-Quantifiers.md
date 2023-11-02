# 1.4 Predicates and Quantifiers

1. Let P (x) denote the statement “x ≤ 4.” What are these truth values?
- (a) P (0): T
- (b) P (4): T
- (c) P (6): F

2. Let P (x) be the statement “the word x contains the letter a.” What are these truth values?
- (a) P (orange): T
- (b) P (lemon): F
- (c) P (true): F
- (d) P (false): T

3. Let Q(x, y) denote the statement “x is the capital of y.” What are these truth values?
- (a) Q(Denver, Colorado): T
- (b) Q(Detroit, Michigan): T
- (c) Q(Massachusetts, Boston): F
- (d) Q(New York, New York): T

4. State the value of x after the statement if P (x) then x := 1 is executed, where P (x) is the statement “x > 1,” if the value of x when this statement is reached is
- (a) x = 0 : 0
- (b) x = 1 : 1
- (c) x = 2 : 1

5. Let P (x) be the statement “x spends more than five hours every weekday in class,” where the domain for x consists of all students. Express each of these quantifications in English.
- (a) ∃x P(x)
  - There is at least one student who spends more ...
- (b) ∀x P(x)
  - All students spend more ...
- (c) ∃x ¬P(x)
  - There is at least one student who doesnt spend more ...
- (d) ∀x ¬P(x)
  - No student spends more ...

6. Let N (x) be the statement “x has visited North Dakota,” where the domain consists of the students in your school. Express each of these quantifications in English.
- (a) ∃x N(x)
  - There is a student ... who has visited ...
- (b) ∀x N(x)
  - All students ... have visited ...
- (c) ¬∃x N(x)
  - There is no student ... who has visited ...
- (d) ∃x ¬N(x)
  - There is a student ... who has not visited ...
- (e) ¬∀x N(x)
  - Not all students ... have visited ...
- (f) ∀x ¬N(x)
  - No student ... has visited ...

7. Translate these statements into English, where C(x) is “x is a comedian” and F (x) is “x is funny” and the domain consists of all people.
- (a) $∀x (C(x) → F(x))$
  - If anyone is a comedian, he is funny.
- (b) $∀x (C(x) ∧ F(x))$
  - Anyone is a comedian and funny.
- (c) $∃x (C(x) → F(x))$
  - There is someone that is funny, if he is a comedian.
- (d) $∃x (C(x) ∧ F(x))$
  - There is someone who is a comedian and funny.

8. Translate these statements into English, where R(x) is “x is a rabbit” and H (x) is “x hops” and the domain consists of all animals.
- **(a) $∀x(R(x) → H (x))$**
  - !!! If an animal hops, its a rabbit.
- (b) $∀x(R(x) ∧ H (x))$
  - All animals are hopping rabbits.
- (c) $∃x(R(x) → H (x))$
  - There is an animal that hops, if it is a rabbit.
- (d) $∃x(R(x) ∧ H (x))$
  - There are animals which are hopping rabbits.

9. Let P(x) be the statement “x can speak Russian” and let Q(x) be the statement “x knows the computer language C++.” Express each of these sentences in terms of P (x), Q(x), quantifiers, and logical connectives. The domain for quantifiers consists of all students at your school.
- (a) There is a student at your school who can speak Russian and who knows C++.
  - $∃x(P(x) ∧ Q(x))$
- (b) There is a student at your school who can speak Russian but who doesn’t know C++.
  - $∃x(P(x) ∧ ¬Q(x))$
- (c) Every student at your school either can speak Russian
or knows C++.
  - $∀x(P(x) ∨ Q(x))$
- (d) No student at your school can speak Russian or knows C++.
  - $∀x(¬P(x) ∧ ¬Q(x))$

10. Let C(x) be the statement “x has a cat,” let D(x) be the statement “x has a dog,” and let F (x) be the statement “x has a ferret.” Express each of these statements in terms of C(x), D(x), F (x), quantifiers, and logical connectives. Let the domain consist of all students in your class.
- (a) A student in your class has a cat, a dog, and a ferret.
  - $∃x(C(x) ∧ D(x) ∧ F(x))$
- (b) All students in your class have a cat, a dog, or a ferret.
  - $∀x(C(x) ∨ D(x) ∨ F(x))$
- (c) Some student in your class has a cat and a ferret, but not a dog.
  - $∃x(C(x) ∧ F(x) ∧ ¬D(x))$
- (d) No student in your class has a cat, a dog, and a ferret.
  - $¬∃x(C(x) ∧ D(x) ∧ F(x))$
- **(e) For each of the three animals, cats, dogs, and ferrets, there is a student in your class who has this animal as a pet.**
  - !!! $∃x(C(x) ∨ D(x) ∨ F(x))$

11. Let P (x) be the statement “x = x².” If the domain consists of the integers, what are these truth values?
- (a) $P(0)$ T
- (b) $P(1)$ T
- (c) $P(2)$ F
- (d) $P(−1)$ F
- (e) $∃xP(x)$ T
- (f) $∀xP(x)$ F

12. Let Q(x) be the statement “x + 1 > 2x.” If the domain consists of all integers, what are these truth values?
- (a) $Q(0)$ T
- (b) $Q(−1)$ T
- (c) $Q(1)$ F
- (d) $∃xQ(x)$ T
- (e) $∀xQ(x)$ F
- (f) $∃x¬Q(x)$ T
- (g) $∀x¬Q(x)$ F

13. Determine the truth value of each of these statements if the domain consists of all integers.
- (a) $∀n(n + 1 > n)$ T
- **(b) $∃n(2n = 3n)$ F**
- **(c) $∃n(n = −n)$ F**
- **(d) $∀n(3n ≤ 4n)$ T**

14. Determine the truth value of each of these statements if the domain consists of all real numbers.
- (a) $∃x(x3 = −1)$ T
- (b) $∃x(x4 < x2)$ T
- **(c) $∀x((−x)2 = x2)$ F**
- (d) $∀x(2x > x)$ F

15. Determine the truth value of each of these statements if the domain for all variables consists of all integers.
- (a) $∀n(n^2 ≥ 0)$ F
- (b) $∃n(n^2 = 2)$ F
- **(c) $∀n(n^2 ≥ n)$ F**
- (d) $∃n(n^2 < 0)$ F

16. Determine the truth value of each of these statements if the domain of each variable consists of all real numbers.
- (a) $∃x(x^2 = 2)$ T
- (b) $∃x(x^2 = −1)$ F
- (c) $∀x(x^2 + 2 ≥ 1)$ T
- (d) $∀x(x^2 ≠ x)$ F

17. Suppose that the domain of the propositional function P (x) consists of the integers 0, 1, 2, 3, and 4. Write out each of these propositions using disjunctions, conjunctions, and negations.
- (a) $∃x P(x)$
  - $\bigvee_{x=0}^{4}p(x)$
- (b) $∀x P(x)$
  - $\bigwedge_{x=0}^{4}p(x)$
- (c) $∃x ¬P(x)$
  - $\bigvee_{x=0}^{4}¬p(x)$
- (d) $∀x ¬P(x)$
  - $\bigwedge_{x=0}^{4}¬p(x)$
- (e) $¬∃x P(x)$
  - $\bigwedge_{x=0}^{4}¬p(x)$
- (f) $¬∀x P(x)$
  - $\bigvee_{x=0}^{4}¬p(x)$

18. Suppose that the domain of the propositional function P (x) consists of the integers −2, −1, 0, 1, and 2. Write out each of these propositions using disjunctions, conjunctions, and negations.
- (a) $∃x P(x)$
  - $\bigvee_{x=-2}^{2}p(x)$
- (b) $∀x P(x)$
  - $\bigwedge_{x=-2}^{2}p(x)$
- (c) $∃x¬ P(x)$
  - $\bigvee_{x=-2}^{2}¬p(x)$
- (d) $∀x¬ P(x)$
  - $\bigwedge_{x=-2}^{2}¬p(x)$
- (e) $¬∃x P(x)$
  - $\bigwedge_{x=-2}^{2}¬p(x)$
- (f) $¬∀x P(x)$
  - $\bigvee_{x=-2}^{2}¬p(x)$

19. Suppose that the domain of the propositional function P (x) consists of the integers 1, 2, 3, 4, and 5. Express these statements without using quantifiers, instead using only negations, disjunctions, and conjunctions.
- (a) $∃xP(x)$
  - $\bigvee_{x=-1}^{5}P(x)$
- (b) $∀xP(x)$
  - $\bigwedge_{x=-1}^{5}P(x)$
- (c) $¬∃xP(x)$
  - $\bigwedge_{x=-1}^{5}¬P(x)$
- (d) $¬∀xP(x)$
  - $\bigvee_{x=-1}^{5}¬P(x)$
- (e) $∀x((x = 3) → P(x)) ∨ ∃x¬P(x)$
  - $∀x(¬(x = 3) ∨ P(x)) ∨ ∃x¬P(x)$
  - $((T ∨ P(1)) ∧ (T ∨ P(2)) ∧ (F ∨ P(3)) ∧ (T ∨ P(4)) ∧ (T ∨ P(5))) ∨ ∃x¬P(x)$
  - $P(3) ∨ ¬P(1) ∨ ¬P(2) ∨ ¬P(3) ∨ ¬P(4) ∨ ¬P(5)$

20. Suppose that the domain of the propositional function P (x) consists of −5, −3, −1, 1, 3, and 5. Express these statements without using quantifiers, instead using only negations, disjunctions, and conjunctions.
- (a) $∃xP(x)$
  - $P(-5) ∨ P(-3) ∨ P(-1) ∨ P(1) ∨ P(3) ∨ P(5)$
- (b) $∀xP(x)$
  - $P(-5) ∧ P(-3) ∧ P(-1) ∧ P(1) ∧ P(3) ∧ P(5)$
- (c) $∀x((x = 1) → P(x))$
  - (!!!) $((-5 = 1) → P(-5)) ∧ ((-3 = 1) → P(-3)) ∧ ((-1 = 1) → P(-1)) ∧ ((1 = 1) → P(1)) ∧ ((3 = 1) → P(3)) ∧ ((5 = 1) → P(5))$
  - (!!!) $(T) ∧ (T) ∧ (T) ∧ P(1) ∧ (T) ∧ (T)$
  - (!!!) $P(1)$
- (d) $∃x((x ≥ 0) ∧ P(x))$
  - $F ∨ F ∨ F ∨ P(1) ∨ P(3) ∨ P(5)$
  - $P(1) ∨ P(3) ∨ P(5)$
- (e) $∃x(¬P(x)) ∧ ∀x((x < 0) → P(x))$
  - $(¬P(-5) ∨ ¬P(-3) ∨ ¬P(-1) ∨ ¬P(1) ∨ ¬P(3) ∨ ¬P(5)) ∧ ∀x((x < 0) → P(x))$
  - $(¬P(-5) ∨ ¬P(-3) ∨ ¬P(-1) ∨ ¬P(1) ∨ ¬P(3) ∨ ¬P(5)) ∧ (P(-5) ∧ P(-3) ∧ P(-1))$
  - $(¬P(1) ∨ ¬P(3) ∨ ¬P(5)) ∧ (P(-5) ∧ P(-3) ∧ P(-1))$

21. For each of these statements find a domain for which the statement is true and a domain for which the statement is false.
- (a) Everyone is studying discrete mathematics.
  - T: Every student in CS
  - F: Every student at the uni
- (b) Everyone is older than 21 years.
  - T: People born before 1988
  - F: People born after 2005
- (c) Every two people have the same mother.
  - T: People who are siblings
  - F: People living in the same city
- (d) No two different people have the same grandmother.
  - T: People from different families
  - F: People within one family.

22. For each of these statements find a domain for which the statement is true and a domain for which the statement is false.
- (a) Everyone speaks Hindi.
- (b) There is someone older than 21 years.
- (c) Every two people have the same first name.
- (d) Someone knows more than two other people.

23. Translate in two ways each of these statements into logical expressions using predicates, quantifiers, and logical connectives. First, let the domain consist of the students in your class and second, let it consist of all people.
- (a) Someone in your class can speak Hindi.
  - class: $∃p H(p)$
  - all: $∃p (C(p) ∧ H(p))$
- (b) Everyone in your class is friendly.
  - class: $∀p F(p)$
  - all: $∀p (C(p) → F(p))$
- (c) There is a person in your class who was not born in California.
  - class: $∃p ¬B(p)$
  - all: $∃p (C(p) ∧ ¬B(p))$
- (d) A student in your class has been in a movie.
  - class: $∃p M(p)$
  - all: $∃p (C(p) ∧ M(p))$
- (e) No student in your class has taken a course in logic programming.
  - class: $¬∃p P(p)$
  - all: $¬∃p (C(p) ∧ P(p))$

24. Translate in two ways each of these statements into logical expressions using predicates, quantifiers, and logical connectives. First, let the domain consist of the students in your class and second, let it consist of all people.
- (a) Everyone in your class has a cellular phone.
  - class: $∀x P(x)$
  - all: $∀x (C(x) → P(x))$
- (b) Somebody in your class has seen a foreign movie.
  - class: $∃x M(x)$
  - all: $∃x(C(x) ∧ M(x))$
- (c) There is a person in your class who cannot swim.
  - class: $∃x ¬S(x)$
  - all: $∃x(C(x) ∧ ¬S(x))$
- (d) All students in your class can solve quadratic equations.
  - class: $∀x E(x)$
  - all: $∀x (C(x) → E(x))$
- (e) Some student in your class does not want to be rich.
  - class: $∃x ¬R(x)$
  - all: $∃x (C(x) ∧ ¬R(x))$

25. Translate each of these statements into logical expressions using predicates, quantifiers, and logical connectives.
- (a) No one is perfect.
  - $∀x ¬P(x)$
- (b) Not everyone is perfect.
  - $¬∀x P(x)$
- (c) All your friends are perfect.
  - $∀x (F(x) → P(x))$
- (d) At least one of your friends is perfect.
  - $∃x (F(x) ∧ P(x))$
- (e) Everyone is your friend and is perfect.
  - $∀x (F(x) ∧ P(x))$
- **(f) Not everybody is your friend or someone is not perfect.**
  - !!! $∀x ¬F(x) ∨ ∃x ¬P(x)$

26. Translate each of these statements into logical expressions in three different ways by varying the domain and by using predicates with one and with two variables.
- (a) Someone in your school has visited Uzbekistan.
  - pupils: $∃x U(x)$
  - all: $∃x (Y(x) ∧ U(x))$
  - all: $∃x (Y(x) ∧ V(x, Uzbekistan))$
- **(b) Everyone in your class has studied calculus and C++.**
  - !!! pupils: $∃x S(x)$
  - !!! all: $∃x (Y(x) ∧ S(x))$
  - !!! all: $∃x (Y(x) ∧ S(x, CPP, Calculus))$
- (c) No one in your school owns both a bicycle and a motorcycle.
  - pupils: $¬∃x O(x)$
  - all: $¬∃x (Y(x) ∧ O(x))$
  - all: $¬∃x (Y(x) ∧ O(x, bicycle, motorcycle))$
- (d) There is a person in your school who is not happy.
  - pupils: $∃x ¬H(x)$
  - all: $∃x (Y(x) ∧ ¬H(x))$
  - all: $∃x (Y(x) ∧ ¬I(x, happy))$
- (e) Everyone in your school was born in the twentieth century.
  - pupils: $∀x B(x)$
  - all: $∀x (Y(x) → B(x))$
  - all: $∀x (Y(x) → B(x, 20th))$

27. Translate each of these statements into logical expressions in three different ways by varying the domain and by using predicates with one and with two variables.
- (a) A student in your school has lived in Vietnam.
  - pupils: $∃x V(x)$
  - all: $∃x (S(x) ∧ V(x))$
  - all: $∃x (S(x) ∧ L(x, Vietnam))$
- (b) There is a student in your school who cannot speak Hindi.
  - pupils: $∃x ¬H(x)$
  - all: $∃x (S(x) ∧ ¬H(x))$
  - all: $∃x (S(x) ∧ ¬S(x, Hindi))$
- (c) A student in your school knows Java, Prolog, and C++.
  - pupils: $∃x (J(x) ∧ P(x) ∧ C(x))$
  - all: $∃x (S(x) ∧ J(x) ∧ P(x) ∧ C(x))$
  - all: $∃x (S(x) ∧ L(x, Java) ∧ L(x, Prolog) ∧ L(x, CPP))$
- (d) Everyone in your class enjoys Thai food.
  - pupils: $∀x T(x)$
  - all: $∀x (C(x) → T(x))$
  - all: $∀x (C(x) → F(x, Thai))$
- (e) Someone in your class does not play hockey.
  - pupils: $∃x ¬H(x)$
  - all: $∃x (C(x) ∧ ¬H(x))$
  - all: $∃x (C(x) ∧ ¬P(x, Hockey))$

28. Translate each of these statements into logical expressions using predicates, quantifiers, and logical connectives.
- (a) Something is not in the correct place.
  - $∃x ¬P(x)$
- (b) All tools are in the correct place and are in excellent condition.
  - $∀x (T(x) → (P(x) ∧ C(x)))$
- (c) Everything is in the correct place and in excellent condition.
  - $∀x (P(x) ∧ C(x))$
- **(d) Nothing is in the correct place and is in excellent condition.**
  - !!! $¬∀x (P(x) ∧ C(x))$
  - $∀x ¬(P(x) ∧ C(x))$
- **(e) One of your tools is not in the correct place, but it is in excellent condition.**
  - !!! $∃x (¬P(x) ∧ C(x))$

29. Express each of these statements using logical operators, predicates, and quantifiers.
- **(a) Some propositions are tautologies.**
  - !!! $∃x (P(x) ∧ T(x))$
- **(b) The negation of a contradiction is a tautology.**
  - !!! $∀x ((N(x) ∧ C(x)) → T(x))$
- **(c) The disjunction of two contingencies can be a tautology.**
  - !!! $∃x ((C(x) ∨ C(x)) ∧ T(x))$
- **(d) The conjunction of two tautologies is a tautology.**
  - !!! $∀x ((T(x) ∧ T(x)) → T(x))$

30. Suppose the domain of the propositional function P (x, y) consists of pairs x and y, where x is 1, 2, or 3 and y is 1, 2, or 3. Write out these propositions using disjunctions and conjunctions.
- (a) ∃x P (x, 3)
  - $P(1,3) ∨ P(2,3) ∨ P(3,3)$
- (b) ∀y P (1, y)
  - $P(1,1) ∧ P(1,2) ∧ P(1,3)$
- (c) ∃y¬P (2, y)
  - $¬P(2,1) ∨ ¬P(2,2) ∨ ¬P(2,3)$
- (d) ∀x ¬P (x, 2)
  - $P(1,2) ∧ P(2,2) ∧ P(3,2)$

31. Suppose that the domain of Q(x, y, z) consists of triples x, y, z, where x = 0, 1, or 2, y = 0 or 1, and z = 0 or 1. Write out these propositions using disjunctions and conjunctions.
- (a) ∀yQ(0, y, 0)
  - $Q(0,0,0) ∧ Q(0,1,0)$
- (b) ∃xQ(x, 1, 1)
  - $Q(0,1,1) ∨ Q(1,1,1) ∨ Q(2,1,1)$
- (c) ∃z¬Q(0, 0, z)
  - $¬Q(0,0,0) ∨ ¬Q(0,0,1)$
- (d) ∃x¬Q(x, 0, 1)
  - $¬Q(0,0,1) ∨ ¬Q(1,0,1) ∨ ¬Q(2,0,1)$

32. Express each of these statements using quantifiers. Then form the negation of the statement so that no negation is to the left of a quantifier. Next, express the negation in simple English. (Do not simply use the phrase “It is not the case that.”)
- **(a) All dogs have fleas.**
  - $∀x F(x)$
  - !!! $∀x ¬F(x)$
  - !!! No dog has fleas.
- (b) There is a horse that can add.
  - $∃x A(x)$
  - $∀x ¬A(x)$
  - No horse can add.
- (c) Every koala can climb.
  - $∀x C(x)$
  - $∃x ¬C(x)$
  - There is a koala that cannot climb.
- (d) No monkey can speak French.
  - $∀x ¬F(x)$
  - $∃x F(x)$
  - There is a monkey that can speak French.
- **(e) There exists a pig that can swim and catch fish.**
  - $∃x (S(x) ∧ F(x))$
  - !!! $∀x (¬S(x) ∧ ¬F(x))$
  - !!! There is no pig that can swim and fish.

33. Express each of these statements using quantifiers. Then form the negation of the statement, so that no negation is to the left of a quantifier. Next, express the negation in simple English. (Do not simply use the phrase “It is not the case that.”)
- (a) Some old dogs can learn new tricks.
  - $∃x L(x)$
  - $∀x ¬L(x)$
  - No old dog can learn new tricks.
- (b) No rabbit knows calculus.
  - $∀x ¬C(x)$
  - $∃x C(x)$
  - There is at least one rabbit that knows calculus.
- (c) Every bird can fly.
  - $∀x F(x)$
  - $∃x ¬F(x)$
  - There are birds that cannot fly.
- (d) There is no dog that can talk.
  - $∀x ¬T(x)$
  - $∃x T(x)$
  - There is a dog that can talk.
- **(e) There is no one in this class who knows French and Russian.**
  - $∀x ¬(F(x) ∧ R(x))$
  - !!! $∃x (F(x) ∨ R(x))$
  - !!! There is someone in this class who knows French or Russian.

34. Express the negation of these propositions using quantifiers, and then express the negation in English.
- (a) Some drivers do not obey the speed limit.
  - $∀x S(x)$
  - All drivers obey the speed limit.
- (b) All Swedish movies are serious.
  - $∃x ¬S(x)$
  - There are movies that are not serious.
- (c) No one can keep a secret.
  - $∃x S(x)$
  - Someone can keep a secret.
- (d) There is someone in this class who does not have a good attitude.
  - $∀x A(x)$
  - All in this class have a good attitude.

35. Find a counterexample, if possible, to these universally quantified statements, where the domain for all variables consists of all integers.
- (a) $∀x(x^2 ≥ x)$
  - $T$
- (b) $∀x(x > 0 ∨ x < 0)$
  - $0$
- (c) $∀x(x = 1)$
  - $2$

36. Find a counterexample, if possible, to these universally quantified statements, where the domain for all variables consists of all real numbers.
- (a) $∀x(x^2 ≠ x)$: 1
- **!!! (b) $∀x(x^2 ≠ 2)$: T**
- (c) $∀x(|x| > 0)$: 0

37. Express each of these statements using predicates and quantifiers.
- (a) A passenger on an airline qualifies as an elite flyer if the passenger flies more than 25,000 miles in a year or takes more than 25 flights during that year.
  - $∀x ((M(x) ∨ F(x)) → E(x))$
- (b) A man qualifies for the marathon if his best previous time is less than 3 hours and a woman qualifies for the marathon if her best previous time is less than 3.5 hours.
  - $∀x ((M(x) ∧ T(x, 3)) ∨ (W(x) ∧ T(x, 3.5)) → Q(x))$
- (c) A student must take at least 60 course hours, or at least 45 course hours and write a master’s thesis, and receive a grade no lower than a B in all required courses, to receive a master’s degree.
  - $∀x (((H(x, 60) ∨ (H(x, 45) ∧ T(x))) ∧ B(x))→ M(x))$
- (d) There is a student who has taken more than 21 credit hours in a semester and received all A’s.
  - $∃x (H(x,21) ∧ A(x))$

Exercises 38–42 deal with the translation between system specification and logical expressions involving quantifiers.

38. Translate these system specifications into English where the predicate S(x, y) is “x is in state y” and where the domain for x and y consists of all systems and all possible states, respectively.
- (a) $∃xS(x, open)$
  - There is a system with state 'open'
- (b) $∀x(S(x, malfunctioning) ∨ S(x, diagnostic))$
  - All systems are either malfunctioning or in diagnostic mode.
- (c) $∃xS(x, open) ∨ ∃xS(x, diagnostic)$
  - There is a system in state 'open' or there is one in state 'diagnostic'.
- (d) $∃x¬S(x, available)$
  - There is a system which is not available.
- **(e) $∀x¬S(x, working)$**
  - No systems are working.

39. Translate these specifications into English where F (p) is “Printer p is out of service,” B(p) is “Printer p is busy,” L(j ) is “Print job j is lost,” and Q(j ) is “Print job j is queued.”
- (a) $∃p(F (p) ∧ B(p)) → ∃j L(j )$
  - If there is a printer that is out of service and busy, some print jobs will be lost.
- (b) $∀pB(p) → ∃j Q(j )$
  - If all printers are busy, some jobs will be queued.
- **(c) $∃j (Q(j ) ∧ L(j )) → ∃pF (p)$**
  - !!! If there is a queued or lost job, some printers will be out of service.
- (d) $(∀pB(p) ∧ ∀j Q(j )) → ∃j L(j )$
  - If all Printers are busy and all jobs are queued, some jobs will be lost.

40. Express each of these system specifications using predicates, quantifiers, and logical connectives.
- (a) When there is less than 30 megabytes free on the hard disk, a warning message is sent to all users.
  - $F(30) → ∀yW(y)$
- (b) No directories in the file system can be opened and no files can be closed when system errors have been detected.
  - $E → (∀d¬O(d) ∧ ∀f¬C(f))$
- (c) The file system cannot be backed up if there is a user currently logged on.
  - $∃uL(u) → ¬B$
- (d) Video on demand can be delivered when there are at least 8 megabytes of memory available and the connection speed is at least 56 kilobits per second.
  - $(M(8) ∧ C(56)) → V$

41. Express each of these system specifications using predicates, quantifiers, and logical connectives.
- **(a) At least one mail message, among the nonempty set of messages, can be saved if there is a disk with more than 10 kilobytes of free space.**
  - !!! $∃m(∃dS(10) → S(m))$
- **(b) Whenever there is an active alert, all queued messages are transmitted.**
  - !!! $A → ∀mT(m)$
- **(c) The diagnostic monitor tracks the status of all systems except the main console.**
  - !!! $∃s¬M(s)$
- (d) Each participant on the conference call whom the host of the call did not put on a special list was billed.
  - $∀p(¬L(p) → B(p))$

42. Express each of these system specifications using predicates, quantifiers, and logical connectives.
- (a) Every user has access to an electronic mailbox.
  - $∀uA(u)$
- (b) The system mailbox can be accessed by everyone in the group if the file system is locked.
  - $L → ∀u(G(u) → A(u))$
- (c) The firewall is in a diagnostic state only if the proxy server is in a diagnostic state.
  - $F → P$
- (d) At least one router is functioning normally if the throughput is between 100 kbps and 500 kbps and the proxy server is not in diagnostic mode.
  - $(T(100, 500) ∧ P) → ∃rF(r)$

43. Determine whether $∀x(P(x) → Q(x))$ and $∀xP(x) → ∀xQ(x)$ are logically equivalent. Justify your answer.
    - No, because the first one can describe a part of the total and the second one makes a statement that is true for all or none.

44. **Determine whether $∀x(P(x) ↔ Q(x))$ and $∀xP(x) ↔ ∀xQ(x)$ are logically equivalent. Justify your answer.**
    - No, see above.

45. Show that $∃x(P(x) ∨ Q(x))$ and $∃xP(x) ∨ ∃xQ(x)$ are logically equivalent.
    - Assuming P is true for x being even and Q for x being odd integers the first expression validly states that one of P or Q will be true for some x. The second statement says that there is either an even or an odd x, which is equivalent.

Exercises 46–49 establish rules for null quantification that we can use when a quantified variable does not appear in part of a statement.

46. Establish these logical equivalences, where x does not occur as a free variable in A. Assume that the domain is nonempty.
- **(a) $(∀xP(x)) ∨ A ≡ ∀x(P(x) ∨ A)$**
  - As A is independent from x it makes not difference if its value is used within or outside of the scope of x.
- (b) $(∃xP(x)) ∨ A ≡ ∃x(P(x) ∨ A)$
  - If A is true both sides are true. If A is false, both sides are equal to $∃xP(x)$ by the law of identity. Another way of showing this is to consider that $∃xP(x)$ means that it will be true for some x which is sufficient for the whole expression being true in both cases.

47. Establish these logical equivalences, where x does not occur as a free variable in A. Assume that the domain is nonempty.
- (a) $(∀xP(x)) ∧ A ≡ ∀x(P(x) ∧ A)$
- (b) $(∃xP(x)) ∧ A ≡ ∃x(P(x) ∧ A)$
  - First, a false A will invalidate both expressions. In case of a true A the expression is in both cases reduced to ∀xP(x)/∃xP(x) by the law of identity.

48. Establish these logical equivalences, where x does not occur as a free variable in A. Assume that the domain is nonempty.
- (a) $∀x(A → P(x)) ≡ A → ∀xP(x)$
  - For a false A both expressions will be true for all x. A true A reduces them to the truth value of ∀xP(x).
- (b) $∃x(A → P(x)) ≡ A → ∃xP(x)$
  - For a false A both expressions will be true for some x. A true A reduces them to the truth value of ∃xP(x).

49. Establish these logical equivalences, where x does not occur as a free variable in A. Assume that the domain is nonempty.
- (a) $∀x(P(x) → A) ≡ ∃xP(x) → A$
  - If P(x) is false for all x on the left then it will also be false for some x on the right. If x is true for all x on the left it will also be true for some x on the right and the expression reduces to the value of A.
- **(b) $∃x(P(x) → A) ≡ ∀xP(x) → A$**
  - !!! If P(x) is false for some x on the left, then it will also render ∀xP(x) false and both sides are true. If P(x) is true for some x the left side reduces to the value of A and the right side will be true due to the condition being false.

50. Show that $∀xP(x) ∨ ∀xQ(x)$ and $∀x(P(x) ∨ Q(x))$ are not logically equivalent.
    - These are not equivalent because in the first case P or Q have to be true for ALL x while on the right either P or Q has to be true for every x.

51. Show that $∃xP(x) ∧ ∃xQ(x)$ and $∃x(P(x) ∧ Q(x))$ are not logically equivalent.
    - Let the domain be all integers, P that x is 1 and Q that x is 2. Then the first expression will be true while the second is false.

52. As mentioned in the text, the notation ∃!xP (x) denotes “There exists a unique x such that P (x) is true.” If the domain consists of all integers, what are the truth values of these statements?
- (a) $∃!x(x > 1)$: F
- (b) $∃!x(x^2 = 1)$: F
- **(c) $∃!x(x + 3 = 2x)$: !!! F**
- (d) $∃!x(x = x + 1)$: F

53. What are the truth values of these statements?
- (a) $∃!xP(x) → ∃xP(x)$: T
- **(b) $∀xP(x) → ∃!xP(x)$: T/F**
- (c) $∃!x¬P(x) → ¬∀xP(x)$: T

54. Write out $∃!xP(x)$, where the domain consists of the integers 1, 2, and 3, in terms of negations, conjunctions, and disjunctions.
    - $(P(1) ∧ ¬P(2) ∧ ¬P(3)) ∨ (¬P(1) ∧ P(2) ∧ ¬P(3)) ∨ (¬P(1) ∧ ¬P(2) ∧ P(3))$

55. Given the Prolog facts in Example 28, what would Prolog return given these queries?

<!--
instructor(chan,math273)
instructor(patel,ee222)
instructor(grossman,cs301)
enrolled(kevin,math273)
enrolled(juana,ee222)
enrolled(juana,cs301)
enrolled(kiko,math273)
enrolled(kiko,cs301) -->

- (a) ?instructor(chan,math273)
- (b) ?instructor(patel,cs301)
- (c) ?enrolled(X,cs301)
- (d) ?enrolled(kiko,Y)
- (e) ?teaches(grossman,Y)

56. Given the Prolog facts in Example 28, what would Prolog return when given these queries?
- (a) ?enrolled(kevin,ee222)
- (b) ?enrolled(kiko,math273)
- (c) ?instructor(grossman,X)
- (d) ?instructor(X,cs301)
- (e) ?teaches(X,kevin)

57. Suppose that Prolog facts are used to define the predicates mother(M,Y) and father(F,X), which represent that M is the mother of Y and F is the father of X, respectively. Give a Prolog rule to define the predicate sibling(X,Y), which represents that X and Y are siblings (that is, have the same mother and the same father).
    - `sibling(X,Y) :- mother(M,Y), father(F,X)`

58. Suppose that Prolog facts are used to define the predicates mother(M, Y ) and father(F, X), which represent that M is the mother of Y and F is the father of X, respectively. Give a Prolog rule to define the predicate grandfather(X, Y ), which represents that X is the grandfather of Y . [Hint: You can write a disjunction in Prolog either by using a semicolon to separate predicates or by putting these predicates on separate lines.]

Exercises 59–62 are based on questions found in the book Symbolic Logic by Lewis Carroll.

59. Let P (x), Q(x), and R(x) be the statements “x is a professor,” “x is ignorant,” and “x is vain,” respectively. Express each of these statements using quantifiers; logical connectives; and P(x), Q(x), and R(x), where the domain consists of all people.
- (a) No professors are ignorant.
  - $¬∃x(P(x) ∧ Q(x))$
- (b) All ignorant people are vain.
  - $∀x(Q(x) → R(x))$
- (c) No professors are vain.
  - $∀x(P(x) → ¬R(x))$
- **(d) Does (c) follow from (a) and (b)?**
  - !!! Yes

60. Let P(x), Q(x), and R(x) be the statements “x is a clear explanation,” “x is satisfactory,” and “x is an excuse,” respectively. Suppose that the domain for x consists of all English text. Express each of these statements using quantifiers, logical connectives, and P (x), Q(x), and R(x).
- (a) All clear explanations are satisfactory.
  - $∀x(P(x) → Q(x))$
- (b) Some excuses are unsatisfactory.
  - $∃x(R(x) ∧ ¬Q(x))$
- (c) Some excuses are not clear explanations.
  - $∃x(R(x) ∧ ¬P(x))$
- **(d) (∗) Does (c) follow from (a) and (b)?**
  - !!! No.

61. Let P(x), Q(x), R(x), and S(x) be the statements “x is a baby,” “x is logical,” “x is able to manage a crocodile,” and “x is despised,” respectively. Suppose that the domain consists of all people. Express each of these statements using quantifiers; logical connectives; and P(x), Q(x), R(x), and S(x).
- (a) Babies are illogical.
  - $∀x(P(x) → ¬Q(x))$
- (b) Nobody is despised who can manage a crocodile.
  - $∀x(R(x) → ¬S(x))$
- (c) Illogical persons are despised.
  - $∀x(¬Q(x) → S(x))$
- (d) Babies cannot manage crocodiles.
  - $∀x(P(x) → ¬R(x))$
- (e) (∗) Does (d) follow from (a), (b), and (c)? If not, is there a correct conclusion?
  - $∀x(P(x) → ¬Q(x))$
  - $∀x(R(x) → ¬S(x))$
  - $∀x(¬Q(x) → S(x))$
  - Yes, by (a) all P are ¬Q. By (c) all ¬Q are S so (d) is equal to $∀x(S(x) → ¬R(x))$ which follows from (b) $∀x(R(x) → ¬S(x))$.

62. Let P (x), Q(x), R(x), and S(x) be the statements “x is a duck,” “x is one of my poultry,” “x is an officer,” and “x is willing to waltz,” respectively. Express each of these statements using quantifiers; logical connectives; and P (x), Q(x), R(x), and S(x).
- (a) No ducks are willing to waltz.
  - $∀x(P(x) → ¬S(x))$
- (b) No officers ever decline to waltz.
  - $∀x(R(x) → S(x))$
- (c) All my poultry are ducks.
  - $∀x(Q(x) → P(x))$
- (d) My poultry are not officers.
  - $∀x(Q(x) → ¬R(x))$
- (e) (∗) Does (d) follow from (a), (b), and (c)? If not, is there a correct conclusion?
  - $∀x(P(x) → ¬S(x))$
  - $∀x(R(x) → S(x))$
  - $∀x(Q(x) → P(x))$
  - $∀x(Q(x) → ¬R(x))$
  - Yes, by (c) Q is P, by (a) P is not S. So (d) is equivalent to $∀x(¬S(x) → ¬R(x))$ which is the contrapositive of (b).
