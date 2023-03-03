"""write a code snippet to reverse a string """

# using for loop 
def rev(s): # pass the string
    n = len(s)
    new_s = ''
    for i in range(n):       
        new_s = s[::-1]
    return new_s

s = "shrinidhi"
print(rev(s))    


# 3 by using inbuilt - function

# s = 'shrinidhi'

# new_s = reversed(s)
# print(new_s)
