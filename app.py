from flask import Flask, redirect, request
import os

app = Flask(__name__)

PYTHONANYWHERE_URL = "https://privacypolicyanalyzertamuct.pythonanywhere.com/"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def redirect_to_pythonanywhere(path):
    """Redirect visitors to the corresponding path on PythonAnywhere."""
    target = PYTHONANYWHERE_URL.rstrip("/")
    if path:
        target += "/" + path
    if request.query_string:
        target += "?" + request.query_string.decode("utf-8")
    return redirect(target, code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
