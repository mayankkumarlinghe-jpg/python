print('Starting advanced features module')
# List comprehensions are powerful
squares = [x**2 for x in range(10)]
print('Squares:', squares)
# Dictionary comprehensions
square_dict = {x: x**2 for x in range(5)}
print('Square Dict:', square_dict)
# Let's look at lambda functions
add = lambda x, y: x + y
print('Lambda add 5+3:', add(5, 3))
# Filter with lambda
