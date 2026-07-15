import os
from docx import Document

target_folder = "自動化テストフォルダ"
# ひな形にするファイル
template_path = os.path.join(target_folder, "Pythonで作った書類.docx")
# 書き換えた後の新しいファイル
output_path = os.path.join(target_folder, "【完成】本日の報告書.docx")

print("ーーー Wordファイルの文字置き換え（置換）を開始します ーーー")

try:
    # 1. ひな形となるWordファイルを読み込む
    doc = Document(template_path)
    
    # 2. 置き換えたい「元の文字」と「新しい文字」のルールを決める
    replace_rules = {
        "【日付】": "2026年6月30日",
        "【お名前】": "ka06_"
    }
    
    # 3. Wordのすべての段落を1行ずつチェックする
    for paragraph in doc.paragraphs:
        
        # 4. ルール（日付とお名前）を1つずつ当てはめて調べる
        for old_text, new_text in replace_rules.items():
            
            # もし行の中に「【日付】」や「【お名前】」を見つけたら
            if old_text in paragraph.text:
                
                # 🌟【重要】文字を新しい文字（2026年6月30日 や ka06_）に置き換える！
                paragraph.text = paragraph.text.replace(old_text, new_text)
                print(f"🔄 「{old_text}」 を 「{new_text}」 に書き換えました！")
                
    # 5. 書き換えた内容を、別名で新しく保存する
    doc.save(output_path)
    print(f"✨ 文字の置き換えが完了しました！➔ {output_path}")

except Exception as e:
    print(f"❌ エラーが発生しました: {e}")