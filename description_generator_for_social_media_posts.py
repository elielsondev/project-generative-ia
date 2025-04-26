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
