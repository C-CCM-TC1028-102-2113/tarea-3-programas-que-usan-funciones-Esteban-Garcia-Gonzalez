
def arearec(b, h):
    area=b*h
    return area

def volumen(a, h):
    vol= a*h
    return vol

def main():
  #escribe tu código abajo de esta línea
  b=float(input('Dame la base: '))
  h=float(input('Dame la altura: '))
  p=float(input('Dame la profundidad: '))
  a=arearec(b,h)
  print('El volumen del prisma es: '+ str(volumen(a, h)))

if __name__ == '__main__':
    main()
