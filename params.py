from flask import Flask, request

app = Flask(__name__)

@app.route('/api/post', methods=['POST'])
def post_data():
    # รับพารามิเตอร์จากคำขอ POST
    params = request.args.to_dict(flat=False)

    # ตรวจสอบว่ามีพารามิเตอร์ที่ถูกส่งมาหรือไม่
    if not params:
        return 'No parameters were provided', 400

    # พิมพ์ข้อมูลที่ได้รับ
    print("Received parameters:")
    for key, values in params.items():
        for value in values:
            print(f"{key}: {value}")

    # ส่งข้อความยืนยันกลับไป
    return 'Received parameters', 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
