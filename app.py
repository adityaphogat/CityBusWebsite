from flask import Flask, render_template

app = Flask(__name__)

# Sample bus data with timetables
buses = {
    'DTC-101': {
        'operator': 'DTC',
        'route': 'Cyber City → Huda City Center',
        'timetable': [
            {'departure': '06:00 AM', 'arrival': '06:45 AM'},
            {'departure': '06:30 AM', 'arrival': '07:15 AM'},
            {'departure': '07:00 AM', 'arrival': '07:45 AM'},
            {'departure': '07:30 AM', 'arrival': '08:15 AM'},
            {'departure': '08:00 AM', 'arrival': '08:45 AM'},
            {'departure': '08:30 AM', 'arrival': '09:15 AM'},
            {'departure': '09:00 AM', 'arrival': '09:45 AM'},
            {'departure': '09:30 AM', 'arrival': '10:15 AM'},
            {'departure': '10:00 AM', 'arrival': '10:45 AM'},
            {'departure': '10:30 AM', 'arrival': '11:15 AM'},
            {'departure': '11:00 AM', 'arrival': '11:45 AM'},
            {'departure': '11:30 AM', 'arrival': '12:15 PM'},
            {'departure': '12:00 PM', 'arrival': '12:45 PM'},
            {'departure': '12:30 PM', 'arrival': '01:15 PM'},
            {'departure': '01:00 PM', 'arrival': '01:45 PM'},
            {'departure': '01:30 PM', 'arrival': '02:15 PM'},
            {'departure': '02:00 PM', 'arrival': '02:45 PM'},
            {'departure': '02:30 PM', 'arrival': '03:15 PM'},
            {'departure': '03:00 PM', 'arrival': '03:45 PM'},
            {'departure': '03:30 PM', 'arrival': '04:15 PM'},
            {'departure': '04:00 PM', 'arrival': '04:45 PM'},
            {'departure': '04:30 PM', 'arrival': '05:15 PM'},
            {'departure': '05:00 PM', 'arrival': '05:45 PM'},
            {'departure': '05:30 PM', 'arrival': '06:15 PM'},
            {'departure': '06:00 PM', 'arrival': '06:45 PM'},
            {'departure': '06:30 PM', 'arrival': '07:15 PM'},
            {'departure': '07:00 PM', 'arrival': '07:45 PM'},
            {'departure': '07:30 PM', 'arrival': '08:15 PM'},
            {'departure': '08:00 PM', 'arrival': '08:45 PM'},
            {'departure': '08:30 PM', 'arrival': '09:15 PM'},
        ]
    },
    'GSRTC-202': {
        'operator': 'GSRTC',
        'route': 'Golf Course Road → Sector 7',
        'timetable': [
            {'departure': '06:15 AM', 'arrival': '07:00 AM'},
            {'departure': '06:45 AM', 'arrival': '07:30 AM'},
            {'departure': '07:15 AM', 'arrival': '08:00 AM'},
            {'departure': '07:45 AM', 'arrival': '08:30 AM'},
            {'departure': '08:15 AM', 'arrival': '09:00 AM'},
            {'departure': '08:45 AM', 'arrival': '09:30 AM'},
            {'departure': '09:15 AM', 'arrival': '10:00 AM'},
            {'departure': '09:45 AM', 'arrival': '10:30 AM'},
            {'departure': '10:15 AM', 'arrival': '11:00 AM'},
            {'departure': '10:45 AM', 'arrival': '11:30 AM'},
            {'departure': '11:15 AM', 'arrival': '12:00 PM'},
            {'departure': '11:45 AM', 'arrival': '12:30 PM'},
            {'departure': '12:15 PM', 'arrival': '01:00 PM'},
            {'departure': '12:45 PM', 'arrival': '01:30 PM'},
            {'departure': '01:15 PM', 'arrival': '02:00 PM'},
            {'departure': '01:45 PM', 'arrival': '02:30 PM'},
            {'departure': '02:15 PM', 'arrival': '03:00 PM'},
            {'departure': '02:45 PM', 'arrival': '03:30 PM'},
            {'departure': '03:15 PM', 'arrival': '04:00 PM'},
            {'departure': '03:45 PM', 'arrival': '04:30 PM'},
            {'departure': '04:15 PM', 'arrival': '05:00 PM'},
            {'departure': '04:45 PM', 'arrival': '05:30 PM'},
            {'departure': '05:15 PM', 'arrival': '06:00 PM'},
            {'departure': '05:45 PM', 'arrival': '06:30 PM'},
            {'departure': '06:15 PM', 'arrival': '07:00 PM'},
            {'departure': '06:45 PM', 'arrival': '07:30 PM'},
            {'departure': '07:15 PM', 'arrival': '08:00 PM'},
            {'departure': '07:45 PM', 'arrival': '08:30 PM'},
            {'departure': '08:15 PM', 'arrival': '09:00 PM'},
            {'departure': '08:45 PM', 'arrival': '09:30 PM'},
        ]
    },
    'EBUS-303': {
        'operator': 'E-BUS',
        'route': 'New Railway Station → MG Road',
        'timetable': [
            {'departure': '06:30 AM', 'arrival': '07:20 AM'},
            {'departure': '07:00 AM', 'arrival': '07:50 AM'},
            {'departure': '07:30 AM', 'arrival': '08:20 AM'},
            {'departure': '08:00 AM', 'arrival': '08:50 AM'},
            {'departure': '08:30 AM', 'arrival': '09:20 AM'},
            {'departure': '09:00 AM', 'arrival': '09:50 AM'},
            {'departure': '09:30 AM', 'arrival': '10:20 AM'},
            {'departure': '10:00 AM', 'arrival': '10:50 AM'},
            {'departure': '10:30 AM', 'arrival': '11:20 AM'},
            {'departure': '11:00 AM', 'arrival': '11:50 AM'},
            {'departure': '11:30 AM', 'arrival': '12:20 PM'},
            {'departure': '12:00 PM', 'arrival': '12:50 PM'},
            {'departure': '12:30 PM', 'arrival': '01:20 PM'},
            {'departure': '01:00 PM', 'arrival': '01:50 PM'},
            {'departure': '01:30 PM', 'arrival': '02:20 PM'},
            {'departure': '02:00 PM', 'arrival': '02:50 PM'},
            {'departure': '02:30 PM', 'arrival': '03:20 PM'},
            {'departure': '03:00 PM', 'arrival': '03:50 PM'},
            {'departure': '03:30 PM', 'arrival': '04:20 PM'},
            {'departure': '04:00 PM', 'arrival': '04:50 PM'},
            {'departure': '04:30 PM', 'arrival': '05:20 PM'},
            {'departure': '05:00 PM', 'arrival': '05:50 PM'},
            {'departure': '05:30 PM', 'arrival': '06:20 PM'},
            {'departure': '06:00 PM', 'arrival': '06:50 PM'},
            {'departure': '06:30 PM', 'arrival': '07:20 PM'},
            {'departure': '07:00 PM', 'arrival': '07:50 PM'},
            {'departure': '07:30 PM', 'arrival': '08:20 PM'},
            {'departure': '08:00 PM', 'arrival': '08:50 PM'},
            {'departure': '08:30 PM', 'arrival': '09:20 PM'},
            {'departure': '09:00 PM', 'arrival': '09:50 PM'},
        ]
    }
}

@app.route('/')
def index():
    """Display home page with all available bus routes"""
    return render_template('index.html', buses=buses)

@app.route('/bus/<bus_id>')
def bus_detail(bus_id):
    """Display detailed timetable for a specific bus"""
    if bus_id in buses:
        bus = buses[bus_id]
        return render_template('bus_detail.html', bus_id=bus_id, bus=bus)
    else:
        return "Bus not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)