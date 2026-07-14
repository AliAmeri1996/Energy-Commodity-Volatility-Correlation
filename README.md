# Energy Commodity Volatility and Correlation Dashboard

## Overview
Analysis of price volatility and correlations across key energy commodities 
(crude oil, natural gas, gold) from 2020-2024. This project identifies how 
different commodities move together and highlights periods of unusual volatility.

## Tools
- Python
- pandas
- NumPy
- matplotlib
- yfinance

## What this project covers
- Downloading and cleaning price data for multiple commodities simultaneously
- Calculating and comparing rolling volatility across all assets
- Building a correlation matrix showing how commodities move together
- Visualising everything in a multi-panel dashboard

## Background: Why correlation matters in commodity markets
Commodities don't move in isolation. Oil and natural gas often move together 
because they compete as energy sources. Gold tends to move independently as a 
safe haven asset. Understanding these relationships helps traders:
- Identify hedging opportunities
- Spot when historical correlations break down (a signal something unusual is happening)
- Manage portfolio risk across multiple commodity positions

## Key concepts
- **Volatility** — how much a price jumps around. Higher volatility = more risk
- **Correlation** — how closely two assets move together. 1 = perfectly together, -1 = perfectly opposite, 0 = no relationship
- **Rolling calculations** — calculated over a moving window of days rather than the whole dataset at once

## Status
In progress
