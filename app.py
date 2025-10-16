from flask import Flask
from routes.students import students_bp
from routes.subjects import subjects_bp
from routes.students_subjects import students_subjects_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(students_bp, url_prefix='/students')
app.register_blueprint(subjects_bp, url_prefix='/subjects')
app.register_blueprint(students_subjects_bp, url_prefix='/students_subjects')

@app.route('/')
def home():
    return {"message": "Welcome to the Flask API 🎓"}

if __name__ == '__main__':
    app.run(debug=True)
