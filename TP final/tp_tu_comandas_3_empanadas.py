 #APP PARA SOLICITAR DESAYUNO CON DELIVERY-TAKE AWAY O CONSUMIR EN EL LUGAR
import json #archivo donde vamos a guardar los datos de clientes

clientes = []   #cargar clientes existentes desde JSON

file = open("registro-clientesPedidos.json","r") # abro archivo / leer los datos 
clientes = json.load(file) #load carga lo que hay en el archivo 'file' retorna una lista que la asigno a clientes
file.close() #me aseguro de cerrar el archivo

#funciones de decoración para hacer el programa mas espacioso, que ayude a la lectura, 
        #y poder separar secciones
def deco1():
    print ("*"*60)
def deco_():
    print ("~-"*20)
    
    
#funciones de validación de entrada de datos, c/u con sus características
def validacion_celu():  #que valide que sean 10 dígitos (ni letras ni mas ni menos cantidad) -->
                        #y sino le indique que es incorrecto y lo vuelva a ingresar
    celu = input("Ingresá tu celu, con cód de área, sin 0 ni 15: ")
    while True:
        if celu.isdigit() and len(celu) == 10:
            break
        else:
            celu = input("por favor ingresá un dato válido. Deben ser 10 números: ")
    return celu
def validacion_dni(): #que valide que sean 7 u 8 dígitos (ni letras ni mas ni menos cantidad) -->
                      #y sino le indique es incorrecto y que lo vuelva a intentar
    dni = input("DNI: ")
    while True:
        if dni.isdigit() and len(dni) == 8 or len(dni) == 7:
            break
        else:
            dni = input("----> Ingresá los 7/8 dígitos de tu DNI, sin puntos: ")
    


# bienvenida e ingreso de datos como cliente
deco1()

print("***** Hola! Te damos la bienvenida a TuComandas *****\n ")

deco1()

print("Por favor, completá todos los campos para AGENDARTE COMO CLIENTE ")
cantidad_de_lineas=2
for _ in range (cantidad_de_lineas):
    print()


nombre = input("Nombre: ")
dni = validacion_dni() #se valida DNI en el mismo momento q se ingresa
celular = validacion_celu() #idem DNI pero con sus características
direccion = input("Dirección: ") #se podrá reutilizar si elige delivery

cliente = { #creamos un diccionario de clientes, con los datos ingresados
          "nombre": nombre,
          "dni" : dni,
          "direccion": direccion,
          "celular": celular,
          }

deco_()
deco_()
print(f""" ** CLIENTE AGENDADO CORRECTAMENTE ** 
      - Nombre: {cliente['nombre']}
      - DNI: {cliente['dni']}
      - Dirección: {cliente['direccion']}
      - Celular: {cliente['celular']}""")
deco_()
deco_()
print("Gracias por registrate, "+ nombre + ". \n        A continuación tu pedido se identificará con el nombre que nos indicaste.")
deco1()



# SE OFRECE EL MENÚ Y VA ARMANDO SU PEDIDO


opciones = [] # Guarda los menúes seleccionados
def menu(): #se despliegan las opciones. A futuro se crearán variables de (x ej) menu1 y precio1 -->
            #para que sea mas accesible la modificación por el dueño del comercio
    print ("***ESTE ES NUESTRO MENU PARA QUE PUEDAS ELEGIR LO QUE DESEAS COMER*** ")# Muestra el menu al usuario
    cantidad_de_lineas = 2
    for _ in range (cantidad_de_lineas):
        print()
    print (" menu 1 -> Cafe con leche y medialunas - $700\n",
           "menu 2 -> Cafe con torta - $1050\n",
           "menu 3 -> Te con scones - $700\n",
           "menu 4 -> Licuado con tostado - $1500\n",
           "     0 -> Salir del menu")
    return menu
def seleccionar_opcion(): # Selecciona menú y ofrece agregar algo + 
    deco1()
    import sys # sale directamente del programa si el usuario sale del menu.
    while True:
        opcion = input("Nro del menú seleccionado: ")
        while opcion not in ['1', '2', '3', '4', '0' ]:
            opcion = input("Opción inválida, volvé a intentarlo! ¿Qué menú querés?: ").lower() # si la opcion es invalida vuelve a preguntar
        if opcion == "0":
           print ("****Saliste del pedido****")
           sys.exit()
        opciones.append (opcion)
        modificar= input ("Añadimos la opcion seleccionada! Te gustaría agregar algo más? (s/n): ").lower()
        while modificar not in ['s', 'n']: #AGREGADO PARA Q NO SEA INFINITO
            modificar= input("Opción inválida, ¿querés agregar algo? s/n : ").lower()
        if modificar=='s':
            seleccionar_opcion()
        else:
         modificar.lower() == 'n' 
        break
    deco_()
    return opcion, opciones
def calcular_costo(opciones): # Se calcula el costo según los pedidos acumulados en "opciones" 
    costo_total = 0
    menu_seleccionado = []
    for opcion in opciones:
        if opcion == "1":
            costo_total += 700
            menu_seleccionado.append("- Menu 1 -> Cafe con leche y medialunas - $700")
        elif opcion == "2":
            costo_total += 1050
            menu_seleccionado.append("- Menu 2 -> Cafe con torta - $1050")
        elif opcion == "3":
            costo_total += 700
            menu_seleccionado.append("- Menu 3 -> Te con scones - $700")
        elif opcion == "4":
            costo_total += 1500
            menu_seleccionado.append("- Menu 4 -> Licuado con tostado - $1500")
    return costo_total, menu_seleccionado  
