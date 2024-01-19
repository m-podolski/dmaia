# 1.5 Nested Quantifiers

1. Translate these statements into English, where the domain for each variable consists of all real numbers.
- (a) ∀x∃y(x < y)
  - For all x there is an y greater than it.
- (b) ∀x∀y(((x ≥ 0) ∧ (y ≥ 0)) → (xy ≥ 0))
  - For all y for all x, if both are greater than or equal to 0, their product is as well.
- (c) ∀x∀y∃z(xy = z)
  - There is a number z for all y for all x which is equal to the product of x and y.

2. Translate these statements into English, where the domain for each variable consists of all real numbers.
- (a) ∃x∀y(xy = y)
  - There is a real number x such that for all real numbers y the product of x and y is y.
- (b) ∀x∀y(((x ≥ 0) ∧ (y < 0)) → (x − y > 0))
  - For all numbers x and all numbers y, if x is nonnegative and y is negative, the difference of x and y is positive.
- (c) ∀x∀y∃z(x = y + z)
  - For all numbers x and all numbers y there exists a number z that when added to y is equal to x.

3. Let Q(x, y) be the statement “x has sent an e-mail message to y,” where the domain for both x and y consists of all students in your class. Express each of these quantifications in English.
- (a) ∃x∃yQ(x, y)
  - There is a student who has sent an email to someone.
- (b) ∃x∀yQ(x, y)
  - There is a student who has sent an email to everyone.
- (c) ∀x∃yQ(x, y)
  - Every student has sent and email to someone.
- (d) ∃y∀xQ(x, y)
  - There is a student who has been sent an email from everyone.
- (e) ∀y∃xQ(x, y)
  - Every student has been sent an email from someone.
- (f) ∀x∀yQ(x, y)
  - Every student has sent everyone an email.

4. Let P (x, y) be the statement “Student x has taken class y,” where the domain for x consists of all students in your class and for y consists of all computer science courses at your school. Express each of these quantifications in English.
- (a) ∃x∃yP (x, y)
  - There is a student that has taken a class.
- (b) ∃x∀yP (x, y)
  - There is a student who has taken all classes.
- (c) ∀x∃yP (x, y)
  - All students have taken at leats one class.
- (d) ∃y∀xP (x, y)
  - There is a class that has been taken by all students.
- (e) ∀y∃xP (x, y)
  - All classes have been taken by at least one student.
- (f) ∀x∀yP (x, y)
  - All students have taken all classes.

5. Let W (x, y) mean that student x has visited website y, where the domain for x consists of all students in your school and the domain for y consists of all websites. Express each of these statements by a simple English sentence.
- (a) $W(Sarah Smith, <www.att.com>)$
  - Sarah Smith has visited att.com
- (b) $∃xW(x, <www.imdb.org>)$
  - There is a student who has visited imdb.org
- (c) $∃yW(José Orez, y)$
  - There is a website which has been visited by Jose Orez.
- (d) $∃y(W(Ashok Puri, y) ∧ W(Cindy Yoon, y))$
  - There is a website which has been visited by Ashok Puri and Cindy Yoon.
- (e) $∃y∀z(y ≠ (David Belcher) ∧ (W(David Belcher, z) → W(y,z)))$
  - There is a student other than David Belcher who has visited every website that David Belcher has visited.
- (f) $∃x∃y∀z((x ≠ y) ∧ (W(x, z) ↔ W(y, z)))$
  - There are two different students who have visited exactly the same websites.

6. Let C(x, y) mean that student x is enrolled in class y, where the domain for x consists of all students in your school and the domain for y consists of all classes being given at your school. Express each of these statements by a simple English sentence.
- (a) C(Randy Goldberg, CS 252)
  - Randy Goldberg is enrolled in CS 252
- (b) ∃xC(x, Math 695)
  - There is a student enrolled in Math 695
- (c) ∃yC(Carol Sitea, y)
  - There is a course in which Carol Sitea is enrolled in.
- (d) ∃x(C(x, Math 222) ∧ C(x, CS 252))
  - There is a student who is enrolled in both Math 222 and CS 252
- (e) ∃x∃y∀z((x ≠ y) ∧ (C(x, z) → C(y, z)))
  - There are two different student such that when x has vsisited any website, y has visited it too.
- (f) ∃x∃y∀z((x ≠ y) ∧ (C(x, z) ↔ C(y, z)))
  - There are two different students who have visited the same websites.

7. Let T (x, y) mean that student x likes cuisine y, where the domain for x consists of all students at your school and the domain for y consists of all cuisines. Express each of these statements by a simple English sentence.
- (a) ¬T(Abdallah Hussein, Japanese)
  - A. H. does not like Japanese.
- (b) ∃xT(x, Korean) ∧ ∀xT(x, Mexican)
  - There is a student who likes Korean and all students like Mexican.
- (c) ∃y(T(Monique Arsenault, y) ∨ T(Jay Johnson, y))
  - There is a dish that either M.A. or J.J. or both like.
- (d) ∀x∀z∃y((x ≠ z) → ¬(T(x, y) ∧ T(z, y)))
  - For any two different students there is a dish they dont like.
- (e) ∃x∃z∀y(T(x, y) ↔ T(z, y))
  - There is a student for which there is another one who likes exactly the same dishes.
- (f) ∀x∀z∃y(T(x, y) ↔ T(z, y))
  - ❌ For all possible pairs of student there is a cusine both like.
  - ❎ For every pair of students, there is some cuisine about which they have the same opinion (either they both like it or they both do not like it).

8. Let Q(x, y) be the statement “student x has been a contestant on quiz show y.” Express each of these sentences in terms of Q(x, y), quantifiers, and logical connectives, where the domain for x consists of all students at your school and for y consists of all quiz shows on television.
- (a) There is a student at your school who has been a contestant on a television quiz show.
  - $∃x∃yQ(x,y)$
- (b) No student at your school has ever been a contestant on a television quiz show.
  - $¬∃x∃yQ(x,y)$
- (c) There is a student at your school who has been a contestant on Jeopardy and on Wheel of Fortune.
  - $∃x(Q(x,Jeopardy) ∧ Q(x,WoF))$
- (d) Every television quiz show has had a student from your school as a contestant.
  - $∀y∃xQ(x,y)$
- (e) At least two students from your school have been contestants on Jeopardy.
  - $∃x∃y(x≠y ∧ Q(x,Jeopardy) ∧ Q(z,Jeopardy))$

