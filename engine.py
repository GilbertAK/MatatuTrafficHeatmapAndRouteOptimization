import numpy as np
import pandas as pd
import time

class MatatuEngine:
    def __init__(self):
        # Coordinates for major Nairobi Hubs
        self.routes = {
            "Thika Road": {"lat": -1.221, "lon": 36.885, "speed_limit": 50},
            "Ngong Road": {"lat": -1.300, "lon": 36.780, "speed_limit": 40},
            "Jogoo Road": {"lat": -1.290, "lon": 36.850, "speed_limit": 35},
            "Waiyaki Way": {"lat": -1.260, "lon": 36.760, "speed_limit": 60},
            "Mombasa Road": {"lat": -1.330, "lon": 36.900, "speed_limit": 55}
        }
        self.fleet_size = 15
        self.fleet = self._initialize_fleet()

    def _initialize_fleet(self):
        fleet_data = []
        for i in range(self.fleet_size):
            route_name = np.random.choice(list(self.routes.keys()))
            fleet_data.append({
                "id": f"K{np.random.choice(['BA','BZ','CQ'])}{np.random.randint(100,999)}X",
                "route": route_name,
                "lat": self.routes[route_name]["lat"] + np.random.uniform(-0.01, 0.01),
                "lon": self.routes[route_name]["lon"] + np.random.uniform(-0.01, 0.01),
                "speed": np.random.randint(10, 60)
            })
        return pd.DataFrame(fleet_data)

    def update_telemetry(self):
        """Simulates GPS drift and speed changes."""
        for idx, row in self.fleet.iterrows():
            # Random movement
            self.fleet.at[idx, 'lat'] += np.random.uniform(-0.001, 0.001)
            self.fleet.at[idx, 'lon'] += np.random.uniform(-0.001, 0.001)
            
            # Speed fluctuations based on route congestion
            current_route = row['route']
            limit = self.routes[current_route]["speed_limit"]
            self.fleet.at[idx, 'speed'] = max(5, min(limit + 10, row['speed'] + np.random.randint(-10, 10)))
        
        return self.fleet

    def get_heat_metrics(self):
        """Calculates congestion levels per route."""
        metrics = []
        for route, coords in self.routes.items():
            route_fleet = self.fleet[self.fleet['route'] == route]
            avg_speed = route_fleet['speed'].mean()
            density = len(route_fleet)
            
            # Congestion score: Low speed + High density = High congestion
            score = (density * 20) / (avg_speed / 5)
            status = "HEAVY" if score > 15 else "MODERATE" if score > 8 else "CLEAR"
            
            metrics.append({
                "Route": route,
                "Active Matatus": density,
                "Avg Speed": f"{avg_speed:.1f} km/h",
                "Status": status,
                "Heat Index": round(score, 1)
            })
        return metrics
