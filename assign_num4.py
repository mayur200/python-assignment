'''You have to write a program for an ATM. You know there are only denominations for 1,
5, 10, 20, 100. Considering you have unlimited number of coins and notes in
each denomination. For an input of X withdrawal amount, What is the
minimum number of coins/notes for the ATM to dispense.
Test 1:
Input: X= 120
Output : 2 {by 2 notes of 100 and 20 denomination}'''
import collections

def wtdAtm(amount):
    
    # All denominations
    lst_denom = [1,5,10,20,100]
    num = len(lst_denom)
     
    # Initialize Result
    
    
    ans = []
 
    # Traverse through all denomination
    i = num - 1
    while(i >= 0):
         
        # Find denominations
        while (amount >= lst_denom[i]):
            amount -= lst_denom[i]
            ans.append(lst_denom[i])
 
        i -= 1
    # Count number of notes/coins required
    lst_number = [i for i in range(len(ans))]
    print(ans)
    print(len(lst_number))
    
    #convert to dictionary
    lsta = [20,20,10,1,1,1]
    dict_ans = collections.Counter(ans)
    print("{By",end=" ")
    
    #Display data in given format
    for i, (x, y) in enumerate(sorted(dict_ans.items())):
        if x == 1 and i != len(dict_ans)-1:
            print(x,"denoamination of",y,"and",end=" ")
        elif x != 1 and i != len(dict_ans)-1:    
            print(x,"notes of",y,"and",end=" ")
        if i == len(dict_ans)-1:
            print(x,"notes of",y,end=" ")
    print("}",end=" ")
     
# Driver Code
if __name__ == '__main__':
    amount = int(input("Input: X="))
    print("output:", amount, ": ", end = "")
    wtdAtm(amount)

