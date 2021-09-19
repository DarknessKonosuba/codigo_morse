codigo_morse = { ".-":"A", "-...":"B", "-.-.":"C", "----":"CH", "-..":"D", ".":"E",
                "..-.":"F", "--.":"G", "....":"H", "..":"I", ".---":"J", "-.-":"K",
                ".-..":"L", "--":"M", "-.":"N", "--.--":"Ñ", "---":"O", ".--.":"P",
                "--.-":"Q", ".-.":"R", "...":"S", "-":"T", "..-":"U", "...-":"V",
                ".--":"W", "-..-":"X", "-.--":"Y", "--..":"Z"
}

lista = input("Ingrese una palabra en morse: ")
lista_convert = list(lista.split(" "))

listaNueva = []

for e in lista_convert:
    conv = codigo_morse[e]
    listaNueva.append(conv)
    
print(listaNueva)
