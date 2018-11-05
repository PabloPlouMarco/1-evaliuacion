def bucle_9():
    print "*******************************"
    print "* EL CONSTRUCTOR DE PRIAMIDES *"
    print "*******************************"
    print "Indica de que altura quieres la priamide. "
    altura=input("altura = ")
    for fil in range(altura,1):
        for col in range(fil-1,1):
            print "*",
        print " "
bucle_9()
