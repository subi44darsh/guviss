a=str(input())
list=['#','@','$','^','&','*','~']
if a in list:
    print("Invalid")
elif a=='a' or a=='e'or a=='i' or a=='o' or a=='u':
    print("Vowel")
elif a!='a' and a!='e'and a!='i'and a!='o'and a!='u':
    print("Consonants")
