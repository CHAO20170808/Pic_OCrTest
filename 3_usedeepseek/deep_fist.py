# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
import os

# 設定 DEEPSEEK_API_KEY 金鑰 (從環境變數讀取)
#genai.configure(api_key=os.environ.get("Deepseek_API_KEY"))
deepseek_api_key = os.environ.get("DEEPSEEK_API_KEY")
"""if deepseek_api_key:
client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)

"""

if deepseek_api_key:
    client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=False
    )

    print(response.choices[0].message.content)

else:
    print("Error: DEEPSEEK_API_KEY environment variable not found. Please set it in your system.")