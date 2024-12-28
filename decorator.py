# def check_negative(func):
#     def wrapper(*numbers):
#         if any(num<0 for num in numbers):
#             raise ValueError("negative inputs not allowed")
        
#         return func(*numbers)
#     return wrapper

# @check_negative
# def sum_numbers(*numbers):
#     return sum(numbers)

# # sum_numbers = check_negative(sum_numbers)


# try:
#     user_input = input("Enter the numbers: ")
#     numbers = list(map(int, user_input.split(",")))

#     result = sum_numbers(*numbers)
#     print(f"sum is: {result}")

#     # print(sum_numbers(1,4,2))
#     # print(sum_numbers(1,-2,8))

# except ValueError as e:
#     print(e)


def check_numbers(check_type):
    def decorator(func):
        def wrapper(*numbers):
            if check_type == "positive" and any(num <= 0 for num in numbers):
                raise ValueError("Negative inputs are not allowed")
            elif check_type == "negative" and any(num >= 0 for num in numbers):
                raise ValueError("Non-negative inputs are not allowed")
            return func(*numbers)
        return wrapper
    return decorator

check_type = input("Enter 'positive' to allow only positive numbers or 'negative' for negative numbers: ")


 
@check_numbers(check_type)  
def sum_numbers(*numbers):
    return sum(numbers)
 
try:

    user_input = input("Enter the numbers: ")
    numbers = list(map(int, user_input.split(",")))

    sum_numbers = check_numbers(check_type)(sum_numbers)
    result = sum_numbers(*numbers)
    print(f"Sum is: {result}")
 
except ValueError as e:
    print(e)

