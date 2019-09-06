n=int(input("Enter a number"))
divisor=[]
for i in range(1,n+1):
    if(n%i==0):
        divisor.append(i)
print("list of divisors of ",n," is ",divisor)

        
