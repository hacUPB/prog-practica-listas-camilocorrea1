# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    return sum(sum(fila) for fila in matriz)


print(suma_matriz([[1, 2], [3, 4]]))


# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):

    return max(max(fila) for fila in matriz)


print(maximo_matriz([[1, 2], [3, 4]]))


# Ejercicio 3: Verificar si un número es primo


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(es_primo(7))
print(es_primo(4))

# Ejercicio 4: Transponer una matriz


def transponer_matriz(matriz):
    return [list(fila) for fila in zip(*matriz)]


print(transponer_matriz([[1, 2], [3, 4]]))


# Ejercicio 5: Filtrar números pares


def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]


print(filtrar_pares([1, 2, 3, 4]))


# Ejercicio 6: Contar la cantidad de palabras en una frase


def contar_palabras(frase):
    return len(frase.split())


print(contar_palabras("Hola Mundo"))


# Ejercicio 7: Crear una tabla de multiplicar


def tabla_multiplicar(n):
    return [n * i for i in range(1, 11)]


print(tabla_multiplicar(2))


# Ejercicio 8: Contar números negativos en una lista


def contar_negativos(lista):
    return sum(1 for num in lista if num < 0)


print(contar_negativos([-1, 0, 1, 2, -3]))


# Ejercicio 9: Determinar si una lista está ordenada


def lista_ordenada(lista):
    return lista == sorted(lista)


print(lista_ordenada([1, 2, 3, 4]))
print(lista_ordenada([1, 3, 2, 4]))


# Ejercicio 10: Cifrar un texto con el cifrado César


def cifrado_cesar(texto, desplazamiento):
    """
    Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César.
    Incluir el código aquí para cifrar el texto con el cifrado César.
    """
    pass


# Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass


if __name__ == "__main__":
    main()
