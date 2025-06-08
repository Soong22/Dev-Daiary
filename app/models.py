from . import db

class Entry(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    # user_id: MVP 단계에선 하드코딩된 값(1)으로 사용
    user_id = db.Column(db.Integer, default=1, nullable=False)
    date    = db.Column(db.Date, nullable=False)
    title   = db.Column(db.String(128), nullable=False)
    kind    = db.Column(db.Enum('auto', 'manual'), default='manual')
    source  = db.Column(db.String(64))
    content  = db.Column(db.Text)
