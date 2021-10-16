def is_prime(x):
    count=0
    divisors=[]
    for i in range(1,(x+1)):
        if x%i==0:
            divisors.append(i)
            count+=1  
    if count<=2 and count>0:
        print("It's a prime......")
        #print(count)
    else:
        print("Not a prime number....")
        print("The number {} is divided by {}".format(x, divisors))
       
       
print("Enter a number to find whether its  prime or not")       

user=int(input('Enter number: '))

is_prime(user)
