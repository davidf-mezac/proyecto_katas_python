# =====================================================================
# 1. Escribe una función que reciba una cadena de texto como parámetro
# y devuelva un diccionario con las frecuencias de cada letra en la cadena.
# Los espacios no deben ser considerados.
# =====================================================================

def contar_letras(texto):
    # Creamos un diccionario vacío. Los diccionarios son ideales aquí porque
    # nos permiten guardar una "clave" (la letra) y un "valor" (la cantidad de veces que aparece).
    frecuencias = {}
    
    # El método replace() busca el primer argumento (un espacio " ")
    # y lo cambia por el segundo (nada ""). Así eliminamos los espacios.
    texto_sin_espacios = texto.replace(" ", "")
    
    # Recorremos cada letra del texto ya sin espacios, una por una.
    for letra in texto_sin_espacios:
        # Comprobamos si la letra ya existe como clave en nuestro diccionario.
        if letra in frecuencias:
            # Si ya existe, tomamos su valor actual y le sumamos 1.
            frecuencias[letra] += 1
        else:
            # Si es la primera vez que vemos esta letra, la creamos en el diccionario con un valor de 1.
            frecuencias[letra] = 1
            
    # Devolvemos el diccionario con el conteo final.
    return frecuencias

# Prueba Kata 1:
print("--- Kata 1 ---")
print(contar_letras("hola mundo"))


# =====================================================================
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor.
# Usa la función map()
# =====================================================================

def doblar_numeros(lista_numeros):
    # map() recibe dos cosas: una función y una lista.
    # Aplica esa función a cada uno de los elementos de la lista.
    # Usamos 'lambda x: x * 2', que es una función anónima y rápida que dice:
    # "toma un valor 'x' y devuelve 'x * 2'".
    # Como map() devuelve un objeto de tipo map, usamos list() para convertirlo de nuevo a una lista normal.
    resultado = list(map(lambda x: x * 2, lista_numeros))
    
    return resultado

# Prueba Kata 2:
print("\n--- Kata 2 ---")
numeros_ejemplo = [1, 2, 3, 4, 5]
print(doblar_numeros(numeros_ejemplo))


# =====================================================================
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo
# como parámetros. La función debe devolver una lista con todas las palabras
# de la lista original que contengan la palabra objetivo.
# =====================================================================

def buscar_palabras(lista_palabras, palabra_objetivo):
    # Preparamos una lista vacía donde iremos guardando las palabras que cumplan la condición.
    palabras_encontradas = []
    
    # Iteramos sobre cada palabra dentro de la lista original.
    for palabra in lista_palabras:
        # El operador 'in' verifica si una cadena de texto (palabra_objetivo)
        # se encuentra dentro de otra cadena de texto más grande (palabra).
        if palabra_objetivo in palabra:
            # Si la condición se cumple, usamos el método append() para agregarla al final de nuestra nueva lista.
            palabras_encontradas.append(palabra)
            
    return palabras_encontradas

# Prueba Kata 3:
print("\n--- Kata 3 ---")
lista_texto = ["sol", "soldado", "girasol", "luna", "playa"]
print(buscar_palabras(lista_texto, "sol"))


# =====================================================================
# 4. Genera una función que calcule la diferencia entre los valores de dos listas.
# Usa la función map()
# =====================================================================

def calcular_diferencia_listas(lista1, lista2):
    # map() también puede recibir múltiples listas al mismo tiempo.
    # En este caso, la función lambda necesita dos variables (x, y).
    # 'x' tomará el valor de la lista1, e 'y' tomará el valor correspondiente en la misma posición de la lista2.
    # Luego, la lambda resta 'x - y'. Finalmente, list() convierte el resultado en una lista.
    diferencias = list(map(lambda x, y: x - y, lista1, lista2))
    
    return diferencias

# Prueba Kata 4:
print("\n--- Kata 4 ---")
l1 = [10, 20, 30]
l2 = [2, 5, 10]
print(calcular_diferencia_listas(l1, l2))


# =====================================================================
# 5. Escribe una función que tome una lista de números como parámetro y un valor
# opcional nota_aprobado, que por defecto es 5. La función debe calcular la media
# de los números en la lista y determinar si la media es mayor o igual que nota aprobado.
# Si es asi, el estado será "aprobado", de lo contrario, será "suspenso".
# La función debe devolver una tupla que contenga la media y el estado.
# =====================================================================

def calcular_media_y_estado(notas, nota_aprobado=5):
    # El parámetro 'nota_aprobado=5' significa que si al llamar a la función no le damos este valor, usará 5 por defecto.
    
    # sum() suma todos los números de la lista, y len() nos dice cuántos números hay.
    # Dividiendo obtenemos el promedio (media).
    media = sum(notas) / len(notas)
    
    # Usamos una estructura condicional (if/else) para determinar el estado de la nota.
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
        
    # En Python, si devolvemos varias variables separadas por comas,
    # automáticamente se agrupan y se devuelven como una Tupla (una estructura de datos que no se puede modificar).
    return media, estado

# Prueba Kata 5:
print("\n--- Kata 5 ---")
notas_alumno = [6, 7, 5, 8]
print(calcular_media_y_estado(notas_alumno))


# =====================================================================
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
# =====================================================================

