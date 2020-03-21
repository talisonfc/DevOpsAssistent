import speech_recognition as sr 

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('estou lhe ouvindo')
        audio = microfone.listen(source)

        try:
            frase = microfone.recognize_google(audio, language='pt-BR')
            print('voce disse: ' + frase)
            if frase != 'sair':
                ouvir_microfone()
        except sr.UnknownValueError:
            ouvir_microfone()

ouvir_microfone()