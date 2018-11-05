def cambio():
    euros=input("Intrduce una cantidad: ")
    respuesta=raw_input("¿dólares o libras (d/l)?")
    if(respuesta=="d"):
        moneda_nueva=euros*1.15
        unidades = "dolares"
    else:
        moneda_nueva=euros*0.88
        unidades = "libras"
    print "Son "+ str(moneda_nueva) +" "+ unidades

cambio()
