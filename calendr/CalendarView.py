from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from datetime import datetime

from calendr.Database import get_db

bp = Blueprint('calendr', __name__, url_prefix='/calendr')

@bp.route('/GetEvents', methods=('GET', 'POST'))
def get_events():
    json_data = request.get_json()
    user_id = json_data['user_id']
    start = json_data['start']
    end = json_data['end']

    db = get_db()

    event_list = db.execute('SELECT * FROM event WHERE user_id = ? AND start_time < ? AND end_time > ?',
                            (user_id, end, start)).fetchall()

    to_return = [{'name': row['name'],
                  'day': datetime.strptime(row['start_time'], "%Y-%m-%d %H:%M:%S").weekday(),
                  'start': datetime.strptime(row['start_time'], "%Y-%m-%d %H:%M:%S").hour,
                  'end': datetime.strptime(row['end_time'], "%Y-%m-%d %H:%M:%S").hour} for row in event_list]

    #event_list = [dict(zip(row.keys(), row)) for row in event_list]

    return jsonify(to_return)
