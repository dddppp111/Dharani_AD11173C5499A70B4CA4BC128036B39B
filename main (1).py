def fact_rect (n):
  if n==0 or n==1:
    return  1
  else :
    return  n*fact_rect(n-1)

number  = int(input("enter the value "))
rec= fact_rect (number) 
print("the factorial is {} is {}.". format (number,rec))