def factorial_recursivo(numero):
    # La recursividad significa que una función se llama a sí misma por dentro.
    # Siempre necesita un "caso base" para saber cuándo detenerse y no crear un bucle infinito.
    # El factorial de 0 y de 1 siempre es 1, así que ese será nuestro freno.
    if numero == 0 or numero == 1:
        return 1
    else:
        # Si el número es mayor a 1, multiplicamos el número actual por el resultado
        # de volver a llamar a la misma función, pero restándole 1 al número.
        # Ejemplo con 3: devuelve 3 * factorial_recursivo(2) -> devuelve 2 * factorial_recursivo(1) -> devuelve 1.
        return numero * factorial_recursivo(numero - 1)

# Prueba Kata 6:
print("\n--- Kata 6 ---")
print(factorial_recursivo(5)) # 5! = 5 * 4 * 3 * 2 * 1 = 120


# =====================================================================
# 7. Genera una función que convierta una lista de tuplas a una lista de strings.
# Usa la función map()
# =====================================================================

def tuplas_a_strings(lista_tuplas):
    # La función str() en Python convierte cualquier cosa a texto (string).
    # map() toma esa función str() y se la aplica a cada tupla de nuestra lista.
    # Por ejemplo, la tupla (1, 2) se convertirá en el texto "(1, 2)".
    # Finalmente, envolvemos todo en list() para que el resultado vuelva a ser una lista.
    resultado = list(map(str, lista_tuplas))
    
    return resultado

# Prueba Kata 7:
print("\n--- Kata 7 ---")
tuplas_ejemplo = [(1, "A"), (2, "B"), (3, "C")]
print(tuplas_a_strings(tuplas_ejemplo))


# =====================================================================
# 8. Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja
# esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.
# =====================================================================

def dividir_numeros():
    # El bloque 'try' (intentar) le dice a Python: "Intenta ejecutar este código,
    # pero si algo sale mal, no te bloquees, yo te diré cómo manejarlo abajo".
    try:
        # input() detiene el programa y espera a que el usuario escriba algo.
        # float() intenta convertir ese texto ingresado en un número con decimales.
        num1 = float(input("Introduce el primer número para dividir: "))
        num2 = float(input("Introduce el segundo número para dividir: "))
        
        # Intentamos hacer la división matemática.
        resultado = num1 / num2
        
    # Si el usuario escribe texto (como "hola") en lugar de un número, float() fallará.
    # Esto genera un error llamado 'ValueError', y lo atrapamos aquí:
    except ValueError:
        print("❌ Error: Por favor, debes ingresar únicamente valores numéricos.")
        
    # Si el usuario pone un 0 en el segundo número, la matemática falla.
    # Esto genera un error llamado 'ZeroDivisionError', y lo atrapamos aquí:
    except ZeroDivisionError:
        print("❌ Error: Matemáticamente no es posible dividir un número entre cero.")
        
    # El bloque 'else' (dentro de un try/except) SOLO se ejecuta si NO hubo ningún error.
    else:
        print(f"¡División exitosa! El resultado es: {resultado}")

# Prueba Kata 8:
print("\n--- Kata 8 ---")
dividir_numeros()


# =====================================================================
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro
# y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón",
# "Cocodrilo", "Oso"]. Usa la función filter()
# =====================================================================

def filtrar_mascotas(lista_mascotas):
    # Guardamos en una lista las mascotas que no están permitidas.
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    
    # filter() hace un "filtro". Recibe una función que da Verdadero o Falso, y una lista.
    # Solo deja pasar los elementos que den Verdadero.
    # 'lambda mascota: mascota not in prohibidas' significa:
    # "Toma un nombre de mascota, y verifica si NO ESTÁ en la lista de prohibidas".
    mascotas_permitidas = list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))
    
    return mascotas_permitidas

# Prueba Kata 9:
print("\n--- Kata 9 ---")
mis_mascotas = ["Perro", "Tigre", "Gato", "Mapache", "Loro"]
print(filtrar_mascotas(mis_mascotas))


# =====================================================================
# 10. Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada y maneja el error
# adecuadamente.
# =====================================================================

def calcular_promedio(lista_numeros):
    # Volvemos a usar try/except, pero esta vez nosotros "crearemos" el error.
    try:
        # Primero, comprobamos si la lista está vacía usando len() (que cuenta los elementos).
        if len(lista_numeros) == 0:
            # 'raise' sirve para "lanzar" o provocar intencionalmente un error.
            # 'Exception' es el tipo de error más general, y le pasamos nuestro propio texto.
            raise Exception("La lista está vacía. No se puede calcular el promedio sin números.")
        
        # Si la lista NO está vacía, el código ignora el 'if' y continúa aquí.
        promedio = sum(lista_numeros) / len(lista_numeros)
        return promedio
    
    # Aquí 'atrapamos' el error que lanzamos arriba.
    # 'as e' nos permite guardar nuestro mensaje de error en una variable llamada 'e'.
    except Exception as e:
        # Devolvemos el mensaje personalizado para que el usuario lo vea.
        return f"Error detectado: {e}"

# Prueba Kata 10:
print("\n--- Kata 10 ---")
lista_llena = [10, 8, 9]
lista_vacia = []
print("Con números:", calcular_promedio(lista_llena))
print("Sin números:", calcular_promedio(lista_vacia))


