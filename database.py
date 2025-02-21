from sqlalchemy import create_engine, text
import os

cert_path = "certs/isrgrootx1.pem"

connection_string = os.environ['DB_CONNECTION_STRING']

connect_args = {
    "ssl_verify_cert": True,
    "ssl_verify_identity": True,
    "ssl_ca": str(cert_path)
}

engine = create_engine(connection_string, connect_args=connect_args)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('select * from jobs'))
        jobs = []
        for row in result:
            jobs.append(row._asdict())
        return jobs

def load_job_from_db(job_id):
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM jobs WHERE id = :val'), {'val':job_id})
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()

def save_form_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO application (job_id, full_name, birthdate, address, resume_link) VALUES (:job_id, :full_name, :birthdate, :address, :resume_link)")
        conn.execute(query, 
                     {'job_id': job_id,'full_name': data['full_name'], 'birthdate': data['date_of_birth'], 'address': data['address'], 'resume_link': data['resume_link']})
        conn.commit()