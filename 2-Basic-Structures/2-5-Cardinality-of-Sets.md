# Cardinality of Sets

1. Determine whether each of these sets is finite, countably infinite, or uncountable. For those that are countably infinite, exhibit a one-to-one correspondence between the set of positive integers and that set.
- (a) the negative integers
  - countably infinite; $f(x) = -x$
- (b) the even integers
  - countably infinite; ❌ $f(x) = 2x$
  - ✅  The even integers are countably infinite. We can list the set of even integers in the order $0, 2, -2, 4, -4, 6, -6, ...$. and pair them with the positive integers listed in their natural order. Thus $1 ↔ 0, 2 ↔ 2, 3 ↔ -2, 4 ↔ 4$, and so on. We see that we are pairing the positive integer $n$ with the even integer $f(n)$, where $f(n) = n$ if $n$ is even and $f(n) = 1 - n$ if $n$ is odd.
- (c) the integers less than $100$
  - countably infinite since it includes all negative integers. $f(n) = - n + 100$
- (d) the real numbers between $0$ and $1/2$
  - uncountable by Hilberts diagonalization argument.
- (e) the positive integers less than $1,000,000,000$
  - finite.
  - ✔⚠️ has cardinality $999,999,999$
- (f) the integers that are multiples of $7$
  - countably infinite; ❌ $f(n) = 7n$.
  - ✅ The correspondence is given by pairing the positive integer $n$ with $7n/2$ if $n$ is even and $-7(n - 1)/2$ if $n$ is odd: $0, 7, -7, 14, -14, 21, -21, ...$.

2. Determine whether each of these sets is finite, countably infinite, or uncountable. For those that are countably infinite, exhibit a one-to-one correspondence between the set of positive integers and that set.
- (a) the integers greater than 10
  - countably infinite; $f(n) = 10 + n$.
- (b) the odd negative integers
  - countably infinite; values can be paired like $1, -1, 2, -3, 3, -5$. ✔ In general $f(n) = -(2n - 1)$
- (c) the integers with absolute value less than 1,000,000
  - finite; from $-999,999$ to $999,999$.
  - ✔⚠️ with cardinality $1,999,999$
- (d) the real numbers between 0 and 2
  - infinite; by Example 5 the real numbers between 0 and 1 are infinite, so this cannot be smaller.
- (e) the set $A × Z^+$ where $A = \{2, 3\}$
  - countably infinite; each positive integer will be assigned 2 and 3, producing $(2,1), (3,1), (2,2), (3,2), ...$.
  - ✔ the one-to-one-correspondence is $1 ↔ (2, 1), 2 ↔ (3, 1), 3 ↔ (2, 2), 4 ↔ (3, 2), 5 ↔ (2, 3), 6 ↔ (3, 3), . . .$
- (f) the integers that are multiples of 10
  - countably infinite; ❌ $(1,10), (2,-10), (3,20), (4,-20)$.
  - ✅ $(1,0), (2,10), (3,-10), (4,20), (5,-20)$

3. Determine whether each of these sets is countable or uncountable. For those that are countably infinite, exhibit a one-to-one correspondence between the set of positive integers and that set.
- (a) all bit strings not containing the bit 0
  - countably infinite; $(1,1), (2,11), (3,111), ...$.
  - ✔ $\{λ, 1, 11, 111,...\}$ where $λ$ denotes the empty string;  matches $n$ with the string of $n - 1$ $1$'s.
- (b) all positive rational numbers that cannot be written with denominators less than 4
  - By adapting  the proof i Example 4 we see that by starting the list at row 4 we obtain all numbers that can have 4 as their denominator. If we now remove all numbers from the set that occured in rows 1-3 already we have the desired result.
  - ✔ ths is a subset of the rational numbers, so it is countable (see Ex. 16).
- (c) the real numbers not containing 0 in their decimal representation
  - infinite by the diagonalization argument.
- (d) the real numbers containing only a finite number of 1s in their decimal representation
  - infinite by the diagonalization argument.

4. Determine whether each of these sets is countable or uncountable. For those that are countably infinite, exhibit a one-to-one correspondence between the set of positive integers and that set.
- (a) integers not divisible by 3
  - countably infinite; $1 ↔ 1, 2 ↔ 2, 3 ↔ 4, ...$.
  - ⭕ $1 ↔ 1 , 2 ↔ −1 , 3 ↔ 2 , 4 ↔ −2, 5 ↔ 4, ...$
- (b) integers divisible by 5 but not by 7
  - countably infinite; $1 ↔ 0, 2 ↔ 5, 3 ↔ -5, 4 ↔ 10, ...$.
