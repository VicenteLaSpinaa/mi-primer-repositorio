
def solicitar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# Uso de la función
edad = solicitar_entero("Por favor, ingrese su edad: ")
print(f"Edad ingresada: {edad}")

def menu_lal(menu):
    while True:
        try:
            menu = input("Escriba 1 para terminar el programa")
            if menu == 1:
                break
        except ValueError:
            print("Opción no válida, por favor ingrese 1")
            
