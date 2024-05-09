from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/post', methods=['POST'])
def post_data():
    # ตรวจสอบว่าคำขอเป็น JSON หรือไม่
    if request.is_json:
        # รับ JSON body จากคำขอ
        data = request.get_json()
        # ดึงอายุจาก JSON body
        age = data.get('age')
        if age is None:
            return 'Age is required', 400
        # พิมพ์ข้อมูล JSON และอายุที่ได้รับ
        print("Received JSON data:", data)
        print("Age:", age)
        # เตรียมข้อความสำหรับส่งคืน
        response_message = "Received JSON data with age: " + str(age)
        # ส่งคำตอบกลับไปพร้อมกับข้อความ #จะไปขึ้นในpostman
        return jsonify({'message': response_message}), 200
    else:
        return 'Request must be JSON', 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
