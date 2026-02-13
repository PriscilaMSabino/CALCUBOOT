from dotenv import load_dotenv
import os
from openai import OpenAI

# Carrega o .env
load_dotenv()

# Pega a chave da OpenAI
api_key = os.getenv("OPENAI_API_KEY")
print("Chave carregada?", bool(api_key))  # Vai mostrar True se a chave foi encontrada

# Cria o cliente
client = OpenAI(api_key=api_key)

try:
    resposta = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": "Quem foi Pedro Álvares Cabral?"}],
        max_completion_tokens=50
    )
    print("Resposta da API:", resposta.choices[0].message.content)
except Exception as e:
    print("Erro na API:", e)
