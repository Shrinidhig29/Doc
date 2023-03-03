# Maximum of two numbers in Python

# num1 = 10
# num2 = 5

# if num1>num2:
#     print(num1)
# else:
#     print(num2)    
# def max(num1, num2):
#     if num1>num2:
#         return num1
#     else:
#         return num2
    
# print(max(num1=2, num2=12))    

            # 1st solution
            
def maxi(lst):
    for i in lst:
        out = []
        for j in lst:
            if i<j:
                out += j
            else:
                pass
            print(out)
    return i 

lst = [1,2,100,3,4,5,10,20,20,30,40]

print(maxi(lst))

# lst = [1000, 2, 3, 4, 20, 200]

                    # 2nd solution

# lst_new = sorted(lst)
# print(lst_new[-1])

                    #3rd solution

# print(max(lst))

# for i in range(0, len(lst)):
#     for j in range(0,len(lst)):
#         if i[]

# list = [30,800,20,9,300]

# current_max_number = list[0]
# for number in list:
#     if number>current_max_number:
#         current_max_number = number

# print (current_max_number)