# =====================================================================
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el
# usuario ingresa un valor no numérico o un valor fuera del rango esperado
# (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
# =====================================================================

def pedir_edad():
    try:
        # input() pide texto. int() intenta convertir ese texto en un número entero (sin decimales).
        # Si el usuario escribe letras, int() fallará automáticamente generando un ValueError.
        edad = int(input("Por favor, introduce tu edad: "))
        
        # Evaluamos si la edad tiene sentido lógico (no puedes tener -5 años o 500 años).
        if edad < 0 or edad > 120:
            # Si no tiene sentido, lanzamos nosotros mismos un ValueError con un mensaje específico.
            raise ValueError("La edad debe estar entre 0 y 120 años.")
        
    # Atrapamos el ValueError. Caeremos aquí por dos razones:
    # 1. El usuario escribió letras (falló int()).
    # 2. El usuario escribió un número raro (se activó nuestro raise ValueError).
    except ValueError as error:
        # Si falló int(), imprimirá un error automático en inglés.
        # Si falló nuestro 'if', imprimirá nuestro mensaje en español.
        print(f"¡Dato inválido! Detalle: {error}")
    
    else:
        # Si pasamos el int() y pasamos el if sin problemas, llegamos al éxito.
        print(f"Edad registrada correctamente: {edad} años.")

# Prueba Kata 11:
print("\n--- Kata 11 ---")
pedir_edad()


# =====================================================================
# 12. Genera una función que al recibir una frase devuelva una lista con la
# longitud de cada palabra. Usa la función map()
# =====================================================================

def longitud_palabras(frase):
    # El método split() corta un texto largo y lo convierte en una lista de palabras.
    # Por defecto, usa los espacios en blanco para saber dónde hacer los cortes.
    # Ejemplo: "Buenos días" debería transformarse en["Buenos", "días"].
    palabras = frase.split()
    
    # map() aplica una función a cada elemento de una lista.
    # Aquí le pasamos la función integrada 'len' (que cuenta caracteres) para que la aplique a cada palabra.
    # Finalmente, envolvemos todo en list() para tener una lista normal.
    longitudes = list(map(len, palabras))
    
    return longitudes

# Prueba Kata 12:
print("\n--- Kata 12 ---")
mi_frase = "Está interesante el curso de python"
print(f"Frase: '{mi_frase}'")
print(f"Longitudes: {longitud_palabras(mi_frase)}")


# =====================================================================
# 13. Genera una función la cual, para un conjunto de caracteres, devuelva
# una lista de tuplas con cada letra en mayúsculas y minúsculas.
# Las letras no pueden estar repetidas. Usa la función map()
# =====================================================================

def mayusculas_minusculas(caracteres):
    # En Python, un 'set' (conjunto) es una estructura de datos que automáticamente
    # elimina cualquier elemento duplicado.
    # Si le pasamos "aab", el set lo convierte en {"a", "b"}.
    caracteres_unicos = set(caracteres)
    
    # map() toma cada letra única y la pasa por nuestra función lambda.
    # La lambda crea y devuelve una tupla con dos versiones de la letra:
    # (letra.upper() para mayúscula, letra.lower() para minúscula).
    resultado = list(map(lambda letra: (letra.upper(), letra.lower()), caracteres_unicos))
    
    return resultado

# Prueba Kata 13:
print("\n--- Kata 13 ---")
# Le pasamos caracteres con letras repetidas (las 'a' y las 'r')
letras_prueba = "carrera"
print(mayusculas_minusculas(letras_prueba))


# =====================================================================
# 14. Crea una función que retorne las palabras de una lista de palabras
# que comience con una letra en especifico. Usa la función filter()
# =====================================================================

def filtrar_por_letra(lista_palabras, letra_inicial):
    # El método startswith() nos dice si un texto empieza con cierto carácter (True/False).
    # Usamos lower() en ambos lados para que no importe si buscamos "A" o "a".
    # filter() usará ese True/False para decidir si conserva la palabra en la lista o no.
    palabras_filtradas = list(filter(
        lambda palabra: palabra.lower().startswith(letra_inicial.lower()),
        lista_palabras
    ))
    
    return palabras_filtradas

# Prueba Kata 14:
print("\n--- Kata 14 ---")
palabras_ejemplo = ["Árbol", "casa", "Avión", "perro", "agua"]
print(filtrar_por_letra(palabras_ejemplo, "a"))


# =====================================================================
# 15. Crea una función Lambda que sume 3 a cada número de una lista dada.
# =====================================================================

# El enunciado pide específicamente crear una función Lambda.
# Podemos crear la función completa en una sola línea y guardarla en una variable.
# Esta lambda recibe una 'lista' y usa map() por dentro para sumarle 3 a cada elemento 'x'.
sumar_tres_a_lista = lambda lista: list(map(lambda x: x + 3, lista))

# Prueba Kata 15:
print("\n--- Kata 15 ---")
numeros = [10, 20, 30]
print(sumar_tres_a_lista(numeros))


# =====================================================================
# 16. Escribe una función que tome una cadena de texto y un número entero n
# como parámetros y devuelva una lista de todas las palabras que sean más
# largas que n. Usa la función filter()
# =====================================================================

