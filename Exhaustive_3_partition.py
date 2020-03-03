import numpy as np
import random
import time

# Determine if a partition can be divided  
# Into three subsets of equal sum.

def randomSet():
    set = []
    # Size of Array.
    size = 20

    for i in range(size):
        r = random.randint(1, 100) 
        set.append(r)

    return set

def partition(arr, n) : 
    sum_part = sum(arr)
     
    if (sum_part % 3 != 0 ) : 
        return False
      
    k = sum_part >> 1
  
    dp = np.zeros((n + 1, k + 1)) 
  
    for i in range(1, k + 1) :  
        dp[0][i] = False
  
    for i in range(n + 1) :  
        dp[i][0] = True
  
    for i in range(1, n + 1) :  
        for currSum in range(1, k + 1) :  
  
            dp[i][currSum] = dp[i - 1][currSum] 
  
            if (arr[i - 1] <= currSum) : 
                dp[i][currSum] = (dp[i][currSum] or
                                  dp[i - 1][currSum - arr[i - 1]])
 

    if (not dp[n][k]) :  
        return False

    set1, set2, set3 = [], [], []
     
    return True
    
  
# Driver Code 
if __name__ == '__main__':
    for i in range (50):
        set = randomSet()
        n = len(set)

        start = time.time()

        result = partition(set, n)
        print(result)

        while result == False:
            set = randomSet()
            #print(set)
            result = partition(set, n)
          
        end = time.time()
        elapsed_time = end - start
        print("--- %s seconds ---" % str(elapsed_time)+"\n")
        f = open("S1.txt", "a+")
        f.write(str(elapsed_time)+"\n")
        f.close()
        

