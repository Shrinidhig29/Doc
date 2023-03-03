# to check if the number is prime or not

# def prime_number(n):
#     flag = False
#     if n>1:
#         for i in range(2, n//2+1):
#             if n%i == 0:
#                 flag =True
#                 break
#         if flag:
#             return "NO! Its not a prime number"
#         else:
#             return "YES! Its a prime number"
        
# print(prime_number(4))

# display all prime numbers within the interval

def prime_number2(start, end):
    for n in range(start, end):
        if n>1:
            for i in range(2, n//2+1):
                if n%i == 0:
                    break
            else:
                print(n)
                    
prime_number2(1,50)