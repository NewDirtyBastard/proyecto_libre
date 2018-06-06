from funciones import *
#primera vercion A

#margenes de decuento
margen_ancho = 3
margen_cierra = 1
margen_de_tela = 0,3
margen_alto = 20

#Entrada de datos
#validacion de cortinas que se pueden hacer
list_anchos = list()
list_altos = list()
cont_cort = 1
max_altoxancho = 0
cortinas_normales = 0

print("-------SW DE COTINAS--------")

while (True):

    print("----------------------------")
    print("Medidas de cortina ", cont_cort)



    while True:
        #hacer mientras
        ancho = float(input(">Ingrese ancho: "))
        #--------------
        if (ancho < 0):
            print("El ancho ingresado no es valido, ingres un valor superior a (0)")
            break
    if (ancho == 0):
        break

    while True:
        #hacer mientras
        alto = float(input(">Ingrese alto: "))
        #--------------
        if (alto < 0 ):
            print("El alto ingresado no es valido, ingres un valor superior a (0)")
            break

    cont_cort += 1
    if (ancho >= 60 and ancho < 260 and alto >= 60 and alto <= 360):
        list_anchos.append(ancho)
        list_altos.append(alto)
    elif (ancho < 280 and alto < 320):
        list_anchos.append(ancho)
        list_altos.append(alto)
    elif (ancho <= 300 and alto <= 280):
        list_anchos.append(ancho)
        list_altos.append(alto)
    else:
        print("No trabajamos con cortinas especiales.")
        print("Lo sentimos.")
        cont_cort -= 1



#Esta funcion indica la cantidad de tubos que se necesitan para un proyecto
cont_tubos(list_anchos,margen_ancho,margen_cierra)

#Esta funcion indica la cantidad de metros de tela que se necesitan para un proyecto
contador_de_tela(list_anchos,list_altos,margen_ancho,margen_alto,margen_de_tela)

