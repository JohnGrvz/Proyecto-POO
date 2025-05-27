import openai
openai.api_key="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"
try:
    response = openai.models.list()
    print("✅ Tu API key funciona correctamente.")
except openai.error.AuthenticationError:
    print("❌ Tu API key es inválida o fue desactivada.")