- (c) the real numbers with decimal representations consisting of all 1s
  - countably infinite; $1 ↔ 1, 2 ↔ 1.1, 3 ↔ 11.1, 4 ↔ 11.11, ...$.
  - ⭕ By arranging the numbers in a two-dimensinal table we show that our set is the countable union of countable sets (each of the countable sets is one row of this table). Therefore by Exercise 27, the entire set is countable. For an explicit correspondence with the positive integers, we can zigzag along the positive-sloping diagonals as in Figure 3: $1 ↔ .\overline{1} , 2 ↔ 1.\overline{1}, 3 ↔ .1 , 4 ↔ .11, 5 ↔ 1$, and so on.
- (d) ❓ the real numbers with decimal representations of all 1s or 9s
  - This set is not countable. We can prove it by the same diagonalization argument as was used to prove that the set of all reals is uncountable in Example 5. All we need to do is choose $d_i = 1$ when $d_{ii} = 9$ and choose $d_i = 9$ when $d_{ii} = 1$ or $d_{ii}$ is blank (if the decimal expansion is finite).

5. Show that a finite group of guests arriving at Hilbert’s fully occupied Grand Hotel can be given rooms without evicting any current guest.
   - By moving each guest to a room with a number larger than the current one by the number of arriving guest the first $n$ rooms, where $n$ is the number of new guests, become free.

6. Suppose that Hilbert’s Grand Hotel is fully occupied, but the hotel closes all the even numbered rooms for maintenance. Show that all guests can remain in the hotel.
   - By moving each guest in the next greater odd-numbered room all can stay.
   - ✔ In general $f(n) = 2n - 1$

7. Suppose that Hilbert’s Grand Hotel is fully occupied on the day the hotel expands to a second building which also contains a countably infinite number of rooms. Show that the current guests can be spread out to fill every room of the two buildings of the hotel.
   - By moving every second guest from building A to the free room with the smallest number in building B and then move each guest from A into the free room with the smallest number in A, both buildings will be fully occupied.
   - ✔ We can use the guests in the even-numbered rooms to occupy the original rooms, and the guests in the odd- numbered rooms to occupy the rooms in the second building. Specifically, for each positive integer $n$, put the guest currently in Room $2n$ into Room $n$, and the guest currently in Room $2n - 1$ into Room $n$ of the new building.

8. Show that a countably infinite number of guests arriving at Hilbert’s fully occupied Grand Hotel can be given rooms without evicting any current guest.
   - By moving each guest to the room with number $2n - 1$ every even-numbered room becomes vacant.

9. (∗) Suppose that a countably infinite number of buses, each containing a countably infinite number of guests, arrive at Hilbert’s fully occupied Grand Hotel. Show that all the arriving guests can be accommodated without evicting any current guest.
    - ⭕ The procedure from Ex. 8 can be repeated infinite times.
    - ✅ gaps between occupied rooms get larger and larger. Specifically, keep the first guest (i.e., the one currently in Room 1) in Room 1; leave Room 2 vacant; put the second guest (the one currently in Room 2) into Room 3; leave Rooms 4 and 5 vacant; put the third guest into Room 6; leave Rooms 7, 8, and 9 vacant, and so on. Have the guests from the first bus fill the first free room in each gap (Rooms 2, 4, 7, 11, and so on). After this is done, once again the gaps between occupied rooms get larger and larger. (The unoccupied rooms are now 5. 8, 9, 12. 13. 14, and so on.) So we can repeat the process with the second busload. We continue in this manner for the countable infinity of busloads. An alternative approach is given in the answer key.

10. ❓ Give an example of two uncountable sets $A$ and $B$ such that $A − B$ is
- ✅ In each case, let us take A to be the set of real numbers.
- (a) finite.
  - ✅ We can let $B$ be the set of real numbers as well; then $A − B = Ø$, which is finite.
- (b) countably infinite.
  - ✅  We can let $B$ be the set of real numbers that are not positive integers; in symbols, $B = A − Z^+$. Then $A − B = Z^+$, which is countably infinite.
- (c) uncountable.
  - ✅ We can let $B$ be the set of positive real numbers. Then $A − B$ is the set of negative real numbers and $0$, which is certainly uncountable.

