class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        res, m = [], len(potions)
        for spell in spells:
            lb, ub = 0, m - 1
            if potions[0] * spell >= success: 
                res.append(m)
                continue
            if potions[-1] * spell < success:
                res.append(0)
                continue
            while lb <= ub:
                mid = (lb + ub) // 2
                if potions[mid] * spell < success and mid + 1 < m and potions[mid + 1] * spell >= success:
                    break
                elif potions[mid] * spell < success:
                    lb = mid + 1
                else:
                    ub = mid - 1
            res.append(m - mid - 1)
        return res