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
#This one needs to take into account out of range values in the list. So easier to start at zero in the sequence
def n_fib(n):
    nums = [0,1]
	
    for i in range(2, n):
        nums.append(nums[i-1] + nums[i-2])
    
    #print(nums)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return nums[-1]
    
#print(n_fib(4))


"""
Recursive Solution with memoization below:
Time - O(n) 
Space - O(n)

"""

def memoize(f):
    memo = {}
    def helper(x):                  #arguments for helper are the arguments of the original function.
        print(x)
        if x not in memo:
            memo[x] = f(x)
            #print(memo[x])
        return memo[x]
    return helper


@memoize
def fibRec(n):
    #base case
    if n <= 1:
        return n
    #recursive case    
    else:
        return fibRec(n-1) + fibRec(n-2)

print(fibRec(4))
