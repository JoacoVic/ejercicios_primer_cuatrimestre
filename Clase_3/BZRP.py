from data import lista_bzrp

bandera_primero = False
maximo_vistas = 0
for video in lista_bzrp:
    vistas = video["views"]
    if bandera_primero == False or vistas > maximo_vistas:
        maximo_vistas = vistas
        bandera_primero = True

print(f"El maximo de vistas es: {maximo_vistas}")

for video in lista_bzrp:
    vistas = video["views"]
    titulo = video["title"]
    if vistas == maximo_vistas:
        print(f"\t{titulo}")

#Tiempo promedio
acumulador = 0
for video in lista_bzrp:
    duracion = video["length"]
    acumulador += duracion
promedio = acumulador / len(lista_bzrp)
print(f"El promedio de duracion es: {promedio:0.2f}")

#Lista d