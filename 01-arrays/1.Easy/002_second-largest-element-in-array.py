class Solution:
    def secondLargest(self, arr, n):
        s = sorted(set(arr))
        return s[-2] if len(s) > 1 else -1