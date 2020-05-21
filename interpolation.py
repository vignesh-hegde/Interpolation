print("=========================================================")
print("               Lagrenger's Interpolation")
print("=========================================================")
print("Note:Consider x and y based on input f(x) and g(y) values")
print("                  Vignesh Hegde V 0.1")
print("---------------------------------------------------------")
def numer(imp):
       num=x[int(imp)]
       for i in range(0,int(last)+1):
              if(imp==i):
                     continue
              else:
                     num=float(num)*(float(fox)-float(y[i]))
       return num

def deno(imp):
       den=1
       for i in range(0,int(last)+1):
              if(imp==i):
                     continue
              else:
                     den=float(den)*(float(y[imp])-float(y[i]))
       return den

x=[]
y=[]
last=input("Enter the last index of x and y\n")
for i in range(0,int(last)+1):
       x.append(input("x("+str(i)+")="))
       y.append(input("y("+str(i)+")="))

print("________________________________________________________")
for i in range(0,int(last)+1):
       print("x("+str(i)+")="+str(x[i])+"   y("+str(i)+")="+str(y[i]))
print("________________________________________________________")

fox=input("Enter value of f(x)/y\n")
s=0
answer=0
for i in range(0,int(last)+1):
       imp=i
       n=numer(imp)
       d=deno(imp)
       s=n/d
       answer=answer+s
x=input("Enter no of decimal place\n")
print("="+str(round(answer,int(x))))
z=input("")


