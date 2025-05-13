import hashlib
import pickle
import subprocess

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from a Flask app with demo vulnerabilities!"

# === INTENTIONALLY INSECURE CODE FOR DEMO ===
password = "admin123"                   # B105: Hardcoded password
eval("2 + 2")                           # B307: Use of eval()
subprocess.Popen("ls", shell=True)     # B602: shell=True
assert True                             # B101: Use of assert
data = pickle.loads(b"cos\nsystem\n(S'ls'\ntR.")  # B301: Unsafe pickle usage
hashlib.md5(b"1234")                    # B303: Weak cryptography

if __name__ == '__main__':
    app.run(debug=True)                # B201: Debug mode enabled
