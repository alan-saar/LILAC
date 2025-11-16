#from openai import OpenAI # new api
import openai

# new api. Not supported by LILAC
# client = OpenAI(api_key="SUA_API_KEY_AQUI")
#
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo-0613",
#     messages=[
#         {"role": "user", "content": "Olá! Responda apenas: OK"}
#     ]
# )
#
# print(response.choices[0].message.content)

#  old openAI api, utilized by LILAC

def get_openai_key(file_path):
    with open(file_path, 'r') as file:
        api_base = file.readline().strip()
        key_str = file.readline().strip()
    return api_base, key_str

openai.api_base, openai.api_key = get_openai_key('openai_key.txt')

response = openai.ChatCompletion.create(
    # model="gpt-3.5-turbo-0613", # deprecated
    model="gpt-3.5-turbo-0125", # deprecated
    messages=[
        {"role": "user", "content": "Teste rápido: diga OK."}
    ]
)

print(response["choices"][0]["message"]["content"])

