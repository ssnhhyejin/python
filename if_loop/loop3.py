i=1;
sign=-1
print('sign= ', i*sign)

idx=tot =0
loc=1

while idx<100:
    if idx%2 != 0:
        if loc%2 !=0:
            tmp=idx*sign
            print(tmp, end=' ')
            tot+=tmp
        else:
            tot+=idx
        loc+=1

    idx+=1

print('\ntot= %d'%tot)
