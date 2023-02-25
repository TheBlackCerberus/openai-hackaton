import openai


from fastapi import FastAPI, Path

app = FastAPI()

@app.get(r'/openai/{prompt}')
def code_review(prompt: str = Path(None, description='Pass the item_id of the item you want to view') ):
    API_KEY = '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'

    openai.api_key = API_KEY
    model = 'text-davinci-003'

    response = openai.Completion.create(
        prompt=prompt,
        model=model
    )

    return response.choices[0].text


code_review('How big is the moon?')
a=2