9. Let L(x, y) be the statement “x loves y,” where the domain for both x and y consists of all people in the world. Use quantifiers to express each of these statements.
- (a) Everybody loves Jerry.
  - $∀xL(x,Jerry)$
- (b) Everybody loves somebody.
  - $∀x∃yL(x,y)$
- (c) There is somebody whom everybody loves.
  - $∃y∀xL(x,y)$
- (d) Nobody loves everybody.
  - $¬∃x∀yL(x,y)$
- (e) There is somebody whom Lydia does not love.
  - $∃y¬L(Lydia,y)$
- (f) There is somebody whom no one loves.
  - $∃y∀x¬L(x,y)$
- (g) There is exactly one person whom everybody loves.
  - ❌ $∃y∀xL(x,y)$
  - $∃x(∀yL(y,x) ∧ ∀z((∀wL(w,z)) → z = x))$
- (h) There are exactly two people whom Lynn loves.
  - ❌ $∃y_1∃y_2L(Lynn,y_1) ∧ L(Lynn,y_2) ∧ (y_1 ≠ y_2)$
  - $∃y_1∃y_2(y_1 ≠ y_2 ∧ L(Lynn,y_1) ∧ L(Lynn,y_2) ∧ ∀z(L(Lynn,z) → (z = y_1 ∨ z = y_2)))$
- (i) Everyone loves himself or herself.
  - $∀xL(x,x)$
- (j) There is someone who loves no one besides himself or herself.
  - ❌ $∃x∀yL(x,x) ∧ ¬L(x,y)$
  - $∃x∀y(L(x,y) ↔ x = y)$

10. Let F (x, y) be the statement “x can fool y,” where the domain consists of all people in the world. Use quantifiers to express each of these statements.
- (a) Everybody can fool Fred.
  - $∀xF(x,Fred)$
- (b) Evelyn can fool everybody.
  - $∀yF(Evelyn,y)$
- (c) Everybody can fool somebody.
  - $∀x∃yF(x,y)$
- (d) There is no one who can fool everybody.
  - $¬∃x∀yF(x,y)$
- (e) Everyone can be fooled by somebody.
  - $∀y∃xF(x,y)$
- (f) No one can fool both Fred and Jerry.
  - $¬∃x(F(x,Fred) ∧ F(x,Jerry))$
- (g) Nancy can fool exactly two people.
  - ❌ $∃yF(Nancy,y) ∧ ∃zF(Nancy,z) ∧ (y ≠ z) ∧ (¬∃w(F(Nancy,w)) ∧ (w ≠ y) ∧ (w ≠ z))$
  - $∃y1∃y2(F (Nancy, y1 ) ∧ F (Nancy, y2 ) ∧ y1 ≠ y2 ∧ ∀y(F (Nancy, y) → (y = y1 ∨ y = y2)))$
- (h) There is exactly one person whom everybody can fool.
  - $∃y(∀xF(x,y) ∧ ∀z(∀wF(w,z) → z = y))$
- (i) No one can fool himself or herself.
  - $¬∃xF(x,x)$
- (j) There is someone who can fool exactly one person besides himself or herself.
  - ❌ $∃x∃y(F(x,y) → (∀z(F(x,z) → (x = z) ∨ )))$
  - $∃x∃y(x ≠ y ∧ F(x, y) ∧ ∀z((F(x, z) ∧ z ≠ x) → z = y))$

11. Let S(x) be the predicate “x is a student,” F (x) the predicate “x is a faculty member,” and A(x, y) the predicate “x has asked y a question,” where the domain consists of all people associated with your school. Use quantifiers to express each of these statements.
- (a) Lois has asked Professor Michaels a question.
  - $A(Lois,Michaels)$
- (b) Every student has asked Professor Gross a question.
  - $∀x(S(x) → A(x,Gross))$
- (c) Every faculty member has either asked Professor Miller a question or been asked a question by Professor Miller.
  - $∀x(F(x) → (A(x,Miller) ∨ A(Miller,x)))$
- (d) Some student has not asked any faculty member a question.
  - $∃x(S(x) ∧ ¬∃y(F(y) ∧ A(x,y)))$
- (e) There is a faculty member who has never been asked a question by a student.
  - $∃x(F(x) ∧ ¬∃y(S(y) ∧ A(y,x)))$
- (f) Some student has asked every faculty member a question.
  - $∃x(S(x) ∧ ∀y(F(y) → A(x,y)))$
- (g) There is a faculty member who has asked every other faculty member a question.
  - ❌ $∃x∀y(x≠y ∧ F(x) ∧ A(x,y))$
  - ❎ $∃x(F(x) ∧ ∀y(F(y) ∧ x ≠ y → A(x,y)))$
- (h) Some student has never been asked a question by a faculty member.
  - = $∃y(S(y) ∧ ¬∃x(F(x) ∧ A(x,y)))$
  - $∃y(S(y) ∧ ∀x(F(x) → ¬A(x,y)))$

12. Let I (x) be the statement “x has an Internet connection” and C(x, y) be the statement “x and y have chatted over the Internet,” where the domain for the variables x and y consists of all students in your class. Use quantifiers to express each of these statements.
- (a) Jerry does not have an Internet connection.
  - $¬I(Jerry)$
- (b) Rachel has not chatted over the Internet with Chelsea.
  - $¬C(Rachel,Chelsea)$
- (c) Jan and Sharon have never chatted over the Internet.
  - $¬C(Jan,Sharon)$
- (d) No one in the class has chatted with Bob.
  - $¬∃xC(x,Bob)$
- (e) Sanjay has chatted with everyone except Joseph.
  - $∀y((y ≠ Bob) → C(Sanjay,y))$
- (f) Someone in your class does not have an Internet connection.
  - $∃x¬I(x)$
- (g) Not everyone in your class has an Internet connection.
  - $¬∀xI(x)$
- (h) Exactly one student in your class has an Internet connection.
  - $∃x(I(x) ∧ ∀y((y ≠ x) → ¬I(y)))$
- (i) Everyone except one student in your class has an Internet connection.
  - $∃x∀y((x ≠ y) ↔ I(x))$
- (j) Everyone in your class with an Internet connection has chatted over the Internet with at least one other student in your class.
  - ❌ $∀x(I(x) → ∃yC(x,y))$
  - ❎ $∀x(I(x) → ∃y(x ≠ y ∧ C(x,y)))$
