# Cifrado César en Python

El cifrado César es uno de los métodos de cifrado más simples y ampliamente conocidos. Es un tipo de cifrado por sustitución en el que cada letra en el texto original es reemplazada por una letra que se encuentra un número fijo de posiciones más adelante en el alfabeto.

## Cómo funciona

1. **Cifrado**: 
   - Cada letra en el mensaje original se desplaza un número específico de posiciones en el alfabeto.
   - Por ejemplo, con un desplazamiento de 3, 'A' se convierte en 'D', 'B' en 'E', y así sucesivamente.

2. **Descifrado**: 
   - Para descifrar, simplemente se revierte el proceso, desplazando las letras en la dirección opuesta.

## Implementación en Python

El código proporcionado incluye dos funciones principales:

1. `cifrar(mensaje, desplazamiento)`: Toma un mensaje y un valor de desplazamiento, y retorna el mensaje cifrado.
2. `descifrar(mensaje_cifrado, desplazamiento)`: Toma un mensaje cifrado y el valor de desplazamiento, y retorna el mensaje original.

### Características clave del código:

- Maneja tanto letras mayúsculas como minúsculas.
- Preserva los caracteres no alfabéticos (espacios, puntuación, etc.) sin modificarlos.
- Utiliza la aritmética modular para "envolver" el alfabeto (por ejemplo, 'Z' con un desplazamiento de 1 se convierte en 'A').

