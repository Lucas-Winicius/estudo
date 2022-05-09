def factorial(n=1, show=False):
    """
    -> CALCULA O FATORIAL DE UM NUMERO.
    :param n: O NUMERO A SER CALCULADO
    :param show: (OPCONAL) MOSTRAR OU NAO A CONTA
    :return: O VALOR DO FATORIAL DE UM NUMERO n
    Function created BY: Abobora
    """
    f = 1
    if show == True:
        for c in range(n, 0, -1):
            if c > 1:
                print(c, end=' X ')
            else:
                print(c, end=' = ')
            f *= c
        return f
    else:
        for c in range(n, 0, -1):
            f *= c
        return f


print('-'*25)
print(factorial(5, True))