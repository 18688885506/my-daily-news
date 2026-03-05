from google import genai
import json, os
from datetime import datetime

print("--- [1] 使用新版 SDK 启动 ---")

# 配置客户端
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
model_id = "gemini-2.0-flash" # 使用最新的 2.0 免费模型

data = {"date": datetime.now().strftime("%Y-%m-%d"), "categories": []}
cats = ["科技", "金融", "生活", "娱乐"]

for c in cats:
    print(f"正在生成 {c}...")
    # 新版调用方式
    response = client.models.generate_content(
        model=model_id, 
        contents=f"Summarize {c} news in JSON: title, summary, prediction. No markdown."
    )
    
    # 清理并解析数据
    txt = response.text.replace('```json', '').replace('```', '').strip()
    data["categories"].append(json.loads(txt))

# 保存文件
with open("daily_report.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("--- [2] 任务大功告成 ---")
