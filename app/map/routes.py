"""Map page routes."""
from flask import Blueprint, jsonify, redirect, render_template, url_for

map_bp = Blueprint('map', __name__)

# Берега Камчатки: lat, lng, прогресс очистки (0–100)
SHORES = [
    {
        'id': 1,
        'name': 'Авачинская бухта',
        'lat': 53.05,
        'lng': 158.65,
        'pollution': 'Пластик, бытовые отходы',
        'progress': 72,
        'status': 'В работе',
    },
    {
        'id': 2,
        'name': 'Халактырский пляж',
        'lat': 52.98,
        'lng': 158.78,
        'pollution': 'Пластиковые бутылки, сети',
        'progress': 45,
        'status': 'В работе',
    },
    {
        'id': 3,
        'name': 'Бухта Русская',
        'lat': 52.87,
        'lng': 158.52,
        'pollution': 'Древесный мусор, пластик',
        'progress': 90,
        'status': 'Почти чисто',
    },
    {
        'id': 4,
        'name': 'Бухта Сараная',
        'lat': 52.92,
        'lng': 158.68,
        'pollution': 'Бытовые отходы',
        'progress': 30,
        'status': 'Требует очистки',
    },
    {
        'id': 5,
        'name': 'Усть-Камчатск',
        'lat': 56.23,
        'lng': 162.48,
        'pollution': 'Промысловый мусор, пластик',
        'progress': 15,
        'status': 'Требует очистки',
    },
    {
        'id': 6,
        'name': 'Октябрьский',
        'lat': 52.35,
        'lng': 156.53,
        'pollution': 'Сетки, пластик',
        'progress': 55,
        'status': 'В работе',
    },
    {
        'id': 7,
        'name': 'Петропавловск-Камчатский (набережная)',
        'lat': 53.02,
        'lng': 158.65,
        'pollution': 'Бытовой мусор',
        'progress': 85,
        'status': 'Почти чисто',
    },
    {
        'id': 8,
        'name': 'Бухта Вилючинская',
        'lat': 52.70,
        'lng': 158.40,
        'pollution': 'Пластик, древесный мусор',
        'progress': 10,
        'status': 'Требует очистки',
    },
]


@map_bp.route('/')
def home():
    return redirect(url_for('map.map_page'))


@map_bp.route('/map')
def map_page():
    return render_template('map/index.html', shores=SHORES)


@map_bp.route('/api/shores')
def shores_api():
    """JSON API со списком берегов и прогрессом очистки."""
    return jsonify(SHORES)
