"""
Write a function that computes the nth fibonacci number.

A series of fibonacci numbers is where each number in the sequence is the sum of the previous number.

0,1,1,2,3,5,8,13

Assumptions: 
	only one integer will be passed to this function.
	this number will represent nth position in a fibonacci sequence
	function will return the fibonacci number for that position in the sequence

given a number:
1. create a empty list to keep track of the sequence
2. add 0 at position 0 and add 1 at position 1 to the list
3. range over input number
4. for each iteration of that, starting at position 2,
   add previous two numbers and append the list with the result
5. return last result.
"""

def n_fib(n):
    nums = [0,1]
	
    for i in range(2, n):
        nums.append(nums[i-1] + nums[i-2])
    
    print(nums)
    return nums[-1] 
    
print(n_fib(4))