11. Give an example of two uncountable sets $A$ and $B$ such that $A ∩ B$ is
- ❎ In each case, let us take $A$ to be the set of real numbers.
- ✅  In each case, we can make the intersection what we want it to be, and then put additional elements into $A$ and into $B$ (with no overlap) to make them uncountable.
- (a) finite.
  - ❎ Let $B$ be the set of positive integers smaller than $100$.
  - ✅ The simplest solution would be to make $A_n B = 0$. So, for example, take $A$ to be the interval $(1, 2)$ of real numbers, and take $B$ to be the interval $(3, 4)$.
- (b) countably infinite.
  - ❎ Let $B = Z⁺ = A ∩ B$.
  - ✅ Take the example from part (a) and adjoin the positive integers. Thus, let $A = (1, 2) ∪ Z⁺$ and let $B = (3, 4) ∪ Z⁺$.
- (c) uncountable.
  - ✅ Let $A$ be the interval $[1,3]$ of the real numbers and $B$ the interval $[2,4]$.

12. Show that if $A$ and $B$ are sets and $A ⊂ B$ then $|A| ≤ |B|$.
    - ❎ Btdo. proper subsets, all elements of $A$ are in $B$ but there is at least one element in $B$ that is not in $A$. Thus $|A| < |B|$.
    - ✅ The definition of $|A| ≤ |B|$ is that there is a one-to-one function from $A$ to $B$. In this case the desired function is just $f (x) = x$ for each $x ∈ A$.

13. Explain why the set $A$ is countable if and only if $|A| ≤ |Z^+|$.
    - ❌ If $A$ is countable, then bd. it is finite and therefore its cardinality is smaller than $Z^+$ or has the same cardinality as $Z^+$. If $|A| ≤ |Z^+|$ it must be countable because its cardinality is at most $|Z^+|$.
    - ✅ Suppose that $A$ is countable. This means either that $A$ is finite or that there exists a one-to-one correspondence $f$ from $A$ to $ℤ^+$. In the former case, there is a one-to-one function $g$ from $A$ to a subset of $ℤ^+$ (the range of $g$ is the first $n$ positive integers, where $|A| = n$). In either case, we have met the requirements of Definition 2, so $|A| ≤ |ℤ^+|$. Conversely, suppose that $|A| ≤ |ℤ^+|$. By definition, this means that there is a one-to-one function $g$ from $A$ to $ℤ^+$, so $A$ has the same cardinality as a subset of $ℤ^+$ (namely, the range of $g$). Now by Exercise 16 we conclude that $A$ is countable.

14. Show that if $A$ and $B$ are sets with the same cardinality, then $|A| ≤ |B|$ and $|B| ≤ |A|$.
    - Bd., if $|B| = |A|$ there is a one-to-one-correspondence from $A$ to $B$, so $|A| ≤ |B|$. ❎ Wlog. this is true in the reverse case.
    - ✔ one-to-one-correspondence $f: A → B$
    - ✅ ... and $f^{−1}$ meets the requirement of the definition that $|B| ≤ |A|$.

15. Show that if $A$ and $B$ are sets, $A$ is uncountable, and $A ⊆ B$, then $B$ is uncountable.
    - ❎ Because $A ⊆ B$ we know that every element of $A$ is also in $B$. Because $A$ is uncountable, we know that it has a cardinality larger than the one of $ℤ⁺$. Therefore $B$s cardinality must also be larger and is uncountable as well.
    - ✅ Suppose that $B$ were countable, say with elements $b_1 , b_2 , ...$. Then since $A ⊆ B$, we can list the elements of $A$ using the order in which they appear in this listing of $B$. Therefore $A$ is countable, contradicting the hypothesis. Thus $B$ is not countable.

16. Show that a subset of a countable set is also countable.
    - ⭕ As a subset has at most as many elements as its superset there is a one-to-one-correspondence, and the subset is also countable.
    - ✅ If a set A is countable, then we can list its elements, $a1 , a2 , a3, . . . , an , . .$. (possibly ending after a finite number of terms). Every subset of $A$ consists of some (or none or all) of the items in this sequence, and we can list them in the same order in which they appear in the sequence. This gives us a sequence (again, infinite or finite) listing all the elements of the subset. Thus the subset is also countable.

17. If $A$ is an uncountable set and $B$ is a countable set, must $A − B$ be uncountable?
    - Yes. ⭕ We need to look at this from the other direction, by noting that $A = (A ∩ B) ∪ (A - B)$. We are given that $B$ is countable, so its subset $A ∩ B$ is also countable (Exercise 16). If $A - B$ were also countable, then, since the union of two countable sets is countable (Theorem 1), we would conclude that $A$ is countable. But we are given that $A$ is not countable. Therefore our assumption that $A - B$ is countable is wrong, and we conclude that $A - B$ is uncountable.

