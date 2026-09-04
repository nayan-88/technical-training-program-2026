def linearSearch(array,value):
    for index in range(len(array)):#i=0
        if array[index] == target:
            return index
    return -1


array =[1,2,3,4,5,6,7,8,9]
target = 7
result=linearSearch(array,target)
if result == -1:
    print("value not found")
else:
    print("value found at index", result)