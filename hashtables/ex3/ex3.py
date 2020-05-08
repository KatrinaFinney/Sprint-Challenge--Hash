def intersection(arrays):
    
    arr = []
    h = {}

    for i in arrays:
        for j in i:
            if j in h:
                h[j] += 1
            else:
                h[j] = 1

    for key in h.keys():
        if h[key] == len(arrays):
            arr.append(key)

    return arr


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