18. Show that if $A$ and $B$ are sets $|A| = |B|$, then $|𝒫(A)| = |𝒫(B)|$.
    - ❌ There are two cases; one where both sets are countable and one where they are uncountable. If both are countable we know that $|𝒫(S)| = 2^n$ and because $|A| = |B|$ both must be $2^n$. If they are uncountable their powersets will be as well because it is necessarily bigger that the original set.
    - ✅⚠️ The hypothesis gives us a one-to-one and onto function f from A to B . By Exercise 16e in the supplementary exercises for this chapter, the function Sf from P(A) to P(B) defined by Sf (X) = f (X) for all X ⊆ A is one-to-one and onto. Therefore P(A) and P(B) have the same cardinality.

19. Show that if $A$, $B$, $C$, and $D$ are sets with $|A| = |B|$ and $|C| = |D|$, then $|A × C| = |B × D|$.
    - ❌ As the cartesian product denotes the set of ordered tuples that can be derived from to sets it will be the same if some pair of sets has the same cardinalities as some other pair. We know that this is the case from the hypothesis.
    - ✅ By what we are given, we know that there are bijections $f$ from $A$ to $B$ and $g$ from $C$ to $D$. Then we can define a bijection from $A × C$ to $B × D$ by sending $(a,c)$ to $(f(a),g(c))$. This is clearly one-to-one and onto, so we have shown that $A × C$ and $B × D$ have the same cardinality.

20. Show that if $|A| = |B|$ and $|B| = |C|$, then $|A| = |C|$.
    - ❎ This is true btdo. equality.
    - ✅ By definition, we have bijections $f : A → B$ and $g : B → C$. Then $g ◦ f$ is a bijection from $A$ to $C$, so $|A| = |C|$.

21. Show that if $A$, $B$, and $C$ are sets such that $|A| ≤ |B|$ and $|B| ≤ |C|$, then $|A| ≤ |C|$.
    - ❌ This is true btdo. inclusive inequality.
    - ✅ The definition of $|A| ≤ |B|$ is that there is a one-to-one function $f : A → B$. Similarly, we are given a one-to-one function $g : B → C$. By Exercise 33 in Section 2.3, the composition $g ○ f : A → C$ is one-to-one. Therefore by definition $|A| ≤ |C|$.

22. Suppose that $A$ is a countable set. Show that the set $B$ is also countable if there is an onto function $f$ from $A$ to $B$.
    - ❎ If for every element of $B$ there is an element in $A$ such that $f(a) = b$ and $A$ is countable, then all $b$ can be counted by listing them like $f(a_1), f(a_2), ..., f(a_n), ...$. (If $A$ happens to be finite this sequence stops at $f(n)$).
    - ⭕ If $A = Ø$, then the only way for the conditions to be met are that $B = Ø$ as well, and we are done. So assume that $A$ is nonempty.
    - ✅ Let $f$ be the given onto function from $A$ to $B$, and let $g : Z^+ → A$ be an onto function that establishes the countability of $A$. (If $A$ is finite rather than countably infinite, say of cardinality $k$, then the function $g$ will be defined so that $g(1), g(2) , . . . , g(k)$ will list the elements of $A$, and $g(n) = g(1)$ for $n > k$.) We need to find an onto function from $Z^+ to B$. The function $f ◦ g$ does the trick, because the composition of two onto functions is onto (Exercise 33b in Section 2.3).

23. Show that if $A$ is an infinite set, then it contains a countably infinite subset.
    - ❌ If $A$ itself is countably infinite there is a bijection to it from $ℤ⁺$. If it is not
    - ✅ Define a sequence $a_1 , a_2 , a_3 , ...$ of elements of $A$ as follows. First, $a_1$ is any element of $A$. Once we have selected $a_1 , a_2 , a_3 , ... , a_k$, let $a_{k+1}$ be any element of $A - \{a_1, a_2, ... , a_k\}$. Such an element must exist because $A$ is infinite. The resulting set $\{a_1, a_2, a_3 , ... \}$ is the desired countably infinite subset of $A$.

24. Show that there is no infinite set $A$ such that $|A| < |ℤ^+| = aleph_0$.
    - ❌ If $A$ is infinite we can always find an element that is larger or which index is larger that the one before it.
    - ✅ Because $|A| < |ℤ^+|$, there is a one-to-one function $f : A → ℤ^+$. We are also given that $A$ is infinite, so the range of $f$ has to be infinite. We will construct a bijection $g$ from $ℤ^+$ to $A$. For each $n ∈ ℤ^+$, let $m$ be the $n$th smallest element in the range of $f$. Then $g(n) = f^{−1}(m)$. The existence of $g$ contradicts the definition of $|A| < |ℤ^+|$, and our proof is complete.

