""" Prime number checker """


def is_prime(num):
    
    # Corner case - 1 and 0 are not prime and negative numbers are also not considered prime.
    if num <= 1:
        prime = False
        return prime
    
    # count is keeping track of how many divisors num has.
    count = 0

    for i in range(1,num+1):
        if num % i == 0:
            count += 1
            
    # If there are more divisors than itself and 1, we know it isn't prime, return false.
    if count > 2:
        prime = False
    else:
        prime = True
    
    return prime