# Exemplos de Uso da API Gemini

Este repositório contém exemplos de como usar a API do Google Gemini para diversas tarefas, utilizando o modelo `gemini-1.5-flash`.  Cada script Python demonstra uma aplicação diferente, exigindo uma chave de API válida (`GEMINI_API_KEY`) configurada como variável de ambiente.

**Pré-requisitos:**

* Uma conta do Google com acesso à API Gemini.
* A chave de API configurada na variável de ambiente `GEMINI_API_KEY`.
* A biblioteca `google-generativeai` instalada: `pip install google-generativeai`
* Os arquivos de imagem e texto mencionados em cada exemplo (ex: `prato-de-comida.png`, `cachorro_collie.png`, `curriculo_elielson_nascimento_ramos.txt`, `desempenho_estudantes_enem.csv`, `social_media_festa.png`).

**Estrutura dos Arquivos:**

O repositório contém os seguintes scripts Python:

1. **`hello_gemini.py`:**  Este script demonstra uma simples interação com a API, enviando o prompt "Hello, Gemini!" e imprimindo a resposta do modelo.

   ```python
   import google.generativeai as genai
   import os

   genai.configure(api_key=os.environ["GEMINI_API_KEY"])
   model = genai.GenerativeModel("gemini-1.5-flash")

   prompt = model.generate_content("Hello, Gemini!")

   print(prompt.text)
   ```

2. **`interactive_terminal_ai.py`:** Este script cria um chatbot simples que interage com o usuário, enviando prompts para o modelo Gemini e imprimindo as respostas até que o usuário digite "sair".

   ```python
    import google.generativeai as genai
    import os

    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = input("Em que posso ajuda-lo(a)? ")

    response = model.generate_content(prompt)

    while prompt != "sair":
        response = model.generate_content(prompt)
        print(response.text)
        print("*Digite sair para encerrar a qualquer momento*")
        prompt = input("Em que posso ajuda-lo(a)? ")
   ```

3. **`calorie_estimate.py`:** Este script analisa uma imagem de um prato de comida (`prato-de-comida.png`), solicitando ao modelo que estime a quantidade de calorias e individualize o valor calórico de cada ingrediente.

   ```python
    import google.generativeai as genai
    import os

    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-1.5-flash")

    food_image = genai.upload_file(path="prato-de-comida.png")

    prompt = """
    Com base na imagem, calcule o valor aproximado do prato
    em calorias aproximadas e individualize o valor de cada
    ingrediente.
    """

    response = model.generate_content([food_image, prompt])

    print(response.text)
   ```

4. **`dog_breed_identifier.py`:** Este script utiliza uma imagem de um cão (`cachorro_collie.png`) como entrada para identificar a raça e suas características.

   ```python
    import google.generativeai as genai
    import os

    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-1.5-flash")

    dog_image = genai.upload_file(path="cachorro_collie.png")

    prompt = """
    Com base na imagem, me informe qual a raça do cão e suas
    caracteristicas.
    """

    response = model.generate_content([dog_image, prompt])

    print(response.text)
   ```

5. **`cv_consultant_and_enhancer.py`:** Este script usa um currículo em um arquivo de texto (`curriculo_elielson_nascimento_ramos.txt`) como entrada. O modelo age como um especialista em currículos, sugerindo melhorias e retornando uma versão aprimorada.

   ```python
    import google.generativeai as genai
    import os

    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    
    model = genai.GenerativeModel("gemini-1.5-flash")

    with open("curriculo_elielson_nascimento_ramos.txt", "r") as file:
        curriculo = file.read()

    prompt = f"""
    Você é um especialista na melhoria de currículo, deixando o mesmo
    perfeito para contratação, aumentando exponencialmente o potencial, avalie o currículo, retorne ele com as melhorias aplicadas e dê as sugestões necessarias.
    Eis o meu currículo: \n{curriculo}
    """

    response = model.generate_content(prompt)

    print(response.text)
   ```

6. **`spreadsheet_report_generator.py`:** Este script analisa uma planilha CSV (`desempenho_estudantes_enem.csv`) contendo notas de estudantes do ENEM, gerando um relatório e sugestões para melhorar o desempenho futuro.

   ```python
    import google.generativeai as genai
    import os

    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    modal = genai.GenerativeModel("gemini-1.5-flash")

    spread_sheets = genai.upload_file(path="desempenho_estudantes_enem.csv")

    prompt = """
    Atráves da planilha fornecida com as notas dos estudantes,
    crie um relatório baseado nas informações dê sugestões para
    ajudar nas notas em exames futuros.
    """

    response = modal.generate_content([prompt, spread_sheets])

    print(response.text)
   ```

7. **`description_generator_for_social_media_posts.py`:** Este script analisa uma imagem (`social_media_festa.png`) e gera uma legenda para redes sociais, incluindo uma descrição acessível para deficientes visuais.

   ```python
    import google.generativeai as genai
    import os

    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")

    image_for_post = genai.upload_file(path="social_media_festa.png")

    prompt = """
    Analize toda imagem e crie uma descrição para redes sociais
    e descrição para deficiêntes visuais com no máximo 200 caracteres.
    """

    response = model.generate_content([prompt, image_for_post])

    print(response.text)
   ```

**Como Executar:**

1. Certifique-se de ter todos os pré-requisitos instalados.

2. Configure a variável de ambiente `GEMINI_API_KEY` com sua chave de API.

3. Execute cada script individualmente usando o interpretador Python: `python <nome_do_script>.py`

**Observações:**

* As respostas do modelo Gemini podem variar a cada execução.
* A qualidade das respostas depende da clareza e precisão dos prompts fornecidos.
* O consumo da API Gemini pode gerar custos, dependendo do uso.  Monitore seu consumo.

Este README fornece uma visão geral concisa e informativa dos scripts presentes neste repositório.  Cada script é auto-explicativo e bem comentado.
