class Solution:
    def findRestaurant(self, list1, list2):
        nameToIndex = {}
        minSumIndex = float('inf')
        sumIndexToNames = {}
        for index, name in enumerate(list1):
            nameToIndex[name] = index
        for index, name in enumerate(list2):
            list1Index = nameToIndex.get(name)
            if list1Index != None:
                sumIndex = list1Index + index
                names = sumIndexToNames.get(sumIndex)
                if names != None:
                    sumIndexToNames[sumIndex] = [*names, name]
                else:
                    sumIndexToNames[sumIndex] = [name]
                if sumIndex < minSumIndex:
                    minSumIndex = sumIndex
            else:
                continue
        return sumIndexToNames[minSumIndex]

solution = Solution()
list1 = ["KFC"]
list2 = ["KFC"]
print(solution.findRestaurant(list1, list2))