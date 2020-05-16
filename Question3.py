#how to find the missing number in the given integer array of 1 to 100 without using any inbuilt functions
array=[1,2,3,4,5,6,7,8,12,16,19,20,34,40,45,49,55,67,78,89,90]    #array with missing number
def missing_number(array):
    for num in range (1,100):        #range between 1to100
        if num not in array:
            print(num)
missing_number(array)        
