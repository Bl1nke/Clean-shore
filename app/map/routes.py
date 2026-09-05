"""Map page routes."""
from flask import Blueprint, jsonify, redirect, render_template, url_for

map_bp = Blueprint('map', __name__)

# Берега Камчатки: lat, lng, прогресс очистки (0–100)
SHORES = [
    {
        'id': 2,
        'name': 'Халактырский пляж',
        'lat': 53.09,
        'lng': 159.03,
        'pollution': 'Пластиковые бутылки, сети',
        'progress': 45,
        'status': 'В работе',
    },
    {
        'id': 3,
        'name': 'Бухта Русская',
        'lat': 52.89,
        'lng': 158.50,
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
        'id': 7,
        'name': 'Петропавловск-Камчатский (набережная)',
        'lat': 53.02,
        'lng': 158.65,
        'pollution': 'Бытовой мусор',
        'progress': 85,
        'status': 'Почти чисто',
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
