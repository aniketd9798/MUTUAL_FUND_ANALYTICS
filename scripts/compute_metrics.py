import pandas as pd
import numpy as np

def sharpe_ratio(returns, rf=0):
    return ((returns.mean()-rf) / returns.std()) * np.sqrt(252)

def max_drawdown(nav):
    cumulative = nav / nav.iloc[0]
    running_max = cumulative.cummax()
    drawdown = (cumulative - running_max) / running_max
    return drawdown.min()

def var_95(returns):
    return returns.quantile(0.05)

def cvar_95(returns):
    var = returns.quantile(0.05)
    return returns[returns <= var].mean()

def hhi(weights):
    weights = weights / 100
    return (weights**2).sum()