# app/views.py
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from datetime import datetime

from .models import Entry
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def month_view():
    """월간 캘린더 뷰"""
    return render_template('calendar_month.html')

@bp.route('/week/<date_str>')
def week_view(date_str):
    """주간 캘린더 뷰"""
    return render_template('calendar_week.html', initial_date=date_str)

@bp.route('/entry/<date_str>', methods=['GET', 'POST'])
def entry_detail(date_str):
    """일별 상세 일지 뷰 & 저장"""
    # 문자열 → date 객체
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()

    # 기존 수기 일지 조회 (임시 user_id=1)
    entry = Entry.query.filter_by(user_id=1, date=date_obj, kind='manual').first()

    if request.method == 'POST':
        content = request.form.get('content', '').strip()
        if entry:
            entry.content = content
        else:
            entry = Entry(
                user_id=1,
                date=date_obj,
                title=f"{date_str} 일지",
                kind='manual',
                source='manual',
                content=content
            )
            db.session.add(entry)
        db.session.commit()
        return redirect(url_for('main.month_view'))

    return render_template('entry.html', entry=entry, date_str=date_str)

@bp.route('/api/events')
def api_events():
    """캘린더용 이벤트 JSON 반환"""
    entries = Entry.query.all()
    events = [{
        'id':    e.id,
        'title': e.title,
        'start': e.date.isoformat(),
        'color': '#4CAF50' if e.kind=='auto' else '#FFC107'
    } for e in entries]
    return jsonify(events)
