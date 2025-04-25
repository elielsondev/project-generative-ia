import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

with open("curriculo_elielson_nascimento_ramos.txt", "r") as file:
    curriculo = file.read()

prompt = f"""
Você é um especialista na melhoria de currículo, deixando o mesmo
perfeito para contratação, aumentando exponencialmente o potencial,
avalie o currículo, retorne ele com as melhorias aplicadas e dê as
sugestões necessarias.Eis o meu currículo: \n{curriculo}
"""

response = model.generate_content(prompt)

print(response.text)
