class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        score=0
        for parenthesises in s:
            if parenthesises =='(':
                stack.append(score)
                score=0
            else:
                score=stack.pop()+max(1,2*score)
        return score;
        
