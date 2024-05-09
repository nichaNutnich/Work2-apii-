from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # สร้างข้อมูล JSON ตัวอย่าง
    data = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }

    # ส่งข้อมูล JSON กลับ
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
