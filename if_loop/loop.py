# idx=tot=0
#
# while idx<5:
#     idx+=1
#     tot+=idx
#     print(idx, tot)
#
# print(idx, tot)

cnt=tot=0
dataset=[]

while cnt<100:
    cnt+=1

    if cnt%3==0:
        tot+=cnt
        dataset.append(cnt)

print('1~100 사이의 3의 배수 합 =%d' % tot)
print('dataset=',dataset)
