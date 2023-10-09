import math

def calculate_distance(body1, body2):
    """Calculate the distance between two celestial bodies."""
    x1, y1 = body1["position"]
    x2, y2 = body2["position"]
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def calculate_distances(celestial_bodies):
    """Calculate the distances between celestial objects."""
    distances = []
    for i in range(len(celestial_bodies)):
        row = []
        for j in range(len(celestial_bodies)):
            if i == j:
                row.append(0.0)
            else:
                distance = calculate_distance(celestial_bodies[i], celestial_bodies[j])
                row.append(distance)
        distances.append(row)

    return distances

def generate_markdown_table(distances):
    """Generate a markdown table with the distances between celestial objects."""
    markdown_table = "| Celestial Body |"
    for i in range(len(distances)):
        markdown_table += f" Body {i+1} |"
    markdown_table += "\n| --- |"
    for _ in range(len(distances)):
        markdown_table += " --- |"
    markdown_table += "\n"
    for i in range(len(distances)):
        markdown_table += f"| Body {i+1} |"
        for j in range(len(distances)):
            markdown_table += f" {distances[i][j]:.2f} |"
        markdown_table += "\n"

    return markdown_table

# Example usage
celestial_bodies = [
    {"position": (0, 0)},
    {"position": (3, 4)},
    {"position": (6, 8)},
    {"position": (9, 12)}
]

distances = calculate_distances(celestial_bodies)
markdown_table = generate_markdown_table(distances)
print(markdown_table)
