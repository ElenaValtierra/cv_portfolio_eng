from pathlib import Path
p = Path(r'c:\Users\Elena\Documents\Portfolio\cv_portfolio_eng\index.html')
text = p.read_text(encoding='utf-8')
new = text.replace('href="/images/','href="images/').replace('src="/images/','src="images/').replace('url(/images/','url(images/').replace("href='/images/","href='images/").replace("src='/images/","src='images/").replace("url('/images/","url('images/")
p.write_text(new, encoding='utf-8')
print('ok')