25. ❓ Prove that if it is possible to label each element of an infinite set $S$ with a finite string, from a finite list of characters, where no two elements of $S$ have the same label, then $S$ is a countably infinite set.
    - ✅  The set of finite strings of characters over a finite alphabet is countably infinite, because we can list these strings in alphabetical order by length. For example, if the alphabet is $\{a, b, c\}$, then our list is $λ, a, b, c, aa , ab, ac, ba, bb, be, ca, cb, cc, aaa, aab, ... $. (See also Exercise 29.) Therefore the infinite set $S$ can be identified with an infinite subset of this countable set, which by Exercise 16 is also countably infinite.

26. Use Exercise 25 to provide a proof different from that in the text that the set of rational numbers is countable. [Hint: Show that you can express a rational number as a string of digits with a slash and possibly a minus sign.]
- ⭕ We can label the rational numbers with strings from the set $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, /, −\}$ by writing down the string that represents that rational number in its simplest form (no leading $0$’s, denominator not $0$, no common factors greater than $1$ between numerator and denominator, and the minus sign in front if the number is negative). The labels are unique. It follows immediately from Exercise 25 that the set of rational numbers is countable.

27. (∗) Show that the union of a countable number of countable sets is countable.
    - By modifying the the proof of the countablity of the rational numbers from page 173 we can see how to create an infinite sequence that contains all members of the set of sets $S = S_1, S_2,..., S_n,...$ as follows. $m1_{S1}, m1_{S2}, m2_{S1}, m3_{S1}, m2_{S2}, m1_{S3}, ...$. Thereby visiting all members in a zig-zag-fashion and omitting already encountered members.
    - ✔ Since empty sets do not contribute any elements to unions, we can assume that none of the sets in our given countable collection of countable sets is the empty set. If there are no sets in the collection, then the union is empty and therefore countable. Otherwise let the countable sets be $A_1 , A_2 , ... $. (If there are only a finite number $k$ of them, then we can still assume that they form an infinite sequence by taking $A_{k+1} = A_{k+2} = · · · = A_1 $. ) Since each set $A$, is countable and nonempty, we can list its elements in a sequence as $a_{i1} , a_{i2} , ...$; again, if the set is finite we can list its elements and then list $a_{i1}$ repeatedly to assure an infinite sequence.
    - Now we just need a systematic way to put all the elements $a_ {ij}$ into a sequence. We do this by listing first all the elements $a_{ij}$ in which $i + j = 2$ (there is only one such pair, $(1, 1)$ ), then all the elements in which $i + j = 3$ (there are only two such pairs, $(1, 2)$ and $(2, 1)$), and so on; except that we do not list any element that we have already listed. So, assuming that these elements are distinct, our list starts $a_{11} , a_{12} , a_{21} , a_{13}, a_{22} , a_{31} , a_{14}, ... $. (If any of these terms duplicates a previous term, then it is simply omitted.) The result of this process will be either an infinite sequence or a finite sequence containing all the elements of the union of the sets $A_i$. Thus that union is countable.

28. Show that the set $ℤ^+ × ℤ^+$ is countable.
    - As each of the sets is countable bd. we only need to list the ordered n-tuples $(z_1, z_2)$ in a way that accounts for the infinity of the sets. We can do that by listing the tuples ordered by the sum of their values; $ℤ^+ × ℤ^+ = (z_11, z_21), (z_12, z_22), ... = (1,1), (1,2), (2,1), (3,1), (2,2), (3,1) ...$.
    - ✔ We can think of $ℤ^+ × ℤ^+$ as the countable union of countable sets, where the $i$th set in the collection, for $i ∈ ℤ^+$, is $\{(i, n) \mid n ∈ ℤ^+\}$. The proof now follows from Exercise 27.

29. (∗) ❓ Show that the set of all finite bit strings is countable.
    - ✅ There are only a finite number of bit strings of each finite length, so we can list all the bit strings by listing first those of length $0$, then those of length $1$, etc. The listing might be $λ, 0, 1, 00, 01, 10, 11, 000, 001, ...$. (Recall that >. denotes the empty string.) Actually this is a special case of Exercise 27: the set of all bit strings is the union of a countable number of countable (actually finite) sets, namely the sets of bit strings of length $n$ for $n = 0, 1, 2, ...$.

