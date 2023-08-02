import re

def trocar_caracteres(string, caracteres_originais, caracteres_troca):
    tabela_de_traducao = str.maketrans(caracteres_originais, caracteres_troca)
    return string.translate(tabela_de_traducao)


def transform_to_morse(text):
    caracteres_opcionais = "p t"
    caracteres_troca = ". -"
    caracteres_distintos = set(text)
    if len(caracteres_distintos) <= 3:
        if set(caracteres_opcionais).issuperset(caracteres_distintos):
            text = trocar_caracteres(text,caracteres_opcionais,caracteres_troca)
        
        morse_letters = text.split(" ")
        print(morse_letters)
        return morse_letters
    
    return None
 
def translate_to_words(morse_list):
    dict_letters ={
        ""      : " ",
        ".-"    : "A",
        "-..."  : "B",
        "-.-."  : "C",
        "-.."   : "D",
        "."     : "E",
        "..-."  : "F",
        "--."   : "G",
        "...."  : "H",
        ".."    : "I",
        ".---"  : "J",
        "-.-"   : "K",
        ".-.."  : "L",
        "--"    : "M",
        "-."    : "N",
        "---"   : "O",
        ".--."  : "P",
        "--.-"  : "Q",
        ".-."   : "R",
        "..."   : "S",
        "-"     : "T",
        "..-"   : "U",
        "...-"  : "V",
        ".--"   : "W",
        "-..-"  : "X",
        "-._-"  : "Y",
        "--.."  : "Z",
        ".----" : "1",    
        "..---" : "2",    
        "...--" : "3",    
        "....-" : "4",    
        "....." : "5", 
        "-...." : "6", 
        "--..." : "7", 
        "---.." : "8", 
        "----." : "9", 
        "-----" : "0", 
        ".-.-.-": ".",
        "--..--": ",",
        "..--..": "?",
        "-.-.--": "!",
        "---...": ":",
        ".----.": "'",
        ".-..-.": "\"",
        }
    text = ""
    for morse_word in morse_list:
        text += dict_letters.get(morse_word,"$")
        
    return text.replace("  "," ")
        
    
    

def get_morse():
    text = input("Digite o código morse: ")
    morse_letters = transform_to_morse(text)
    if morse_letters != None:
        return translate_to_words(morse_letters)
    return None
    
print(get_morse())
