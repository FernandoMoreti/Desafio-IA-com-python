from openai import OpenAI
import json

client = OpenAI(
    base_url = "http://127.0.0.1:1234/v1",
    api_key = "lm_studio"
)

lista_de_resenhas = []

with open("Resenha_App_ChatGPT.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_de_resenhas.append(linha)

conteudo_resenhas = "\n".join(lista_de_resenhas)

resposta_da_ia = client.chat.completions.create(
    model = "google/gemma-3-4b",
    messages = [
        {
            "role": "system",
            "content": 
            """
                Quero que você analise a lista que irei enviar e a separe em um JSON retornando somente a lista,
                contendo 4 atributos que na lista estão separadas por um $, esses 4 atributos são obrigatorios:
                - nome
                - avaliação (texto original)
                - avaliação-pt (Traduza para o portugues a avaliação)
                - feedback (Positiva, Negativa ou Neutra, com base na avaliação, essa parte não pode seer diferente de (Positiva, Negativa ou Neutra))

                Cada item da lista está separado por '/n'.
            """
        },
        {
            "role": "user",
            "content": conteudo_resenhas
        }
    ],
    temperature = 0.2
)

def extrair_json(texto):
    texto = texto.strip()

    if texto.startswith("```"):
        linhas = texto.split("\n")
        linhas = linhas[1:]
        if linhas[-1].strip().startswith("```"):
            linhas = linhas[:-1]
        texto = "\n".join(linhas)

    return texto.strip()



json_puro = extrair_json(resposta_da_ia.choices[0].message.content)

lista_retornada = json.loads(json_puro)


def exec(lista):

    positiva = 0
    neutra = 0
    negativa = 0

    for item in lista:
        if item["feedback"] == "Positiva":
            positiva += 1
        elif item["feedback"] == "Negativa":
            negativa += 1
        elif item["feedback"] == "Neutra":
            neutra += 1

    
    print(f"Notas Positivas: {positiva}")
    print(f"Notas Neutras: {neutra}")
    print(f"Notas Negativas: {negativa}\n")

exec(lista_retornada)