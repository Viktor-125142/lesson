from scipy.stats import poisson

s = poisson.cdf(mu=5, k=5)
print(s)
