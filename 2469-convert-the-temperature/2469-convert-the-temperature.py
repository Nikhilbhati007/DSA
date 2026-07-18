class Solution(object):
    def convertTemperature(self, celsius):
        ans=[]
        kel= celsius + 273.15
        ans.append(kel)
        fra= celsius * 1.80 + 32.00
        ans.append(fra)
        return ans
