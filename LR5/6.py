n, p = int(input('Vvedite cictemy c4isleniya: ')), int(input('Vvedite 4islo: '))
def convert(n, p): return convert(n, p // n) * 10 + p % n if p > 0 else 0
print(convert(n, p))
