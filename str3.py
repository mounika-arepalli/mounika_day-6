#write a python program to print the number of vowels and consonents present in the user entered integer?
str=input("enter the string:")
vowel_count=0
consonent_count=0
for i in str:
    if(i in ('A','E','I','O','U','a','e','i','o','u')):
        vowel_count+=1
    else:
        consonent_count+=1
print("number of vowels is:",vowel_count)
print("number of consonents is:",consonent_count)
