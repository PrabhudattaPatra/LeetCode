class Solution:
    def sumofsqofdigit(self,n:int):
        return sum(int(digit)**2 for digit in str(n))
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while fast != 0:
            slow = self.sumofsqofdigit(slow)
            fast = self.sumofsqofdigit(self.sumofsqofdigit(fast))
        
            if fast == 1:
                return True
            
            if slow == fast:
                return False
        
        return True
        