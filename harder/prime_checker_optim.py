import math

def is_prime(num):

    # Corner cases - 1 and 0 are not prime and negative numbers are also not considered prime.
    if num <= 1:
        prime = False
        return prime
    
    # All even numbers greater than two are not prime. So lets not go over those
    if num > 2:
        if num % 2 == 0:
            prime = False
            return prime

    # Since half of the calculation for this is the same, we can cut out half again by using the square root 
    # If we range up to the square root of a number (or nearest for not square numbers), we avoid doing things like 3*4.. then 4*3 after
    max_div = math.floor(math.sqrt(num))
    print(max_div)

    for i in range(2,1 +max_div):
        if num % i == 0:
            prime = False
            return prime
        
    prime = True
    return prime

print(is_prime(15))