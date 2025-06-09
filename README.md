# Weather Dashboard

A Django application that fetches and displays weather information using OpenWeatherMap API and Chart.js.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your OpenWeatherMap API key:
```
OPENWEATHER_API_KEY=your_api_key_here
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

## Features
- Current weather information
- Historical weather data visualization using Chart.js
- City search functionality
- Temperature, humidity, and pressure visualization
