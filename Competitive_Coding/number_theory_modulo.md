## Euclidean algorithms (Basic and Extended)
- http://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
- GCD

## Euler’s Totient Function
- http://www.geeksforgeeks.org/eulers-totient-function/
```
 gcd(a, b):
   if a == 0: return b
   return gcd(b % a, a)
```

## Moduloar Exponentiation
- http://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
```
 Given three numbers x, y and p, compute (xy) % p.
```

## Modular Multiplicative Inverse
- http://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
```
 Find x s.t. a * x = 1 (mod m)
  x in {0, ..., m-1}

 Method 1: naive
  try from 1 .. m-1

 Method 2 (m and a co-prime): 
  find ax + by = gcd(a, b)
  b = m

  solve(a, b, x, y)
   1. base case: return
   2. solve(b%a, a, x1, y1)
   3. x = y1 - (b/a) x1
      y = x1
```

## Chinese Remainder Theorem
- http://www.geeksforgeeks.org/chinese-remainder-theorem-set-1-introduction/
```
 given two arrays num[0..k-1] and rem[0..k-1] (coprime)
 find minimum integer s.t.:
     x % num[0]    =  rem[0], 
     x % num[1]    =  rem[1], 
     .......................
     x % num[k-1]  =  rem[k-1]
```
- http://www.geeksforgeeks.org/chinese-remainder-theorem-set-2-implementation/
```
prod = num[0] * num[1] * ... * num[k-1]
pp[i] = prod / num[i]
x =  ( sum (rem[i]*pp[i]*inv[i]) ) % prod
   Where 0 <= i <= n-1
```

## Compute nCr % p | Set 2 (Lucas Theorem)
- http://www.geeksforgeeks.org/compute-ncr-p-set-2-lucas-theorem/
```
Naive:
 nCr % p with dp
```
- http://www.geeksforgeeks.org/compute-ncr-p-set-1-introduction-and-dynamic-programming-solution/
```
 C(n, r) % p = [C(n-1, r-1) % p + C(n-1, r) % p] % p
 C(n, 0) = C(n, n) = 1

 O(n) space, O(nr) time
```

## Lucas Theorem
```
 nCr = Prod n_iCr_i (mod p)
 where:
  n = n_k p^k + n_k-1 p^k-1 + ... + n_1 p + n_0
  r = r_k p^k + r_k-1 p^k-1 + ... + r_1 p + r_0
```
- Alg:
```
  one-by-one: n_iCr_i
```