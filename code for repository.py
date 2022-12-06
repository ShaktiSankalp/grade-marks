a=int(input('enter your marks: '))
if(a>=90):
    print('Grade A')
elif a>=80 and a<90:
    print('Grade B')
elif a>=70 and a<80:
    print('Grade C')
elif a<50:
    print('FAIL')
else:
    print('Grade D')