from openai import OpenAI
client = OpenAI(api_key = "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")

response = client.responses.create(
    model="gpt-6-astra",
    input="what is coding ?",
)

print(response.output_text)