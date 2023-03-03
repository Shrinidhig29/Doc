#I_AM_SHRINIDHI
#i.aM.sHRINIDHI

# s = "I_AM_SHRINIDHI"
s = "NIDHI_IS_GOOD_CODER"
# using list 

# def modi_string(s):
#     l = []
#     temp = s.split('_')
#     print(temp)
#     for i in temp:
#         l.append(i[0].lower()+i[1:].upper())
#         print(l)
#     s = ".".join(l)
#     print(s)
    
# modi_string(s)

#using string
def modi_string2(s):
    new_str = ''
    temp = s.split('_')
    # print(temp)
    for i in temp:
        new_str = new_str + (i[0].lower()+i[1:].upper())
    print(new_str)
    
modi_string2(s)