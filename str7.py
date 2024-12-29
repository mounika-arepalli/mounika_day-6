#write a python program to print number of alphabets special characters digits present in the user entered string?
str=input("enter the string:")
alp=0
spe=0
dig=0
str=str.replace(' ','')
for i in str:
    if(i in (i.isalpha())):
        alp+=1
    elif(i.isalnum()):
        sep+=1
    else:
        dig+=1
print("the alphabets are:",alp)
print("the special characters are:",sep)
print("the digits are:",dig)