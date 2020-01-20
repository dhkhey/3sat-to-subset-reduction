# 3sat-to-subset-reduction
The program executes a polynomial time reduction from 3-SAT --> SUBSET-SUM, then solves SUBSET-SUM in non-polynomial time.
3-SAT is a known NP-Complete problem. The reduction shows that SUBSET-SUM is also NP-Complete. 
If we find a polynomial time algorithm to solve SUBSET-SUM, we would be able to solve 3-SAT in polynomial time
and prove P = NP.

Usage: User must manually set a 3-SAT formula to test (CNF form) within the code using list of lists.
Each sublist is a clause, which has three string variables "x", "y", "z". Use ~ for negation.  
[['x', '~y', 'z'], ['x', 'y', '~z'], ['~x', '~y', 'z'], ['~x', 'y', '~z']] = 
(x ∨ ~y ∨ z) ∧ (x ∨ y ∨ ~z) ∧ (~x ∨ ~y ∨ z) ∧ (~x ∨ y ∨ ~z)