def mostrar_resultados(costo_total, menu_seleccionado): # muestra el pedido hecho por el cliente
    deco_()
    print("Tu pedido es: ")
    for menu in menu_seleccionado:
        print(menu)
    print(f"Total a pagar: $ {costo_total}") 
    deco_() 



menu() # se ofrece el menú disponible
seleccionar_opcion() # Debe seleccionar una opción del menú
costo_total , menu_seleccionado = calcular_costo(opciones)# llamamos a la funcion y asignamos variables a sus retornos
mostrar_resultados(costo_total, menu_seleccionado)  # muestra al cliente su pedidio y el total a pagar

cliente = { 
          "nombre": nombre,
          "dni" : dni,
          "direccion": direccion,
          "celular": celular,
          "pedido": menu_seleccionado,
          "total": costo_total
          }

clientes.append(cliente) #agregando elemento al listado

file = open("registro-clientesPedidos.json","w")
json.dump(clientes,file, indent=2) #listado que escribimos en el arhivo (file) 
file.close() #se genera el archivo json una vez que se registra el primer cliente




# seleccionar tipo de pedido


import sys #lo importamos para poder ulizar la función de salir del programa ante una cancelación de pedido
def seleccionar_entrega(): # Debe seleccionar entre delivery, consumir en el local o retiro
    print("""Seleccioná el TIPO DE ENTREGA:
    1- Comer en el lugar
    2- Delivery
    3- Retiro 
    ------
    0- Cancelar pedido 
    
  ******** Nota: el delivery es sin cargo y con todos los medios de pagos habilitados ********""""")
    
    

    tipo_entrega = input("Tipo de entrega elegido = ")
    while tipo_entrega not in ['1', '2', '3', '0' ]:
        tipo_entrega = input("Opción inválida. Elegí tu tipo de entrega: ") # si la opcion es invalida vuelve a preguntar
    if tipo_entrega == "0":
        cantidad_de_lineas = 2
        for _ in range (cantidad_de_lineas):
         print()
         deco1()
        print ("***Pedido cancelado. Gracias de todas formas! Te esperamos pronto.***") 
        deco1() 
        sys.exit()   
    if tipo_entrega == "1":
        deco1()
        mesa = input("Decime tu número de mesa: ")
        deco1()
        print("---> En breve te lo acercamos a la mesa " + mesa )
        deco1()
    elif tipo_entrega == "2":
        deco1()
        print("¿Te lo enviamos al domicilio registrado? (" , cliente["direccion"], ") ",end="")
        envio= input("(s/n): ").lower()
        while envio not in ["s", "n"]:
            print ("Por favor elegí 's' ó 'n')")
            break
        if envio == "n":
            envio = input ("indicanos dónde lo enviamos esta vez (no modificará tus datos): ")
            deco1()
            print("Gracias!! agendado!!")
            deco1()
        print("---> En 20 minutos te lo enviamos a: ", end=  "")
        if envio == "s":
            print (cliente["direccion"])
        else:
            print (envio)
    elif tipo_entrega =="3":
        deco1()
        
        print("---> En 25 minutos ya podés pasar por nuestro local -San Martin 922- para retirar tu pedido")
        
        deco1()
    deco_()
    return tipo_entrega
def pago(tipo_entrega): # Se ofrece y debe seleccionar forma de pago, con diferentes bonificaciones
    #si elige delivery, se reutiliza la dirección brindada en sus datos
    #cada tipo de opción, tendrá su correspondiente tiempo de entrega
    if tipo_entrega == 0: #si cancela el pedido, finaliza la sección
        pass
    else:
        print(               "********** OPCIONES DE PAGO **********")
        
        cantidad_de_lineas=2
        for _ in range (cantidad_de_lineas):
            print()
        
        
        print("***** Elegi el medio de pago preferido *****")
        
        
        print('''
        1 - Efectivo:  10% de descuento  
        2 - Aplicacion o QR: 5% de descuento
        3 - Debito : precio de lista
        4 - Credito: 20% de interes en hasta 3 cuotas
        ''')

        opcion = input("Seleccione el número de la opción deseada: ")
        while True:
            if opcion == "1": #tratar todo como string
                print(f"Elegiste Efectivo el total es:$ {costo_total * 0.9:.2f}") #se ingresa resultado con 2 decimales
                break
            elif opcion == "2":
                print(f"Elegiste Aplicacion o QR el total es: $ {costo_total * 0.95:.2f}")
                break
            elif opcion == "3":
                print(f"Elegiste Debito, el total es : $ {costo_total}")
                break
            elif opcion == "4":
                print(f"Elegiste Tarjeta de credito: 3 cuotas de $ {(costo_total * 1.20)/ 3:.2f}")
                break
            else:
                opcion = input("Opción no válida. ¿qué tipo de pago elegís?: ")

    deco1()
    print(         "***** Ahora podes pagar tu pedido en caja o a nuestro delivery*****")
    deco1()
tipo_entrega = seleccionar_entrega()
pago(tipo_entrega)
cantidad_de_lineas = 3
for _ in range (cantidad_de_lineas): # sirve para dejar renglones y que sea mas claro el mensaje final
    print()
    
deco1()  
print ("~~Gracias por elegirnos! Esperamos difrutes tu comida~~")
deco1()

cantidad_de_lineas = 3
for _ in range (cantidad_de_lineas):
    print()
