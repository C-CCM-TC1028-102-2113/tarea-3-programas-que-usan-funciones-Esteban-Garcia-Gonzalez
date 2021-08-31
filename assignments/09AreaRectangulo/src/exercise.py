def arearec(b,h):
    area=b*h
    return area
def main():
    b= float(input('Dame la base: '))
    h= float(input('Dame la altura: '))
    print('El área del rectángulo es: '+str(arearec(b,h)))

if __name__=='__main__':
    main()
