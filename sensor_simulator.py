import random
import time
from neo4j import GraphDatabase
from datetime import datetime

class SensorDataManager:
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    def create_sensor_reading(self, temperature, pressure, humidity, timestamp):
        with self.driver.session() as session:
            session.write_transaction(
                self._create_sensor_reading,
                temperature,
                pressure,
                humidity,
                timestamp
            )

    @staticmethod
    def _create_sensor_reading(tx, temperature, pressure, humidity, timestamp):
        query = (
            "CREATE (r:Reading {timestamp: $timestamp, temperature: $temperature, "
            "pressure: $pressure, humidity: $humidity})"
        )
        tx.run(query, timestamp=timestamp, temperature=temperature,
               pressure=pressure, humidity=humidity)

def simulate_sensor_data():
    # Simulate realistic sensor data ranges
    temperature = round(random.uniform(20.0, 30.0), 2)  # 20-30°C
    pressure = round(random.uniform(980.0, 1020.0), 2)  # 980-1020 hPa
    humidity = round(random.uniform(30.0, 70.0), 2)     # 30-70%
    return temperature, pressure, humidity

def main():
    # Neo4j connection details
    uri = "neo4j://localhost:7687"
    username = "neo4j"
    password = "your_password"  # Replace with your Neo4j password

    sensor_manager = SensorDataManager(uri, username, password)

    try:
        # Generate and store 25 sensor readings
        for _ in range(25):
            temp, pressure, humidity = simulate_sensor_data()
            timestamp = datetime.now().isoformat()
            
            print(f"Recording: Temp: {temp}°C, Pressure: {pressure}hPa, Humidity: {humidity}%")
            sensor_manager.create_sensor_reading(temp, pressure, humidity, timestamp)
            
            # Wait 2 seconds between readings
            time.sleep(2)

    finally:
        sensor_manager.close()

if __name__ == "__main__":
    main()
