import pandas as pd

# URL del archivo .csv en Kaggle
url = '/kaggle/input/cybersecurity-suspicious-web-threat-interactions/CloudWatch_Traffic_Web_Attack.csv'

# Leer el archivo .csv desde la URL
df = pd.read_csv(url)

# Mostrar las primeras filas del DataFrame
print(df.head())
