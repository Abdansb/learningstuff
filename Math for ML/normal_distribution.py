#!/usr/bin/env python3

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Random Generation of 1000 independent Normal samples
mu = 0
sigma = 1
N = 1000
X = np.random.normal(mu,sigma,N)
 
# Population distribution
x_values = np.arange(-5,5,0.01)
y_values = norm.pdf(x_values)

#Sample histogram with Population distribution
counts, bins, ignored = plt.hist(X, 30, density = True,color = 'purple',label = 'Sampling Distribution')
plt.plot(x_values,y_values, color = 'y',linewidth = 2.5,label = 'Population Distribution')
plt.title("Randomly generating 1000 obs from Normal distribution mu = 0 sigma = 1")
plt.ylabel("Probability")
plt.legend()
plt.show()