# Como vamos a usar reduce(), necesitamos "importarla" (traerla) desde
# la biblioteca de herramientas integradas de Python llamada 'functools'.

from functools import reduce

def palabras_mas_largas(texto, n):
    # Usamos split() para separar la frase en una lista de palabras.
    palabras = texto.split()
    
    # filter() revisará palabra por palabra.
    # La lambda dice: "Mide la longitud de la palabra con len(). ¿Es estrictamente mayor que 'n'?"
    # Si es True, la palabra se queda; si es False, se descarta.
    palabras_filtradas = list(filter(lambda palabra: len(palabra) > n, palabras))
    
    return palabras_filtradas

# Prueba Kata 16:
print("\n--- Kata 16 ---")
mi_texto = "Yo sembré una flor y llovía y llovía, esperando a mi amor"
print(f"Palabras con más de 5 letras: {palabras_mas_largas(mi_texto, 5)}")


# =====================================================================
# 17. Crea una función que tome una lista de dígitos y devuelva el número
# correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos
# setenta y dos (572). Usa la función reduce()
# =====================================================================

from functools import reduce

def lista_a_numero(digitos):
    # reduce() es especial: toma los dos primeros elementos, los opera, y luego
    # toma ese resultado y lo opera con el tercer elemento, y así hasta reducir todo a un solo valor.
    
    # Nuestra lambda necesita dos variables:
    # 'acumulado' (lo que llevamos hasta ahora) y 'actual' (el nuevo dígito que entra).
    # La magia matemática es: acumulado * 10 + actual.
    # Ejemplo con [5, 7, 2]:
    # Paso 1: 5 * 10 + 7 = 57.
    # Paso 2: 57 * 10 + 2 = 572.
    resultado = reduce(lambda acumulado, actual: acumulado * 10 + actual, digitos)
    
    return resultado

# Prueba Kata 17:
print("\n--- Kata 17 ---")
lista_digitos = [5, 7, 2]
print(f"La lista {lista_digitos} se convierte en el número: {lista_a_numero(lista_digitos)}")


# =====================================================================
# 18. Escribe un programa en Python que cree una lista de diccionarios que
# contenga información de estudiantes (nombre, edad, calificación) y use la
# función filter para extraer a los estudiantes con una calificación mayor o
# igual a 90. Usa la función filter()
# =====================================================================

def filtrar_estudiantes_sobresalientes(lista_estudiantes):
    # Cada elemento de nuestra lista ahora es un diccionario entero (con nombre, edad, etc.).
    # La lambda recibe ese diccionario bajo el nombre 'estudiante'.
    # Para saber su nota, accedemos a la clave usando corchetes: estudiante['calificación'].
    # Si esa nota es >= 90 (True), el diccionario entero del estudiante se guarda en el resultado.
    sobresalientes = list(filter(lambda estudiante: estudiante['calificación'] >= 90, lista_estudiantes))
    
    return sobresalientes

# Prueba Kata 18:
print("\n--- Kata 18 ---")
# Creamos la lista de diccionarios de prueba
alumnos = [
    {"nombre": "Ana", "edad": 20, "calificación": 95},
    {"nombre": "Luis", "edad": 22, "calificación": 85},
    {"nombre": "María", "edad": 19, "calificación": 92}
]
print("Estudiantes con nota >= 90:")
print(filtrar_estudiantes_sobresalientes(alumnos))


# =====================================================================
# 19. Crea una función Lambda que filtre los números impares de una lista dada.
# =====================================================================

# Una función Lambda se escribe en una sola línea.
# Esta recibe una 'lista' y usa filter() por dentro.
# Para saber si un número es impar, usamos el operador módulo '%' que calcula el resto de una división.
# Si al dividir un número entre 2 el resto NO es cero (x % 2 != 0), entonces es impar.
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# 🧪 Prueba Kata 19:
print("\n--- Kata 19 ---")
numeros_mezclados = [1, 2, 3, 4, 5, 6, 7]
print(f"Lista original: {numeros_mezclados}")
print(f"Solo impares: {filtrar_impares(numeros_mezclados)}")


# =====================================================================
# 20. Para una lista con elementos tipo integer y string obtén una nueva lista
# sólo con los valores int. Usa la función faiter()
# =====================================================================

def filtrar_enteros(lista_mixta):
    # La función isinstance(elemento, tipo) nos devuelve True si el elemento es del tipo que buscamos.
    # En este caso, preguntamos si cada 'x' es de la familia de los enteros ('int').
    solo_enteros = list(filter(lambda x: isinstance(x, int), lista_mixta))
    
    return solo_enteros

# Prueba Kata 20:
print("\n--- Kata 20 ---")
lista_revuelta = [10, "hola", 42, "mundo", 7]
print(f"De la lista {lista_revuelta}, extraemos:")
print(filtrar_enteros(lista_revuelta))


# =====================================================================
# 21. Crea una función que calcule el cubo de un número dado mediante una
# función Lambda
# =====================================================================

# El cubo de un número es multiplicarlo por sí mismo tres veces (n * n * n).
# En Python, el operador para calcular potencias es el doble asterisco '**'.
# Así que 'x ** 3' eleva la 'x' al cubo.
calcular_cubo = lambda x: x ** 3

