# Storytelling Inclusivo: Dando Voz a Todas as Crianças

![Exemplo de História](https://github.com/Pablopinheiroo/storytelling_inclusivo_DandoVozATodasAsCriancas/blob/main/gatofofo.png)
![Exemplo de História](https://github.com/Pablopinheiroo/storytelling_inclusivo_DandoVozATodasAsCriancas/blob/main/img.png)

Imagine um universo onde cada criança é transportada para um mundo de magia e aventura através de histórias feitas sob medida para elas. O Storytelling Mágico é uma iniciativa que utiliza a API do Google Gemini para criar contos encantadores, enriquecidos com elementos visuais e narrativas envolventes.

## Apresentação:

A ideia do Storytelling Inclusivo é clara, concisa e inspiradora. O projeto aborda um problema real e oferece uma solução eficaz e criativa, com potencial para impactar positivamente a vida de muitas crianças.

### Funcionalidades:

- **Reconhecimento de Imagens:** As crianças podem escolher suas imagens favoritas, e o Gemini as utiliza como inspiração para criar histórias únicas.
  
- **Síntese de Voz Cativante:** As narrativas são transformadas em áudio, com vozes expressivas que dão vida aos personagens e cenários.

### Acessibilidade Aprimorada:

Nosso projeto oferece uma experiência inclusiva, priorizando a acessibilidade para todas as crianças. Ao gerar contos infantis personalizados, proporcionamos narrações expressivas para permitir que crianças com deficiência visual desfrutem plenamente das histórias. Adicionalmente, para garantir uma experiência enriquecida, oferecemos descrições de áudio detalhadas das imagens, beneficiando também as crianças com deficiência visual.

## Impacto:

- **Promove a inclusão:** Permite que crianças com diferentes necessidades acessem e desfrutem da literatura.
  
- **Desenvolve habilidades de linguagem:** A narração expressiva e os recursos visuais auxiliam no desenvolvimento da linguagem e da compreensão.
  
- **Incentiva o amor pela leitura:** Cria uma experiência imersiva e envolvente que desperta o interesse das crianças pela leitura.

## Criatividade:

O projeto combina tecnologias avançadas de IA com o poder do storytelling para criar uma solução inovadora que atende às necessidades de crianças com diferentes habilidades.

## Eficácia:

A API do Gemini oferece recursos poderosos de reconhecimento de imagens e síntese de voz, garantindo a precisão dos audiolivros.


# Funcionamento do Script
## Pip install necessário
Esses comandos instalarão os pacotes necessários para que o seu script funcione corretamente. Certifique-se de executá-los no terminal ou prompt de comando antes de tentar rodar o script novamente.
```
pip install google-generativeai
pip install pillow
pip install pyttsx3
```

## Instalação de Dependências:
Essas são as importações necessárias para o funcionamento do script. google.generativeai é o módulo que você está utilizando para acessar a API do Google Gemini, responsável pela geração de conteúdo. PIL.Image é uma parte da biblioteca PIL (Python Imaging Library) que permite abrir e manipular imagens. pyttsx3 é uma biblioteca que possibilita a síntese de voz no Python.
```
import google.generativeai as genai
import PIL.Image
import pyttsx3
```

## Configuração do Google Gemini:
Esta linha configura a API do Google Gemini. É necessário fornecer uma chave de API válida para acessar os recursos do Google Gemini.
```
genai.configure(api_key="sua_chave_api_aqui")
```

## Configuração do Assistente Falante:
Aqui, definimos se o assistente falante deve ser ativado (True). Em seguida, inicializamos o mecanismo de síntese de voz (pyttsx3) e configuramos sua velocidade (rate) e a voz a ser usada.
```
assistente_falante = True
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 190)
voz = 0
engine.setProperty('voice', voices[voz].id)
```

## Configuração do Modelo de Geração de Contos Infantis:
Aqui, definimos as configurações de geração do modelo, como o número de candidatos (candidate_count) e a temperatura (temperature). Além disso, configuramos as definições de segurança para bloquear conteúdos indesejados.
```
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

```

## Carregamento da Imagem:
Essa linha carrega uma imagem que será usada como entrada para a geração do conto infantil.
```
# Carregamento da imagem
img = PIL.Image.open('img.png')
```

## Diretriz para Criação:
Esta é a diretriz para a criação do conto infantil. É uma string que contém instruções sobre como o conto deve ser criado.
```
# Diretriz para criação do conto infantil
diretriz_para_criacao = """
1. Elabore uma história encantada e bonita para criança. 
2. Use elementos da imagem para dar vida a história
3. Comece com "Era uma vez..."
4. Evite repetir palavras.
5. Deve ser uma mini história divertida e empolgante
6. O protagonista da história é o que aparece na imagem
"""
```

## Geração do Conto Infantil Mágico:
Esta parte do código utiliza o modelo previamente configurado para gerar um conto infantil com base na diretriz fornecida e na imagem carregada.
```
response = model.generate_content([diretriz_para_criacao, img])
response.resolve()
```

## Impressão da resposta do modelo:
A História é gerada pelo modelo e impressa no console.
```
print("Resposta da pergunta", response.text)
```

## Fala da história gerada:
Se a variável assistente_falante estiver definida como True, o texto do conto gerado é convertido em fala usando o mecanismo de síntese de voz e reproduzido pelo sistema de áudio.
```
if assistente_falante:
    engine.say(response.text)
    engine.runAndWait()
```


## Áudio:
[Acesse o áudio narrado](https://github.com/Pablopinheiroo/storytelling_inclusivo_DandoVozATodasAsCriancas/blob/main/audio_narrado.mp3)

