import emoji
import random
import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega a chave da OpenAI do arquivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Função para normalizar texto (remover acentos)
import unicodedata
def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return texto

def calcubot_resposta(pergunta):
    pergunta = normalizar(pergunta)

    # Emojis por tipo de resposta
    emojis_matematica = [":tada:", ":bar_chart:", ":1234:"]
    emojis_curiosidade = [":thinking_face:", ":books:", ":earth_americas:", ":sun_with_face:", ":bulb:"]
    emojis_historia = [":open_book:", ":sparkles:", ":star:", ":robot_face:"]

    # Operacoes matematicas
    if any(op in pergunta for op in ["+", "-", "*", "/"]):
        emoji_escolhido = emoji.emojize(random.choice(emojis_matematica), language="alias")
        try:
            resultado = eval(pergunta)
            return f"🎉 O resultado da operacao e {resultado}! {emoji_escolhido}"
        except:
            return f"😅 Nao consegui entender a operacao. Tente escrever algo como '2 + 2'. {emoji_escolhido}"

    # Perguntas educativas programadas
    elif "sistema solar" in pergunta:
        emoji_escolhido = emoji.emojize(random.choice(emojis_curiosidade), language="alias")
        return f"🌞 O sistema solar tem 8 planetas girando ao redor do Sol. A Terra 🌍 e um deles! {emoji_escolhido}"

    elif "fotossintese" in pergunta:
        emoji_escolhido = emoji.emojize(random.choice(emojis_curiosidade), language="alias")
        return f"🌱 As plantas usam a luz do Sol para produzir energia. Isso se chama fotossintese! {emoji_escolhido}"

    elif "brasil" in pergunta:
        emoji_escolhido = emoji.emojize(random.choice(emojis_curiosidade), language="alias")
        return f"🇧🇷 O Brasil foi descoberto em 1500 por Pedro Alvares Cabral. {emoji_escolhido}"

    elif "sol" in pergunta:
        emoji_escolhido = emoji.emojize(random.choice(emojis_curiosidade), language="alias")
        return f"☀️ O Sol da luz e calor, permitindo que a vida exista na Terra! {emoji_escolhido}"

    # Historias ou curiosidades automaticas
    elif "conte uma historia" in pergunta or "historia" in pergunta or "curiosidade" in pergunta:
        emoji_escolhido = emoji.emojize(random.choice(emojis_historia), language="alias")
        historias = [
            "📖 Era uma vez uma pequena estrela que queria brilhar mais do que o Sol. Ela aprendeu que cada estrela tem seu brilho unico! ✨",
            "🤖 Um robozinho curioso viajou pelo mundo e descobriu que ate a Lua tem sua propria historia! 🌙",
            "🌱 Uma sementinha sonhava em tocar o ceu. Cresceu e virou uma arvore gigante, dando sombra e frutos para todos. 🍎"
        ]
        return random.choice(historias) + f" {emoji_escolhido}"

    # Perguntas nao programadas → chama a OpenAI
    else:
        emoji_escolhido = emoji.emojize(random.choice(emojis_curiosidade), language="alias")
        try:
            resposta_openai = client.chat.completions.create(
                model="gpt-5.2",
                messages=[
                    {"role": "system", "content": "Voce e um chatbot educativo e divertido para criancas. Responda com frases curtas e alegres."},
                    {"role": "user", "content": pergunta}
                ],
                max_completion_tokens=150
            )

            texto_resposta = resposta_openai.choices[0].message.content
            return f"{texto_resposta} {emoji_escolhido}"

        except Exception as e:
            print("Erro na chamada API OPEN AI:", str(e))
            return f"🤔 Ops! Algo deu errado ao me comunicar com o chatbot. {emoji_escolhido}"


# Introducao
print("=== Bem-vindo ao Calcubot! 🤖🎉 ===")
print("Eu posso te ajudar com operacoes matematicas, curiosidades e ate contar historias!")
print("Digite 'sair' para encerrar.\n")

# Loop principal
while True:
    pergunta = input("Digite sua pergunta ou operacao: ")
    if pergunta.lower() == "sair":
        print("Tchauzinho! Ate a proxima 👋🤖")
        break

    resposta = calcubot_resposta(pergunta)
    print(resposta.encode('utf-8', errors='replace').decode('utf-8'))


