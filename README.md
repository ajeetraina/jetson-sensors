# Jetson Sensors Data Collection

This project simulates sensor data collection (temperature, pressure, and humidity) and stores it in a Neo4j graph database. It's designed to work with NVIDIA Jetson devices but can be used on any system for testing and development.

## Features

- Simulates realistic sensor data (temperature, pressure, humidity)
- Stores readings in Neo4j graph database
- Configurable sampling rate
- Realistic data ranges:
  - Temperature: 20-30°C
  - Pressure: 980-1020 hPa
  - Humidity: 30-70%

## Prerequisites

- Python 3.8+
- Neo4j Database (local or remote)
- pip package manager

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ajeetraina/jetson-sensors.git
   cd jetson-sensors
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Neo4j connection:
   - Open `sensor_simulator.py`
   - Update the Neo4j connection details:
     ```python
     uri = "neo4j://localhost:7687"
     username = "neo4j"
     password = "your_password"  # Replace with your password
     ```

## Usage

Run the sensor simulator:
```bash
python sensor_simulator.py
```

The script will:
1. Generate simulated sensor readings
2. Store them in Neo4j database
3. Print readings to console
4. Create 25 readings with 2-second intervals

## Data Model

Each sensor reading is stored as a node in Neo4j with the following properties:
- timestamp: ISO format timestamp
- temperature: Temperature in Celsius
- pressure: Atmospheric pressure in hPa
- humidity: Relative humidity percentage

## Query Examples

View all readings:
```cypher
MATCH (r:Reading)
RETURN r
ORDER BY r.timestamp DESC
LIMIT 10
```

Get average temperature:
```cypher
MATCH (r:Reading)
RETURN avg(r.temperature) as avg_temp
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

MIT License