30. (∗) ❓ Show that the set of real numbers that are solutions of quadratic equations $ax^2 + bx + c = 0$, where $a$, $b$, and $c$ are integers, is countable.
    - ✅ There are at most two real solutions of each quadratic equation, so the number of solutions is countable as long as the number of triples $(a, b, c)$, with $a$, $b$, and $c$ integers, is countable. But this follows from Exercise 27 in the following way. There are a countable number of pairs $(b, c)$, since for each $b$ (and there are countably many b’s) there are only a countable number of pairs with that $b$ as its first coordinate. Now for each $a$ (and there are countably many a’s ) there are only a countable number of triples with that a as its first coordinate (since we just showed that there are only a countable number of pairs $(b, c)$). Thus again by Exercise 27 there are only countably many triples.

31. (∗) ❓ Show that $ℤ^+ × ℤ^+$ is countable by showing that the polynomial function $f : ℤ^+ × ℤ^+ → ℤ^+$ with
$f (m, n) = (m + n − 2)(m + n − 1)/2 + m$ is one-to-one and onto.
    - ✅ A little experimentation with this function shows the pattern: $f(1, 1) = 1, f(2, 1) = 3, f(3, 1) = 6, f(1, 2) = 2, f(2, 2) = 5, f(1, 3) = 4$.
    - We see by looking at the diagonals of this table that the function takes on successive values as $m+n$ increases. When $m + n = 2, f(m, n) = 1$. When $m + n = 3$, $f(m, n)$ takes on the values $2$ and $3$. When $m + n = 4$, $f(m, n)$ takes on the values $4$, $5$, and $6$. And so on. It is clear from the formula that the range of values the function takes on for a fixed value of $m + n$, say $m + n = x$, is ⚠️ $(x-2)(x-1)/2 + 1$ through $(x-2)(x-1)/2 + (x-1)$, since $m$ can assume the values $1, 2, 3, ..., (x - 1)$ under these conditions, and the first term in the formula is a fixed positive integer when $m + n$ is fixed. To show that this function is one-to-one and onto, we merely need to show that the range of values for $x + 1$ picks up precisely where the range of values for $x$ left off, i.e., that $f(x - 1, 1) + 1 = f(1, x)$. We compute:

32. (∗) ❓ Show that when you substitute $(3n + 1)^2$ for each occurrence of $n$ and $(3m + 1)^2$ for each occurrence of $m$ in the right-hand side of the formula for the function $f (m, n)$ in Exercise 31, you obtain a one-to-one polynomial function $ℤ × ℤ → ℤ$. It is an open question whether there is a one-to-one polynomial function $ℚ × ℚ → ℚ$.
    - $(f◦g)(m, n) = \frac{((3m + 1)^2 + (3n + 1)^2 − 2)((3m + 1)^2 + (3n + 1)^2 − 1)}{2} + (3m + 1)^2$
    - ✅ We saw in Exercise 31 that $f(m, n) = (m + n − 2)(m + n − 1)/2 + m$ is a one-to-one function with domain $ℤ+ × ℤ+$. We want to expand the domain to be $ℤ × ℤ$, so things need to be spread out a little if we are to keep it one-to-one. If we can find a one-to-one function $g$ from $ℤ × ℤ$ to $ℤ+ × ℤ+$, then composing these two functions will be our desired one-to-one function from $ℤ × ℤ$ to $ℤ$ (we know from Exercise 33a in Section 2.3 that the composition of one-to-one functions is one-to- one). The function suggested here is $g(m, n) = ((3m + 1)^2, (3n + 1)^2 )$, so that the composed function is $(f ◦ g)(m, n) = ((3m + 1)^2 + (3n + 1)^2 − 2)((3m + 1)^2 + (3n + 1)^2 − 1)/2 + (3m + 1)^2$. To see that $g$ is one-to-one, first note that it is enough to show that the behavior in each coordinate is one-to-one; that is, the function that sends integer $k$ to positive integer $(3k + 1)^2$ is one-to-one. To see this, first note that if $k_1 ≠ k_2$ and $k_1$ and $k_2$ are both positive or both negative, then $(3k1 + 1)2 ≠ (3k2 + 1)^2$. And if one is nonnegative and the other is negative, then they cannot have the same images under this function because the nonnegative integers are sent to squares of numbers that leave a remainder of $1$ when divided by $3$ ($0 → 1^2 , 1 → 4^2 , 2 → 7^2 ,... $), but negative integers are sent to squares of numbers that leave a remainder of $2$ when divided by $3$ ($−1 → 2^2 , −2 → 5^2 , −3 → 8^2 ,...$).

