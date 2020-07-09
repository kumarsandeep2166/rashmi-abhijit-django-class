# by Rasmi



num=int(input("How fibonacci num. you want ="))
val1 = 0
val2 = 1

count=0

if num > 0:
    while num>=count:
        print(val1)
        val=val1 + val2
        val1=val2
        val2=val
        count+=1


num=int(input("Print fibonacci serise till = "))
# val1 = 0
# val2 = 1
# count1 = num + 1
# if num > 0:
#     while num<count1:
#         print(val1)
#         val=val1 + val2
#         val1=val2
#         val2=val
#         # count+=1