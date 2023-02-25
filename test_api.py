# write me an example test for open_ai_api.py

# write a test for OpenAI API connection
import openai
import pytest

API_KEY = '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'

# write a test for OpenAI API connection
def test_openai_api_connection():
    openai.api_key = API_KEY
    model = 'text-davinci-003'

    prompt = 'How big is the moon?'

    response = openai.Completion.create(
        prompt=prompt,
        model=model
    )

    assert response.status_code == 200
    