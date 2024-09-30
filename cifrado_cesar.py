def cifrar(mensaje, desplazamiento):
    resultado = ""
    for char in mensaje:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            nuevo_char = chr((ord(char) - ascii_offset + desplazamiento) % 26 + ascii_offset)
            resultado += nuevo_char
        else:
            resultado += char
    return resultado

def descifrar(mensaje_cifrado, desplazamiento):
    return cifrar(mensaje_cifrado, -desplazamiento)

# Ejemplo de uso
mensaje_original = "HOLA MUNDO"
desplazamiento = 3

mensaje_cifrado = cifrar(mensaje_original, desplazamiento)
mensaje_descifrado = descifrar(mensaje_cifrado, desplazamiento)

print(f"Mensaje original: {mensaje_original}")
print(f"Mensaje cifrado: {mensaje_cifrado}")
print(f"Mensaje descifrado: {mensaje_descifrado}")