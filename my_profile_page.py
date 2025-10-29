from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="utf-8">
  <title>صفحه شخصی من</title>
  <style>
    body {
      font-family: system-ui, sans-serif;
      background-color: #f5f6fa;
      max-width: 700px;
      margin: 50px auto;
      padding: 30px;
      border-radius: 20px;
      box-shadow: 0 0 15px rgba(0,0,0,0.1);
      background: white;
      line-height: 1.8;
    }
    h1 {
      color: #2d3436;
      text-align: center;
    }
    p {
      font-size: 1.1rem;
    }
    .label {
      font-weight: bold;
      color: #0984e3;
    }
  </style>
</head>
<body>
  <h1>👋 درباره من</h1>
  <p><span class="label">نام و نام خانوادگی:</span> هانیه گلشن</p>
  <p><span class="label">سن:</span> ۲۴ سال</p>
  <p><span class="label">رشته تحصیلی:</span> علوم کامپیوتر</p>
  <p><span class="label">ایمیل:</span> haniegolshan@gmail.com</p>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
