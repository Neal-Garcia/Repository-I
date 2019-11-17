V = np.arange(1,101).reshape(10,10)
print("The Matrix is\n"+str(V*V))

R=(V*V)%3
a,b = np.where(R == 0)

K = V*V
D = K[a,b]
print("The Numbers which are divisible by 3 are\n"+str(D))