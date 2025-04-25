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
