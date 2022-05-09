def linha(txt):
    print('-'*45)
    print(f'{txt:^45}')
    print('-'*45)

def opcs(lst):
    for o, o1 in enumerate(lst):
        if o < 9:
            print(f'{o+1:^2} -  {o1}')
        else:
            print(f'{o+1:^2} - {o1}')
    print()

