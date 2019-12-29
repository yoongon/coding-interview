import re
def get_inputs(filename):
    with open(filename, 'r') as f:
        s = f.read()
    s = remove_comments_slash(s)
    valid, s = compress_nests(s)

    if valid:
        inputs = list(map(lambda x:x.rstrip(), s.split('\n')))
    return inputs

def remove_comments_slash(s):
    return re.sub('#.*|\'\'\'(.|\n)*?\'\'\'|"""(.|\n)*?"""|\\\(.)*?\n', '', s)

def compress_nests(s):
    det = {'}': '{', ']': '[', ')': '('}
    res, stack = '', []

    for c in s:
        if c in '{[(':
            stack.append(c)
        elif c in det:
            if stack and det[c] == stack[-1]:
                stack.pop()
            else:
                return False, None

        if stack and c == '\n':
            continue
        res += c
    return not stack, res

def validate_indents(inputs):
    stack, prev, prev_diff = [], None, 0
    skip = False

    for org in inputs:
        mod = org.strip()

        if mod and mod[:3] == '\'\'\'':
            if len(mod) > 3 and mod[-3:] == '\'\'\'':
                skip = False
            else:
                skip = True

        if not mod or mod[0] == '#' or skip:
            continue

        diff = len(org) - len(mod)
        if prev is not None and prev[-1] == ':':
            if diff <= prev_diff:
                return False
        else:
            while stack and diff < stack[-1]:
                stack.pop()
            if stack and diff != stack[-1]:
                return False

        stack.append(diff)
        prev, prev_diff = org, diff
    return True

if __name__ == '__main__':
    s = get_inputs('sample.py')
    res = validate_indents(s)
    print (res)
