from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, save_form_to_db

app = Flask(__name__)

@app.route("/")
def start_web():
  jobs = load_jobs_from_db()
  return render_template("main.html", jobs = jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_jobpage(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job = job)

@app.route("/job/<id>/apply", methods = ["post"])
def application_submitted(id):
  data = request.form
  job = load_job_from_db(id)
  save_form_to_db(id, data)
  return render_template('application_submitted.html', application = data, job=job)
  

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
