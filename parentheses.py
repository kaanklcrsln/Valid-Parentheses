class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # s is a string that only has '(', ')', '{', '}', '[' and ']'
        # s is valid if all the brackets match like { }
        # s is not valid if brackets mismatch like { ]

        for char in s:
            # if it's an opening bracket, push it onto the stack
            if char in "({[":
                stack.append(char)
            else:
                # if stack is empty or the match is wrong, it's invalid
                if not stack:
                    return False
                last = stack.pop()
                if char == ")" and last != "(":
                    return False
                if char == "]" and last != "[":
                    return False
                if char == "}" and last != "{":
                    return False
        
        # if stack is empty at the end, everything matched up
        return not stack
