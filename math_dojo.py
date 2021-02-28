
class Math_Dojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in range ( len(nums) ):
            self.result += nums[i]
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for i in range ( len(nums) ):
            self.result -= nums[i]
        return self

md = Math_Dojo()

x = md.add(2).add(6,7).add(7,8,9).subtract(2).subtract(7,10).subtract(5,8,9).result
print(x)