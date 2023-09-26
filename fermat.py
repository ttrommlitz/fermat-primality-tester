import random


def prime_test(N, k):
    # This is the main function connected to the Test button. You don't need to touch it.
    return run_fermat(N,k), run_miller_rabin(N,k)


def mod_exp(x, y, N):
    if y == 0:
        return 1
    
    z = mod_exp(x, y // 2, N)
    if y % 2 == 0:
        return z**2 % N
    return x * z**2 % N
    

def fprobability(k):  
    # probability of correct answer >= 1 - 1 / (2^k)
    return 1 - (1 / 2**k)


def mprobability(k):
    return 1 - (1/ 4**k)


def run_fermat(N,k):
    # we compute k random a's, then run Fermat's Little Theorem for each a. 
    # If all a's return 1 for mod_exp, then N is very likely to be prime
    for i in range(k):
        a = random.randint(1, N - 1)
        if mod_exp(a, N - 1, N) != 1:
            return 'composite'

    return 'prime'


def run_miller_rabin(N,k):
    for i in range(k):
        # initial test for a. This is identical to the fermat test.
        a = random.randint(1, N - 1)
        exponent = N - 1
        res = mod_exp(a, exponent, N)
        if res != 1: 
            return 'composite'
        exponent == exponent / 2

        # if the fermat test passes, then we half the exponent if possible, and then continually
        # run mod_exp. If that function returns 1, continue. If it returns -1, start with a new a.
        # If it returns anything else, the number is composite. If all a's pass, then the number is prime
        while (exponent % 2 == 0):
            res = mod_exp(a, exponent, N)
            if res == 1:
                exponent = exponent / 2
            elif res == N - 1:
                break
            else:
                return 'composite'
    return 'prime'
