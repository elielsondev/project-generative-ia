import google.generativeai as genai
import os


genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")


prompt = model.generate_content("Hello, Gemini!")


print(prompt.text)
