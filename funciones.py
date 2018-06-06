def cont_tubos(lista,margen_ancho,margen_cierra):
    #margenes de corte

    # Contador de tubos
    cant_tubos = 0
    tubo = 600
    j = 0
    lista_sobras = []
    for ancho in lista:
        ancho -= -(margen_ancho+margen_cierra)
        if (ancho <= tubo):
            tubo -= ancho
            if(tubo < 0):
                tubo += ancho
                lista_sobras.append(tubo)
            if (j == 0):
                cant_tubos += 1
                j += 1
        else:
            encontro = False
            cant_tubos += 1
            for t in lista_sobras:
                if (t > ancho):
                    tubo = 600
                    print("El tubo de ", ancho, "cm se encuentra en las sobras")
                    t = 0
                    encontro = True
            if (encontro == True):
                pass
            else:
                tubo = 600 - ancho
    print("La cantidad de tubos es :", cant_tubos)



def contador_de_tela(lista_de_anchos,lista_de_altos,margen_ancho,margen_alto,margen_de_tela):

    lista_de_anchos_de_telas = []
    lista_de_altos_de_telas = []

    #cantidad de tela a comprar
    contador_de_tela = 0

    # descontar margenes
    for ancho in lista_de_anchos:
        temp = ancho
        temp -= margen_ancho - margen_de_tela
        lista_de_anchos_de_telas.append(temp)
    for alto in lista_de_altos:
        temp = alto
        temp += margen_alto
        lista_de_altos_de_telas.append(temp)

    for ancho,alto in zip(lista_de_anchos_de_telas,lista_de_altos_de_telas):
        if(True):
            pass
        else:
            pass




    return contador_de_tela