# Prueba Kata 21:
print("\n--- Kata 21 ---")
numero_prueba = 4
print(f"El cubo de {numero_prueba} es {calcular_cubo(numero_prueba)}")


# =====================================================================
# 22. Dada una lista numérica, obtén el producto total de los valores
# de dicha lista. Usa la función reduce().
# =====================================================================

from functools import reduce

def producto_total(numeros):
    # reduce() toma los dos primeros números (acumulado y actual), los multiplica,
    # y luego multiplica ese resultado por el siguiente número de la lista.
    resultado = reduce(lambda acumulado, actual: acumulado * actual, numeros)
    return resultado

# Prueba Kata 22:
print("\n--- Kata 22 ---")
lista_multiplicar = [2, 3, 4]
print(f"El producto de {lista_multiplicar} es {producto_total(lista_multiplicar)}")


# =====================================================================
# 23. Concatena una lista de palabras. Usa la función reduce()
# =====================================================================

from functools import reduce

def concatenar_palabras(palabras):
    # La "concatenación" es simplemente unir textos.
    # Al sumar dos strings en Python ("a" + "b"), el resultado es "ab".
    # Aquí añadimos un espacio " " en medio para que las palabras no queden pegadas.
    resultado = reduce(lambda frase_acumulada, palabra_actual: frase_acumulada + " " + palabra_actual, palabras)
    return resultado

# Prueba Kata 23:
print("\n--- Kata 23 ---")
palabras_sueltas = ["El", "curso", "es", "muy", "largo"]
print(f"Texto unido: '{concatenar_palabras(palabras_sueltas)}'")


# =====================================================================
# 24. Calcula la diferencia total en los valores de una lista.
# Usa la función reduce()
# =====================================================================

from functools import reduce

def diferencia_total(numeros):
    # Toma el primer número y le va restando todos los demás números de la lista uno por uno.
    resultado = reduce(lambda acumulado, actual: acumulado - actual, numeros)
    return resultado

# Prueba Kata 24:
print("\n--- Kata 24 ---")
lista_restar = [100, 20, 10, 5]
print(f"La diferencia total de {lista_restar} es {diferencia_total(lista_restar)}")


# =====================================================================
# 25. Crea una función que cuente el número de caracteres en una cadena
# de texto dada
# =====================================================================

def contar_caracteres(texto):
    # La función incorporada len() no solo sirve para saber cuántos elementos hay
    # en una lista, sino que también nos devuelve la longitud de una cadena de texto.
    total_caracteres = len(texto)
    return total_caracteres

# Prueba Kata 25:
print("\n--- Kata 25 ---")
texto_ejemplo = "Buenas tardes!"
print(f"El texto '{texto_ejemplo}' tiene {contar_caracteres(texto_ejemplo)} caracteres.")


# =====================================================================
# 26. Crea una función lambda que calcule el resto de la división
# entre dos números dados.
# =====================================================================

# Las funciones Lambda pueden recibir múltiples variables si las separamos por comas (a, b).
calcular_resto = lambda a, b: a % b

# Prueba Kata 26:
print("\n--- Kata 26 ---")
num1, num2 = 10, 3
print(f"El resto de dividir {num1} entre {num2} es {calcular_resto(num1, num2)}")


# =====================================================================
# 27. Crea una función que calcule el promedio de una lista de números.
# =====================================================================

def calcular_promedio_simple(numeros):
    # Prevenimos el error matemático de dividir por cero si la lista está vacía.
    if len(numeros) == 0:
        return 0
        
    promedio = sum(numeros) / len(numeros)
    return promedio

# Prueba Kata 27:
print("\n--- Kata 27 ---")
lista_notas = [10, 8, 9, 7]
print(f"El promedio de {lista_notas} es {calcular_promedio_simple(lista_notas)}")


# =====================================================================
# 28. Crea una función que busque y devuelva el primer elemento
# duplicado en una lista dada.
# =====================================================================

def primer_duplicado(lista):
    # Un 'set' (conjunto) es perfecto para recordar cosas que ya hemos visto,
    # porque las búsquedas dentro de un set son extremadamente rápidas en Python.
    vistos = set()
    
    # Recorremos la lista elemento por elemento.
    for elemento in lista:
        # Preguntamos: ¿Este elemento ya está en nuestra bolsa de "vistos"?
        if elemento in vistos:
            # Si ya está, ¡encontramos el primer duplicado! Lo devolvemos y la función termina.
            return elemento
        else:
            # Si no está, lo agregamos a nuestro set usando el método add() para recordarlo.
            vistos.add(elemento)
            
    # Si terminamos de revisar toda la lista y no hubo duplicados, devolvemos None (Nada).
    return None

# Prueba Kata 28:
print("\n--- Kata 28 ---")
mi_lista_numeros = [1, 2, 3, 4, 2, 5]
print(f"En la lista {mi_lista_numeros}, el primer duplicado es: {primer_duplicado(mi_lista_numeros)}")


# =====================================================================
# 29. Crea una función que convierta una variable en una cadena de texto
# y enmascare todos los caracteres con el carácter '#', excepto los
# últimos cuatro.
# =====================================================================

