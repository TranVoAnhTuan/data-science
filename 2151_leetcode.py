import copy
def maximumGoodPeople(statements):
    maxGood = 0
    n = len(statements)
    assumption = [2] * n
    def backtrack(id, assumption):
        nonlocal maxGood
        good = sum(assumption)
        
        if id == n:
            if good > maxGood:
                maxGood = good
                return
        if good + n - id < maxGood:
            return
        if assumption[id] == 2 or assumption[id] == 1:
            nextAssumption = copy.copy(assumption)
            for j in range(n):
                if statements[id][j] == 2:
                    continue
                if assumption[j] == 2:
                    nextAssumption[j] = statements[id][j]
                elif assumption[j] != statements[id][j]:
                    break
            else:
                nextAssumption[id] = 1
                backtrack(id+1,nextAssumption)
        if assumption[id] == 2 or assumption[id] == 0:
            nextAssumption = copy.copy(assumption)
            nextAssumption[id] = 0
            backtrack(id+1, nextAssumption)
    backtrack(0, assumption)
    return maxGood
if __name__ == '__main__':
    arr = [[2,1,2],[1,2,2],[2,0,2]]
    print(maximumGoodPeople(arr))
            