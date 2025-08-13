import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import POSSIBLE




data = pd.DataFrame(POSSIBLE.DISTRICTS_POINTS).T
data.columns = ['lon', 'lat', 'demand']
data = data.astype(float)

sns.kdeplot(
    x=data['lon'], 
    y=data['lat'], 
    weights=data['demand'], 
    cmap="Reds", 
    fill=True, 
    bw_adjust=0.05,     
    levels=20,          
    thresh=0.01        
)

# Optional: plot original points
plt.scatter(data['lon'], data['lat'], c='black', s=2, alpha=0.2, label='District Centers')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Demand Density (KDE)")
plt.legend()
plt.tight_layout()
plt.show()