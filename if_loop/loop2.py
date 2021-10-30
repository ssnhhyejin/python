i=tot=0
dataset=[]

while i<100:
    i+=1
    if i%5 == 0 and i % 3 != 0:
        dataset.append(i)
        print(i, end=' ')
        tot+=i

print('tot=%d' % tot)
print()
print('dataset:', dataset)
