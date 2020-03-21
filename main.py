# -*- coding: utf-8 -*-
import speech_recognition as sr 
from controllers import DBController

dbController = DBController.DBController()

mapOfHandlers = {
    "adicionar banco de dados": dbController.addDB,
    "meus bancos de dados": dbController.show,
    "remover banco de dados": dbController.removeDB,
    "conectar com banco de dados": dbController.connectDB,
    "criar banco de dados": dbController.createDB,
    "excluir banco de dados": dbController.dropDB,
    "carregar banco de dados": dbController.loadDump
}

def dispatch(command):
    # if command == "adicionar banco de dados":
    #     dbController.addDB()
    try:
        if command.encode("utf-8") in "O que você sabe fazer":
            print("Eu sei fazer isso:")
            for action in mapOfHandlers.keys():
                print('- '+action)
        else:
            mapOfHandlers[command]()
    except KeyError:
        print("nenhum handler disponivel")

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('estou lhe ouvindo')
        audio = microfone.listen(source)

        try:
            frase = microfone.recognize_google(audio, language='pt-BR')
            print('voce disse: ' + frase)
            
            if frase != '':

                dispatch(frase)

            if frase != 'tchau':
                ouvir_microfone()
            else:
                print("Obrigado Sr.")
        except sr.UnknownValueError:
            ouvir_microfone()

# mode = 'text'
mode = 'voz'

if mode == 'text':
    dispatch("carregar banco de dados")
else:
    ouvir_microfone()
