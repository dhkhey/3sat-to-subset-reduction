# 3sat-to-subset-reduction
The program executes a polynomial time reduction from 3-SAT --> SUBSET-SUM, then solves SUBSET-SUM in non-polynomial time.
3-SAT is a known NP-Complete problem. The reduction shows that SUBSET-SUM is also NP-Complete. 
If we find a polynomial time algorithm to solve SUBSET-SUM, we would be able to solve 3-SAT in polynomial time
and prove P = NP.
If interested, this document has great explanations in detail: https://www.cs.bgu.ac.il/~algo132/wiki.files/3sat-susu.pdf

Usage: As of now, user must manually set a 3-SAT formula to test (CNF form) within the code using list of lists.
Each sublist is a clause, which has three string variables "x", "y", "z". Use ~ for negation.  
[['x','~y','z'], ['x', 'y', '~z'], ['~x', '~y', 'z'], ['~x', 'y', '~z']] = 
(x ∨ ~y ∨ z) ∧ (x ∨ y ∨ ~z) ∧ (~x ∨ ~y ∨ z) ∧ (~x ∨ y ∨ ~z)
I am a student learning programming, so the code probably has a lot of flaws. 
I plan to clean up code and add/modify interface to try do something cool with it. 

