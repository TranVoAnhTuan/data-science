def shortest_subarray(arr):
    n = len(arr)
    min_len = n + 1
    left = 0
    right = 0
    count = 0
    hash_map = {}
    while right < n:
        if arr[right] not in hash_map:
            count += 1
            hash_map[arr[right]] = 0
        hash_map[arr[right]] += 1
        while count == len(set(arr)):
            if right - left + 1 < min_len:
                start = left
                end = right
                min_len = right - left + 1
            hash_map[arr[left]] -= 1
            if hash_map[arr[left]] == 0:
                count -= 1
            left += 1
        right += 1
    return arr[start:end + 1]


if __name__ == '__main__':
    arr = [2,1,1,2,1,1,11,1,5,2,7,1]
    print(shortest_subarray(arr))
# sliding window