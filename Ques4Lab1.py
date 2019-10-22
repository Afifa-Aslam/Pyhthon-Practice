num=7
fib=lambda x:x if(x==0) or (x==1) else fib(x-1)+fib(x-2)
for a in range (0,num):
    print(fib(a))