- (k) Someone in your class has an Internet connection but has not chatted with anyone else in your class.
  - $∃x∀y(I(x) ∧ (x ≠ y → ¬C(x,y)))$
- (l) There are two students in your class who have not chatted with each other over the Internet.
  - ❌ $∃x∃y(¬C(x,y))$
  - ❎ $∃x∃y(x ≠ y ∧ ¬C(x,y))$
- (m) There is a student in your class who has chatted with everyone in your class over the Internet.
  - $∃x∀yC(x,y)$
- (n) There are at least two students in your class who have not chatted with the same person in your class.
  - $∃x∃y(x ≠ y ∧ ¬∀z(C(x,z) ∧ C(y,z)))$
- (o) There are two students in the class who between them have chatted with everyone else in the class.
  - ❌ $∃x∃y∀z((x ≠ z ∧ y ≠ z) → C(x,z) ∧ C(y,z))$
  - ❎ $∃x∃y(x ≠ y ∧ ∀z(C(x, z) ∨ C(y, z)))$

13. Let M(x, y) be “x has sent y an e-mail message” and T (x, y) be “x has telephoned y,” where the domain consists of all students in your class. Use quantifiers to express each of these statements. (Assume that all e-mail messages that were sent are received, which is not the way things often work.)
- (a) Chou has never sent an e-mail message to Koko.
  - $¬M(Chou,Koko)$
- (b) Arlene has never sent an e-mail message to or telephoned Sarah.
  - $¬M(Arlene,Sarah) ∧ ¬T(Arlene,Sarah)$
- (c) José has never received an e-mail message from Deborah.
  - $¬M(Deborah,Jose)$
- (d) Every student in your class has sent an e-mail message to Ken.
  - $∀x(x ≠ Ken → M(x,Ken))$
- (e) No one in your class has telephoned Nina.
  - ❌ $¬∀xT(x,Nina)$
  - ❎ $∀x¬T(x,Nina)$
- (f) Everyone in your class has either telephoned Avi or sent him an e-mail message.
  - $∀x(M(x,Avi) ∨ T(x,Avi))$
- (g) There is a student in your class who has sent everyone else in your class an e-mail message.
  - $∃x∀y(x ≠ y → M(x,y))$
- (h) There is someone in your class who has either sent an e-mail message or telephoned everyone else in your class.
  - $∃x∀y(x ≠ y → (M(x,y) ∨ T(x,y)))$
- (i) There are two different students in your class who have sent each other e-mail messages.
  - $∃x∃y(x ≠ y ∧ M(x,y) ∧ M(y,x))$
- (j) There is a student who has sent himself or herself an e-mail message.
  - $∃xM(x,x)$
- (k) There is a student in your class who has not received an e-mail message from anyone else in the class and who has not been called by any other student in the class.
  - $∃x∀y(x ≠ y → (¬M(y,x) ∧ ¬T(y,x)))$
- (l) Every student in the class has either received an email message or received a telephone call from another student in the class.
  - $∀x∃y(x ≠ y ∧ (M(y,x) ∨ T(y,x)))$
- (m) There are at least two students in your class such that one student has sent the other e-mail and the second student has telephoned the first student.
  - $∃x∃y(x ≠ y ∧ M(x,y) ∧ T(y,x))$
- (n) There are two different students in your class who between them have sent an e-mail message to or telephoned everyone else in the class.
  - ❌ $∃x∃y(x ≠ y ∧ ∀z((M(x,z) ∨ T(x,z)) ∧ (M(y,z) ∨ T(y,z))))$
  - ❎ $∃x∃y(x ≠ y ∧ ∀z((z ≠ x ∧ z ≠ y) → (M(x,z) ∨ T(x,z)) ∨ (M(y,z) ∨ T(y,z))))$

14. Use quantifiers and predicates with more than one variable to express these statements.
- (a) There is a student in this class who can speak Hindi.
  - $∃xS(x, Hindi)$
- (b) Every student in this class plays some sport.
  - $∀x∃yS(x,y)$
- (c) Some student in this class has visited Alaska but has not visited Hawaii.
  - $∃x(V(x,Alaska) ∧ ¬V(x,Hawaii))$
- (d) All students in this class have learned at least one programming language.
  - $∀x∃yL(x,y)$
- (e) There is a student in this class who has taken every course offered by one of the departments in this school.
  - ❌ $∃x∃y∀zC(x,z)$
  - ❎ $∃x∃z∀y(O(y, z) → T (x, y))$
- (f) Some student in this class grew up in the same town as exactly one other student in this class.
  - ❌ $∃x∃y(x ≠ y ∧ G(x,y) ∧ ∀z(z ≠ y → ¬G(x,z)))$
  - ❎ $∃x∃y(x ≠ y ∧ G(x,y) ∧ ∀z(G(x,z) → (x = y ∨ x = z)))$
- (g) Every student in this class has chatted with at least one other student in at least one chat group.
  - $∀x∃y∃z(x ≠ y ∧ C(x,y,z))$

15. Use quantifiers and predicates with more than one variable to express these statements.
- (a) Every computer science student needs a course in discrete mathematics.
  - ❌ $∀x(C(x) → M(x))$
  - ❎ $∀xN(x,disMath)$
  - ✅ $∀x(CS-Student(x) → Course-Needed(DiscreteMath))$
- (b) There is a student in this class who owns a personal computer.
  - $∃xO(x,PC)$
- (c) Every student in this class has taken at least one computer science course.
  - $∀x∃yC(x,y)$
- (d) There is a student in this class who has taken at least one course in computer science.
  - $∃x∃yC(x,y)$
- (e) Every student in this class has been in every building on campus.
  - $∀x∀yB(x,y)$
- (f) There is a student in this class who has been in every room of at least one building on campus.
  - $∃x∃y∀zR(x,y,z)$
- (g) Every student in this class has been in at least one room of every building on campus.
  - $∀x∀y∃zR(x,y,z)$

16. A discrete mathematics class contains 1 mathematics major who is a freshman, 12 mathematics majors who are sophomores, 15 computer science majors who are sophomores, 2 mathematics majors who are juniors, 2 computer science majors who are juniors, and 1 computer science major who is a senior. Express each of these statements in terms of quantifiers and then determine its truth value.
- (a) There is a student in the class who is a junior.
  - $∃xJ(x)$: T
