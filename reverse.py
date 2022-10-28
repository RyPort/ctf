import math
otp1 = 3640950455282009581
f = open('out.txt', 'r')
f.readline()
l1 = f.readline()
l1 = l1.split(' ')
#print(l1.split(' '))

m = int(l1[2].strip())
print('m = '+str(m))

l2 = f.readline()
l2 = l2.split(' ')


results = []
flag = r'flag{'
for i in range(5):
    #print('otp = ' +l2[i+2])
    results.append(int(l2[i+2]) ^ ord(flag[i]))


coprime = []
f2 = open('coprime.txt','w')
for i in range(m):
    
    if math.gcd(m,i) == 1:
        f2.write(str(i)+'\n')
    #else:
        #print('Not Found: '+str(i))
        





#print(results[1]-results[0])
#print(results[2]-results[1])
#print((results[2]-results[1])/(results[1]-results[0]))
#A = (results[2]-results[1])/(results[1]-results[0])

f.close()
f2.close()