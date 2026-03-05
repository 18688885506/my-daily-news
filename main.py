import google.generativeai as genai
import json
import os
from datetime import datetime

print("--- [1] 脚本已启动 ---")

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
print("错误：没有找到 API KEY")
exit(1)

try:
print("--- [2] 正在连接 AI... ---")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

except Exception as e:
print(f"错误信息: {str(e)}")
