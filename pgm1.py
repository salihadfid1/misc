num = [40000000000000000,61,3,4,81,3000,7]
m = 0
for i in range (len(num)-1,-1,-2):


    if num[i] > num[i-1]:
        m = num[i]
    else:
        m = num[i-1]
print (m)



