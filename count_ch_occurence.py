## USING BULIT IN FUNCTION
l = [1,2,23,344,55,5,55,6,7,8,6,7,7]
print(l.count(55))

# using for loop
def count_chr_occ(s, searc_ch):
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i] + 1
        else:
            ch[i] = 1
        print(ch)
        try:
            print(ch[searc_ch])
        except :
            print(0)
            
s = "aaasssfffffccccccvvvn"
count_chr_occ(s, 'f')