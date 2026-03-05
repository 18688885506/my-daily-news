import google.generativeai as genai
import json
import os
from datetime import datetime

# 1. 拿钥匙开门 (读取环境变量中的 API Key)
GOOGLE_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 召唤 AI (使用免费且速度快的 Flash 模型)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. 准备格式
categories = ["科技", "金融", "生活健康", "娱乐八卦"]
report_data = {
    "date": datetime.now().strftime("%Y-%m-%d"),
    "categories": []
}

# 4. 让 AI 开始按类别写简报
for cat in categories:
    prompt = f"""
    你是一个资深资讯主编。请根据你的知识库，总结今天（或近期）关于【{cat}】领域的最新核心动态（约80字），并给出一条相关的趋势预测或行动建议（约50字）。
    必须严格返回以下 JSON 格式，不要包含任何其他多余的文字或 markdown 符号：
    {{"title": "{cat}", "summary": "你的总结内容", "prediction": "你的建议内容"}}
    """
    
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        # 清理可能出现的代码块符号
        if text.startswith("```json"): text = text[7:-3]
        elif text.startswith("```"): text = text[3:-3]
        
        data = json.loads(text.strip())
        report_data["categories"].append(data)
    except Exception as e:
        print(f"生成 {cat} 失败，原因: {e}")
        report_data["categories"].append({"title": cat, "summary": "数据获取失败", "prediction": "无"})

# 5. 把 AI 写的报告存入文件，给网页读取
with open("daily_report.json", "w", encoding="utf-8") as f:
    json.dump(report_data, f, ensure_ascii=False, indent=4)

print("✅ 每日简报生成成功！")
