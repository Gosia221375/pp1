def f(array2D):
    result = []
    for array in array2D:
        for x in range(len(array)):
            if len(result) < x+1:
                result.append(array[x])
            else:
                result[x] = result[x]+ array[x]
    return result


arr = [ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]

print(f(arr))