- (b) Every student in the class is a computer science major.
  - $∀xM(x,CS)$: F
- (c) There is a student in the class who is neither a mathematics major nor a junior.
  - $∃x∀y(¬M(x,Math) ∧ ¬J(x,y))$: T
- (d) Every student in the class is either a sophomore or a computer science major.
  - $∀x∀y(S(x,y) ∨ M(x,CS))$: F
- (e) There is a major such that there is a student in the class in every year of study with that major.
  - $∃m∀y∃s(S(m,s) ∧ Y(s,y))$: F

17. Express each of these system specifications using predicates, quantifiers, and logical connectives, if necessary.
- (a) Every user has access to exactly one mailbox.
  - $∀x∃y(A(x,y) ∧ ∀z(y ≠ z → ¬A(x,z)))$
- (b) There is a process that continues to run during all error conditions only if the kernel is working correctly.
  - $∃p∀e(R(p,e) → K)$
- (c) All users on the campus network can access all websites whose url has a .edu extension.
  - $∀u∀w(E(w,'.edu') → A(u,w))$
- (d) (∗) There are exactly two systems that monitor every remote server.
  - ❌ $∃s_1∃s_2(s_1 ≠ s_2 ∧ ∀r(M(s_1,r) ∧ M(s_2,r) ∧ ∀s(M(s,r) → (s = s_1 ∨ s = s_2))))$
  - ❎⚠️ $∃s_1∃s_2(s_1 ≠ s_2 ∧ ∀s((∀rM(s,r)) ↔ (s = s_1 ∨ s = s_2)))$

18. Express each of these system specifications using predicates, quantifiers, and logical connectives, if necessary.
- (a) At least one console must be accessible during every fault condition.
  - $∀x∃yA(x,y)$
- (b) The e-mail address of every user can be retrieved whenever the archive contains at least one message sent by every user on the system.
  - ❌ $∀u(∃m∀vM(m,v) → R(u))$
  - $(∀u∃m (A(m) ∧ S(u, m))) → ∀v R(v)$
- (c) For every security breach there is at least one mechanism that can detect that breach if and only if there is a process that has not been compromised.
  - $∀b∃m(D(m,b) ↔ ∃pU(p))$
- (d) There are at least two paths connecting every two distinct endpoints on the network.
  - ❌ $∀e_1∃e_2(e_1 ≠ e_2 ∧ ∃p_1∃p_2(p_1 ≠ p_2 ∧ C(p_1,p_2,e_1,e_2)))$
  - ❎ $∀e_1∀e_2(e_1 ≠ e_2 → ∃p_1∃p_2(p_1 ≠ p_2 ∧ C(p_1,e_1,e_2) ∧ C(p_2,e_1,e_2)))$
- (e) No one knows the password of every user on the system except for the system administrator, who knows all passwords.
  - ❌ $∀x∀p(K(x,p) → A(x))$
  - ❎ $∀x((∀u K(x, u)) ↔ x = SysAdm)$

19. Express each of these statements using mathematical and logical operators, predicates, and quantifiers, where the domain consists of all integers.
- (a) The sum of two negative integers is negative.
  - $∀x∀y((x < 0 ∧ y < 0) → (x + y < 0))$
- (b) The difference of two positive integers is not necessarily positive.
  - $∀x∀y((x > 0 ∧ y > 0) → ((x - y < 0) ∨ (x - y > 0)))$
- (c) The sum of the squares of two integers is greater than or equal to the square of their sum.
  - $∀x∀y(x² + y² \geq (x + y)²)$
- (d) The absolute value of the product of two integers is the product of their absolute values.
  - $∀x∀y(|xy| = |x||y|)$

20. Express each of these statements using predicates, quantifiers, logical connectives, and mathematical operators where the domain consists of all integers.
- (a) The product of two negative integers is positive.
  - $∀x∀y((x < 0) ∧ (y < 0) → (xy > 0))$
- (b) The average of two positive integers is positive.
  - $∀x∀y((x > 0) ∧ (y > 0) → ({x + y \over 2} > 0))$
- (c) The difference of two negative integers is not necessarily negative.
  - $¬∀x∀y((x < 0) ∧ (y < 0) → (x - y < 0))$
- (d) The absolute value of the sum of two integers does not exceed the sum of the absolute values of these integers.
  - $∀x∀y(|x + y| \leq |x| + |y|)$

21. Use predicates, quantifiers, logical connectives, and mathematical operators to express the statement that every positive integer is the sum of the squares of four integers.
- $∀x∃i_1∃i_2∃i_3∃i_4(x > 0 → (x = i_1² + i_2² + i_3² + i_4²))$

22. Use predicates, quantifiers, logical connectives, and mathematical operators to express the statement that there is a positive integer that is not the sum of three squares.
    - ❌ $∃x∃a∃b∃c(x > 0 → x ≠ a² + b² + c²)$
    - ❎ $∃x∀a∀b∀c(x > 0 → x ≠ a² + b² + c²)$

23. Express each of these mathematical statements using predicates, quantifiers, logical connectives, and mathematical operators.
- (a) The product of two negative real numbers is positive.
  - $∀x∀y((x < 0) ∧ (y < 0) → xy > 0)$
- (b) The difference of a real number and itself is zero.
  - $∀x(x - x = 0)$
- (c) Every positive real number has exactly two square roots.
  - ❌ $∀x(x > 0 → ∃a∃b((a ≠ b) ∧ ∀c(c = a ∨ c = b) ∧ (\sqrt{x} = a ∨ \sqrt{x} = b)))$
  - ❎ $∀x∃a∃b(a ≠ b ∧ ∀c(c² = x) ↔ (c = a ∨ c = b))$
- (d) A negative real number does not have a square root that is a real number.
  - ✅ $∀x¬∃y(x < 0 ∧ \sqrt{x} = y)$
  - ❎ $∀x(x < 0 → ¬∃y(x = y²))$

24. Translate each of these nested quantifications into an English statement that expresses a mathematical fact. The domain in each case consists of all real numbers.
- (a) $∃x∀y(x + y = y)$
  - There is a number whose sum with any other is equal to that other number.
- (b) $∀x∀y(((x ≥ 0) ∧ (y < 0)) → (x − y > 0))$
  - For any two numbers the difference is greater 0 if the first one is greater than or equal to 0 and the second one is negative.
