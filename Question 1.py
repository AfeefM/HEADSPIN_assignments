#write a program to insert an element into an array to the n th position without using any inbuilt functions
arr=[1,2,3,4,5,6,7,8,9,10]   #array
position=3       #position to which element to be inserted
insert_num=5     #element to be inserted
index=position-1    
ar1=arr[:index]
ar2=[insert_num]
ar3=arr[index:]
print(ar1+ar2+ar3)
