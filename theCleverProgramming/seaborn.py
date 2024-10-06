import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.style.use('classic')

rng = np.random.RandomState(0)
# Usada em Python para criar um gerador de números aleatórios que é reproduzível
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)
# Calcula a soma cumulativa dos elementos ao longo de um eixo especificado.
"""
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

sns.set_theme()
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()
"""

"""
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

sns.kdeplot(data)
"""