- (c) $∃x∃y(((x ≤ 0) ∧ (y ≤ 0)) ∧ (x − y > 0))$
  - There is at least one pair of numbers whose difference is positive if both are smaller than or equal to 0.
- (d) $∀x∀y((x ≠ 0) ∧ (y ≠ 0) ↔ (xy ≠ 0))$
  - The product of two numbers is nonzero if and only if both factors are nonzero.

25. Translate each of these nested quantifications into an English statement that expresses a mathematical fact. The domain in each case consists of all real numbers.
- (a) $∃x∀y(xy = y)$
  - There is a multiplicative identity.
- (b) $∀x∀y(((x < 0) ∧ (y < 0)) → (xy > 0))$
  - The product of negative numbers is positive.
- (c) $∃x∃y((x^2 > y) ∧ (x < y))$
  - There are numbers such that the first one is less than the second one but its square is greater.
- (d) $∀x∀y∃z(x + y = z)$
  - Any two numbers can be summed.

26. Let Q(x, y) be the statement “x + y = x − y.” If the domain for both variables consists of all integers, what are the truth values?
- (a) ❌ $Q(1,1)$ T
- (b) $Q(2,0)$ T
- (c) $∀yQ(1,y)$ F
- (d) $∃xQ(x,2)$ F
- (e) $∃x∃yQ(x,y)$ T
- (f) ❌ $∀x∃yQ(x,y)$ F ❎ T(0)
- (g) $∃y∀xQ(x,y)$ T
- (h) $∀y∃xQ(x,y)$ F
- (i) $∀x∀yQ(x,y)$ F

27. Determine the truth value of each of these statements if the domain for all variables consists of all integers.
- (a) $∀n∃m(n^2 < m)$ T
- (b) ❌ $∃n∀m(n < m^2)$ F ❎ T (n < 0)
- (c) $∀n∃m(n + m = 0)$ T
- (d) $∃n∀m(nm = m)$ T
- (e) $∃n∃m(n^2 + m^2 = 5)$ T
- (f) $∃n∃m(n^2 + m^2 = 6)$ F
- (g) $∃n∃m(n + m = 4 ∧ n − m = 1)$ F
- (h) $∃n∃m(n + m = 4 ∧ n − m = 2)$ T
- (i) $∀n∀m∃p(p = (m + n)/2)$ F

28. Determine the truth value of each of these statements if the domain of each variable consists of all real numbers.
- (a) $∀x∃y(x^2 = y)$ T
- (b) $∀x∃y(x = y^2 )$ ❌ T ❎ F (no such x if y is < 0)
- (c) $∃x∀y(xy = 0)$ T
- (d) $∃x∃y(x + y ≠ y + x)$ ❌ T ❎ F (commutative law of addition)
- (e) $∀x(x ≠ 0 → ∃y(xy = 1))$ T
- (f) $∃x∀y(y ≠ 0 → xy = 1)$ ❌ T ❎ F (the reciprocal of y depends on y-there is not one x that works for all y)
- (g) $∀x∃y(x + y = 1)$ T
- (h) $∃x∃y(x + 2y = 2 ∧ 2x + 4y = 5)$ ❌ T ❎ F (this system of equations is inconsistent)
- (i) $∀x∃y(x + y = 2 ∧ 2x − y = 1)$ F
- (j) $∀x∀y∃z(z = (x + y)/2)$ T

29. Suppose the domain of the propositional function P (x, y) consists of pairs x and y, where x is 1, 2, or 3 and y is 1, 2, or 3. Write out these propositions using disjunctions and conjunctions.
- (a) $∀x∀yP(x,y)$
  - $P(1,1) ∧ P(1,2) ∧ P(1,3) ∧ P(2,1) ∧ P(2,2) ∧ P(2,3) ∧ P(3,1) ∧ P(3,2) ∧ P(3,3)$
- (b) $∃x∃yP(x,y)$
  - $P(1,1) ∨ P(1,2) ∨ P(1,3) ∨ P(2,1) ∨ P(2,2) ∨ P(2,3) ∨ P(3,1) ∨ P(3,2) ∨ P(3,3)$
- (c) $∃x∀yP(x,y)$
  - $(P(1,1) ∧ P(1,2) ∧ P(1,3)) ∨ (P(2,1) ∧ P(2,2) ∧ P(2,3)) ∨ (P(3,1) ∧ P(3,2) ∧ P(3,3))$
- (d) $∀y∃xP(x,y)$
  - $(P(1,1) ∨ P(2,1) ∨ P(3,1)) ∧ (P(1,2) ∨ P(2,2) ∨ P(3,2)) ∧ (P(1,3) ∨ P(2,3) ∨ P(3,3))$

30. Rewrite each of these statements so that negations appear only within predicates (that is, so that no negation is outside a quantifier or an expression involving logical connectives).
- (a) $¬∃y∃xP(x,y)$
  - $∀y∀x¬P(x,y)$
- (b) $¬∀x∃yP(x,y)$
  - $∃x∀y¬P(x,y)$
- (c) $¬∃y(Q(y) ∧ ∀x¬R(x,y))$
  - $∀y(¬Q(y) ∨ ∃xR(x,y))$
- (d) $¬∃y(∃xR(x,y) ∨ ∀xS(x,y))$
  - $∀y(∀x¬R(x,y) ∧ ∃x¬S(x,y))$
- (e) $¬∃y(∀x∃zT(x,y,z) ∨ ∃x∀zU(x,y,z))$
  - $∀y(∃x∀z¬T(x,y,z) ∧ ∀x∃z¬U(x,y,z))$

31. Express the negations of each of these statements so that all negation symbols immediately precede predicates.
- (a) $∃x∀y∃z¬T(x,y,z)$
- (b) $∃x∀y¬P(x,y) ∧ ∃x∀y¬Q(x,y)$
- (c) $∃x∀y(¬P(x,y) ∨ ∀z¬R(x,y,z))$
- (d) $∃x∀y(P(x,y) ∧ ¬Q(x,y))$

32. Express the negations of each of these statements so that all negation symbols immediately precede predicates.
- (a) $∃z∀y∀xT(x,y,z)$
  - $∀z∃y∃x¬T(x,y,z)$
- (b) $∃x∃yP (x, y) ∧ ∀x∀yQ(x, y)$
  - ❌ $∀x∀y¬P(x,y) ∧ ∃x∃y¬Q(x,y)$
  - ❎ $∀x∀y¬P(x,y) ∨ ∃x∃y¬Q(x,y)$
