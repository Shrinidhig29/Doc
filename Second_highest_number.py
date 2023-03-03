# using for loop 

# def second_highest_number(l):
#     if l[0]>l[1]:
#         first = l[0]
#         second = l[1]
#     else:
#         first = l[1]
#         second =l[0]
        
#     for i in range(2, len(l)):
#         if l[i]>first:
#             second =first
#             first = l[i]
#         elif l[i]>second:
#             second =l[i]
#     return second 
    
# l = [10,20,30,20,33,200,299,299]
# print(second_highest_number(l))

# prevent the repeatation of numbers 

# def second_highest_number2(l):
#     if l[0]>l[1]:
#         first = l[0]
#         second = l[1]
#     else:
#         second = l[1]
#         first = l[0]
#     for i in range(2,len(l)) :
#         if l[i]>first:
#             second = first
#             first = l[i]
#         elif l[i]>second and first !=l[i]:
#             second = l[i]
#     return second

    
# l = [10,20,30,20,33,200,299,299]
# print(second_highest_number2(l))

# using reverse sort
def second_highest_number3(l):
    l.sort(reverse=True)
    # print(l[1])
    l.sort()
    print(l[-2])
    
l = [10,20,30,20,33,200,299,209]
second_highest_number3(l)

#nth reverse sort
# def second_highest_number4(l, n):
#     l.sort(reverse=True)
#     # print(l[1])
#     l.sort()
#     print(l[-2])
    
# l = [10,20,30,20,33,200,299,209]
# second_highest_number4(l, 5)

# using set and max
l = [10,20,30,20,38,999,2,0]
new_l = set(l)
print(l)
new_l.remove(max(new_l))
print(new_l)
print(max(new_l))
