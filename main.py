import google.generativeai as genai
import json
import os
from datetime import datetime

print("--- [1] START ---")
api_key = os.environ.get("GEMINI_API_KEY")

强制配置
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
cats = ["科技", "金融", "生活", "娱乐"]
data = {"date": datetime.now().strftime("%Y-%m-%d"), "categories": []}

for c in cats:
print(f"Doing {c}...")
res = model.generate_content(f"JSON format: title, summary, prediction. Topic: {c} news today.")
txt = res.text.replace("json", "").replace("", "").strip()
data["categories"].append(json.loads(txt))

with open("daily_report.json", "w", encoding="utf-8") as f:
json.dump(data, f, ensure_ascii=False, indent=4)

print("--- [2] SUCCESS ---")
