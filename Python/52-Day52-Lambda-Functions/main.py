# # def double(x):
# #   return x*2

# def appl(fx, value):
#   return 6 + fx(value)

# # double = lambda x: x * 2
# # # cube = lambda x: x * x * x
# # # avg = lambda x, y, z: (x + y + z) / 3

# # print(double(5))
# # # print(cube(5))
# # # print(avg(3, 5, 10))
# print(appl(lambda x: x * x , 2))

# Lambda function to calculate the product of two numbers,
# with additional print statement
a = lambda x, y: print(f'{x} * {y} = {x * y}')
print(a(2, 3))
