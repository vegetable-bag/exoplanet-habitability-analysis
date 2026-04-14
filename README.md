#Exoplanet Habitability Analysis

This project explores the habitability of exoplanets using stellar flux and equilibrium temperature models.

##Overview

With the discovery of thousands of exoplanets, identifying potentially habitable worlds has become a key area of research. This project applies simplified physics-based models to estimate planetary temperatures and evaluate habitability.

##Methodology

- Stellar flux calculated relative to Earth
- Equilibrium temperature estimated using radiative balance
- Habitability range: 273 K – 373 K

##Dataset

The dataset includes 20 confirmed exoplanets with:
- Orbital distance (AU)
- Stellar flux (relative to Earth)
- Estimated equilibrium temperature

##Results

Two main relationships were analyzed:

1. Flux vs Temperature → strong positive correlation  
2. Distance vs Temperature → inverse-square trend  

##Key Findings

- Planets with flux between 0.7 and 1.2 are most likely habitable  
- Temperature strongly depends on stellar radiation  
- Habitability exists on a spectrum, not a fixed category  

##How to Run

```bash
pip install -r requirements.txt
cd src
python analysis.py
