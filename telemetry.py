import random

class TelemetryData:
    def __init__(self, distance, speed, acceleration, rpm, tire_pressure, fuel, engine_temperature, braking, fuel_consumption):
        self.distance = distance
        self.speed = speed
        self.acceleration = acceleration
        self.rpm = rpm
        self.tire_pressure = tire_pressure
        self.fuel = fuel
        self.engine_temperature = engine_temperature
        self.braking = braking
        self.fuel_consumption = fuel_consumption

def generate_telemetry_data(traveled_distance, remaining_fuel):
    speed = random.uniform(0, 200)  # km/h
    acceleration = random.uniform(-5, 5)  # m/s²
    rpm = random.randint(1000, 8000)  # RPM
    tire_pressure = random.uniform(30, 40)  # PSI
    engine_temperature = random.uniform(60, 100)  # °C
    braking = random.choice([True, False])
    fuel_consumption = random.uniform(0.1, 1.0) if not braking else 0

    distance = traveled_distance + random.uniform(0.1, 1.0)
    traveled_distance = distance

    remaining_fuel = max(remaining_fuel - fuel_consumption, 0)
    
    return TelemetryData(distance, speed, acceleration, rpm, tire_pressure, remaining_fuel, engine_temperature, braking, fuel_consumption)
