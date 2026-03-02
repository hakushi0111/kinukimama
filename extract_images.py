import re, base64, os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

counter = {}
os.makedirs('images', exist_ok=True)

def replace_b64(match):
    mime = match.group(1)
    b64  = match.group(2)
    ext  = mime.split('/')[1].split(';')[0]
    ext  = 'jpg' if ext == 'jpeg' else ext
    counter[ext] = counter.get(ext, 0) + 1
    filename = f"images/img_{ext}_{counter[ext]:03d}.{ext}"
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(b64))
    print(f"  保存: {filename}")
    return f'src="{filename}"'

new_html = re.sub(r'src="data:(image/[^;]+);base64,([^"]+)"', replace_b64, html)

with open('index_new.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"\n完了！")
print(f"元のHTMLサイズ: {len(html):,} 文字")
print(f"新HTMLサイズ:   {len(new_html):,} 文字")
