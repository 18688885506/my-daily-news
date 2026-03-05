from google import genai
import json, os, time
from datetime import datetime

print("--- [开始运行终极修复版] ---")

try:
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    # 使用 1.5-flash，它是目前最稳定的免费选择
    model_id = "gemini-1.5-flash" 

    data = {"date": datetime.now().strftime("%Y-%m-%d"), "categories": []}
    cats = ["科技", "金融", "生活", "娱乐"]

    for c in cats:
        print(f"正在为【{c}】请求 AI...")
        success = False
        for attempt in range(3): # 失败自动重试3次
            try:
                response = client.models.generate_content(
                    model=model_id, 
                    contents=f"Summarize {c} news in JSON: title, summary, prediction. No markdown, no formatting."
                )
                txt = response.text.strip()
                # 强力清理所有非 JSON 字符
                if "{" in txt and "}" in txt:
                    txt = txt[txt.find("{"):txt.rfind("}")+1]
                
                item = json.loads(txt)
                data["categories"].append(item)
                print(f"✅ {c} 成功")
                success = True
                break 
            except Exception as e:
                print(f"⚠️ {c} 第 {attempt+1} 次尝试失败: {e}")
                time.sleep(5) # 等5秒再试
        
        if not success:
            # 如果 AI 实在不给力，给一个保底显示，防止网页报错
            data["categories"].append({
                "title": f"今日{c}资讯",
                "summary": "AI 正在思考中，请稍后再试。",
                "prediction": "内容更新中。"
            })

    with open("daily_report.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("--- [任务全部完成] ---")

except Exception as global_e:
    print(f"❌ 全局错误: {global_e}")
