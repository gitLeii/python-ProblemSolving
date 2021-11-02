

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum_ = n
        for i in range(1,n//2+1):
            if n%i == 0:
                sum_ +=i
        return sum_

