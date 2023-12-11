import numpy as np

Xi = np.array([1, 5])
Et = np.array([1, 2, 4])
distr = np.array([[0.06, 0.20, 0.36], [0.18, 0.10, 0.10]])

distrXi = distr.sum(axis=1)
distrEt = distr.sum(axis=0)

E_Xi = np.dot(Xi, distrXi)
E_Et = np.dot(Et, distrEt)

sigma_Xi = (np.dot(Xi**2, distrXi) - E_Xi**2) ** 0.5
sigma_Et = (np.dot(Et**2, distrEt) - E_Et**2) ** 0.5

E_Mul = 0
for i in range(len(distrXi)):
    for j in range(len(distrEt)):
        E_Mul += Xi[i] * Et[j] * distr[i][j]

r = (E_Mul - E_Xi * E_Et) / (sigma_Xi * sigma_Et)
print(r)
