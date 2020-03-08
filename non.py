import random
import time


def randomSet():
    #initialize the array
    set = []

    #set length of array
    length = 20

    #for loop append randomize numbers into array
    for i in range(length):
        set.append(random.randint(1, 200))
    
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
    #print(set)

    sum = sumOfSet(set)

    #print(sum)

    #if the sum is divisible by 3, it can be divided into 3 partitions with equal sum
    if (sum % 3) == 0 :
        #print(sum)
        return set
    else:
        return False


def greedy(arr):
    A = []
    B = []
    C = []
    #numbers are sorted
    print(arr);
    for i in sorted(arr, reverse=True):
        #print(sum(A))
        if sum(A) <= sum(B) and sum(A) <= sum(C):
            A.append(i)

        elif sum(B) <= sum(A) and sum(B) <= sum(C):
            B.append(i)
            
        else: 
            C.append(i)
    print("Set A :", A, "\n" , "Set B :", B, "\n", "Set C :",C, "\n")
    return (A,B,C)
    

#main is the solution, arr is the another array from greedy where numbers
#not in solution is stored, target is the half of total sum, dif is difference to target
def localSearch(main, arr, target, dif):
    
    betterMain = []
    betterArr = []

    #print("before local search: ", main)

    for h in range(3):
        
        #Step 1: add a smallest number into main array to swaps and search for a better solution
        if h==1 and abs(target - _sum(main,len(main))) != 0:
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
                    #print("Found: ",main, " and ", arr)
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

def compareDiffSets(diffA,diffB,diffC){
    result = False
    if abs(difSetA) <= abs(difSetB):
        a = True
    elif abs(difSetC) <= abs(difSetB):
        a = True
    elif abs(difSetA) <= abs(difSetC)
        a = True
    elif abs(difSetB > difSetA):
        a = True
    elif abs(difSetA < difSetB):
        a = True
    else:
        a = True
    return result, a
}

def main():
    #for best solution found

    for i in range (1):
        t = time.perf_counter_ns()#initialize var to store starting time
        f = open("factor_3_nonexact.txt", "a+")

        betterA = []
        betterB = []
        betterC = []
        betterDif1 = 0   
        betterDif2 = 0   

        set = initialArr()
        while set == False:
            set = initialArr()

        setA, setB, setC = greedy(set)# get partitions after greedy - return 3 arrays 

        #get a solution that is better
        sum = sumOfSet(set)
        #print(sum)

        # to get difference to sum/3
        difSetA = sum/3 - _sum(setA, len(setA))
        difSetB = sum/3 - _sum(setB, len(setB))
        difSetC = sum/3 - _sum(setC, len(setC))
        print('difSetA :', difSetA, difSetB, difSetC)


        betterA.extend(setA); 
        betterB.extend(setB);
        betterC.extend(setC);
        
        betterDif1 += difSetA
        betterDif2 += difSetB

        #print("A",sum - _sum(setA, len(setA))," B",sum - _sum(setB, len(setB)))
        #print(abs(difSetA) < abs(difSetB))
        print("Total Set A ", _sum(setA, len(setA)))
        print("Total Set B ", _sum(setB, len(setB)))
        print("Total Set C ", _sum(setC, len(setC)))
        print("difSetA : ",abs(difSetA))
        print("difSetB : ",abs(difSetB))
        print("difSetC : ",abs(difSetC))
        # if the difference to the half of the sum of array is smaller, that is a better solution
        if sum/3 == _sum(setA, len(setA)) and sum/3 == _sum(setB, len(setB)) and sum/3 == _sum(setC, len(setC)):
            #print("Found: ", setA, " and ", setB)
            elapsed_time = time.perf_counter_ns() - t
            #print(elapsed_time/1000000)
            f.write(str(elapsed_time/1000000)+"\n")
        elif compareDiffSets(abs(difSetA),abs(difSetB),abs(diffSetC)) == True :
            # print(setA, setB, sum/3, difSetA);
            sA, sB, sDif, found = localSearch(setA,setB,sum/3, difSetA)
            
            betterA,betterB,betterDif = getBetter(sA,sB,betterA,betterB,betterDif1,sum/3)

            for n in range(99):
                if found is True:
                    elapsed_time = time.perf_counter_ns() - t
                    #print(elapsed_time/1000000)
                    f.write(str(elapsed_time/1000000)+"\n")
                    break
                sA, sB, sDif, found = localSearch(sA,sB, sum/3, sDif)

                betterA,betterB,betterDif = getBetter(sA,sB,betterA,betterB,betterDif1,sum/3)

                
            if found is False:
                #print("Better solution: ",betterA," and ", betterB, sumOfSet(betterA))
                elapsed_time = time.perf_counter_ns() - t
                #print(elapsed_time/1000000)
                f.write(str(elapsed_time/1000000)+"\n")        

        else:
            sB, sA, sDif, found = localSearch(setB,setA, sum/3, difSetB)

            betterA,betterB,betterDif = getBetter(sB,sA,betterA,betterB,betterDif1,sum/3)


            for n in range(99):
                if found is True:# to avoid going in the loop anymore if solution is found
                    elapsed_time = time.perf_counter_ns() - t
                    #print(elapsed_time/1000000)
                    f.write(str(elapsed_time/1000000)+"\n")
                    break
                sB, sA, sDif, found = localSearch(sB,sA, sum/3, sDif)

                betterA,betterB,betterDif = getBetter(sB,sA,betterA,betterB,betterDif1,sum/3)


            if found is False:
                #print("Better solution: ",betterA," and ", betterB, sumOfSet(betterA))
                elapsed_time = time.perf_counter_ns() - t
                #print(elapsed_time/1000000)
                f.write(str(elapsed_time/1000000)+"\n")

        print("--- %s seconds ---" % str(elapsed_time/1000000)+"\n")
        f.close()
    

main()

# print(abs(1/3 - _sum(main,len(main))))
