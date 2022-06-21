class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ch = letters[0]
        lb, ub = 0, len(letters) - 1
        while lb <= ub:
            mid = (lb + ub) // 2
            if letters[mid] > target:
                ch = letters[mid]
                ub = mid - 1
            else: lb = mid + 1
        return ch
            