# reverse a number

# def rev(s): # pass the number
#     new_s = 0 #1
#     for num in s:
#         if s[num]>s[num+1]:
#             n
#             new_s += i
#     return new_s

num = 1234
rev_num = 0

while num != 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(rev_num))




