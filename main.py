import concurrent.futures
import flask
from flask import Flask, jsonify
from google.cloud import bigquery

app = flask.Flask(__name__)
bigquery_client = bigquery.Client()

@app.route("/json")
def get_patients():
    query_job = bigquery_client.query(
        """
        SELECT
            id,
            name,
            birth_date,
            gender
        FROM `projetocc-452811.Projeto.pacientes`
        ORDER BY id ASC
        LIMIT 10
        """
    )

    results = query_job.result()  # Espera a conclusão da consulta

    data = [
        {"id": row.id, "name": row.name, "birth_date": row.birth_date, "gender": row.gender}
        for row in results
    ]

    return jsonify(data)  # Retorna os resultados como JSON

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

