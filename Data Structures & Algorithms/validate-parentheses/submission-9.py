class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {')' : '(',
                    '}' : '{',
                    ']' : '['}
        stack = []
        

        for i in s:
            if i not in hash_map:
                stack.append(i)

            else:
                if len(stack) == 0:
                    return False
                
                temp = stack.pop()
                if temp != hash_map[i]:
                    return False
        
        if not stack:
            return True            
        
        return False