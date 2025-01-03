def findPermutations(nums, target):
    #create an array to store the solution of the subproblems
    T = [0] * (target + 1)
    # there is only one way to reach the target of 0 - dont consider any element
    T[0] = 1
    #fill T[] in bottom-up manner
    for i in range(1, len(T)):
        for k in nums:
            if i - k >= 0:
                T[i] += T[i - k]

    
    #last element of T[] stores the result
    return T[target]

if __name__ == '__main__':
    nums = [1,2,3]
    target = 4

    print(findPermutations(nums, target))