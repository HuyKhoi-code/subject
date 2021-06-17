def print_brackets (brackets, n):
    balance (brackets, n , 0, 0, 0)
    return
def balance (brackets, n, pos, op, cl):
    if (cl ==n):
        print (*brackets)
    else:
        if (cl< op):
            brackets[pos] = ')'
            balance (brackets, n , pos+1, op, cl+1)
        if (op < n):
            brackets[pos] = '('
            balance (brackets, n, pos+1, op+1, cl)

n = int(input())
brackets = [" "] * 2 * n
print_brackets(brackets, n)

