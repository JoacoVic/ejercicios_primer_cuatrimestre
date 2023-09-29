# Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar
# en la bolsa de valores:
# A) Para ello se cargarán los siguientes datos hasta que el usuario lo decida:
# * Nombre
# * Monto en pesos de la operación (no menor a $10000)
# * Cantidad de instrumentos
# * Tipo (CEDEAR, BONOS, MEP)
# B) Luego del ingreso mostrar en pantalla todos los datos.
# C) Realizar los siguientes informes:
# 1. Tipo de instrumento que más se operó.
# 2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron
# más de $50000.
# 3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP,
# que menos dinero invirtió. Puede ser más de uno.
# 4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el
# monto promedio
# 5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto
# no supere los $50000.

lista_nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta"]

lista_monto = [99000, 60000, 45000, 75000, 55000, 25000, 104000, 67000, 19000, 49000]
       
lista_cantidad = [180, 12, 150, 157, 192, 9, 2, 4, 65, 27]

lista_tipo = ["CEDEAR", "BONOS", "MEP", "BONOS", "BONOS", "MEP", "CEDEAR", "MEP", "CEDEAR", "BONOS"]

# A) Para ello se cargarán los siguientes datos hasta que el usuario lo decida:
# * Nombre
# * Monto en pesos de la operación (no menor a $10000)
# * Cantidad de instrumentos
# * Tipo (CEDEAR, BONOS, MEP)

while True:
    nombre = input("Ingrese su nombre: ")
    while not nombre.isalpha():
        nombre = input("Ingrese su nombre: ")
    lista_nombres.append(nombre)

    monto = input("Ingrese el monto de la operación: $")
    while not monto.isdigit():
        monto = input("Ingrese el monto de la operación: $")
    monto = int(monto)
    lista_monto.append(monto)

    cantidad = input("Ingrese la cantidad de instrumentos: ")
    while not cantidad.isdigit():
        cantidad = input("Ingrese la cantidad de instrumentos: ")
    cantidad = int(cantidad)
    lista_cantidad.append(cantidad)

    tipo = input("Ingrese el tipo (CEDEAR, BONOS o MEP): ")
    while tipo.upper() != "CEDEAR" and tipo.upper() != "BONOS" and tipo.upper() != "MEP":
        tipo = input("Ingrese el tipo (CEDEAR, BONOS o MEP): ")
    lista_tipo.append(tipo.upper())

    continuar = input("¿Desea continuar? (s/n): ")
    while continuar.lower() != "s" and continuar.lower() != "n":
        continuar = input("¿Desea continuar? (s/n): ")
    if continuar == "s":
        continue
    else:
        break

# # B) Luego del ingreso mostrar en pantalla todos los datos.

for i in range(len(lista_nombres)):
    nombre = lista_nombres[i]
    monto = lista_monto[i]
    cantidad = lista_cantidad[i]
    tipo = lista_tipo[i]
    print(f"nombre: {nombre}\tmonto: {monto}\tcantidad: {cantidad}\ttipo: {tipo}")


# C) 
# 1. Tipo de instrumento que más se operó.

contador_cedears = 0
contador_bonos = 0
contador_mep = 0

for tipo in lista_tipo:
    if tipo == "CEDEAR":
        contador_cedears += 1
    elif tipo == "BONOS":
        contador_bonos += 1
    elif tipo == "MEP":
        contador_mep += 1
    else:
        print("1. La lista está vacía\n")

lista_contadores = [contador_bonos, contador_mep, contador_cedears]
lista_variables_de_tipo = ["BONO", "MEP", "CEDEAR"]

bandera_contadores = False
mayor_cantidad = 0
for i in range(len(lista_contadores)):
    contador = lista_contadores[i]
    variable_de_tipo = lista_variables_de_tipo[i]
    if bandera_contadores == False or contador > mayor_cantidad:
        bandera_contadores = True
        mayor_cantidad = contador
        mayor_tipo = variable_de_tipo


print(f"1. El tipo de instrumento que más se operó es: {mayor_tipo}\n")

# 2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000.

contador_usuarios = 0
bandera = False
if bandera == False:
    for i in range(len(lista_tipo)):
        tipo = lista_tipo[i]
        cantidad = lista_cantidad[i]
        monto = lista_monto[i]

        if tipo == "BONOS":
            if cantidad > 150 and cantidad < 200:
                if monto > 50000:
                    contador_usuarios += 1
    if contador_usuarios == 0:
        print("2. No hay usuarios que cumplan con los requisitos\n")
    else:
        print(f"2. La cantidad de usuarios que cumplen con los requisitos son: {contador_usuarios}\n")

else:
    print("2. La lista está vacía\n")

#3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió. Puede ser más de uno.

bandera_monto = False
menor_monto = 0
print("3. Usuarios que compraron BONOS o MEP que menos dinero invirtieron:")

for i in range(len(lista_tipo)):
        tipo = lista_tipo[i]
        monto = lista_monto[i]

        if tipo == "BONOS" or tipo == "MEP":
            if bandera_monto == False or monto < menor_monto:
                menor_monto = monto
                bandera_monto = True
            if bandera_monto == False:
                print("No hay usuarios que hayan invertido en BONOS o en MEP\n")
for i in range(len(lista_tipo)):
    tipo = lista_tipo[i]
    cantidad = lista_cantidad[i]
    monto = lista_monto[i]
    nombre = lista_nombres[i]

    if tipo == "BONOS" or tipo == "MEP":
        if monto == menor_monto:
            print(f"nombre: {nombre}\tcantidad: {cantidad}\n")

# 4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el monto promedio
print("4. Usuarios que invirtieron en CEDEAR y su inversión supera el monto promedio:")
acumulador_montos = 0
for monto in lista_monto:
    acumulador_montos += monto

promedio_montos = acumulador_montos / len(lista_monto)
bandera_promedios = False

for i in range(len(lista_tipo)):
    tipo = lista_tipo[i]
    monto = lista_monto[i]
    nombre = lista_nombres[i]
    if tipo == "CEDEAR":
        if monto > promedio_montos:
            bandera_promedios = True
            print(f"{nombre}\n")
    if bandera_promedios == False:
        print("No hay usuarios que hayan invertido en CEDEAR y superen el monto promedio\n")
# 5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto no supere los $50000.

contador_mep = 0
for i in range(len(lista_tipo)):
    tipo = lista_tipo[i]
    monto = lista_monto[i]
    if tipo != "MEP":
        if monto < 50000:
            contador_mep += 1
if contador_mep == 0:
    print("5. No hay usuarios que no hayan invertido en MEP y su monto no supere los $50000")
porcentaje_mep = (contador_mep * 100) / len(lista_tipo)

print(f"5. Porcentaje de usuarios que no invirtieron en MEP y el monto no supera los $50000: {porcentaje_mep:0.2f}%")