class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        self.__elements.sort()
        n = len(self.__elements) # size N
        self.maximumDifference = abs(self.__elements[n - 1] - self.__elements[0]) #positive number

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