- (c) $∃x∃y(Q(x,y) ↔ Q(y,x))$
  - $∀x∀y(Q(x,y) ↔ ¬Q(y,x))$
- (d) $∀y∃x∃z(T(x,y,z) ∨ Q(x,y))$
  - $∃y∀x∀z(¬T(x,y,z) ∧ ¬Q(x,y))$

33. Rewrite each of these statements so that negations appear only within predicates (that is, so that no negation is outside a quantifier or an expression involving logical connectives).
- (a) $¬∀x∀yP (x, y)$
- (b) $¬∀y∃xP (x, y)$
- (c) $¬∀y∀x(P (x, y) ∨ Q(x, y))$
- (d) $¬(∃x∃y¬P (x, y) ∧ ∀x∀yQ(x, y))$
- (e) $¬∀x(∃y∀zP (x, y, z) ∧ ∃z∀yP (x, y, z))$

34. Find a common domain for the variables x, y, and z for which the statement ∀x∀y((x ≠ y) → ∀z((z = x) ∨ (z = y))) is true and another domain for which it is false.
- ❓ $∀x∀y((x ≠ y) → ∀z((z = x) ∨ (z = y)))$
  - T: ❌ Integers, real numbers,...
  - T: ❎ any domain with one or two elements
  - F: ❎ any domain with more than two elements
  - ❎ The statemants says that, whenever you have two unequal objects, any object has to be one of those two. It is vacuously true for domains with one element.

35. Find a common domain for the variables x, y, z, and w for which the statement ∀x∀y∀z∃w((w ≠ x) ∧ (w ≠ y) ∧ (w ≠ z)) is true and another common domain for these variables for which it is false.
    - $∀x∀y∀z∃w((w ≠ x) ∧ (w ≠ y) ∧ (w ≠ z))$
      - T: any set with more than 3 objects
      - F: any set with no more than 3 objects

36. Express each of these statements using quantifiers. Then form the negation of the statement so that no negation is to the left of a quantifier. Next, express the negation in simple English. (Do not simply use the phrase “It is not the case that.”)
- (a) No one has lost more than one thousand dollars playing the lottery.
  - ✅ $¬∃xL(x,1000)$
  - ❌ $∀x¬L(x,1000)$
  - ❌ Everone has lost more than 1000$.
  - ❎ $¬∃x∃y(y > 1000 ∧ L(x, y))$
  - ❎ $∃x∃y(y > 1000 ∧ L(x, y))$
  - ❎ someone has lost more than $1000 playing the lottery.
- (b) There is a student in this class who has chatted with exactly one other student.
  - ❌ $∃x∃y(x ≠ y ∧ ∀z(y = z → C(x,y)))$
  - ❌ $∀x∀y(x = y ∨ ∃z(y = z ∧ ¬C(x,y)))$
  - ❌ All students are either the same person or there is a person in a pair that has not chatted with any other.
  - ❎ $∃x∃y(y ≠ x ∧ ∀z(z ≠ x → (z = y ↔ C(x, z))))$
  - ❎ $∀x∀y(y ≠ x → ∃z(z ≠ x ∧ ¬(z = y ↔ C(x, z))))$
  - ❎ everybody in this class has either chatted with no one else or has chatted with two or more others.
- (c) No student in this class has sent e-mail to exactly two other students in this class.
  - ❌ $¬∃x∃y(x ≠ y ∧ ∃z((z ≠ x ∧ z ≠ y) ∧ E(z,x) ∧ E(z,y)))$
  - ❌ $∃x∃y(x ≠ y ∧ ∃z((z ≠ x ∧ z ≠ y) ∧ E(z,x) ∧ E(z,y)))$
  - There is a student that has sent email to exactly two others.
  - ❎ $¬∃x∃y∃z(y ≠ z ∧ x ≠ y ∧ x ≠ z ∧ ∀w(w ≠ x → (E(x, w) ↔ (w = y ∨ w = z))))$
  - ❎ $∃x∃y∃z(y ≠ z ∧ x ≠ y ∧ x ≠ z ∧ ∀w(w ≠ x → (E(x, w) ↔ (w = y ∨ w = z))))$
- (d) Some student has solved every exercise in this book.
  - $∃x∀yE(x,y)$
  - $∀x∃y¬E(x,y)$
  - ❌ No student has solved any exercise in the book.
  - ❎ For every student there is an exercise that he has not solved.
- (e) No student has solved at least one exercise in every section of this book.
  - ❌ $¬∃x∃e∀s(S(x,e) ∧ B(e,s))$
  - ❌ $∃x∃e∀s(S(x,e) ∧ B(e,s))$
  - There is a student that has solved every exercise.
  - ❎ $¬∃x∀s∃e(S(x,e) ∧ B(e,s))$

37. Express each of these statements using quantifiers. Then form the negation of the statement so that no negation is to the left of a quantifier. Next, express the negation in simple English. (Do not simply use the phrase “It is not the case that.”)
- (a) Every student in this class has taken exactly two mathematics classes at this school.
  - ✅ $∀x∃y∃z(y ≠ z ∧ ∀w((w = y ∨ w = z) ↔ C(x,w)))$
  - ✅ $∃x∀y∀z(y = z ∨ ∃w¬((w = y ∨ w = z) ↔ C(x,w)))$
  - ❌ There is a student for which there is a math class that he has not taken.
  - ❎ $∀x∃y∃z(y ≠ z ∧ C(x,y) ∧ C(x,z) ∧ ∀w(C(x,w) → (w = y ∨ w = z)))$
  - ❎ $∃x∀y∀z(y = z ∨ ¬C(x,y) ∨ ¬C(x,z) ∨ ∃w(C(x,w) ∧ (w ≠ y ∨ w ≠ z)))$
  - ❎ $∃x∀y∀z(y ≠ z → (¬C(x,y) ∨ ¬C(x,z) ∨ ∃w(C(x,w) ∧ (w ≠ y ∨ w ≠ z))))$
  - ❎ There is someone in this class for whom no matter which two distinct math courses you consider, these are not the two and only two math courses this person has taken.
