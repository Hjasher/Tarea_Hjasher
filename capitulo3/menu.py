from autos_arreglo import Array  # type: ignore 
from import_random import Pila    # type: ignore 

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Usar la clase Pila")
        print("2. Usar la clase Array")
        print("3. Salir")
        
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == '1':
            usar_pila()
        elif opcion == '2':
            usar_array()
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

def usar_pila():
    pila = Pila()
    while True:
        print("\n--- Clase Pila ---")
        print("1. Apilar")
        print("2. Desapilar")
        print("3. Ver tope")
        print("4. Verificar si está vacía")
        print("5. Volver al menú principal")
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == '1':
            item = input("Introduce el elemento a apilar: ")
            pila.apilar(item)
        elif opcion == '2':
            if not pila.esta_vacia():
                print("Desapilando:", pila.desapilar())
            else:
                print("La pila está vacía.")
        elif opcion == '3':
            if not pila.esta_vacia():
                print("Elemento en la parte superior:", pila.ver_tope())
            else:
                print("La pila está vacía.")
        elif opcion == '4':
            print("¿Está vacía la pila?", pila.esta_vacia())
        elif opcion == '5':
            break
        else:
            print("Opción no válida.")

def usar_array():
    array_autos = Array()
    while True:
        print("\n--- Clase Array ---")
        print("0. Mostrar Lista De Vehiculos")
        print("1. Agregar Vehiculo")
        print("2. Eliminar Vehiculo")
        print("3. Modificar Vehiculo")
        print("4. Contar Vehiculo")
        print("5. Filtrar Vehiculos")
        print("6. Volver al menú principal")
        
        opcion = input("Elige una opción (1-6): ")

        if opcion == '0':
            array_autos.mostrar_autos()
        elif opcion == '1':
            auto = input("Introduce el vehiculo a agregar: ")
            array_autos.agregar_auto(auto)
        elif opcion == '2':
            auto = input("Introduce el vehiculo a eliminar: ")
            array_autos.eliminar_auto(auto)
        elif opcion == '3':
            indice = int(input("Introduce el índice del vehiculo a modificar: "))
            nuevo_auto = input("Introduce el nuevo vehiculo: ")
            array_autos.modificar_fruta(indice, nuevo_auto)
        elif opcion == '4':
            auto = input("Introduce el auto a contar: ")
            cantidad, posiciones = array_autos.contar_autos(auto)
            print(f"La fruta '{auto}' aparece {cantidad} veces en las posiciones: {posiciones}")
        elif opcion == '5':
            letra = input("Introduce la letra para filtrar autos: ")
            autos_encontrados, posiciones = array_autos.filtrar_autos(letra)
            print(f"autos que empiezan con '{letra}': {autos_encontrados}")
            print(f"Posiciones: {posiciones}")
        elif opcion == '6':
            break
        else:
            print("Opción no válida.")

# Ejecutar el menú
menu()