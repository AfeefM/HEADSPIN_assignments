#write a program to display prime numbers between 2 intervals without using any inbuilt functons
interval1=int(input("Enter lower prime number"))  #lower interwal
interval2=int(input("Enter higher prime number"))  #higer interval
for num in range(interval1,interval2 + 1): 
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  
