def brute_force(a, queries):
    ''' time complexity: O(K * N)'''
    sums = []
    # iterates over all queries
    for query in queries: # O(K)
        kSum = 0
        i, j = query
        # calculate sum for the query
        for index in range(i, j + 1): # O(N); total time complexity: O(K * N) because it's nested loop
            kSum += a[index]
        # save result
        sums.append(kSum)
    return sums

def faster(a, queries):
    ''' time complexity: O(K + N)'''
    # acc_sum[i] = a[0] + a[1] + a[2] + .... + a[i]
    acc_sum = [0] * len(a)
    # calculate accumulated sums
    current_sum = 0
    for index, num in enumerate(a): # O(N)
        current_sum += num
        acc_sum[index] = current_sum
    sums = []
    # iterates over all queries
    for query in queries: # O(K)
        i, j = query
        # calculates sum for the query
        # acc_sum[i] = a[0] + a[1] + a[2] + .... + a[i]
        # acc_sum[j] = a[0] + a[1] + a[2] + .... + a[i] + .... + a[j]
        # kSum = a[i] + acc_sum[j] - acc_sum[i] = a[i] + .... + a[j]
        kSum = a[i] + acc_sum[j] - acc_sum[i]
        # save the result
        sums.append(kSum)
    return sums

a = [1,2,3,4,5,6,7,8,9]
queries = [[1,1], [1,2], [1,3], [4,7], [5,8]]
print('brute force method: ', brute_force(a, queries))
print('faster method: ', faster(a, queries))