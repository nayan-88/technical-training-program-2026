arr=[10,11,7,12,8]
dis=0
for i in range(len(arr) - 1):
    dis+=abs(arr[i]-arr[i+1])

    print(dis)