def enmascarar_variable(variable):
    # Primero, nos aseguramos de que lo que entre (sea número o lo que sea) se vuelva texto.
    texto = str(variable)
    
    # Si el texto tiene 4 letras o menos, no hay nada que enmascarar.
    if len(texto) <= 4:
        return texto
    
    # Calculamos cuántos caracteres debemos ocultar restando los 4 finales al total.
    cantidad_a_ocultar = len(texto) - 4
    
    # En Python podemos multiplicar textos. "#" * 3 nos da "###".
    parte_oculta = "#" * cantidad_a_ocultar
    
    # Usamos "Slicing" para cortar textos.
    # texto[-4:] significa: "Corta el texto empezando 4 posiciones desde el final, hasta el último carácter".
    parte_visible = texto[-4:]
    
    # Unimos ambas partes.
    return parte_oculta + parte_visible

# Prueba Kata 29:
print("\n--- Kata 29 ---")
tarjeta_credito = 1234567890123456
print(f"Dato original: {tarjeta_credito}")
print(f"Dato oculto: {enmascarar_variable(tarjeta_credito)}")


# =====================================================================
# 30. Crea una función que determine si dos palabras son anagramas,
# es decir, si están formadas por las mismas letras pero en diferente orden.
# =====================================================================

def son_anagramas(palabra1, palabra2):
    # Primero, "limpiamos" las palabras: las pasamos a minúsculas para que no haya
    # problemas entre "A" y "a", y quitamos espacios por si nos pasan frases.
    p1 = palabra1.lower().replace(" ", "")
    p2 = palabra2.lower().replace(" ", "")
    
    # La función sorted() toma cualquier texto y lo devuelve como una lista
    # con sus letras ordenadas alfabéticamente.
    # Si "amor" y "roma" tienen las mismas letras, al ordenarlas ambas serán ['a', 'm', 'o', 'r'].
    # Solo nos queda comparar si esas dos listas ordenadas son exactamente iguales.
    return sorted(p1) == sorted(p2)

# Prueba Kata 30:
print("\n--- Kata 30 ---")
palabra_a = "amor"
palabra_b = "mora"
print(f"¿'{palabra_a}' y '{palabra_b}' son anagramas?: {son_anagramas(palabra_a, palabra_b)}")


# =====================================================================
# 31. Crea una función que solicite al usuario ingresar una lista de nombres
# y luego solicite un nombre para buscar en esa lista. Si el nombre está en
# la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario,
# se lanza una excepción.
# =====================================================================

def buscar_nombre_usuario():
    try:
        # Pedimos los nombres y usamos split() para convertirlos en una lista.
        # Por defecto, split() separará los nombres por los espacios.
        entrada_nombres = input("Por favor ingresa nombres separados por espacios: ")
        lista_nombres = entrada_nombres.split()
        # Si queremos que la persona ingrese los nombres separados por comas y luego espacio
        # lista_nombres = entrada_nombres.split(", ")
        
        nombre_a_buscar = input("¿Qué nombre deseas buscar?")
        
        if nombre_a_buscar in lista_nombres:
            print(f"¡El nombre '{nombre_a_buscar}' fue encontrado en la lista!")
        else:
            # Si la condición es False, lanzamos nuestra propia excepción
            raise ValueError(f"El nombre '{nombre_a_buscar}' no está registrado.")
            
    except ValueError as e:
        print(f"Error detectado: {e}")

# Prueba Kata 31:
print("\n--- Kata 31 ---")
buscar_nombre_usuario()


# =====================================================================
# 32. Crea una función que tome un nombre completo y una lista de empleados,
# busque el nombre completo en la lista y devuelve el puesto del empleado si
# está en la lista, de lo contrario, devuelve un mensaje indicando que la
# persona no trabaja aquí.
# =====================================================================

def buscar_empleado(nombre_completo, lista_empleados):
    # Asumimos que lista_empleados es una lista de diccionarios,
    # ya que necesitamos guardar tanto el 'nombre' como el 'puesto' de cada persona.
    for empleado in lista_empleados:
        # Pasamos todo a minúsculas con lower() para evitar que falle por diferencias de mayúsculas
        if empleado["nombre"].lower() == nombre_completo.lower():
            # Si coincide, devolvemos el puesto y la función termina inmediatamente
            return f"El puesto de {nombre_completo} es: {empleado['puesto']}"
            
    # Si el bucle 'for' termina de revisar toda la lista y no encontró a nadie:
    return f"La persona '{nombre_completo}' no trabaja aquí."

# Prueba Kata 32:
print("\n--- Kata 32 ---")
base_datos_empleados = [
    {"nombre": "Carlos Pérez", "puesto": "Desarrollador"},
    {"nombre": "Laura Gómez", "puesto": "Diseñadora"}
]
print(buscar_empleado("Laura Gómez", base_datos_empleados))
print(buscar_empleado("Pedro Díaz", base_datos_empleados))


# =====================================================================
# 33. Crea una función Lambda que sume elementos correspondientes
# de dos listas dadas.
# =====================================================================

# map() puede recibir múltiples iterables (listas).
# En cada paso, tomará un elemento de lista1 y un elemento de lista2,
# y se los pasará a las variables 'x' e 'y' de nuestra lambda interna.
sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

# Prueba Kata 33:
print("\n--- Kata 33 ---")
lista_a = [1, 2, 3]
lista_b = [10, 20, 30]
print(f"La suma elemento por elemento es: {sumar_listas(lista_a, lista_b)}")


