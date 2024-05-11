import google.generativeai as genai
import PIL.Image
import pyttsx3

# Configuração do Google Gemini
genai.configure(api_key="sua_chave_api_aqui")

# Configuração do assistente falante
assistente_falante = True
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 190)  # velocidade 120 = lento
voz = 0
engine.setProperty('voice', voices[voz].id)

# Configuração do modelo de geração de contos infantis
generation_config = {
    "candidate_count": 1,
    "temperature": 1,
}

safety_settings = {
    "HARASSMENT": "BLOCK_MEDIUM_AND_ABOVE",
    "HATE": "BLOCK_MEDIUM_AND_ABOVE",
    "SEXUAL": "BLOCK_MEDIUM_AND_ABOVE",
    "DANGEROUS": "BLOCK_MEDIUM_AND_ABOVE",
}

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Carregamento da imagem
img = PIL.Image.open('img.png')

# diretriz para criação:
diretriz_para_criacao = """

1. Elabore uma história encantada e bonita para criança. 
2. Use elementos da imagem para dar vida a história
3. Comece com Era uma vez..
4. evite repetir palavras.
5. Deve ser uma mini história divertida e empolgante
6. O protagonista da história é o que aparece na imagem
"""

# Geração do conto infantil mágico
response = model.generate_content([diretriz_para_criacao, img])
response.resolve()

# Impressão da resposta do modelo
print("Resposta da pergunta", response.text)

# Fala da história gerada
if assistente_falante:
    engine.say(response.text)
    engine.runAndWait()
