import markdown,pdfkit

#קריאת תוכן הקובץ
with open("index.md", "r", encoding='utf-8') as f:
    md_text = f.read()
#md to html
html_text = markdown.markdown(md_text)

#יצירת קובץ PDF
pdfkit.from_string(html_text,'output-pdf.pdf')