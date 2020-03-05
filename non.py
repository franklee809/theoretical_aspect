import random
import time


def randomSet():
    #initialize the array
    set = []

    #set length of array
    length = 10

    #for loop append randomize numbers into array
    for i in range(length):
        set.append(random.randint(1, 100))
    
    return set

def sumOfSet(set):
    sum = 0
    for i in range (len(set)):
        sum += set[i]
    return sum

def initialArr():
    #get set from randomSet function
    set = randomSet()
    #print out array
    print(set)

    sum = sumOfSet(set)

    #print(sum)

    #if the sum is divisible by 2, it can be divided into 2 partitions with equal sum
   # if (sum%2) == 0 :
        #print(sum)
    return set
    """else:
        return False"""


def greedy(arr):
    A = []
    B = []
    #numbers are sorted
    for i in sorted(arr, reverse=True):
        if sum(A) < sum(B):
            A.append(i)
        else: 
            B.append(i)
    return (A,B)

#main is the solution, arr is the another array from greedy where numbers
#not in solution is stored, target is the half of total sum, dif is difference to target
def localSearch(main, arr, target, dif):
    
    betterMain = []
    betterArr = []

    #print("before local search: ", main)

    for h in range(3):
        #add a smallest number into main array to swaps and search for a better solution

        if h==1 and abs(target - _sum(main,len(main))) is not 0:
            minIndex = 0
            for k in range(len(arr)):
                if k == 0:
                    min=arr[k]
                elif min>arr[k]:
                    min = arr[k]
                    minIndex=k
                       
            #print("h ==1: ", arr, minIndex)  #this print for determine which index in arr has smallest value
              
            main.append(arr[minIndex])# append the eliminated number to arr

            arr.remove(arr[minIndex])# remove eliminated number, which is the smallest one

        #remove 2 smallest number from the main array to search for better solution (also append the removed number to arr)
        if h==2:
            for m in range(2):
                minIndex = 0
                for k in range(len(main)):
                    if k == 0:
                        min=main[k]
                    elif min>main[k]:
                            min = main[k]
                            minIndex=k
                
                arr.append(main[minIndex])# append the eliminated number to arr

                main.remove(main[minIndex])# remove eliminated number, which is the smallest one


        for i in range(len(main)):
            #print("New Loop")
            for j in range(len(arr)):
                temp = main[i]    #store swapped number from main
                main[i] = arr[j]
                #print("in loop:", main, "sum",_sum(main,len(main)), abs(target - _sum(main,len(main))), dif, (abs(target - _sum(main,len(main))) < dif))

                if target == _sum(main,len(main)):                    
                    arr[j] = temp
                    print("Found: ",main, " and ", arr)
                    return main, arr, dif, True
                    break

                elif abs(target - _sum(main,len(main))) < dif:
                          
                    betterMain = []
                    betterArr = []
                    betterMain.extend(main)
                    betterArr.extend(arr)

                    arr[j] = temp

                    dif = abs(target - _sum(main,len(main)))

                    #print("changed", main, "   ", arr, abs(target - _sum(main,len(main))))

                else:
                    main[i] = temp

    if (len(betterMain) > 0 ):
        #print("better", betterMain," and ", betterArr)
        if betterMain is not None:
            #print('better return:' , betterMain," and ", betterArr)
            return betterMain, betterArr, abs(target - _sum(betterMain,len(betterMain))), False
    else:#if after local search, neighbourhood does not have better solution, return and halt

        #add back smallest number to back to the original array
        minIndex = 0
        for k in range(len(arr)):
            if k == 0:
                min=arr[k]
            elif min>arr[k]:
                min = arr[k]
                minIndex=k
                       
        main.append(arr[minIndex])# append the eliminated number to arr
        arr.remove(arr[minIndex])# remove eliminated number, which is the smallest one

        
        #print('RANDOMED')
        numbersToChange = random.randint(0, len(main))

        for i in range (numbersToChange):
            numToAppend = random.randint(0, len(arr)-1)#so that it randoms in array index
            numToRemove = random.randint(0, len(main)-1)#so that it randoms in array index

            main.append(arr[numToAppend])
            arr.remove(arr[numToAppend])

            arr.append(main[numToRemove])
            main.remove(main[numToRemove])
 
       #print("Best solution can be found", main, "and", arr)
        return main, arr, abs(target - _sum(main,len(main))), False
        
    

