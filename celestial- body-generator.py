import random

class CelestialBodyGenerator:
    def __init__(self):
        self.generated_bodies = []

    def create_bodies(self, num_bodies):
        for _ in range(num_bodies):
            mass = random.uniform(1e20, 1e30)  # Random mass between 1e20 and 1e30 kg
            radius = random.uniform(1e5, 1e7)  # Random radius between 1e5 and 1e7 meters
            position = (random.uniform(-1e9, 1e9), random.uniform(-1e9, 1e9))  # Random (x, y) position between -1e9 and 1e9

            body = {
                'mass': mass,
                'radius': radius,
                'position': position
            }
            self.generated_bodies.append(body)

    def generate_report(self):
        report = "# Generated Celestial Bodies\n\n"
        for i, body in enumerate(self.generated_bodies):
            report += f"## Body {i+1}\n"
            report += f"- Mass: {body['mass']} kg\n"
            report += f"- Radius: {body['radius']} meters\n"
            report += f"- Position: {body['position']}\n\n"
        return report

# Example usage
generator = CelestialBodyGenerator()
generator.create_bodies(5)
report = generator.generate_report()
print(report)
