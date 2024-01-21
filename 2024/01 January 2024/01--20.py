#1------------------------------------------------------------------

# input=input("Enter:")
# new=input.upper()
# if new=="A" or new=="E" or new=="I" or new=="O" or new=="U":
#     print("vowel")
# else:
#     print("consonant")

#2-------------------------------------------------------------------

# var=input("Enter:")
# if var>='a' and var<='z':
#     print("alphabet")
# elif var>='A' and var<='Z':
#     print("alphabet")
# else:
#     print("Not alphabet")

#3------------------------------------------------------------------

# int=input("Enter:")
# asc=ord(int)
# print(asc)

#4---------------------------------------------------------------

# var=int(input("Enter:"))
# if var>0:
#     print("positive")
# elif var<0:
#     print("negative")
# else:
#     print("Not a positive or negative")

#5----------------------------------------------------------------

# var=int(input("Enter:"))
# if var%2==0:
#     print("even")
# else:
#     print("odd")

#6-------------------------------------------------------------------

# a=int(input("Enter:"))
# b=int(input("Enter:"))
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)

#7-------------------------------------------------------------

# r=int(input("Enter:"))
# circle_radius=22/7*r*r
# print(circle_radius)

#8--------------------------------------------------------------

# def lcm(a,b):
#     if b>a:
#         a,b=b,a
#     i=1
#     while True:
#         if (a*i)%b==0:
#             return a*i
#         else:
#             i+=1


# a=int(input("Enter:"))
# b=int(input("Enter:"))
# c=lcm(a,b)
# print(c)

#9--------------------------------------------------------------

# def gcd(a,b):
#     if a>b:
#         a,b=b,a
#     if b%a==0:
#         return a
#     else:
#         return gcd(b%a,a)

# a=int(input("Enter:"))
# b=int(input("Enter:"))

# hcf=gcd(a,b)
# print(hcf)

#10--------------------------------------------------------------

# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# if a>b:
#     print("a is greatest")
# else:
#     print("b is greatest")

#11--------------------------------------------------------------

# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# c=int(input("Enter c:"))

# if a>b and a>c:
#     print ("A is greatest")
# elif b>a and b>c:
#     print ("B is greatest")
# else:
#     print ("C is greatest")

#12--------------------------------------------------------------

# num=int(input("Enter number:"))
# size=0
# while num !=0:
#     num=num//10
#     size+=1
# print(size)

#13--------------------------------------------------------------

# num=int(input("Enter number:"))
# sum=0
# while num!=0:
#     sum=sum+(num%10)
#     num=num//10
# print(sum)

#14--------------------------------------------------------------

# num=int(input("Enter number:"))
# if num<0:
#     print("Enter a positive number")
# sum=0
# while num!=0:
#     sum=sum+num
#     num-=1
# print(sum)


#15--------------------------------------------------------------

# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# sum=0
# for i in range(a,b+1):
#     sum=sum+i
#     i+=1
# print(sum)

#16--------------------------------------------------------------

# num=25365
# num2=str(num)
# print(num2[::-1])

#17--------------------------------------------------------------

# def fact(num):
#     if num>1:
#         return num*fact(num-1)
#     else:
#         return 1
# num=5
# f=fact(num)
# print(f)

#18--------------------------------------------------------------

                # fibonacchi

#19--------------------------------------------------------------

# year=int(input("Enter  : "))
# if (year%4==0 and year%400==0) or (year%100!=0):
#     print("it is a leap year")
# else:
#     print("not a leap year")

#20--------------------------------------------------------------

# num=5
# flag=False
# if num==1:
#     print("Not a prime number")
# elif num>1:
#     for i in range(2,num):
#         if num%i==0:
#             flag=True
#             break
#     if flag:
#         print("Not prime")
#     else:
#         print("Prime")