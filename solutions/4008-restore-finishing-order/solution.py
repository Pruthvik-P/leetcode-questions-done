class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        wins = []
        for i in order:
            for j in friends:
                if i == j:
                    wins.append(i)

        return wins