# =====================================================================
# 34. Crea la clase Arbol, define un árbol genérico con un tronco y ramas
# como atributos.Los métodos disponibles son:
# crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol.
# El objetivo es implementar estos métodos para manipular la estructura del árbol.
# =====================================================================

class Arbol:
    # 1. Inicializar un árbol con tronco de longitud 1 y ramas vacías
    # El método __init__ es el "constructor". Se ejecuta automáticamente al crear el árbol.
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    # 2. Aumentar la longitud del tronco en una unidad
    def crecer_tronco(self):
        self.tronco += 1

    # 3. Agregar una nueva rama de longitud 1 a la lista de ramas
    def nueva_rama(self):
        self.ramas.append(1)

    # 4. Aumentar en una unidad la longitud de todas las ramas existentes
    def crecer_ramas(self):
        # Recorremos cada rama y le sumamos 1 usando comprensión de listas
        self.ramas = [rama + 1 for rama in self.ramas]

    # 5. Eliminar una rama en una posición específica
    def quitar_rama(self, posicion):
        # pop() elimina un elemento de una lista basándose en su índice
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)

    # 6. Devolver información sobre tronco, número de ramas y longitudes
    def info_arbol(self):
        return f"Tronco: {self.tronco} | Total ramas: {len(self.ramas)} | Longitud ramas: {self.ramas}"


# Prueba Kata 34
print("\n--- Kata 34 ---")
mi_arbol = Arbol()              # 1. Crear un árbol
mi_arbol.crecer_tronco()        # 2. Crecer tronco 1 unidad
mi_arbol.nueva_rama()           # 3. Añadir nueva rama
mi_arbol.crecer_ramas()         # 4. Crecer todas las ramas 1 unidad
mi_arbol.nueva_rama()           # 5. Añadir dos nuevas ramas
mi_arbol.nueva_rama()
mi_arbol.quitar_rama(2)         # 6. Retirar rama en posición 2
print(mi_arbol.info_arbol())    # 7. Obtener información


# =====================================================================
# 36. Crea la clase UsuarioBanco, representa a un usuario de un banco
# con su nombre, saldo y si tiene o no cuenta corriente.
# Proporciona métodos para realizar operaciones como retirar dinero,
# transferir dinero desde otro usuario y agregar dinero al saldo.
# =====================================================================

class UsuarioBanco:
    # 1. Inicializar con nombre, saldo y cuenta corriente (True/False)
    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    # 2. Retirar dinero. Lanzará un error en caso de no poder hacerse
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            # Lanzamos nuestra propia excepción si no hay dinero suficiente
            raise ValueError(f"⚠️ {self.nombre} no tiene saldo suficiente.")
        self.saldo -= cantidad
        print(f"✅ {self.nombre} ha retirado {cantidad}. Saldo restante: {self.saldo}")

    # 4. Agregar dinero al saldo del usuario
    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"✅ {cantidad} agregados a {self.nombre}. Nuevo saldo: {self.saldo}")

    # 3. Realizar transferencia desde otro usuario. Lanzará error si falla
    def transferir_dinero(self, otro_usuario, cantidad):
        print(f"🔄 Iniciando transferencia de {cantidad} de {otro_usuario.nombre} a {self.nombre}...")
        # Primero le quitamos el dinero al otro usuario.
        # Si no tiene saldo, 'retirar_dinero' lanzará el error y el código se detendrá aquí.
        otro_usuario.retirar_dinero(cantidad)
        # Si tuvo éxito, nos agregamos el dinero a nosotros mismos
        self.agregar_dinero(cantidad)


# Prueba Kata 36
print("\n--- Kata 36 ---")
# 1. Crear Alicia (100) y Bob (50), ambos con cuenta (True)
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades a Bob
bob.agregar_dinero(20)

# 3. Transferencia de 80 de Bob a Alicia
# Usamos try/except porque sabemos que Bob solo tiene 70 (50+20) y esto lanzará el error que programamos
try:
    alicia.transferir_dinero(bob, 80)
except ValueError as e:
    print(e)

# 4. Retirar 50 a Alicia
alicia.retirar_dinero(50)


# =====================================================================
# 37. Crea una función llamada procesar_texto que procesa un texto según
# la opción: contar_palabras, reemplazar_palabras o eliminar_palabra.
# Estas opciones son otras funciones que tenemos que definir primero y
# llamar dentro de la función procesar_texto.
# =====================================================================

# 1. Función para contar palabras
def contar_palabras(texto):
    palabras = texto.lower().split()
    diccionario = {}
    for p in palabras:
        if p in diccionario:
            diccionario[p] += 1
        else:
            diccionario[p] = 1
    return diccionario

# 2. Función para reemplazar palabras
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    # Los strings en Python ya tienen un método integrado llamado replace()
    return texto.replace(palabra_original, palabra_nueva)

# 3. Función para eliminar palabra
def eliminar_palabra(texto, palabra_a_eliminar):
    # Eliminar es básicamente reemplazar una palabra por "nada" (texto vacío "")
    return texto.replace(palabra_a_eliminar, "")

