#write a python program to print the number of consonents present in the user entered string?
str=input("enter the string:")
consonent_count=0
for i in str:
    if(i not in ('A','E','I','O','U','a','e','i','o','u')):
        consonent_count+=1
print("consonent count is:",consonent_count)