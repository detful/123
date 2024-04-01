import pandas as pd
import matplotlib.pyplot as plt

prices = [
    (1, 2.12),
    (2, 2.56),
    (3, 3.10),
    (4, 3.16),
    (5, 3.58),
    (6, 5.12),
    (7, 5.16),
    (8, 5.20),
    (9, 4.12),
    (10, 4.10),
    (11, 3.65),
    (12, 4.25),
]

df = pd.DataFrame(prices, columns=['month', 'pricePLN'])

df.set_index('month', inplace=True)

df['priceUSD'] = df['pricePLN'] / 4

plt.figure()
df['priceUSD'].plot(color='red', linestyle='--')
plt.title('Price of goods (USD)')
plt.ylabel('Price (USD)')
plt.xlabel('month')
plt.show()
