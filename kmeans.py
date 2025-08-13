import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import POSSIBLE


data = pd.DataFrame(POSSIBLE.DISTRICTS_POINTS).T
data.columns = ['lon', 'lat', 'demand']
data = data.astype(float)

k = 6


kmeans = KMeans(n_clusters=k, random_state=0)
data['cluster'] = kmeans.fit_predict(data[['lon', 'lat']])

demand_per_cluster = data.groupby('cluster')['demand'].sum()
total_demand = demand_per_cluster.sum()


centroids = kmeans.cluster_centers_


fig, ax = plt.subplots(figsize=(14, 8))
scatter = ax.scatter(data['lon'], data['lat'], c=data['cluster'], cmap='tab10',
                     s=data['demand'], alpha=0.7)


ax.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, label='Centroids')

for i, (x, y) in enumerate(centroids):
    rel = demand_per_cluster[i] / total_demand * 100
    ax.text(x, y, f'{rel:.1f}%', fontsize=15, ha='center', va='center',
            color='white', weight='bold',
            bbox=dict(facecolor='black', alpha=0.6, boxstyle='round'))

# Formatting
ax.set_xlabel("Longitude", fontsize=16)
ax.set_ylabel("Latitude", fontsize=16)
ax.set_title(f"KMeans Clustering of Demand Centers (k={k})")
legend = ax.legend(fontsize=12)
cbar = plt.colorbar(scatter, label='Cluster')
cbar.ax.tick_params(labelsize=16)  
cbar.set_label('Cluster', fontsize=16) 

plt.tight_layout()
plt.savefig("graphs/kmeans_clusters_bigger.png", dpi=300)  # Save the figure as a PNG with 300 dpi
plt.show()