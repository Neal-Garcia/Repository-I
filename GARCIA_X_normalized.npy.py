import numpy as np

X = np.random.random((5,5))
xm = np.mean(X)
sd = np.std(X)

Z = (X-xm)/sd

print("Your Random Matrix is\n" + str(X))
print("The Normalized Matrix is\n" + str(Z))



