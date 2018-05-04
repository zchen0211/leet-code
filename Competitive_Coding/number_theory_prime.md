# Prime Numbers

## Prime Test (School Method)
- http://www.geeksforgeeks.org/primality-test-set-1-introduction-and-school-method/
 go from 2 to sqrt(x)

## Prime Test (Fermat Method)
- http://www.geeksforgeeks.org/primality-test-set-2-fermet-method/
```
 Fermat's Little Theorem:
  If n is a prime number, then for every a, 1 <= a < n,

  a ** (n-1) = 1 (mod n)

Eg
 5 is prime, 2 ^ 4 = 1 (mod 5)
 7 is prime, 3 ^ 6 = 1 (mod 7)
```
- Alg (probabilistic):
```
 1)  Repeat following k times:
      a) Pick a randomly in the range [2, n - 2]
      b) If a ** (n-1) != 1 (mod n), then return false
 2) Return true [probably prime].
```

## Prime Test (Miller-Rabin)
```
 bool isPrime(int n, int k)
  1) Handle base cases for n < 3
  2) If n is even, return false.
  3) Find an odd number d such that n-1 can be written as d * (2^r). 
     Note that since n is odd, (n-1) must be even and r must be 
     greater than 0.
  4) Do following k times
     if (millerTest(n, d) == false)
          return false
  5) Return true.

 bool millerTest(int n, int d)
  1) Pick a random number 'a' in range [2, n-2]
  2) Compute: x = pow(a, d) % n
  3) If x == 1 or x == n-1, return true.

  // Below loop mainly runs 'r-1' times.
  4) Do following while d doesn't become n-1.
     a) x = (x*x) % n.
     b) If (x == 1) return false.
     c) If (x == n-1) return true.
```
- Example
```
e.g. n = 13, k = 2
 13 - 1 = 3 * 2 ^ 2 => d = 3, r = 2
 1) pick 'a' in range [2, 13-2], suppose a = 4
  4 ^ 3 = 12 (mod 13)
 2) pick 'a', suppose a = 5
  x = 5 ^ 3 = 8 (mod 13)
  x is neither 1 or 12
  do following r - 1 = 1 times:
   a) x = (x * x) % 13 = 12
      x == n - 1 => return true
```

## Sieve of Eratosthenes
- http://www.geeksforgeeks.org/sieve-of-eratosthenes/
```
 Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.
 choose p not marked, mark 2p, 3p, ...
```

## Segmented Sieve
- http://www.geeksforgeeks.org/segmented-sieve/
- The idea of segmented sieve is to divide the range [0..n-1] in different segments and compute primes in all segments one by one. This algorithm first uses Simple Sieve to find primes smaller than or equal to sqrt(n). Below are steps used in Segmented Sieve.
```
 1. Use Simple Sieve to find all primes upto square root of ‘n’ and store these primes in an array “prime[]”. Store the found primes in an array ‘prime[]’.
 2. We need all primes in range [0..n-1]. We divide this range in different segments such that size of every segment is at-most sqrt(n)
 3. Do following for every segment [low..high]
Create an array mark[high-low+1]. Here we need only O(x) space where x is number of elements in given range.
Iterate through all primes found in step 1. For every prime, mark its multiples in given range [low..high].
```

## Wilson's Theorem
```
 p > 1 is a prime iif (p-1)! = -1 (mod p)
 
 Usage: compute (25)! % 29 = ?
  we know (28)! % 29 = -1
  calculate inverse
```

## to calculate inverse
- http://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/

## Prime Factorisation
- http://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
```
 1) While n is divisible by 2, print 2 and divide n by 2.
 2) After step 1, n must be odd. Now start a loop from i = 3 to square root of n. While i divides n, print i and divide n by i, increment i by 2 and continue.
 3) If n is a prime number and is greater than 2, then n will not become 1 by above two steps. So print n if it is greater than 2.
```

## Pollard Rho Alg for Prime Factorization
- Given a positive integer n, and that it is composite, find a divisor of it.
```
 Brute approach: Test all integers less than n until a divisor is found.
 Improvisation: Test all integers less than sqrt(n)
```
- Concepts:
```
  congruent modulo: x = y (mod n)
  gcd
  birthday paradox: The probability of two persons having same birthday is unexpectedly high even for small set of people.
  Floyd’s cycle-finding algorithm:
```
- Algorithm:
```
 1. Start with random x and c. Take y equal to x and f(x) = x2 + c.
 2. While a divisor isn't obtained
    a. Update x to f(x) (modulo n) [Tortoise Move]
    b. Update y to f(f(y)) (modulo n) [Hare Move]
    c. Calculate GCD of |x-y| and n
    d. If GCD is not unity
      i. If GCD is n, repeat from step 2 with another set of x, y and c
      ii. Else GCD is our answer 
```
- Example
```
e.g. y = x = 2, c = 1
 x = f(x) | y = f(f(y)) | c | d = gcd(|x-y|, n)
  5 | 26 | 1 | 1
  26 | 180 | 1 | 11
```
