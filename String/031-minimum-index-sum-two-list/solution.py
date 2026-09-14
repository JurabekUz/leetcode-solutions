class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        res = []
        min_sum = None
        for i in range(len(list1)):
            if list1[i] in list2:
                j = list2.index(list1[i])
                if min_sum == None or min_sum == j + i:
                    min_sum = i + j
                    res.append(list1[i])
                elif i + j < min_sum:
                    res = [list1[i]]
                    min_sum = i + j
        return res







