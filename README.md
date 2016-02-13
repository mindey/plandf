# PlanDF
DataFrame for computing Value-Over-Time for lists of tuples (Step.investables, Step.deliverables) of a Plan.

Depends on [pandas.DataFrame](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) and [stepio](https://github.com/wefindx/StepIO).

```
git clone git@github.com:WeFindX/PlanDF.git
pip instal -r requirements.txt
```

## Examples

Using [hour](https://research.stlouisfed.org/fred2/series/CES0500000003) as currency.

```{python}
>>> import plandf
>>> breakfast = [
 ('time: 0.003~0.004@24h; loaf of black bread: 1@0.1h; butter grams: 15@0.01h; tomato: 0.5@0.2h',
  'sandwitch: 1@0.12h'),
 ('eggs: 2~5@0.012h; scrambling actions: 50~100; time: 0.003~0.005@24h',
  'scrambled egg servings: 1@0.16h'),
 ('coffee teaspoon: 1~2@0.00012h; liters of water: 0.2~0.3@0.0001h; time: 0.003~0.005@24h',
  'cup of coffee: 1~1.5@0.08h')
]

>>> df = plandf.read(breakfast)
>>> # show worst/mean/best scenarios over time:
>>> df.to_json()
'{"worst":{"0.0":0.0,"0.072":-0.0766666667,"0.084":-0.1533333333,"0.096":-0.23,"0.144":-0.1966666667,"0.18":-0.1633333333,"0.216":-0.13,"0.216":-0.1034233333,"0.276":-0.0768466667,"0.336":-0.05027},"mean":{"0.0":0.0,"0.072":-0.115,"0.084":-0.23,"0.096":-0.1906666667,"0.144":-0.1513333333,"0.18":-0.112,"0.216":-0.078735,"0.216":-0.04547,"0.276":-0.012205,"0.336":-0.012205},"best":{"0.0":0.0,"0.072":-0.23,"0.084":-0.1846666667,"0.096":-0.1393333333,"0.144":-0.094,"0.18":-0.0540466667,"0.216":-0.0140933333,"0.216":0.02586,"0.276":0.02586,"0.336":0.02586}}'
>>> df.plot()
```

![alt text](https://raw.githubusercontent.com/Mindey/mindey.github.io/master/media/conversations/breakfast.png "Plan value over time")

Using [other](https://openexchangerates.org/) currencies.

```{python}
>>> breakfast_in_currencies = [
 ('time: 0.003~0.004@24h; loaf of black bread: 1@2.22eur; butter grams: 15@0.25usd; tomato: 0.5@5usd',
  'sandwitch: 1@3usd'),
 ('eggs: 2~5@0.3usd; scrambling actions: 50~100; time: 0.003~0.005@24h',
  'scrambled egg servings: 1@4usd'),
 ('coffee teaspoon: 1~2@0.003usd; liters of water: 0.2~0.3@0.0025usd; time: 0.003~0.005@24h',
  'cup of coffee: 1~1.5@2usd')
]

import pandas as pd
conversion_rates = pd.DataFrame({'h': [25.39],
                                 'usd': [1.],
                                 'eur': [1.12565],
                                 'cny': [0.153078],
                                 'rub': [0.012709],
                                 'jpy': [0.008832]})
>>> df = plandf.read(breakfast_in_currencies,conversion_rates)
>>> # show worst/mean/best scenarios over time:
>>> df.to_json()
'{"worst":{"0.0":0.0,"0.072":-0.0766666667,"0.084":-0.1533333333,"0.096":-0.23,"0.144":-0.1966666667,"0.18":-0.1633333333,"0.216":-0.13,"0.216":-0.1034233333,"0.276":-0.0768466667,"0.336":-0.05027},"mean":{"0.0":0.0,"0.072":-0.115,"0.084":-0.23,"0.096":-0.1906666667,"0.144":-0.1513333333,"0.18":-0.112,"0.216":-0.078735,"0.216":-0.04547,"0.276":-0.012205,"0.336":-0.012205},"best":{"0.0":0.0,"0.072":-0.23,"0.084":-0.1846666667,"0.096":-0.1393333333,"0.144":-0.094,"0.18":-0.0540466667,"0.216":-0.0140933333,"0.216":0.02586,"0.276":0.02586,"0.336":0.02586}}'
>>> df.plot()
```

If you have _[OpenExchangeRates](https://openexchangerates.org/)_ or _[Federal Reserve Bank of St. Louis](https://research.stlouisfed.org/fred2/series/CES0500000003)_ API keys, you can edit [settings.py](https://github.com/WeFindX/PlanDF/blob/master/plandf/settings.py) get the *conversion_rates* from there:

```
import rates
#xrates = rates.Rates(OXE_API='', FRED_API='')
conversion_rates = xrates.df
```
