from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# Stała grawitacyjna (m^3/kg/s^2)
G = 6.67430e-11

# Masa Słońca (kg)
m_s = 1.989e30

# Wartość jednostki astronomicznej (AU) w kilometrach
au_in_km = 149.6e6


@app.route('/distance/<planet_name>', methods=['GET'])
def calculate_distance(planet_name):
    planet_name = planet_name.capitalize()

    # Okres obiegu i przyspieszenie grawitacyjne dla poszczególnych planet
    planet_data = {
        'Merkury': {'period': 7600526, 'gravity': 3.7},
        'Wenus': {'period': 19413907, 'gravity': 8.87},
        'Ziemia': {'period': 31558118, 'gravity': 9.81},
        'Mars': {'period': 59354294, 'gravity': 3.71},
        'Jowisz': {'period': 374335776, 'gravity': 24.79},
        'Saturn': {'period': 929596608, 'gravity': 10.44},
        'Uran': {'period': 2650461899, 'gravity': 8.69},
        'Neptun': {'period': 5200418560, 'gravity': 11.15}
    }

    if planet_name not in planet_data:
        return jsonify({'error': 'Planeta nie znaleziona'}), 404

    planet_info = planet_data[planet_name]
    T = planet_info['period']
    g = planet_info['gravity']

    r_m = ((G * m_s * T ** 2) / (4 * math.pi ** 2)) ** (1 / 3)
    r_km = r_m / 1000
    r_au = r_km / au_in_km

    result = {
        'planet': planet_name,
        'distance_km': round(r_km, 2),
        'distance_au': round(r_au, 2)
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run()
