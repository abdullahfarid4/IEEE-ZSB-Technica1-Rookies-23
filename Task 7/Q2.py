class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while True:
            if len(stones) == 1:
                return stones[0]
            elif len(stones) == 0:
                return 0
            stones = sorted(stones)
            if stones[-1] == stones[-2]:
                stones.remove(stones[-1])
                stones.remove(stones[-1])
            else:
                stones[-1] -= stones[-2]
                stones.remove(stones[-2])
