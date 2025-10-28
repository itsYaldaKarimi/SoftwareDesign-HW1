from flask import Flask, render_template_string

app = Flask(__name__)

profile = {
    "name": "Yalda Karimi",
    "student_number": "40113012004",
}

TEMPLATE = """
<!doctype html>
<html lang="fa" dir="rtl">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>پروفایل Yalda Karimi</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
      body { background: #E5B5FF; }
      .card { max-width: 680px; margin: 40px auto; border-radius: 12px; }
      .avatar { width: 96px; height: 96px; border-radius: 50%; background: linear-gradient(135deg,#6f42c1,#0d6efd); display:flex; align-items:center; justify-content:center; color:white; font-weight:700; font-size:32px; }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="card shadow-sm">
        <div class="card-body d-flex gap-4 align-items-center">
          <div class="avatar">YK</div>
          <div>
            <h3 class="card-title mb-1">{{ profile.name }}</h3>
            <p class="text-muted mb-2">Student Number: <strong>{{ profile.student_number }}</strong></p>
            
          </div>
        </div>
        <div class="card-footer text-muted small">Developer: Yalda Karimi </div>
      </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(TEMPLATE, profile=profile)


if __name__ == '__main__':
    app.run(debug=True)
    print("🚀 CI/CD working!")
