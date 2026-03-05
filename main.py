from google import genai
import json, os
from datetime import datetime

print("--- [1] 使用稳定版模型启动 ---")

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
# 换回 1.5-flash，这个配额最稳
model_id = "gemini-1.5-flash" 

data = {"date": datetime.now().strftime("%Y-%m-%d"), "categories": []}
cats = ["科技", "金融", "生活", "娱乐"]

for c in cats:
    print(f"正在生成 {c}...")
    try:
        response = client.models.generate_content(
            model=model_id, 
            contents=f"Summarize {c} news in JSON: title, summary, prediction. No markdown."
        )
        txt = response.text.replace('```json', '').replace('```', '').strip()
        data["categories"].append(json.loads(txt))
        print(f"✅ {c} 完成")
    except Exception as e:
        print(f"❌ {c} 失败: {e}")

with open("daily_report.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("--- [2] 任务大功告成 ---")
