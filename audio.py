import speech_recognition as sr
import difflib

def get_most_similar_word(word, valid_words):
    return difflib.get_close_matches(word, valid_words, n=1, cutoff=0.1)

def get_microfone_morse():
    # Inicializa o reconhecedor de fala
    recognizer = sr.Recognizer()

    # Lista das palavras a serem reconhecidas
    target_words = ["ponto", "traço", "espaço"]

    while True:
        try:
            # Captura o áudio do microfone
            with sr.Microphone() as source:
                print("Diga alguma coisa...")
                audio = recognizer.listen(source, timeout=5)

            # Realiza o reconhecimento de fala
            text = recognizer.recognize_google(audio, language="pt-BR")
            print( text  )
            # Tokeniza o texto em palavras
            words = text.split()

            # Lista para armazenar as palavras corrigidas
            corrected_words = []

            # Corrige cada palavra reconhecida
            for word in words:
                if word in target_words:
                    corrected_words.append(word)
                else:
                    # Encontramos a palavra mais similar
                    most_similar_word = get_most_similar_word(word, target_words)
                    corrected_words.extend(most_similar_word)
            break

        except sr.WaitTimeoutError:
            print("Nenhum áudio detectado. Tente novamente.")
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio. Tente novamente.")
        except sr.RequestError as e:
            print(f"Erro na solicitação ao serviço de reconhecimento de fala: {e}")
            
    return corrected_words

def transform_to_morse(text):
    morse_list = list(map(lambda word: word.replace("ponto",".").replace("traço","-").replace("espaço"," "),text))
    morse_words = "".join(morse_list).split(' ')
    morse_final_words = []
    for word in morse_words:
        if word.strip() != '':
            morse_final_words.append(word)
    return morse_words

if __name__ == "__main__":
    list_of_words = get_microfone_morse()
    print(list_of_words)
    print(transform_to_morse(list_of_words))