class Solution(object):
    def kthSmallest(self, matrix, k):
        list=[val for row in matrix for val in row]
        list.sort()
        return list[k-1]
        