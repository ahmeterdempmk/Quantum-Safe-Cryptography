from random import randint

q = 11
p = 23
g = 4

assert( (p-1) % q  == 0 )
assert( g>=2)
assert( g <= (p-2) )
assert( ( pow(g,(p-1)/q) % p) != 1)

print(f"Public information is good: q={p}, p={q}, g={g}")

alice_private_key = randint(2, q-1)

assert(alice_private_key >= 2)
assert(alice_private_key <= (q-1) ) 
print(f"Alice's private key is {alice_private_key}")

alice_public_key = pow(g,alice_private_key,p)
print(f"Alice's public key is {alice_public_key}")

hash_dict = {}
def mock_hash_func(inp):
    print(inp)
    if not inp in hash_dict:
        hash_dict[inp] = randint(1,q)
    return hash_dict[inp]

alice_message = "Inspection tomorrow!"
alice_hash = mock_hash_func(alice_message) 
print(f"Alice's message hash is: {alice_hash}")

def modular_inverse(k, q):
    for i in range(0, q):
        if (k * i) % q == 1:
            return i
    print(f'error! no inverse found! for {k},{q}')
    return 0 

n1 = modular_inverse(3,7)
n2 = modular_inverse(4,11)
n3 = modular_inverse(7,5)
m1 = pow(3,-1,7)
m2 = pow(4,-1,11)
m3 = pow(7,-1,5)

assert(n1==m1)
assert(n2==m2)
print (f"modular_inverse(3,7) = {m1}")
print (f"modular_inverse(4,11) = {m2}")
print (f"modular_inverse(7,5) = {m3}")

n4 = modular_inverse(2,6)

try:
  m4 = pow(2,-1,6)
except:
  print("Exception from pow() - no modular inverse found!")

signed=False
while( signed==False ):
    k = randint(1, q-1)  
    print("Using random k =",k)
    r = pow(g,k,p) % q
    if (r == 0):
      print(f"{k} is not a good random value to use to calculate r. Trying another k")
      continue
    s = (pow(k,-1,q) * (alice_hash + alice_private_key * r)) % q  
    if (s == 0):
      print(f"{k} is not a good random value to use to calculate s. Trying another k")
      continue  
    signed=True
    
signature = (r, s)
print(f"Alice's signature is : {(r,s)}")

bob_hash = mock_hash_func(alice_message) 

w = (pow(s,-1,q)) % q  
u1 = (bob_hash * w) % q
u2 = (r * w) % q
v = ((g**u1 * alice_public_key**u2) % p) % q

if v == r:
    print("Signature is valid!")
else:
    print("Signature is invalid!")