from django.conf import settings
import os
from openai import OpenAI
import openai

# def get_financial_advice(prompt):
#     openai.api_key = settings.OPENAI_API_KEY
#     response = openai.ChatCompletion.create(
#         model="gpt--3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are an helpful assistant."
#             },
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )
#     print(response)

def get_financial_advice(prompt):
    client = OpenAI(
        api_key=settings.OPENAI_API_KEY,
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "Salom nima?"
                        }
                    ]
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        response = response.choices[0].message.content

        return response
    except openai.APIConnectionError as e:
        print(f"Error: {e}")
    except openai.RateLimitError as e:
        print(f"Error: {e}")