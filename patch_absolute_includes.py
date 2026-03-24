import os
import re
abs_header = 'https://elenavaltierra.com/header.html'
abs_footer = 'https://elenavaltierra.com/footer.html'
for root, dirs, files in os.walk('.'):
    for name in files:
        if name.lower().endswith('.html'):
            path = os.path.join(root, name)
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            text = re.sub(r"fetch\(\s*['\"](?:\.\./|\./)?header\.html['\"]\s*\)", f"fetch('{abs_header}')", text)
            text = re.sub(r"fetch\(\s*['\"](?:\.\./|\./)?footer\.html['\"]\s*\)", f"fetch('{abs_footer}')", text)
            text = re.sub(r"includeHtml\(\s*['\"]header\.html['\"]\s*,\s*['\"]header['\"]\s*\)", f"fetch('{abs_header}').then(r=>r.text()).then(t=>document.getElementById('header').innerHTML=t).catch(e=>console.error(e))", text)
            text = re.sub(r"includeHtml\(\s*['\"]footer\.html['\"]\s*,\s*['\"]footer['\"]\s*\)", f"fetch('{abs_footer}').then(r=>r.text()).then(t=>document.getElementById('footer').innerHTML=t).catch(e=>console.error(e))", text)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(text)
print('patched all html includes to absolute paths')

