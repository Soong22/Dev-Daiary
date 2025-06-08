from flask import Blueprint, render_template, jsonify
from .models import Entry
from . import db
from datetime import date

bp = Blueprint('main', __name__)

@bp.route('/')
def calendar():
    return render_template('calendar.html')

@bp.route('/api/events')
def api_events():
    # 모든 Entry를 불러와 FullCalendar 형태로 반환
    entries = Entry.query.all()
    events = []
    for e in entries:
        events.append({
            'id':    e.id,
            'title': e.title,
            'start': e.date.isoformat(),
            'color': '#4CAF50' if e.kind=='auto' else '#FFC107'
        })
    return jsonify(events)
