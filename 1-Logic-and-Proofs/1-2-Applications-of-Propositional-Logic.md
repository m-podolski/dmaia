# 1.2 Applications of Propositional Logic

## Exercises

1. You cannot edit a protected Wikipedia entry unless you are an administrator. Express your answer in terms of e: “You can edit a protected Wikipedia entry” and a: “You are an administrator.”

    - $\neg a \implies \neg e$

3. **You can graduate only if you have completed the require- ments of your major and you do not owe money to the university and you do not have an overdue library book. Express your answer in terms of g: “You can graduate,” m: “You owe money to the university,” r: “You have com- pleted the requirements of your major,” and b: “You have an overdue library book.”**

    - !!! $(r \land \neg m \land \neg b) \implies g$
    - $g \implies (r \land \neg m \land \neg b)$

5. **You are eligible to be President of the U.S.A. only if you are at least 35 years old, were born in the U.S.A, or at the time of your birth both of your parents were citizens, and you have lived at least 14 years in the country. Express your answer in terms of e: “You are eligible to be Pres- ident of the U.S.A.,” a: “You are at least 35 years old,” b: “You were born in the U.S.A,” p: “At the time of your birth, both of your parents where citizens,” and r: “You have lived at least 14 years in the U.S.A.”**

    - !!! $e \implies (a \lor b \lor p) \land r$
    - $e \implies (a \land (b \lor p) \land r)$

7. Express these system specifications using the proposi- tions p “The message is scanned for viruses” and q “The message was sent from an unknown system” together with logical connectives (including negations).

- (a) “The message is scanned for viruses whenever the message was sent from an unknown system.”
  - $q \implies p$
- (b) “The message was sent from an unknown system but it was not scanned for viruses.”
  - $q \land \neg p$
- (c) “It is necessary to scan the message for viruses when- ever it was sent from an unknown system.”
  - $q \implies p$
- (d) “When a message is not sent from an unknown system it is not scanned for viruses.”
  - $\neg q \implies \neg p$

9. **Are these system specifications consistent?**
- “The system is in multiuser state if and only if it is operating normally
- If the system is operating normally, the kernel is functioning
- The kernel is not functioning or the system is in interrupt mode
- If the system is not in multiuser state, then it is in interrupt mode
- The system is not in interrupt mode.”

  - $m$ = The system is in multiuser state
  - $n$ = The system is operating normally
  - $k$ = the kernel is functioning
  - $i$ = the system is in interrupt mode

  - $m \iff n$
  - $n \implies k$
  - $\neg k \lor i$
  - $\neg m \implies i$
  - $\neg i$

11. Are these system specifications consistent?
- “The router can send packets to the edge system only if it supports the new address space.
- For the router to support the new ad- dress space it is necessary that the latest software release be installed.
- The router can send packets to the edge sys- tem if the latest software release is installed,
- The router does not support the new address space.”

  - $s$ = The router can send packets to the edge system
  - $a$ = The router supports the new address space
  - $r$ = the latest software release is installed
  - $s \implies a$
  - $a \implies r$
  - $r \implies s$
  - $\neg a$
  - Yes

13. What Boolean search would you use to look for Web pages about beaches in New Jersey? What if you wanted to find Web pages about beaches on the isle of Jersey (in the English Channel)?

    - beaches new jersey
    - beaches jersey not new

15. (*) Each inhabitant of a remote village always tells the truth or always lies. A villager will give only a “Yes” or a “No” response to a question a tourist asks. Suppose you are a tourist visiting this area and come to a fork in the road. One branch leads to the ruins you want to visit; the other branch leads deep into the jungle. A villager is standing at the fork in the road. What one question can you ask the villager to determine which branch to take?

17. When three professors are seated in a restaurant, the host- ess asks them: “Does everyone want coffee?” The first professor says: “I do not know.” The second professor then says: “I do not know.” Finally, the third professor says: “No, not everyone wants coffee.” The hostess comes back and gives coffee to the professors who want it. How did she figure out who wanted coffee?

    - only the third professor does not want coffee

19. **A says “At least one of us is a knave” and B says nothing.**

    - if A = Knight, then B = Knave
    - !!! B = Knave, A = ?
    - if A = Knave, then A AND B = Knights -> Contradiction
    - A = Knight, B = Knave

20. A says “The two of us are both knights” and B says “A is a knave.”

    - A = T, then B = T
    - A = F, then B T or F
    - B = T, then A = F
    - B = F, then A = T

21. **A says “I am a knave or B is a knight” and B says nothing.**

    - !!! If A = T, then B = F
    - !!! If A = F, then B = F
    - If A = T, then B = T
    - If A = F, then statement is contradictory

23. **A says “We are both knaves” and B says nothing.**

    - $a \land b$
    - !!! A = T, then B = T
    - A = T, then contradiction
    - A = F, then B = T

25. **A says “I am the knight,” B says “I am the knave,” and C says “B is the knight.”**

27. A says “I am the knight,” B says “A is telling the truth,” and C says “I am the spy.”

    - *A = Knight, then B = Spy and C = Knave*
    - A = Knave, then C and B = Spy or Knave
    - A = Spy, then NS (B and C would have to be Knaves)
    - B and C cannot be Knights, therefore A = Knight

29. A says “I am the knight,” B says “I am the knight,” and C says “I am the knight.”

    - All permutations possible; one would be true and the others would lie

31. A says “I am not the spy,” B says “I am not the spy,” and C says “I am not the spy.”

    - impossible because there has to be one lying knave

33. **Steve would like to determine the relative salaries of three coworkers using two facts. First, he knows that if Fred is not the highest paid of the three, then Janice is. Sec- ond, he knows that if Janice is not the lowest paid, then Maggie is paid the most. Is it possible to determine the relative salaries of Fred, Maggie, and Janice from what Steve knows? If so, who is paid the most and who the least? Explain your reasoning.**

    - $(\neg fh \implies jh) \land (\neg jl \implies mh)$

35. **A detective has interviewed four witnesses to a crime. From the stories of the witnesses the detective has con- cluded that if the butler is telling the truth then so is the cook; the cook and the gardener cannot both be telling the truth; the gardener and the handyman are not both lying; and if the handyman is telling the truth then the cook is lying. For each of the four witnesses, can the detective de- termine whether that person is telling the truth or lying? Explain your reasoning.**

    - $b \implies c$
    - !!! $c ⊕ g$
    - $¬(c ∧ g)$ ... $¬c ∨ ¬g$
    - $¬(¬g ∧ ¬h)$ ... $g ∨ h$
    - $h \implies ¬c$

37. Suppose there are signs on the doors to two rooms. The
sign on the first door reads “In this room there is a lady, and in the other one there is a tiger”; and the sign on the second door reads “In one of these rooms, there is a lady, and in one of them there is a tiger.” Suppose that you know that one of these signs is true and the other is false. Behind which door is the lady?

    - 1: A = Lady, B = Tiger
    - 2: X = Lady XOR Tiger
    - 1 true, 2 false: 1 invalidates 2
    - 2 true, 1 false: valid

39. Freedonia has fifty senators. Each senator is either honest or corrupt. Suppose you know that at least one of the Free- donian senators is honest and that, given any two Free- donian senators, at least one is corrupt. Based on these facts, can you determine how many Freedonian senators are honest and how many are corrupt? If so, what is the answer?

    - 6 Senators
    - 1 h, 1 c
    - c >= 3
    - half is corrupt

41. Find the output of each of these combinatorial circuits.

- (a) $¬(p ∧ (q ∨ ¬r))$
- (b) $(¬p ∧ ¬q) ∨ (p ∧ r)≡ \equiv$
