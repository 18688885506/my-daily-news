import google.generativeai as genai
import json, os
from datetime import datetime

# 1. 基础配置
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. 准备数据容器
data = {"date": datetime.now().strftime("%Y-%m-%d"), "categories": []}
cats = ["科技", "金融", "生活", "娱乐"]

# 3. 运行核心逻辑 (请确保下面这三行每一行开头都有 4 个空格)
for c in cats:
    print(f"正在生成 {c}...")
    res = model.generate_content(f"Summarize {c} news in JSON: title, summary, prediction. No markdown.")
    data["categories"].append(json.loads(res.text.strip().replace('```json', '').replace('```', '')))

# 4. 保存结果
with open("daily_report.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("--- SUCCESS ---")
