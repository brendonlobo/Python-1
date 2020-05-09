list1=[]
num=int(input("Enter the number of elements:"))
for i in range(num):
    elements=int(input())
    list1.append(elements)
print("Input:",list1)
list2=[]
length=len(list1)
for j in range(length):
  if list1[j]>0:
    list2.append(list1[j])
print("Output:",list2)
