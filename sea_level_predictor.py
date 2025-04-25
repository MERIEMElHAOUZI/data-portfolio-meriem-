import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 1. Charger les données
df = pd.read_csv('epa-sea-level.csv')

# 2. Créer un scatter plot
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# 3. Calculer la régression linéaire pour toute la période de 1880 à 2050
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = range(1880, 2051)
sea_levels_extended = [slope * year + intercept for year in years_extended]
plt.plot(years_extended, sea_levels_extended, label='Fit line (1880-2050)', color='blue')

# 4. Régression linéaire à partir de 2000
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
sea_levels_recent = [slope_recent * year + intercept_recent for year in years_extended]
plt.plot(years_extended, sea_levels_recent, label='Fit line (2000-2050)', color='red')

# 5. Ajouter des labels et un titre
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# 6. Ajouter la légende
plt.legend()

# 7. Sauvegarder l'image
plt.savefig('sea_level_rise.png')

# 8. Afficher le graphique
plt.show()
