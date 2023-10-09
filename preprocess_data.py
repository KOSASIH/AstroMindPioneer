import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def preprocess_data(data):
    # Convert data to pandas DataFrame
    df = pd.DataFrame(data)
    
    # Preprocess the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    
    return scaled_data

def train_model(data):
    # Perform dimensionality reduction using PCA
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(data)
    
    # Train a clustering model
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(reduced_data)
    
    return kmeans

def generate_report(data, model):
    # Generate markdown report with analysis results
    report = "# Astronomy Data Analysis Report\n\n"
    report += "## Clustering Analysis\n\n"
    
    # Add cluster labels to the data
    data['cluster_label'] = model.labels_
    
    # Generate markdown table with cluster information
    report += "### Cluster Information\n\n"
    report += "| Cluster Label | Count |\n"
    report += "| ------------- | ----- |\n"
    for label, count in data['cluster_label'].value_counts().items():
        report += f"| {label} | {count} |\n"
    report += "\n"
    
    # Generate markdown visualization of clusters
    report += "### Cluster Visualization\n\n"
    report += "![Cluster Visualization](path/to/cluster_visualization.png)\n\n"
    
    return report

# Example usage
data = fetch_astronomical_data()
preprocessed_data = preprocess_data(data)
model = train_model(preprocessed_data)
report = generate_report(data, model)
