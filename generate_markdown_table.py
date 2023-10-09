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
