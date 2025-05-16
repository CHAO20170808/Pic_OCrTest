from openai import OpenAI
import os
import pytesseract
from PIL import Image

# 設定 DEEPSEEK_API_KEY 金鑰 (從環境變數讀取)
deepseek_api_key = os.environ.get("DEEPSEEK_API_KEY")

# 圖片路徑
image_path = "C:/Users/agk32/Opencv_Test/1_Busin/Selected/3_20250514.jpg"

try:
    img = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(img, lang='chi_sim') # 指定語言為簡體中文，根據你的圖片內容調整
    print("提取到的文字:")
    print(extracted_text)
except FileNotFoundError:
    print(f"Error: Image not found at {image_path}")
    exit()
except Exception as e:
    print(f"Error during OCR: {e}")
    exit()

if deepseek_api_key:
    client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")

    prompt = f"""這是從名片圖片中識別出的文字：\n\n{extracted_text}\n\n請提取以下資訊，如果存在的話：

- 公司名稱：
- 公司地址：
- 名片人員姓名與職稱：
- QQ 號碼：
- 電話號碼：
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一個可以從名片文字中提取特定資訊的助理。"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )

    print("\nDeepSeek 的回應:")
    print(response.choices[0].message.content)

else:
    print("Error: DEEPSEEK_API_KEY environment variable not found. Please set it in your system.")