def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n = 247  
e = 5    
a = 6    
assert gcd(a, n) == 1
print(f"Checked {n} and {a} are coprime.")

r = 0
rem = 100
while(rem != 1):
    r += 1
    rem = (a**r) % n
    
print(f'period r is: {r}')
assert a**r % n == 1

print(f"Checked {a}^{r} mod {n} is 1")

f1 = int ( a**(r/2) - 1)
f2 = int ( a**(r/2) + 1)

print(f"f1 = {f1}")
print(f"f2 = {f2}")

q_found = gcd(f1, n)
print(f'One possible prime factor of n ({n}) is: {q_found}')

p_found = int ( n/q_found )
print(f'The second prime factor of n ({n}) is: {p_found}')

assert n == p_found * q_found

phi_found = ( p_found -1 ) * ( q_found - 1 ) 
print(f'The totient is: {phi_found}')

d_found = 1
while(True):
    if((d_found*e) % phi_found == 1):
        break
    else:
        d_found += 1
print("Private Key number:", d_found)