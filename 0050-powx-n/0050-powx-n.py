class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1  # Base case: x^0 = 1
        if n < 0:
            return 1 / self.myPow(x, -n)  # Handle negative exponent
        else:
            half_pow = self.myPow(x, n // 2)  # Compute x^(n//2) once
            if n % 2 == 0:
                return half_pow * half_pow  # Even case: (x^(n//2))^2
            else:
                return half_pow * half_pow * x  # Odd case: (x^(n//2))^2 * x
