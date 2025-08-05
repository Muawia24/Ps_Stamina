class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for i, fruit in enumerate(fruits):
            for j in range(len(baskets)):
                if baskets[j] >= fruit:
                    baskets.pop(j)
                    break
        return len(baskets)        