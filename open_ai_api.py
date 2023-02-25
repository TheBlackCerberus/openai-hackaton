import openai
import requests
from fastapi import FastAPI, Path
from fastapi import FastAPI
from pydantic import BaseModel
import base64


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



class Prompt(BaseModel):
    text: str



@app.post("/items/")
async def create_item(prompt: Prompt):
    # code = "RXhwbGFpbiB0aGUgY29kZQoKLy8gVGltZTogTyhsb2cgbikKY29uc3QgYmluYXJ5U2VhcmNoID0gKGFyciwgdGFyZ2V0KSA9PiB7CiByZXR1cm4gYmluYXJ5U2VhcmNoSGVscGVyKGFyciwgdGFyZ2V0LCAwLCBhcnIubGVuZ3RoIC0gMSk7Cn07Cgpjb25zdCBiaW5hcnlTZWFyY2hIZWxwZXIgPSAoYXJyLCB0YXJnZXQsIHN0YXJ0LCBlbmQpID0+IHsKIGlmIChzdGFydCA+IGVuZCkgewogICByZXR1cm4gZmFsc2U7CiB9CiBsZXQgbWlkID0gTWF0aC5mbG9vcigoc3RhcnQgKyBlbmQpIC8gMik7CiBpZiAoYXJyW21pZF0gPT09IHRhcmdldCkgewogICByZXR1cm4gbWlkOwogfQogaWYgKGFyclttaWRdIDwgdGFyZ2V0KSB7CiAgIHJldHVybiBiaW5hcnlTZWFyY2hIZWxwZXIoYXJyLCB0YXJnZXQsIG1pZCArIDEsIGVuZCk7CiB9CiBpZiAoYXJyW21pZF0gPiB0YXJnZXQpIHsKICAgcmV0dXJuIGJpbmFyeVNlYXJjaEhlbHBlcihhcnIsIHRhcmdldCwgc3RhcnQsIG1pZCAtIDEpOwogfQp9OwoKY29uc3QgYXJyID0gWzEsIDIsIDMsIDQsIDUsIDYsIDcsIDgsIDksIDEwXTsKY29uc3QgdGFyZ2V0ID0gNTsKY29uc29sZS5sb2coYmluYXJ5U2VhcmNoKGFyciwgdGFyZ2V0KSk7"
    decoded_prompt = str(base64.b64decode(prompt.text).decode('utf-8'))
    # return item.name
    API_KEY = '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'

    openai.api_key = API_KEY
    model = 'text-davinci-003'

    response = openai.Completion.create(
        prompt=decoded_prompt,
        model = model
    )

    return response.choices[0].text


a=2

# test = requests.post('http://127.0.0.1:8000/items/', json={"text":"how are you today?"})


