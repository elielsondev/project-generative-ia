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
