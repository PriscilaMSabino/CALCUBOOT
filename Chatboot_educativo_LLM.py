import emoji
import random
import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega a chave da OpenAI do arquivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def calcubot_resposta(pergunta):
    pergunta = pergunta.lower()

    # Emojis por tipo de resposta
    emojis_matematica = [":tada:", ":bar_chart:", ":1234:"]
    emojis_curiosidade = [":thinking_face:", ":books:", ":earth_americas:", ":sun_with_face:", ":bulb:"]
    emojis_historia = [":open_book:", ":sparkles:", ":star:", ":dog:"]

    # Operações matemáticas
    if any(op in pergunta for op in ["+", "-", "*", "/"]):
        emoji_escolhido = emoji.emojize(random.choice(emojis_matematica), language="alias")
        try:
            resultado = eval(pergunta)
            return f"🎉 O resultado da operação é {resultado}! {emoji_escolhido}"
        except:
            return f"😅 Não consegui entender a operação. Tente escrever algo como '2 + 2'. {emoji_escolhido}"

    # Perguntas educativas programadas
    elif "sistema solar" in pergunta:
        emoji_escolhido = emoji.emojize(random.choice(emojis_curiosidade), language="alias")
        return f"🌞 O sistema solar tem 8 planetas girando ao redor do Sol. A Terra 🌍 é um deles! {emoji_escolhido}"
    elif "fotossíntese" in pergunta:
        emoji_escolhido = emoji.emojize(random.choice(emojis_curiosidade), language="alias")
        return f"🌱 As plantas usam a luz do Sol para produzir energia. Isso se chama fotossíntese! {emoji_escolhido}"
    elif "brasil" in pergunta:
        emoji_escolhido = emoji.emojize(random.choice(emojis_curiosidade), language="alias")
        return f"🇧🇷 O Brasil foi descoberto em 1500 por Pedro Álvares Cabral. {emoji_escolhido}"
    elif "sol" in pergunta:
        emoji_escolhido = emoji.emojize(random.choice(emojis_curiosidade), language="alias")
        return f"☀️ O Sol dá luz e calor, permitindo que a vida exista na Terra! {emoji_escolhido}"

    # Histórias ou curiosidades automáticas
    elif "conte uma história" in pergunta or "história" in pergunta or "curiosidade" in pergunta:
        emoji_escolhido = emoji.emojize(random.choice(emojis_historia), language="alias")
        historias = [
            "📖 Era uma vez uma pequena estrela que queria brilhar mais do que o Sol. Ela aprendeu que cada estrela tem seu brilho único! ✨",
            "🐶 Um cachorrinho curioso viajou pelo mundo e descobriu que até a Lua tem sua própria história! 🌙",
            "🌱 Uma sementinha sonhava em tocar o céu. Cresceu e virou uma árvore gigante, dando sombra e frutos para todos. 🍎"
        ]
        return random.choice(historias) + f" {emoji_escolhido}"

    # Perguntas não programadas → chama a OpenAI
    else:
        emoji_escolhido = emoji.emojize(random.choice(emojis_curiosidade), language="alias")
        try:
            resposta_openai = client.chat.completions.create(
                model="gpt-5.2",
                messages=[
                    {"role": "system", "content": "Você é um chatbot educativo e divertido para crianças. Responda com frases curtas e alegres."},
                    {"role": "user", "content": pergunta}
                ],
                max_completion_tokens=150
            )
            texto_resposta = resposta_openai.choices[0].message.content
            return f"{texto_resposta} {emoji_escolhido}"
        except Exception as e:
            # Mostra o erro real no terminal
            print("Erro na chamada API OPEN AI:", e)
            return f"🤔 Ops! Algo deu errado ao me comunicar com o chatbot. {emoji_escolhido}"


# Introdução
print("=== Bem-vindo ao Calcubot! 🐶🎉 ===")
print("Eu posso te ajudar com operações matemáticas, curiosidades e até contar histórias!")
print("Digite 'sair' para encerrar.\n")

# Loop principal
while True:
    pergunta = input("Digite sua pergunta ou operação: ")
    if pergunta.lower() == "sair":
        print("Tchauzinho! Até a próxima 👋🐶")
        break
    resposta = calcubot_resposta(pergunta)
    print(resposta)