# 4. Función principal procesar_texto
# Usamos *args para recibir un "número de argumentos variable"
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        # Para contar no necesitamos argumentos extra
        return contar_palabras(texto)
        
    elif opcion == "reemplazar":
        # args[0] es la palabra a buscar, args[1] es la palabra nueva
        return reemplazar_palabras(texto, args[0], args[1])
        
    elif opcion == "eliminar":
        # args[0] es la palabra a eliminar
        return eliminar_palabra(texto, args[0])
        
    else:
        return "Opción no válida."

# Prueba Kata 37
print("\n--- Kata 37 ---")
mi_texto = "Desde inicios del 2000 las señales han aumentado"
print(f"Texto original: '{mi_texto}'")

print("\n1. Contar palabras:")
print(procesar_texto(mi_texto, "contar"))

print("\n2. Reemplazar '2000' por '2026':")
print(procesar_texto(mi_texto, "reemplazar", "2000", "2026"))

print("\n3. Eliminar 'Desde':")
print(procesar_texto(mi_texto, "eliminar", "Desde "))


# =====================================================================
# 38. Genera un programa que nos diga si es de noche, de día o tarde
# según la hora proporcionada por el usuario.
# =====================================================================

def momento_del_dia():
    try:
        # Usamos input() para pedir la hora y la convertimos a entero (int)
        entrada = input("Por favor, ingresa la hora (formato 0 a 23): ")
        hora = int(entrada)
        
        # Validamos en qué rango cae la hora
        if 6 <= hora < 12:
            print("Es de día")
        elif 12 <= hora < 20:
            print("Es de tarde")
        elif (20 <= hora <= 23) or (0 <= hora < 6):
            print("Es de noche")
        else:
            print("Esa hora no es válida. Debe ser entre 0 y 23.")
            
    except ValueError:
        print("Error: Debes ingresar un número entero.")

# Prueba Kata 38:
print("\n--- Kata 38 ---")
momento_del_dia()


# =====================================================================
# 39. Escribe un programa que determine qué calificación en texto
# tiene un alumno en base a su calificación numérica.
# =====================================================================

def clasificar_nota(nota):
    # Evaluamos usando los rangos exactos que pide el ejercicio
    if 90 <= nota <= 100:
        return "excelente"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 70 <= nota <= 79:
        return "bien"
    elif 0 <= nota <= 69:
        return "insuficiente"
    else:
        return "nota fuera de rango"

# Prueba Kata 39:
print("\n--- Kata 39 ---")
nota_alumno = 85
print(f"Una calificación de {nota_alumno} equivale a: {clasificar_nota(nota_alumno)}")


# =====================================================================
# 40. Escribe una función que tome dos parámetros: figura (una cadena que
# puede ser "rectangulo" , "circulo" o "triangulo") y datos (una tupla con
# los datos necesarios para calcular el área).
# =====================================================================

def calcular_area(figura, datos):
    # Convertimos la figura a minúsculas para evitar errores tipográficos
    figura = figura.lower()
    
    if figura == "rectangulo":
        # Extraemos los datos de la tupla. Esto se llama "desempaquetado".
        base, altura = datos
        return base * altura
        
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
        
    elif figura == "circulo":
        # Para el círculo, la tupla solo trae un dato (el radio)
        radio = datos[0]
        # Usamos 3.14159 como valor de Pi aproximado
        return 3.14159 * (radio ** 2)
        
    else:
        return "Figura no reconocida"

# Prueba Kata 40:
print("\n--- Kata 40 ---")
# Le pasamos una tupla (5, 10) que representa base y altura
datos_rectangulo = (5, 10)
print(f"Área del rectángulo: {calcular_area('rectangulo', datos_rectangulo)}")


# =====================================================================
# 41. Programa que utilice condicionales para determinar el monto final
# de una compra en una tienda en línea, después de aplicar un descuento.
# =====================================================================

def calcular_compra():
    try:
        # 1. Solicita al usuario el precio original
        precio_original = float(input("Ingresa el precio original del artículo (€): "))
        
        # 2. Pregunta si tiene cupón
        # .strip().lower() limpia espacios extra y pasa a minúsculas la respuesta
        tiene_cupon = input("¿Tienes un cupón de descuento? (si/no): ").strip().lower()
        
        # 6. Uso de if, elif y else
        if tiene_cupon == "sí" or tiene_cupon == "si":
            # 3. Solicita el valor del cupón
            valor_cupon = float(input("Ingresa el valor del cupón (€): "))
            
            # 4. Aplica el descuento si es mayor a cero
            if valor_cupon > 0:
                precio_final = precio_original - valor_cupon
                
                # Pequeña validación extra: evitar que la tienda nos deba dinero
                if precio_final < 0:
                    precio_final = 0
                    
                # 5. Muestra precio final con descuento
                print(f"Descuento aplicado. Total a pagar: {precio_final}€")
            else:
                print(f"Cupón no válido (debe ser > 0). Total a pagar: {precio_original}€")
                
        elif tiene_cupon == "no":
            # 5. Muestra precio final sin descuento
            print(f"No hay descuento. Total a pagar: {precio_original}€")
            
        else:
            print(f"Respuesta no reconocida. Total a pagar: {precio_original}€")
            
    except ValueError:
        print("Error: Por favor, ingresa solo valores numéricos para los precios.")

# Prueba Kata 41:
print("\n--- Kata 41 ---")
calcular_compra() 