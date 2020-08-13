def valid_parentheses(chars):
    if len(chars) == 1:
        return False
    if not chars:
        return True  

    balanced = True                                     # Using this to flag if we find ")" when there are no "("'s to match
    stack = []

    for i in range(len(chars)):
        if chars[i] == "(":
            stack.append(chars[i])                      # If we come across a "(" add it to the stack
        elif chars[i] == ")":
            if len(stack) > 0:                          # If there is a matching "(" for our ")" remove from stack
                stack.pop()
            elif len(stack) == 0:                       # Case for if we've come across a ")" with no matching ( before it
                balanced = False
        
    if balanced and len(stack) == 0:
        return True
    else:
        return False


print(valid_parentheses("vpbkmt(v()jl)xkeiyicl"))