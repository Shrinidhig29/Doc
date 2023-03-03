# draw simple pyramids 

"""_summary_
*
**
***
****
*****
    """

# n = int(input("Enter the number of rows: "))
# for i in range(0, n):
#     for j in range(0, i+1):
#         print("*", end='')
#     print()

# ==================================================================================

"""_summary_
1
22
333
4444
55555
    """

# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i, end="")
#     print()
    
# ===================================================================================

"""_summary_
*****
****
***
**
*
    """
    
# n = int(input("enter the number of rows:"))
# for i in range(2, n+2):
#     for j in range(0, i-1):
#         print("*", end="")
#     print()
    
# ========================================================================

"""_summary_
*
**
***
**
*
    """
    
n = int(input("enter the number of columns: "))
for i in range(0,n):
    for j in range(0, i+1):
        print("*", end="")
    print()
for k in range(2,n+2):
    for l in range(0,k-1):
        print("*", end="")
    print()
    
    
        