- (b) Someone has visited every country in the world except Libya.
  - ❌ $∃x∀y(V(x,y) → y ≠ Lybia)$
  - ❌ $∀x∃y(V(x,y) ∧ y = Lybia)$
  - ❌ Everyone has visited Lybia.
  - ❎ $∃x∀y(V(x,y) ↔ y ≠ Lybia)$
  - ❎ $∀x∃y(V(x,y) ↔ y = Lybia)$
  - ❎ For every person, either that person has visited Lybia or else that person has failed to visit some country other than Lybia.
- (c) No one has climbed every mountain in the Himalayas.
  - $¬∃x∀yC(x,y)$
  - $∃x∀yC(x,y)$
  - There is a person...
- (d) Every movie actor has either been in a movie with Kevin Bacon or has been in a movie with someone who has been in a movie with Kevin Bacon.
  - ❌ $∀x(M(x,Bacon) ∨ ∃y(M(y,Bacon) ∧ M(x,y)))$
  - ❎ $∀x(∃zM(x,Bacon,z) ∨ ∃y∃z_1∃z_2(M(x,y,z_1) ∧ M(y,Bacon,z_2)))$

38. Express the negations of these propositions using quantifiers, and in English.
- (a) Every student in this class likes mathematics.
  - $¬∀xL(x)$
  - Not every student...
- (b) There is a student in this class who has never seen a computer.
  - $∀xC(x)$
  - Every student has seen a computer.
- (c) There is a student in this class who has taken every mathematics course offered at this school.
  - $∀x∃y¬C(x,y)$
  - For ever student there is a course he has not taken.
- (d) There is a student in this class who has been in at least one room of every building on campus.
  - $∀x∃y∀z¬R(x,z,y)$
  - For every student there is a building in which that student hasnt been in any room.

39. Find a counterexample, if possible, to these universally quantified statements, where the domain for all variables consists of all integers.
- (a) $∀x∀y(x^2 = y^2 → x = y)$ (1,-1)
- (b) $∀x∃y(y^2 = x)$ (2,_)
- (c) $∀x∀y(xy ≥ x)$ (1,-1)

40. Find a counterexample, if possible, to these universally quantified statements, where the domain for all variables consists of all integers.
- (a) $∀x∃y(x = 1/y)$ (1,3)
- (b) $∀x∃y(y^2 − x < 100)$ (0,10)
- (c) $∀x∀y(x^2 ≠ y^3 )$ (1,1)

41. Use quantifiers to express the associative law for multiplication of real numbers.
    - ❌ $∀x∀y∀z(x * y = z ∧ y * z = x)$
    - ❎ $∀x∀y∀z((x * y) * z = x * (y * z))$

42. Use quantifiers to express the distributive laws of multiplication over addition for real numbers.
    - $∀x∀y∀z(x * (y + z) = xy + xz)$

43. Use quantifiers and logical connectives to express the fact that every linear polynomial (that is, polynomial of degree 1) with real coefficients and where the coefficient of x is nonzero, has exactly one real root.
    - ❌ $∀x∀m∀b(m ≠ 0 → ∃z(z² = mx + b ∧ ∀w(w = z)))$
    - ❎ $∀m∀b(m ≠ 0 → ∃x(mx + b = 0 ∧ ∀w(mw + b = 0 → w = x)))$

44. ❓ Use quantifiers and logical connectives to express the fact that a quadratic polynomial with real number coefficients has at most two real roots.
    - ❎ $∀a∀b∀c(a ≠ 0 → ∀x_1∀x_2∀x_3 (ax^2_1 + bx_1 + c = 0 ∧ ax^2_2 + bx_2 + c = 0 ∧ ax^2_3 + bx_3 + c = 0) → (x_1 = x_2 ∨ x_1 = x_3 ∨ x_2 = x_3 ))$

45. Determine the truth value of the statement $∀x∃y(xy = 1)$ if the domain for the variables consists of
- (a) the nonzero real numbers. T
- (b) the nonzero integers. F
- (c) the positive real numbers. T

46. Determine the truth value of the statement $∃x∀y(x ≤ y 2)$ if the domain for the variables consists of
- (a) the positive real numbers. F
- (b) the integers. T (0)
- (c) the nonzero real numbers. ❌ F ❎ T (ex. x=-1)

47. Show that the two statements $¬∃x∀yP(x, y)$ and $∀x∃y¬P(x, y)$, where both quantifiers over the first variable in P (x, y) have the same domain, and both quantifiers over the second variable in P (x, y) have the same domain, are logically equivalent.
- Both examples can be derived from another by moving the negation from the whole expression to the predicate and vice versa.

48. (∗) Show that $∀xP(x) ∨ ∀xQ(x)$ and $∀x∀y(P(x) ∨ Q(y))$, where all quantifiers have the same nonempty domain, are logically equivalent. (The new variable y is used to combine the quantifications correctly.)
    - ❌ Since the domain is the same for all quantifiers it doesnt matter if the variable is quantified seperately for every predicate or if two different variables are quantified for the whole expression.
    - ❎ We need to show that each of these propositions implies the other.
    - If $∀xP(x) ∨ ∀xQ(x)$ then $∀x∀y(P(x) ∨ Q(y))$: By our hypothesis, one of two things must be true. Either P is universally true, or Q is universally true. In the first case $∀x∀y(P(x) ∨ Q(y))$ is true, since the first expression in the disjunction is true, no matter what x and y are.
    - If $∀x∀y(P(x) ∨ Q(y))$ then $∀xP(x) ∨ ∀xQ(x)$: If $∀xP(x)$ is true, then we are done. Otherwise, $P(x_0)$ must be false for some $x_0$ in the domain. For this $x_0$, then, the hypothesis tells us that $P(x_0) ∨ Q(y)$ is true, no matter what y is. Since $P(x_0)$ is false, it must be the case that $Q(y)$ is true for each y. In other words, $∀yQ(y)$ is true, or, to change the name of the variable $∀xQ(x)$ is true. This certainly implies that $∀xP(x) ∨ ∀xQ(x)$ as desired.

