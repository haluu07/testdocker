from flask import Flask, jsonify

app = Flask(__name__)

# Định nghĩa route mặc định
@app.route('/')
def home():
    return "Hello, Docker World!"

# Route API trả về dữ liệu JSON
@app.route('/api')
def api():
    return jsonify({
        "message": "This is a simple API endpoint",
        "status": "success"
    })

# Chạy ứng dụng trên cổng 5000
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
