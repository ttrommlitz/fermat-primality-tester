import random


def prime_test(N, k):
    # This is the main function connected to the Test button. You don't need to touch it.
    return run_fermat(N,k), run_miller_rabin(N,k)


def mod_exp(x, y, N):
    # You will need to implement this function and change the return value.   
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
    # You will need to implement this function and change the return value.   
    return 0.0


def run_fermat(N,k):
    for i in range(k):
        a = random.randint(1, N - 1)
        if mod_exp(a, N - 1, N) != 1:
            return 'composite'

    return 'prime'


def run_miller_rabin(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    for i in range(k):
        a = random.randint(1, N - 1)
        exponent = N - 1
        res = mod_exp(a, exponent, N)
        if res != 1: 
            return 'composite'
        exponent == exponent / 2

        while (exponent % 2 == 0):
            res = mod_exp(a, exponent, N)
            if res == 1:
                exponent = exponent / 2
            elif res == N - 1:
                break
            else:
                return 'composite'
    return 'prime'

print(run_miller_rabin(97, 100))

