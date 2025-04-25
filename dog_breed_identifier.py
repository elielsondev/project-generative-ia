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
