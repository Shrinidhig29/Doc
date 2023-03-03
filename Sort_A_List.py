lst = [1,4,9, 3, 4, 5,5,6,7,8]

# # using for loop

# new_lst = []
# def sort_func(lst):
#     n = len(lst)
#     for i in range(n):
#         if lst[i]<lst[i+1]:
#             new_lst += i
#         elif lst[i]==lst[i+1]:
#             new_lst += i
#         else:
#             new_lst = i
                
#     return new_lst

# print(sort_func(lst))
        


for i in range(len(lst)):
    for j in range(i + 1, len(lst)):

        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(lst)





# using invult function
# srt_lst = sorted(lst)
# print(srt_lst)