n = int(input())

fib = [0,1]
for i in range(2,11):
	fib.append(fib[i-1]+fib[i-2])

fizzBuzz = ''
for i in range(1,n+1):
	fizzBuzz += 'fizz' if i in fib else 'buzz'

print(fizzBuzz)