49. (∗)
- (a) Show that $∀xP(x) ∧ ∃xQ(x)$ is logically equivalent to $∀x∃y(P(x) ∧ Q(y))$, where all quantifiers have the same nonempty domain.
  - ❌ Assuming the first expression is true the conjunction of both prediacates in the second expressions will also be true.
  - ❎ We prove this by arguing that whenever the first proposition is true, so is the second; and whenever the second proposition is true, so is the first. So suppose $∀xP(x) ∧ ∃xQ(x)$ is true. In particular, P always holds, and there is some object, call it y, in the domain that makes Q true. Now to show that the second proposition is true, suppose that x is any object in the domain. By our assumptions, P(x) is true. Furthermore, Q(y) is true for the particular y we mentioned above. Therefore $P(x) ∧ Q(y)$ is true for this x and y. Since x was arbitrary, we have showed that $∀x∃y(P(x) ∧ Q(y))$ is true, as desired.
  Conversely, suppose that the second proposition is true. ⚠️ Letting x be any member of the domain allows us to assert that there exists a y such that $P(x) ∧ Q(y)$ ⚠️ is true and therefore $Q(y)$ is true. Thus by definition of existential quantifiers, $∃yQ(y)$ holds, and thus the first proposition is true.
- (b) ❓ Show that $∀xP(x) ∨ ∃xQ(x)$ is equivalent to $∀x∃y (P(x) ∨ Q(y))$, where all quantifiers have the same nonempty domain.
  - ❎ Suppose that $∀xP(x) ∨ ∃xQ(x)$ is true. Thus either P always holds, or there is some object, call it y, in the domain that makes Q true. In the first case it follows that $P(x) ∨ Q(y)$ is true for all x, and so we can conclude that $∀x∃y (P(x) ∨ Q(y))$ is true (it does not matter in this case whether Q(y) is true or not).
  In the second case, Q(y) is true for this particular y, and so $P(x) ∨ Q(y)$ is true regardless of what x is. Again, it follows that $∀x∃y (P(x) ∨ Q(y))$ is true.
  Conversly, suppose that the second proposition is true. If P(x) is true for all x, then the first proposition must be true. If not, then P(x) fails for some x, but for this x there must be a y such that $P(x) ∨ Q(y)$ is true; hence Q(y) must be true. Therefore $∃xQ(x)$ holds, and thus the first proposition is true.

A statement is in prenex normal form (PNF) if and only if it is of the form
$$Q_1 x_1 Q_2 x_2 · · · Q_k x_k P (x_1, x_2 , . . . , x_k )$$
where each $Q_i , i = 1, 2, . . . , k$, is either the existential quantifier or the universal quantifier, and $P(x_1, . . . , x_k)$ is a predicate involving no quantifiers. For example, $∃x∀y(P(x, y) ∧ Q(y))$ is in prenex normal form, whereas $∃xP(x) ∨ ∀xQ(x)$ is not (because the quantifiers do not all occur first).

Every statement formed from propositional variables, predicates, T, and F using logical connectives and quantifiers is equivalent to a statement in prenex normal form. Exercise 51 asks for a proof of this fact.

50. (∗) Put these statements in prenex normal form. [Hint: Use logical equivalence from Tables 6 and 7 in Section 1.3, Table 2 in Section 1.4, Example 19 in Section 1.4, Exercises 45 and 46 in Section 1.4, and Exercises 48 and 49.]
- (a) $∃xP(x) ∨ ∃xQ(x) ∨ A$, where A is a proposition not involving any quantifiers.
  - $∃x_1∃x_2(P(x_1) ∨ Q(x_2) ∨ A)$
  - $∃x(P(x) ∨ Q(x) ∨ A)$
- (b) $¬(∀xP(x) ∨ ∀xQ(x))$
  - ✅ $∃x¬P(x) ∧ ∃x¬Q(x)$
  - ❌ $∃x(¬P(x) ∧ ¬Q(x))$
  - ❎ $¬(∀x∀y(P(x) ∨ Q(y)))$
  - ❎ $∃x∃y¬(P(x) ∨ Q(y))$
- (c) $∃xP(x) → ∃xQ(x)$
  - $∀x¬P(x) ∨ ∃xQ(x)$
  - $∀x_1∃x_2(¬P(x) ∨ Q(x))$

51. ❓ (∗∗) Show how to transform an arbitrary statement to a statement in prenex normal form that is equivalent to the given statement. (Note: A formal solution of this exercise requires use of structural induction, covered in Section 5.3.)
- ❎ Proof by induction (Sections 5.1-5.3), where we show how an expression can be put into prenex normal form if its subexpressions can. First we invoke the result from  45/1.3 WLOG: ¬ and ∨ form a functionally complete collection of logical operators. Then every proposition must either be a single variable, a disjunction, a negation or a quantification of a predicate. (We are assuming that the logical operators are defined for predicates as well.)
Now every proposition that involves no quantifiers is already in PNF (base case of induction). Next suppose that our proposition is of the form $QxP(x)$. Then $P(x)$ is a shorter expression than the given proposition, so (by the inductive hypothesis) we can put it into PNF, with all of its quantifiers coming at the beginning. Then $Qx$ followed by this PNF is again in PNF and equivalent to the original proposition. Next suppose that our proposition is of the form $¬P$. Again, we invoke the inductive hypothesis and assume that P is already in PNF. We now slide the negation symbol past all the quantifiers, using equivalences (Table 2, 1.4).
Finally, suppose we have a disjunction, $P ∨ Q$, each of which can (by hypothesis) be assumed to be in PNF. There are several cases. If only one of P and Q has quantifiers, then we invoke the result of 46/1.4 to bring the quantifier in front of both. We then apply our process to what remains. For example, $P∨∀xQ(x)$ is equivalent to $∀x(P∨Q(x))$. Another case is that the proposition might look like $∃xR(x)∨∃xS(x)$. In this case, by 45/1.4, the proposition is equivalent to $∃x(R(x)∨S(x))$. Once again, by the inductive hypothesis we can then put $R(x)∨S(x)$ into PNF, so the entire proposition can be put into PNF. Similarly, using 48/1.5 we can transform $∀xR(x)∨∀xS(x)$ into the equivalent $∀x∀y(R(x)∨S(y))$; putting $R(x)∨S(y)$ into PNF then brings the entire proposition into PNF. Finally if the proposition is of the form $∀xR(x)∨∃xQ(y)$, then we invoke 49b/1.5 and apply the same construction.
Note that this proof actually gives us the process for finding the proposition in PNF equivalent to the given proposition-we just work from the inside out, dealing with one logical operation or quantifier at a time. (See SSG for example)

52. (∗) Express the quantification $∃!xP(x)$, introduced in Section 1.4, using universal quantifications, existential quantifications, and logical operators.
    - $∃x∀y(x = y ↔ P(x))$
    - ❎ $∃x(P(x) ∧ ∀y(P(x) → y=x))$
