from flask import Flask, request, jsonify
import resume_analyzer

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Analyzes a resume and returns a JSON object with the results.

    Args:
        request: The HTTP request object.

    Returns:
        A JSON object with the results of the resume analysis.
    """

    resume = request.files["resume"]
    results = resume_analyzer.analyze(resume)

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)