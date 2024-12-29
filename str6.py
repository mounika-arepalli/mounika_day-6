str=input("enter the string:")
str=str.lower()
str=str.replace(' ','')
vowel_count=0
consonent_count=0
for i in str:
    if(i in ('a','e','i','o','u')):
        vowel_count+=1
    elif(i.isalpha()):
        consonent_count+=1
print("vowels count:",vowel_count)
print("consonent_count:",consonent_count)