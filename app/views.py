from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from datetime import datetime

from .models import Entry
from . import db


bp = Blueprint('main', __name__)

@bp.route('/')
def calendar():
    # 월간 달력
    return render_template('calendar_month.html')

@bp.route('/week/<date_str>')
def week_view(date_str):
    # 주간 달력 – URL에서 받은 날짜를 초기 주간 날짜로 사용
    return render_template('calendar_week.html', initial_date=date_str)

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
