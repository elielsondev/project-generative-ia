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