33. Show that $(0, 1)$ and $[0, 1]$ have the same cardinality.
    - ❌ We know that $(0, 1)$ is uncountable by Cantors diagonalization argument. So $[0, 1]$ is a superset of an uncountable set and must also be uncountable.
    - ✅  It suffices to find one-to-one functions $f : (0, 1) → [0, 1]$ and $g : [0, 1] → (0, 1)$. We can obviously use the function $f(x) = x$ in the first case. For the second, we can just compress $[0, 1]$ into, say, $[1/3,2/3]$; the increasing linear function $g(x) = (x + 1)/3$ will do that. It then follows from the Schroder-Bernstein theorem that $|(0, 1)| = |[0, 1]|$.

34. ❓ Show that $(0, 1)$ and $ℝ$ have the same cardinality.
    - ✅ It suffices to find one-to-one functions $f : (0, 1) → ℝ$ and $g : ℝ → (0, 1)$. We can obviously use the function $f (x) = x$ in the first case. For the second, we can compress $ℝ$ onto $(0, 1)$ by using the arctangent function, which is known to be injective; let $g(x) = 2 arctan(x)/π$. It then follows from the Schröder-Bernstein theorem that $|(0, 1)| = |R|$.

35. ❓ Show that there is no one-to-one correspondence from the set of positive integers to the power set of the set of positive integers. [Hint: Assume that there is such a one-to-one correspondence. Represent a subset of the set of positive integers as an infinite bit string with $i$th bit $1$ if $i$ belongs to the subset and $0$ otherwise. Suppose that you can list these infinite strings in a sequence indexed by the positive integers. Construct a new bit string with its $i$th bit equal to the complement of the $i$th bit of the $i$th string in the list. Show that this new bit string cannot appear in the list.]
    - $f: ℤ⁺ → 𝒫(ℤ⁺)$
    - ✅ We can follow the hint or argue as follows, which really amounts to the same thing. (See the answer key for a proof using bit strings.) Suppose there were such a one-to-one correspondence $f$ from $ℤ⁺$ to the power set of $ℤ⁺$ (the set of all subsets of $ℤ⁺$ ). Thus, for each $x ∈ ℤ⁺$, $f(x)$ is a subset of $ℤ⁺$. We will derive a contradiction by showing that $f$ is not onto; we do this by finding an element not in its range. To this end, let $A = \{ x \mid x ∉ f(x)\}$. We claim that $A$ is not in the range of $f$. If it were, then $A = f(x_0)$ for some $x_0 ∈ ℤ⁺$ . Let us look at whether $x_0 ∈ A$ or not. On the one hand, if $x_0 ∈ A$, then by the definition of $A$, it must be true that $x_0 ∉ f ( x_0 )$, which means that $x_0 ∉ A$; that is a contradiction. On the other hand, if if $x_0 ∉ A$, then by the definition of $A$, it must be true that $x_0 ∈ f(x_0 )$, which means that $x_0 ∈ $, again a contradiction. Therefore no such one-to-one correspondence exists.

36. ❓ (∗) Show that there is a one-to-one correspondence from the set of subsets of the positive integers to the set real numbers between 0 and 1. Use this result and Exercises 34 and 35 to conclude that $א_0 < |P(ℤ⁺)| = |ℝ|$. [Hint: Look at the first part of the hint for Exercise 35.]
    - ✅ We can encode subsets of the set of positive integers as strings of, say, $5$’s and $6$’s , where the ith symbol is a $5$ if $i$ is in the subset and a $6$ otherwise. If we interpret this string as a real number by putting a $0$ and a decimal point in front, then we have constructed a one-to-one function from $P(ℤ⁺)$ to $(0, 1)$. Also, we can construct a one-to-one function from $(0, 1)$ to $P(ℤ⁺)$ by sending the number whose binary expansion is $0.d_1 d_2 d_3 . . .$ to the set $\{i \mid d_i = 1\}$ . Therefore we have $|P(ℤ⁺)| = |(0, 1)|$. By Exercise 34, $|(0, 1)| = |R|$, so we have shown that $|P(ℤ⁺)| = |R|$. (We already know from Cantor’s diagonal argument that $א_0 < |R|$.) There is one technical point here. In order for our function from $(0, 1)$ to $P(ℤ⁺)$ to be well-defined, we must choose which of two equivalent expressions to represent numbers that have terminating binary expansions to use (for example, $0.100101$ versus $0.100110$); we can decide to always use the terminating form, i.e., the one ending in all $0$’s.)

