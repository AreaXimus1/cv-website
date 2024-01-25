from flask import Flask, render_template, send_file
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/academic-portfolio")
def academia():
    return render_template("academic_portfolio.html")


@app.route("/academic-portfolio/wes-article")
def wes_article():
    return render_template("academic_portfolio/bitcoin.html")


@app.route("/academic-portfolio/dissertation")
def dissertation():
    return render_template("academic_portfolio/dissertation.html")


@app.route("/download_dissertation", methods=["POST"])
def download_dissertation():
    file_path = "static/portfolio_download/Max_Vorster_dissertation.pdf"
    return send_file(file_path, as_attachment=True)


@app.route("/academic-portfolio/health-inequalities")
def health_inequalities():
    return render_template("academic_portfolio/health_inequalities.html")


@app.route("/download_health-inequalities", methods=["POST"])
def download_health_inequalities():
    file_path = "static/portfolio_download/Max_Vorster_Health_Inequalities.pdf"
    return send_file(file_path, as_attachment=True)


@app.route("/academic-portfolio/wizz-air")
def wizz_air():
    return render_template("academic_portfolio/wizz_air.html")


@app.route("/download_wizz-air", methods=["POST"])
def download_wizz_air():
    file_path = "static/portfolio_download/Max_Vorster_Wizz_Air.pdf"
    return send_file(file_path, as_attachment=True)


@app.route("/python-portfolio")
def python():
    return render_template("python_portfolio.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
