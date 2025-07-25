#### Programita de banco donde tienes 4 opciones
### imprimir el saldo, hacer un retiro, hacer un deposito, salirte del progama

def mostrar_saldo(saldo):
    print(f'Tu saldo es {saldo} MXN')

def retiro(saldo):
    mostrar_saldo(saldo=saldo)
    monto = float(input("Cuanto deseas retirar:"))
    if monto >= saldo:
        print("Saldo insuficiente")
    else:
        saldo -= monto
    return saldo

def deposito(saldo):
    mostrar_saldo(saldo=saldo)
    monto = float(input("Cuanto deseas depositar:"))
    if monto < 0:
        print("Opcion no valida")
    else:
        saldo += monto 
    return saldo    

def main():
    is_running = True
    saldo = 0

    while is_running:
        print('##### Banking UI, opciones: #####')
        print('1. Saldo')
        print('2. Depósito')
        print('3. Retiro')
        print('4. Salir')

        selection = int(input("Elige una opción:"))

        if selection==1:
            mostrar_saldo(saldo=saldo)
        elif selection==2:
            saldo = deposito(saldo=saldo)
        elif selection==3:
            saldo = retiro(saldo=saldo)
        elif selection==4:
            print('Bye')
            is_running = False
        else:
            print('Opción no válida')

if __name__ == '__main__':
    main()
