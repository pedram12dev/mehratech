from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}})

projects = [
    {"id": 1, "title": "detective", "image": "https://via.placeholder.com/300x150?text=Project+1"},
    {"id": 2, "title": "gymAI", "image": "https://via.placeholder.com/300x150?text=Project+2"},
    {"id": 3, "title": "tradeUP", "image": "https://via.placeholder.com/300x150?text=Project+3"},
    {"id": 4, "title": "hbcb", "image": "https://via.placeholder.com/300x150?text=Project+4"},
    {"id": 5, "title": "elrflernf", "image": "https://via.placeholder.com/300x150?text=Project+5"},

]

members = [
    {"id": 1, "name": "REZVAN ZAREE", "specialty": "محقق و برنامه نویس هوش مصنوعی", "photo": "https://via.placeholder.com/100?text=Rezvan"},
    {"id": 2, "name": "MOHAMAD SOLEYMANI", "specialty": "برنامه نویس پایتون و هوش مصنوعی", "photo": "https://via.placeholder.com/100?text=Mohamad"},
    {"id": 3, "name": "PEDRAM NAJAFI", "specialty": "برنامه‌نویس بک‌اند", "photo": "https://via.placeholder.com/100?text=Pedram"},
    {"id": 4, "name": "MEHRANA ABIAN", "specialty": "طراح رابط کاربری", "photo": "https://via.placeholder.com/100?text=Mehrana"},
    {"id": 4, "name": "HOSSEIN HOSSEINI", "specialty": "برنامه نویس فرانت اند", "photo": "https://via.placeholder.com/100?text=Hossein"},

]

consultations = []

@app.route('/api/projects')
def get_projects():
    return jsonify(projects)

@app.route('/api/members')
def get_members():
    return jsonify(members)

@app.route('/api/consultations', methods=['POST'])
def add_consultation():
    data = request.get_json()
    if not data:
        return jsonify({"error": "داده‌ای ارسال نشده"}), 400

    required_fields = ["firstName", "lastName", "phone", "subject"]
    for field in required_fields:
        if field not in data or not data[field].strip():
            return jsonify({"error": f"فیلد {field} الزامی است"}), 400

    consultations.append(data)
    print("New consultation added:", data)
    return jsonify({"message": "درخواست با موفقیت ثبت شد"}), 201

@app.route('/api/consultations', methods=['GET'])
def get_consultations():
    return jsonify(consultations)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
