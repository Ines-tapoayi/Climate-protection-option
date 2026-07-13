# Climate-protection-option

Oui, c'est exactement ce style que je ferais. Il est propre, professionnel et les recruteurs peuvent comprendre ton projet en 30 secondes.

Je te propose ce README.

---

# Climate Protection Option (CPO)

## Overview

This project presents the design and pricing of a **Climate Protection Option (CPO)** inspired by Hull's *Options, Futures and Other Derivatives*.

The option is designed to protect firms against financial losses caused by extreme summer heat.

A custom **Heat Index** is constructed from historical daily maximum temperatures and used as the underlying variable of the option. The premium is estimated using **Bootstrap Monte Carlo simulation**.

---

## Objectives

* Design an innovative climate derivative
* Build a Heat Index from historical weather data
* Price the option using Bootstrap Monte Carlo (10,000 simulations)
* Determine an objective strike using the 95th percentile
* Analyze the sensitivity of the option premium

---

## Methodology

* Historical daily maximum temperatures (Paris, 2000–2026)
* Summer filtering (June–August)
* Heat Index construction
* Bootstrap Monte Carlo simulation
* Option payoff calculation
* Discounted premium estimation
* Sensitivity analysis

---

## Key Results

* Custom Heat Index successfully identifies major French heatwaves
* Strike determined at the **95th percentile**
* Estimated option premium: **€0.64**
* Exercise probability: **7.41%**
* Sensitivity analysis performed for different strike levels


---

## Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Monte Carlo Simulation
* Bootstrap
* Quantitative Finance



## Future Improvements

* Use multiple French regions
* Integrate climate change scenarios
* Calibrate the option using real economic losses
* Compare Bootstrap with stochastic temperature models

---

## Author

Inès Tapoayi

