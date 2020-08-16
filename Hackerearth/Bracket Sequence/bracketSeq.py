def brak(a):
    count = 0
    if '()' in a:
        count += 1
    if ')' in a:
        count += 1
    if '(' in a:
        count += 1
    return count

a = [')', '()', '()', '(']
print(brak(a))
