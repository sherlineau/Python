class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for a in nums:
            self.result += a
        return self

    def subtract(self, num, *nums):
        # if self.result == 0:
        #     self.result += num
        self.result -= num
        for a in nums:
            self.result -= a
        return self

# create an instance:
md = MathDojo()
ni = MathDojo()
ai = MathDojo()

# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5

y = ni.add(5).add(2,5,1).add(2,5,1).add(2,5,1).result
print(y)

a = ai.add(2,5).subtract(2,5,1).subtract(3,2).result 
print(a)
# run each of the methods a few more times and check the result!