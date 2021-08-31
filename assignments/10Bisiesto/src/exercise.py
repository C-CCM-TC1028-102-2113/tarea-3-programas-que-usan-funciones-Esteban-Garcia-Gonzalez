def es_bisiesto(a,b):
    if (a%4==0 or a%400==0):
        b=True
        return b
    else:
        b=False
        return b
def main():
    a=int(input())
    b=0
    print(es_bisiesto(a,b))

if __name__=='__main__':
    main()
