def median(l):
    half = len(l)//2
    l.sort()
    if not len(l)%2:
        return (l[half - 1] + l[half]) / 2.0
    return (l[half])

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = 0
        array1 = []
        for i in range(len(nums1)):
            array1.append(nums1[i])
        for j in range(len(nums2)):
            array1.append(nums2[j])
        for z in range(len(array1)):
            array1.sort()
        return median(array1)