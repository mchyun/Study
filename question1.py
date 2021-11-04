def isSubset(arr1, arr2):
    x = 0
    for x in range(len(arr2)):
        if(arr2[x] not in arr1):
            return False
    return True

arr1 = ["A", "B", "C", "D", "E"]
arr2 = ["A", "A", "D", "E"]

if(isSubset(arr1, arr2)):
    print("True")
else:
    print("False")
