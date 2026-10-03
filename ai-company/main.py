import os
from google import genai
from google.genai import types

client = genai.Client()

# 1. マーケティング部
marketing_instruction = "あなたはマーケティング部長です。テーマについて、ターゲットの悩みやトレンドキーワードを3つ厳選して分析レポートを作ってください。"
theme = "AI副業・自動化ツール"

marketing_response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=f"テーマ: 「{theme}」について市場調査を行ってください。",
    config=types.GenerateContentConfig(system_instruction=marketing_instruction)
)
marketing_report = marketing_response.text

# 2. コンテンツ作成部
content_instruction = "あなたは優秀なライターです。マーケティング部のレポートを元に、ブログやSNSに使える記事を作ってください。キーワードを必ず含めること。"
content_response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=f"レポート:\n\n{marketing_report}",
    config=types.GenerateContentConfig(system_instruction=content_instruction)
)
final_product = content_response.text

# 3. 成果物をテキストファイルとして保存する
with open("result_article.txt", "w", encoding="utf-8") as f:
    f.write(final_product)

print("成果物（result_article.txt）の作成が完了しました。")
