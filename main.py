import random; random.seed(42)
import math

# Brute force primality testing algorithm
#####################################################################
def is_prime(n):
    for div in range(2, int(math.sqrt(n)) + 1):
        if n % div == 0:
            return False
    return True

# Randomly generating "big" prime
# 1 thousand to 2 thousand

#####################################################################
def generate_big_prime():
    prime_candidate = random.randint(1000, 2000)
    if is_prime(prime_candidate): return prime_candidate
    return generate_big_prime()

# Brute force finding inverse for a (mod N)
#####################################################################
def find_inverse(a, N):
    for b in range(N):
        if (a * b) % N == 1:
            return b
    raise Exception(f"{a} and {N} are not relatively prime")
    
# Euclidean algorithm for GCD of two non-negative numbers
#####################################################################
def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)
    
    
# RSA algorithm
#####################################################################
# STEPS
#    1) find two primes p, q
#    2) N = p * q
#    3) calculate phi(N)
#    4) find e such that e and phi(N) are coprime, and 1 < e < phi(N)
#    5) find d such that ed = 1 (mod phi(N))
#    6) convert message into integer form
#    7) encrypt
#    8) decrypt
#    9) convert decrypted form to character message

def rsa(msg):
    # STEP 1
    p = generate_big_prime()
    q = generate_big_prime()
    while p == q:
        q= generate_big_prime()
    print (f'p: {p}, q: {q}')
    
    # STEP 2
    N = p * q
    print (f'N: {N}')
    
    # STEP 3
    phi_N = (p - 1) * (q - 1)
    print (f'phi_N: {phi_N}')

    # STEP 4
    e = random.randrange(1, N)
    while gcd(e, phi_N) != 1:
        e = random.randrange(1, N)
    print (f'e: {e}')

    # STEP 5
    d = find_inverse(e, phi_N)
    print (f'd: {d}')
    
    # STEP 6
    int_msg = 0
    for character in msg:
        int_msg *= 100
        int_msg += ord(character) - ord('a') + 1
    print (f'int_msg: {int_msg}')
    
    # STEP 7
    encrypted_msg = (int_msg ** e) % N
    print (f'encrypted: {encrypted_msg}')

    # STEP 8
    decrypted_msg = (encrypted_msg ** d) % N
    print (f'decrypted: {decrypted_msg}')
    
    # STEP 9
    character_msg = []
    while decrypted_msg != 0:
        current_char = decrypted_msg % 100
        character = chr(ord('a') - 1 + current_char)
        decrypted_msg //= 100
        character_msg.append(character)

    character_msg = ''.join(character_msg[::-1])
    print (f'decrypted back to characters: {character_msg}')

    
    

    
msg = input()
rsa(msg)
