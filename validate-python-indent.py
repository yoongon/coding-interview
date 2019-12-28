def get_inputs(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    inputs = list(map(lambda x:x.rstrip(), lines))
    return inputs

def validate_indents(inputs):
    stack, prev, prev_diff = [], None, 0

    for org in inputs:
        mod = org.strip()
        if not mod or mod[0] == '#':
            continue

        diff = len(org) - len(mod)
        if prev is not None and prev[-1] == ':':
            if diff <= prev_diff: return False
        else:
            while stack and diff < stack[-1]:
                stack.pop()
            if stack and diff != stack[-1]:
                return False

        stack.append(diff)
        prev, prev_diff = org, diff
    return True

if __name__ == '__main__':
    inputs = get_inputs('sample.py')
    res = validate_indents(inputs)
    print (res)
