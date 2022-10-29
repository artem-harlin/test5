def printStatistics(arr):
    arr.sort()
    print('count:', len(arr))
    if len(arr) == 0:
        print('average: 0')
    else:
        print('average:', sum(arr)/len(arr))       
    if len(arr) == 1:
        arr1 = arr.copy()
        n = arr1.pop(0)
        if n == 0:
            print('min: 0')
            print('max: 0')
        else:
            print('min:', float(n))
            print('max:', float(n))