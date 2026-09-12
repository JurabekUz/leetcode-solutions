
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        res = []
        for i in range(1, n + 1):
            item = ""
            if i % 3 == 0:
                item = "Fizz"
            if i % 5 == 0:
                item += "Buzz"
            item = item or str(i)
            res.append(item)
        return res
