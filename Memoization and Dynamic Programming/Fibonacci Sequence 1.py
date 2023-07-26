
# "memo" refers to memoization dictionary for fibonacci function.
# "fibonacci(n)"" is a function calculates fibonacci numbers.
# "n" represents the position of the number being searched for in the Fibonacci sequence. 

memo={}

def fibonacci(n):
    
    if n in memo:
        return memo[n]
    
    memo[0]=0
    memo[1]=1
    
    if n >= 2:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    
    return memo[n]

result=fibonacci(15)
print(result)
