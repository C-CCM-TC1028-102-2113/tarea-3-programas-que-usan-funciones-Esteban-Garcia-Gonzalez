
def arearec(b, p):
    area=b*p
    return area

def volumen(a, h):
    vol= a*h
    return vol

def main():
  #escribe tu código abajo de esta línea
  b=float(input('Dame la base: '))
  h=float(input('Dame la altura: '))
  p=float(input('Dame la profundidad: '))
  a=arearec(b,p)
  print('El volumen del prisma es: '+ str(volumen(a, h)))

if __name__ == '__main__':
    main()
