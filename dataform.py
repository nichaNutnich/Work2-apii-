from flask import Flask, request

app = Flask(__name__)

@app.route('/api/post', methods=['POST'])
def post_data():
    # รับข้อมูลจาก form data
    form_data = request.form

    # ตรวจสอบว่ามีข้อมูลที่ถูกส่งมาหรือไม่
    if not form_data:
        return 'No form data was provided', 400

    # พิมพ์ข้อมูลที่ได้รับ
    print("Received form data:")
    for key, value in form_data.items():
        print(f"{key}: {value}")

    # ส่งข้อความยืนยันกลับไป
    return 'Received form data', 200

if __name__ == '__main__':
    app.run(debug=True, port=123)
