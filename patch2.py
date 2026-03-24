import os
import re
abs_header = "https://elenavaltierra.com/header.html"
abs_footer = "https://elenavaltierra.com/footer.html"

patterns = [
    (r"fetch\(\s*'\.\./header\.html'\s*\)", f"fetch('{abs_header}')"),
    (r"fetch\(\s*'\./header\.html'\s*\)", f"fetch('{abs_header}')"),
    (r"fetch\(\s*'header\.html'\s*\)", f"fetch('{abs_header}')"),
    (r"fetch\(\s*'\.\./footer\.html'\s*\)", f"fetch('{abs_footer}')"),
    (r"fetch\(\s*'\./footer\.html'\s*\)", f"fetch('{abs_footer}')"),
    (r"fetch\(\s*'footer\.html'\s*\)", f"fetch('{abs_footer}')"),
    (r"includeHtml\(\s*'header\.html'\s*,\s*'header'\s*\)", f"fetch('{abs_header}').then(r=>r.text()).then(t=>document.getElementById('header').innerHTML=t).catch(e=>console.error(e))"),
    (r"includeHtml\(\s*'footer\.html'\s*,\s*'footer'\s*\)", f"fetch('{abs_footer}').then(r=>r.text()).then(t=>document.getElementById('footer').innerHTML=t).catch(e=>console.error(e))"),
]

for root, _, filenames in os.walk('.'):
    for fn in filenames:
        if fn.lower().endswith('.html'):
            path = os.path.join(root, fn)
            text = open(path, 'r', encoding='utf-8').read()
            new = text
            for pat, repl in patterns:
                new = re.sub(pat, repl, new)
            if new != text:
                open(path, 'w', encoding='utf-8').write(new)
                print('patched', path)
print('done')

