# City Bus Gurugram - Timetable Website

A Flask-based web application that displays bus timetables for various routes across Gurugram, Haryana.

## Features

- 🚌 View multiple bus routes with detailed information
- ⏱️ Daily timetables for each bus route
- 📍 Route information and bus operators
- 📱 Responsive design for mobile and desktop
- 🎨 Modern UI with gradient styling

## Project Structure

```
CityBusWebsite/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── templates/
│   ├── index.html     # Home page with bus routes
│   └── bus_detail.html # Detailed timetable view
└── static/
    └── style.css      # Styling stylesheet
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/adityaphogat/CityBusWebsite.git
   cd CityBusWebsite
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Available Bus Routes

Currently, the application includes the following bus routes:

1. **DTC-101**: Cyber City to Huda City Center
2. **GSRTC-202**: Golf Course Road to Sector 7
3. **EBUS-303**: New Railway Station to MG Road

## Usage

- **Home Page**: View all available bus routes with basic information
- **Route Details**: Click "View Schedule" on any bus card to see the complete daily timetable

## Future Enhancements

- Database integration for real-time updates
- User authentication and favorites
- Real-time GPS tracking
- Push notifications for delays
- Mobile app version
- Advanced search and filtering

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3
- **Templating**: Jinja2

## License

This project is open source and available under the MIT License.

## Author

Aditya Phogat

## Contact

For questions or suggestions, please open an issue on GitHub.
