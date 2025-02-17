from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {"title": "Data Analyst","location": "Bengaluru, India","salary": "MYR 4,000"},
  {"title": "Data Scientist","location": "Delhi, India","salary": "MYR 3,000"},
  {"title": "Frontend Engineer","location": "Remote","salary": "MYR 1,000"},
  {"title": "Backend Engineer","location": "San Francisco, USA","salary": "USD 1,500"}
]

@app.route("/")
def hello():
  return render_template("main.html", jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
