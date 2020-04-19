from stack import Stack
"""
Stack client Parentheses that reads a string e.g. [()]{}{[()()]()}
and returns true if it's correct and false if not, e.g. for [(]).
"""
to_parse = input('Insert a string of parentheses,\ne.g. [()]{}{[()()]()}: ')
to_parse = ''.join(to_parse.split())

stack = Stack()

last_char = 'a'

for ch in to_parse:
    if (last_char == '{' and ch == '}'
    or last_char == '(' and ch == ')'
    or last_char == '[' and ch == ']'):
        stack.pop()
        if not stack.is_empty():
            last_char = stack.pop()
            stack.push(last_char)
        else:
            last_char = 'a'
    else:
        stack.push(ch)
        last_char = ch

print(stack.is_empty())