import os
import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("API_KEY_OPENAI"))

def generar_cuidados_por_ia(tratamiento):
    prompt = f"Dado el tratamiento odontológico: '{tratamiento}', sugiere cuidados posteriores específicos para el paciente."
    try:
        respuesta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente dental profesional."},
                {"role": "user", "content": prompt}
            ]
        )
        return respuesta.choices[0].message.content

    except Exception as e:
        return f"⚠️ No se pudieron generar los cuidados con IA: {e}"
