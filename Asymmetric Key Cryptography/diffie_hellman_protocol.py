p = 11
a = 7

print(f"prime: {p}")
print(f"primitive root: {a}")

k_A = 4  
h_A = (a**(k_A)) % p 
print(f"Alice's private key is {k_A} and public key is {h_A}")

k_B = 8  
h_B = (a**(k_B)) % p 
print(f"Bob's private key is {k_B} and public key is {h_B}")

secret_key_alice  = h_B**k_A % p
secret_key_bob = h_A**k_B % p 
assert secret_key_alice == secret_key_bob
print(f'The shared secret key is: {secret_key_bob}')