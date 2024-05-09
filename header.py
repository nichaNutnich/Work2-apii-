from flask import Flask, request

app = Flask(__name__)

@app.route('/api/post', methods=['POST'])
def receive_headers():
    # รับ headers จาก request
    headers = request.headers

    # พิมพ์ค่า headers ทั้งหมดออกมา
    for key, value in headers.items():
        print(f'{key}: {value}')

    return 'Received headers', 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)