37. (∗) Show that the set of all computer programs in a particular programming language is countable. [Hint: A computer program written in a programming language can be thought of as a string of symbols from a finite alphabet.]
    - By interpreting the set of possible programs as an infinite string coposed from a finite alphabet we can count the programs by first listing all programs of length $1$ for each possible character, then all programs of length $2$ and so on. We get $i^n$ possible programs, where $i$ is the number of characters the program consists of and $n$ the size of the alphabet of possible characters. As there are (theoretically) an infinite number of programs this hat has the same cardinality as $ℤ⁺$.
    - ✔ Refer to Ex. 27 to establish the countability of a union of countable sets and to Ex. 16 to establish the countability of subsets of countable sets.

38. ❓ (∗) Show that the set of functions from the positive integers to the set $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$ is uncountable. [Hint: First set up a one-to-one correspondence between the set of real numbers between $0$ and $1$ and a subset of these functions. Do this by associating to the real number $0.d_1 d_2 ... d_n ...$ the function $f$ with $f (n) = d_n$.]
    - ✅ We know from Example 5 that the set of real numbers between $0$ and $1$ is uncountable. Let us associate to each real number in this range (including $0$ but excluding $1$) a function from the set of positive integers to the set $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$ as follows: If $x$ is a real number whose decimal representation is $0.d1 d2 d3 ...$ (with ambiguity resolved by forbidding the decimal to end with an infinite string of $9$’s), then we associate to $x$ the function whose rule is given by $f (n) = d_n$. Clearly this is a one-to-one function from the set of real numbers between $0$ and $1$ and a subset of the set of all functions from the set of positive integers to the set $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$. Two different real numbers must have different decimal representations, so the corresponding functions are different.  Since the set of real numbers between $0$ and $1$ is uncountable, the subset of functions we have associated with them must be uncountable. But the set of all such functions has at least this cardinality, so it, too, must be uncountable (by Exercise 15).

39. (∗) We say that a function is computable if there is a computer program that finds the values of this function. Use Exercises 37 and 38 to show that there are functions that are not computable.
    - From Ex. 38 we know that the set of functions from the positive integers to the set of numbers $0$ through $9$ is uncountable. But by Ex. 37 we see that the number of computer programs is countably infinite.
    - ✔ In Exercise 37 we saw that there are only a countable number of computer programs, so there are only a countable number of computable functions. In Exercise 38 we saw that there are an uncountable number of functions. Hence not all functions are computable. Indeed, in some sense, since uncountable sets are so much bigger than countable sets, almost all functions are not computable! This is not really so surprising; in real life we deal with only a small handful of useful functions, and these are computable. Note that this is a nonconstructive proof-we have not exhibited even one noncomputable function, merely argued that they have to exist. Actually finding one is much harder, but it can be done. For example, the following function is not computable. Let $T$ be the function from the set of positive integers to $\{0, 1\}$ defined by letting $T(n)$ be $0$ if the number $0$ is in the range of the function computed by the $n$ th computer program (where we list them in alphabetical order by length) and letting $T(n) = 1$ otherwise.

40. (∗) ❓ Show that if $S$ is a set, then there does not exist an onto function $f$ from $S$ to $P(S)$, the power set of $S$. Conclude that $|S| < |P(S)|$. This result is known as Cantor’s theorem. [Hint: Suppose such a function $f$ existed. Let $T = \{s ∈ S | s ∉ f (s)\}$ and show that no element $s$ can exist for which $f (s) = T$ .]
    - ✅ We follow the hint. Suppose that $f$ is a function from $S$ to $P(S)$. We must show that $f$ is not onto. Let $T = { s ∈ S | s ∉ f (s) }$. We will show that $T$ is not in the range of $f$. If it were, then we would have $f (t) = T$ for some $t ∈ S$. Now suppose that $t ∈ T$. Then because $t ∈ f (t)$, it follows from the definition of $T$ that $t ∉ T$; this is a contradiction. On the other hand, suppose that $t ∉ T$. Then because $t ∉ f (t)$, it follows from the definition of $T$ that $t ∈ T$; this is again a contradiction. This completes our proof by contradiction that $f$ is not onto. On the other hand, the function sending $x$ to $\{x\}$ for each $x ∈ S$ is a one-to-one function from $S$ to $P(S)$, so by Definition 2 $|S| ≤ |P(S)|$. By the same definition, since $|S| = |P(S)|$ (from what we have just proved and Definition 1), it follows that $|S| < |P(S)|$.
