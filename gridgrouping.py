import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import POSSIBLE




data = pd.DataFrame(POSSIBLE.DISTRICTS_POINTS).T
data.columns = ['lon', 'lat', 'demand']
data = data.astype(float)

xbins = np.linspace(data['lon'].min(), data['lon'].max(), 50)
ybins = np.linspace(data['lat'].min(), data['lat'].max(), 50)


heatmap, xedges, yedges = np.histogram2d(
    data['lon'], data['lat'], 
    bins=[xbins, ybins], 
    weights=data['demand']
)

plt.figure(figsize=(10, 8))
plt.imshow(
    heatmap.T, origin='lower', 
    extent=[xbins[0], xbins[-1], ybins[0], ybins[-1]], 
    cmap='Reds', aspect='auto'
)
plt.colorbar(label='Total Demand per Grid Cell')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Demand Concentration by Grid")
plt.show()
