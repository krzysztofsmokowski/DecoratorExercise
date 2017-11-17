import sys
def sanitize_input(funkcja):
    def wrapper(*argumenty):
        lista_argumentow = []
        for argument in argumenty:
            if argument.__class__.__name__=='str':
                lista_argumentow.append(int(argument))
            else:
                lista_argumentow.append(argument)
        return_value = funkcja(*lista_argumentow)
        true_return = ' '*20 + str(return_value)
        return true_return
    return wrapper

@sanitize_input
def dodaj(arg1, arg2):
    return arg1+arg2
@sanitize_input
def kwadrat(liczba):
    return liczba**2


print(dodaj(1,2))

dodaj('1',1)
kwadrat('3 ')


class Kalkulator(object):
    def __init__(self):
        pass
    @sanitize_input
    def dodaj(self, arg1, arg2):
        return arg1+arg2
    @sanitize_input
    def odejmij(self, arg1, arg2):
        return arg1-arg2

    @sanitize_input
    def kwadrat(self, arg1):
        return arg1**2

kalkulator = Kalkulator()


kalkulator.dodaj(3, 5)
kalkulator.odejmij(3, 5)
kalkulator.kwadrat(3)


print(kalkulator.dodaj('5        ', 7))
kalkulator.dodaj('2', '2')
kalkulator.kwadrat('2')

