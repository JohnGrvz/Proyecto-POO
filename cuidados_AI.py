import os
import openai


client = openai.OpenAI(api_key="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")

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
