import logging

from flask import Flask, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/")
def index():
    return "OK", 200


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    # This is the message the OpenShift application logs need to show
    # (Question 8 of the final project asks for "SERVICERUNNING" on port 8000).
    logger.info("SERVICERUNNING")
    app.run(host="0.0.0.0", port=8000)
