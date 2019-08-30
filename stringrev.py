print("enter a string with multiple words")
str1=[x for x in input().split()]
#print(str1)
str2=str1[::-1]
#print(str2)
str3=" ".join(str2)
print(str3)
str4=" ".join(str1)
str4=str4[::-1]
print(str4)
