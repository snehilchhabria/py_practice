# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)

# try:
#     n  = 4
#     result = fact(n)

#     print(result)
# except ValueError as e:
#     print(e)

#lambda function
x = lambda num : 1 if num <=1 else num*x(num-1)

number = int(input('Enter number: '))

print(x(number))