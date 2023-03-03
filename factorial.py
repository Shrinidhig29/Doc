# # whether number follows the case
# def factorial(n):
#     facto = 1
#     for i in range(1, n+1):
#         facto = facto * i
#     return facto 


def sum_of_fac(n):
    temp = n
    sum = 0
    while (temp>0):
        digit = temp%10
        temp = temp//10
        facto = (digit)
        sum = sum + facto
    if sum == n :
        print('yes')
    else:
        print('no')
        
sum_of_fac(145)

# def sum_of_fact(start, end):
#     for n in range(start, end):
#         temp = n
#         sum = 0
#         while (temp>0):
#             digit = temp % 10
#             temp = temp//10
#             facto = factorial(digit)
#             sum = sum + facto
#         if sum == n:
#             print(n)
            
# sum_of_fact(1, 200000)