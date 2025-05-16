def responder(pergunta):
    pergunta = pergunta.lower()

    if "oi" in pergunta or "ola" in pergunta:
        return "Ola!! Como posso ajudar voçe?"
    elif "tudo bem" in pergunta:
        return "Tudo otimo!! e com voçe?"
    elif "qual seu nome" in pergunta:
        return "Eu sou um kiwi, seu assistente virtual!"
    elif "ajuda" in pergunta:
        return "Claro!! Do que voçe precisa?"
    elif "tchau" in pergunta or "até mais" in pergunta:
        return "até logo!! "
    else: 
        return "Desculpa, não entendi. Pode repetir?"
    
def iniciar_chatbot():
    print("KiwiBot: Ola!! Tudo bem? Digite 'sair' para encerrar.")
    while True:
        usuario = input("Voce: ")
        if usuario.lower() == "sair":
            print("KiwiBot: Tchau!! Ate mais!!")
            break
        resposta = responder(usuario)
        print("KiwiBot", resposta)


# iniciar chatbot

if __name__ == "__main__":
    iniciar_chatbot()