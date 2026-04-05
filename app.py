from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

FIREBASE_URL = "https://event-reg-74653-default-rtdb.asia-southeast1.firebasedatabase.app/registrations.json"


@app.route('/')
def index():
    success = request.args.get("success")
    return render_template("index.html", success=success)


@app.route('/register', methods=['POST'])
def register():

    name = request.form.get('name')
    enrollment = request.form.get('enrollment')
    ku_id = request.form.get('ku_id')
    student_class = request.form.get('class')
    event_type = request.form.get('event_type')
    event_name = request.form.get('event_name')

    if not name or not enrollment or not ku_id or not student_class or not event_name:
        return "❌ Please fill all fields"

    data = {
        "name": name,
        "enrollment": enrollment,
        "ku_id": ku_id,
        "class": student_class,
        "event_type": event_type,
        "event_name": event_name
    }

    response = requests.post(FIREBASE_URL, json=data)

    if response.status_code == 200:
        return redirect(url_for('index', success="1"))
    else:
        return f"❌ Error: {response.text}"


if __name__ == '__main__':
    print("Server started at http://localhost:5000")
    app.run(debug=True)
