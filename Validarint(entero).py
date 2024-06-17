
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
