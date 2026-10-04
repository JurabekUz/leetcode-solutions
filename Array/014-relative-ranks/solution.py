class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        ranks = {
            value: rank
            for rank, value in enumerate(sorted(score, reverse=True), start=1)
        }

        answer = []

        for value in score:
            rank = ranks[value]

            if rank == 1:
                answer.append("Gold Medal")
            elif rank == 2:
                answer.append("Silver Medal")
            elif rank == 3:
                answer.append("Bronze Medal")
            else:
                answer.append(str(rank))

        return answer
