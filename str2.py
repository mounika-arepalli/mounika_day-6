#write a python program to print the number of vowels present in the user entered string?
str=input("enter the string:")
vowel_count=0
for i in str:
    if(i in ('A','E','I','O','U','a','e','i','o','u')):
        vowel_count+=1
print("vowel count is:",vowel_count)