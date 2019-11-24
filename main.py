import sys
from Operaciones import Operaciones

def calcular(operacion,a,b):
    if(operacion == "suma"):
        resultado=Operaciones.suma(a,b)
    if(operacion == "resta"):
        resultrado=Operaciones.resta(a,b)
    if(operacion == "multiplicar"):
        resultado=Operaciones.multiplicar(a,b)
    if(operacion == "dividir"):
        resultado= Operaciones.dividir(a,b)
    print("el resultado es: " + str(resultado))

operacion= sys.argv[1]
a=sys.argv[2]
b=sys.argv[3]

calcular(operacion,int(a),int(b))