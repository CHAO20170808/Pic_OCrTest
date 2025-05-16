import google.generativeai as genai
import cv2
from PIL import Image
import io
import os

# 設定 Gemini API 金鑰 (從環境變數讀取)
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# 載入圖片
image_path = "C:/Users/agk32/Opencv_Test/1_Busin/Selected/3_20250514.jpg"  # 替換為你的圖片路徑
img_cv = cv2.imread(image_path)
if img_cv is not None:
    img_pil = Image.fromarray(cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB))
    byte_stream = io.BytesIO()
    img_pil.save(byte_stream, format="JPEG")
    image_data = byte_stream.getvalue()
else:
    print(f"Error: Could not read the image at {image_path}")
    exit()

# 初始化 Gemini Pro Vision 模型
model = genai.GenerativeModel('gemini-1.5-flash')

# 準備更詳細的提示和圖片資料
prompt = """
This image contains a business card. Please identify and extract the following information if present:

- Company Name
- Phone Number(s)
- Address(es)
- QQ Number(s)
- General Manager (or equivalent title) and their name

Provide the extracted information in a clear and structured format.
"""

contents = [
    prompt,
    {"mime_type": "image/jpeg", "data": image_data}
]

# 產生回應
response = model.generate_content(contents)

if response.parts:
    print("Extracted Information:")
    print(response.parts[0].text)
else:
    print("No response from the model.")