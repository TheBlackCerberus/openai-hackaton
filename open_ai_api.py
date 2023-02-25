import openai

API_KEY = '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'

openai.api_key = API_KEY
model = 'text-davinci-003'

prompt = 'How big is the moon?'

response = openai.Completion.create(
    prompt=prompt,
    model=model
)

a=2


