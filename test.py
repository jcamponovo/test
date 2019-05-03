import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
val=[37, 72, 122, 211, 366]
val2 = [v - val[0] for v in val]

U = [0.00489 * v for v in val2]
P = [v * 500000 / 4.5 + 101325 for v in U]

vtube = 3.
Vmes = [57, 47, 37, 27, 17]
V = [(val + vtube) / 1e6 for val in Vmes]

plt.plot(V, P, "+")
plt.xlabel("Volume (m\u00B3)")
plt.ylabel("Pression (Pa)")
plt.title("Pression en fonction du Volume")
plt.show()
