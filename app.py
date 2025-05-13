from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from DevSec!"

@app.route('/echo', methods=['POST'])
def echo():
    data = request.form.get('data')  # Potential security issue: unsanitized input
    return f"Received: {data}"

if __name__ == '__main__':
    app.run(debug=False)
    #trigger bandit scan
# Trigger Bandit scan demo again
