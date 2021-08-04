'''
You have an array C = [1,-4,5,3,2] or distinct integers. You need to choose exactly 3
numbers from the array such that their sum is closes to the target value T = 5
Test 1:
Input > C = [1,-4,5,3,2] , T = 5
Output> the closest to the target value 5 is sum of [-4,5,3] =4 or [1,3,2] = 6
Test 2:
Input > C = [7,20,-6,4,6] , T = 20
Output> the closest to the target value 20 is sum of [20,-6,6] = 20 exactly
'''


# Python3 implementation of the above approach
import sys
 
# Function to return the sum of a
# triplet which is closest to x
def solution(arr, x):
 
    # To store the closets sum
    equlaSum = 0
    closestSum = sys.maxsize
    closetsum_lst = []
    closestSumLess = arr[0]
    closestSumLess_lst = []
    equlaSum_lst = []
    flag = x
    # Run three nested loops each loop
    # for each element of triplet
    for i in range (len(arr)) :
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len( arr)):
             
                # Update the closestSum
                if(abs(x - closestSum) >
                abs(x - (arr[i] +arr[j] + arr[k]))):
                    if abs(arr[i] +arr[j] + arr[k]) != abs(x):
                        closestSum = (arr[i] +
                                        arr[j] + arr[k])
                        closetsum_lst = [arr[i], arr[j], arr[k]]                
                if(abs(x - (arr[i] +arr[j] + arr[k]))) < abs(x):
                    diff = abs(x - (arr[i] +arr[j] + arr[k]))
                    if abs(arr[i] +arr[j] + arr[k]) != abs(x):
                        if diff < flag and  x > abs(arr[i] +arr[j] + arr[k]):
                            closestSumLess = (arr[i] +arr[j] + arr[k])
                            closestSumLess_lst = [arr[i], arr[j], arr[k]] 
                            flag = diff
                if(abs(arr[i] +arr[j] + arr[k])) == abs(x):
                    equlaSum = abs(x)
                    equlaSum_lst = [arr[i], arr[j], arr[k]]
                    
    
    if equlaSum:
        return equlaSum, closetsum_lst
    # Return the closest sum found
    elif closestSum and closestSumLess:
        return closestSum,closetsum_lst, closestSumLess,closestSumLess_lst
 
# Driver code
if __name__ == "__main__":
    
    #Give space seprated input 
    arr = list(map(int,input("\nInput C= ").strip().split()))
 
    #Give target value
    x = int(input("Input T = "))
    print("The closest to the target value",x,'is a sum of',arr,':', solution(arr, x))
     
