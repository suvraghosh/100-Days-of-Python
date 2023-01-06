a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
print("I'm calculator!Calculate me..!")
c=input("Enter operator to evaluate: ")
if c=='+':
  print(a+b)
elif c=='-':
  print(a-b)
elif c=='*':
  print(a*b)
elif c=='**':
  print(a**b)
elif c=='/':
  print(a/b)
elif c=='//':
  print(a//b)
elif c=='%':
  print(a%b)