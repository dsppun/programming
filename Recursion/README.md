# Recursion
Two important factors for recursion :
* Base Case - Identify Terminating Scenario
* Recurrence Relation - Identify how the given problem or scenario is going to reduce in 
                        each iteration to reach Base Case.

[Code Examples](https://github.com/dsppun/programming/blob/main/Recursion/main.py)

# Memoization
Sometimes while using recursion, while iterating to reach base, some cases may be duplicated i.e. the function is called 
with same arguments which is already done in some earlier iteration.

To eliminate the duplicate calculation in the above case, one of the ideas would be to store the intermediate results in the cache so that we could reuse them later without re-calculation.
This idea is also known as memoization. 

[Code Examples](https://github.com/dsppun/programming/blob/main/Recursion/memoization.py)
