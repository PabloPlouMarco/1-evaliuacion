def bucle_8():
    print "*******************************"
    print "* EL CONSTRUCTOR DE PRIAMIDES *"
    print "*******************************"
    print "Indica de que altura quieres la priamide. "
    altura=input("altura = ")
    for fil in range(1,altura):
        for col in range(1,fil+1):
            print "*",
        print " "
bucle_8()
