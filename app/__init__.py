import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, 
                template_folder="templates",
                static_folder="static")
    # 개발 편의를 위해 SQLite 사용 (나중에 MySQL URI로 바꾸세요)
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        os.getenv('DATABASE_URL', 'sqlite:///dev_diary.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'replace-with-a-secure-key'

    db.init_app(app)

    # 블루프린트 등록
    from .views import bp as main_bp
    app.register_blueprint(main_bp)

    # DB 파일이 없으면 생성
    with app.app_context():
        db.create_all()

    return app
