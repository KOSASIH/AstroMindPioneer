# AstroMindPioneer
Merging AI and human consciousness to explore the depths of the universe.

# Guide 

```python
import requests
import json

def fetch_data():
    url = "https://api.example.com/astronomy/discoveries"
    response = requests.get(url)
    data = response.json()
    return data

def process_data(data):
    discoveries = data["discoveries"]
    processed_data = []
    for discovery in discoveries:
        name = discovery["name"]
        description = discovery["description"]
        date = discovery["date"]
        source = discovery["source"]
        processed_data.append({"name": name, "description": description, "date": date, "source": source})
    return processed_data

def generate_markdown_report(data):
    report = "# Latest Discoveries in the Universe\n\n"
    for discovery in data:
        report += "## {}\n\n".format(discovery["name"])
        report += "- Description: {}\n".format(discovery["description"])
        report += "- Date: {}\n".format(discovery["date"])
        report += "- Source: {}\n\n".format(discovery["source"])
    return report

def save_report(report):
    with open("latest_discoveries.md", "w") as file:
        file.write(report)

def main():
    data = fetch_data()
    processed_data = process_data(data)
    report = generate_markdown_report(processed_data)
    save_report(report)

if __name__ == "__main__":
    main()
```

This Python script fetches astronomical data from a public API, processes it, and generates a markdown report summarizing the latest discoveries in the universe. The `fetch_data` function retrieves the data from the API, the `process_data` function extracts the relevant information from the fetched data, and the `generate_markdown_report` function creates a markdown report with sections for each discovery. Finally, the `save_report` function saves the generated report to a file named `latest_discoveries.md`. To execute the script, simply run it in a Python environment.

# Markdown Table Generator 

```python
def generate_markdown_table(celestial_objects):
    # Create the table header
    table_header = "| Name | Type | Distance | Magnitude |\n"
    table_header += "|------|------|----------|-----------|\n"
    
    # Create the table rows
    table_rows = ""
    for obj in celestial_objects:
        name = obj.get('name', '')
        obj_type = obj.get('type', '')
        distance = obj.get('distance', '')
        magnitude = obj.get('magnitude', '')
        
        table_rows += f"| {name} | {obj_type} | {distance} | {magnitude} |\n"
    
    # Combine the header and rows to generate the markdown table
    markdown_table = table_header + table_rows
    
    return markdown_table
```

Example usage:
```python
celestial_objects = [
    {'name': 'Sirius', 'type': 'Star', 'distance': '8.6 light years', 'magnitude': '-1.46'},
    {'name': 'Andromeda Galaxy', 'type': 'Galaxy', 'distance': '2.537 million light years', 'magnitude': '3.44'},
    {'name': 'Betelgeuse', 'type': 'Star', 'distance': '643 light years', 'magnitude': '0.42'}
]

markdown_table = generate_markdown_table(celestial_objects)
print(markdown_table)
```

Output:
```
| Name               | Type   | Distance               | Magnitude |
|--------------------|--------|------------------------|-----------|
| Sirius             | Star   | 8.6 light years         | -1.46     |
| Andromeda Galaxy   | Galaxy | 2.537 million light years | 3.44      |
| Betelgeuse         | Star   | 643 light years         | 0.42      |
```

This code defines a function `generate_markdown_table` that takes a list of celestial objects as input. It iterates over each object and extracts the relevant attributes (name, type, distance, magnitude) to generate a markdown table. The function then combines the table header and rows to create the final markdown table. An example usage is provided to demonstrate how to use the function and generate the desired markdown output.
