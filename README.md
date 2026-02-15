# Conflict-Recovery
A Dynamic Simulation of Post-Conflict Economic Recovery
Overview

This project develops a dynamic macroeconomic simulation framework to analyze recovery trajectories in fragile, post-conflict economies.

Using an augmented Solow growth model with:

Physical Capital (K)

Human Capital (H)

Governance/Productivity (A)

the model evaluates how different policy interventions affect long-run economic performance after conflict shocks.

# Research Questions

Does capital reconstruction restore long-run growth?

Does human capital reform generate stronger recovery?

Is there a threshold level of education investment required for sustainable stabilization?

How sensitive is recovery to structural parameters?

# Model Structure

Production Function:

Yₜ = Aₜ · Kₜ^α · Hₜ^(1−α)

Dynamic Equations:

Capital accumulation

Human capital depreciation and investment

Governance/productivity evolution

Conflict shock mechanism

The model allows counterfactual simulations including:

Baseline fragile economy

Conflict shock

Conflict + capital injection

Conflict + human capital reform

Sensitivity analysis across parameters

# Key Findings

Capital injection produces short-term output recovery but does not reverse long-run decline.

Human capital reform improves long-run trajectory more effectively than physical reconstruction alone.

Recovery dynamics exhibit threshold behavior in education investment.

Structural fragility amplifies the persistence of conflict shocks.

# Repository Structure
model.py                 → Core economic equations
simulation.py            → Dynamic simulation engine
visualization.py         → Plotting utilities
sensitivity_analysis.py  → Parameter robustness testing
analysis.ipynb           → Experimental simulations
data/                    → Placeholder for datasets
figures/                 → Generated plots
outputs/                 → Simulation outputs

# Policy Insight

The simulations suggest that sustainable post-conflict recovery requires structural investment in human capital and institutional quality rather than exclusive reliance on capital reconstruction.

# Technical Stack

Python 3

NumPy

Matplotlib

Jupyter Notebook

# Author

Ujanga Adil Surur
Development Economics | Quantitative Modeling | Economic Simulation

