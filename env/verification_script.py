import sys
print(f'Python version: {sys.version}')
print(f'Python location: {sys.executable}')

# Test key libraries
try:
    import geopandas as gpd
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import folium
    from esda.getisord import G_Local
    from sklearn.cluster import DBSCAN
    import jupyter
    print('✓ All required libraries imported successfully!')
    print(f"✓ GeoPandas version: {gpd.__version__}")
    print(f"✓ Pandas version: {pd.__version__}")
    print(f"✓ NumPy version: {np.__version__}")
    print('✓ Environment setup is complete and consistent!')
except ImportError as e:
    print(f'✗ Import error: {e}')
    print('Please contact IT or Lecturer for assistance., follow the troobleshooting guidance')
