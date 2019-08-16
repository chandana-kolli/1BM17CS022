n=int(input("How many numbers?"))
print("Enter ",n," numbers")
li=[]
even=[]
for i in range(n):
    a=int(input())
    li.append(a)
print(li)
for ele in li:
    if(ele%2==0):
        even.append(ele)
print("List of even numbers is:")
print(even)
    
    
