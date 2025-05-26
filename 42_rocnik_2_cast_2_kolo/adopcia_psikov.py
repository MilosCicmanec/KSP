n = input()
s = input()

stack = []

for char in s:
    if stack and ((stack[-1] == "C" and char == "P") or (stack[-1] == "P" and char == "C")):
        stack.pop()
    else:
        stack.append(char)

print(len(stack))