def getBetter(A, B, betterA,betterB, betterDif, target):
    #print('before go in and change better arrays',abs(betterDif) , abs(target-sumOfSet(A)), betterA, sumOfSet(betterA), A, sumOfSet(A))
    if abs(betterDif) > abs(target-sumOfSet(A)):
        betterA = []
        betterB = []
        betterA.extend(A)
        betterB.extend(B)
        betterDif = abs(target-sumOfSet(A))
        #print('take only better: ', betterA, 'and' , betterB, sumOfSet(betterA))

    return betterA,betterB,betterDif



def _sum(arr, n):
    return sum(arr)


def main():
    #for best solution found

    for i in range (20):
        t = time.perf_counter_ns()#initialize var to store starting time
        f = open("factor_3_nonexact.txt", "a+")

        betterA = []
        betterB = []
        betterDif = 0   

        set = initialArr()
        while set == False:
            set = initialArr()

        setA, setB = greedy(set)# get partitions after greedy

        #print("A", setA)
        #print("B", setB)

        #get a solution that is better
        sum = sumOfSet(set)
        #print(sum)

        # to get difference to sum/2
        difSetA = sum/2 - _sum(setA, len(setA))
        difSetB = sum/2 - _sum(setB, len(setB))

        betterA.extend(setA)
        #print('betterA',betterA)
        betterB.extend(setB)
        betterDif += difSetA

        #print("A",sum - _sum(setA, len(setA))," B",sum - _sum(setB, len(setB)))
        #print("A",difSetA," B",difSetB)
        #print(abs(difSetA) < abs(difSetB))

        # if the difference to the half of the sum of array is smaller, that is a better solution
        if sum/2 == _sum(setA, len(setA)):
            #print("Found: ", setA, " and ", setB)
            elapsed_time = time.perf_counter_ns() - t
            #print(elapsed_time/1000000)
            f.write(str(elapsed_time/1000000)+"\n")
        elif abs(difSetA) <= abs(difSetB):
            #print(sum/2, " ", difSetA)

            sA, sB, sDif, found = localSearch(setA,setB, sum/2, difSetA)
            
            betterA,betterB,betterDif = getBetter(sA,sB,betterA,betterB,betterDif,sum/2)

            for n in range(99):
                if found is True:
                    elapsed_time = time.perf_counter_ns() - t
                    #print(elapsed_time/1000000)
                    f.write(str(elapsed_time/1000000)+"\n")
                    break
                sA, sB, sDif, found = localSearch(sA,sB, sum/2, sDif)

                betterA,betterB,betterDif = getBetter(sA,sB,betterA,betterB,betterDif,sum/2)

                
            if found is False:
                #print("Better solution: ",betterA," and ", betterB, sumOfSet(betterA))
                elapsed_time = time.perf_counter_ns() - t
                #print(elapsed_time/1000000)
                f.write(str(elapsed_time/1000000)+"\n")
                

        else:
            sB, sA, sDif, found = localSearch(setB,setA, sum/2, difSetB)

            betterA,betterB,betterDif = getBetter(sB,sA,betterA,betterB,betterDif,sum/2)


            for n in range(99):
                if found is True:# to avoid going in the loop anymore if solution is found
                    elapsed_time = time.perf_counter_ns() - t
                    #print(elapsed_time/1000000)
                    f.write(str(elapsed_time/1000000)+"\n")
                    break
                sB, sA, sDif, found = localSearch(sB,sA, sum/2, sDif)

                betterA,betterB,betterDif = getBetter(sB,sA,betterA,betterB,betterDif,sum/2)


            if found is False:
                #print("Better solution: ",betterA," and ", betterB, sumOfSet(betterA))
                elapsed_time = time.perf_counter_ns() - t
                #print(elapsed_time/1000000)
                f.write(str(elapsed_time/1000000)+"\n")

        print("--- %s seconds ---" % str(elapsed_time/1000000)+"\n")
        f.close()
    

main()
