class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)//2
        skills=sum(skill)
        if skills%n !=0:
            return -1
        left=0
        right=len(skill)-1
        sumc=0
        skill=sorted(skill)
        while left<right:
            if skill[left]+skill[right]==skills//n:
                sumc+=skill[left]*skill[right]
                left+=1
                right-=1
            else:
                return -1
        return int(sumc)
       
            
            
            
        
