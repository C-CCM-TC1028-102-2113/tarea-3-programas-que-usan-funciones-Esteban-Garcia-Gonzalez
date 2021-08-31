def palbanene(cpa, t):
    t=12
    total= cpa*t
    return total
def plumon (cpl, t):
    t=35
    total2=cpl*t
    return total2
def main():
    cpa= int(input('Dame la cantidad de pliegos de papel albanene: '))
    cpl= int(input('Dame la cantidad de plumones: '))
    t=0
    if (palbanene(cpa,t)<plumon(cpl,t)):
        print('El número máximo de tarjetas que se pueden hacer es: '+str(palbanene(cpa,t)))
    elif (plumon(cpl,t)<palbanene(cpa,t)):
        print('El número máximo de tarjetas que se pueden hacer es: '+str(plumon(cpl,t)))

if __name__=='__main__':
    main()
