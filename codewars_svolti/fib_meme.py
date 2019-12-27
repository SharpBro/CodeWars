import time

_CUTOFF = 1536


def multiply(x, y):
	if x.bit_length() <= _CUTOFF or y.bit_length() <= _CUTOFF:  # Base case
		return x * y
	
	else:
		n = max(x.bit_length(), y.bit_length())
		half = (n + 32) // 64 * 32
		mask = (1 << half) - 1
		xlow = x & mask
		ylow = y & mask
		xhigh = x >> half
		yhigh = y >> half
		
		a = multiply(xhigh, yhigh)
		b = multiply(xlow + xhigh, ylow + yhigh)
		c = multiply(xlow, ylow)
		d = b - a - c
		return (((a << half) + d) << half) + c


# (Private) Returns the tuple (F(n), F(n+1)).
def fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = fib(n // 2)
		print(a,b)
		c = multiply(a, (b * 2 - a))
		d = multiply(a,a) + multiply(b,b)
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)
    
start = time.time()
fib(10)
print("--- %s seconds ---" % (time.time() - start))
