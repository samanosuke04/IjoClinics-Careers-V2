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