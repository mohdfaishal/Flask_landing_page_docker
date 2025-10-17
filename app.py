from flask import Flask, render_template, jsonify
from models import db, User
import os

app = Flask(__name__)

# PostgreSQL connection URL
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/users')
def list_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

@app.route('/add/<name>')
def add_user(name):
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message=f"User '{name}' added successfully!")

@app.route('/delete/<name>', methods=['DELETE'])
def delete_user(name):
    user = User.query.filter_by(name=name).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify(message=f"User '{name}' deleted successfully!")
    else:
        return jsonify(message=f"User '{name}' not found."), 404
    
@app.route('/update/<int:id>/<new_name>', methods=['PUT', 'GET'])
def update_user(id, new_name):
    user = User.query.get(id)
    if user:
        user.name = new_name
        db.session.commit()
        return jsonify(message=f"User ID {id} updated to '{new_name}'!")
    else:
        return jsonify(error=f"User with ID {id} not found"), 404

# Auto-create tables on startup
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=5001, debug=debug_mode)
