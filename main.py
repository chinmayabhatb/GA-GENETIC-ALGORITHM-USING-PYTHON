import matplotlib.pyplot as plt
from ypstruct import structure
import GA

# Sphere Test Function
def sphere(x):
    return sum(x**2)

# Problem Definition
problem = structure()
problem.costfunc = sphere
coords=[]
city1=[]
city2=[]
with open('./data/att48.txt') as f:
    for line in f.readlines():
        city = line.split(' ')
        coords.append((int(city[1]), int(city[2])))
        
problem.nvar = len(coords)
for i in range (problem.nvar):
    for j in range(2):
        if j==1:
            city2.append(coords[i][j])
        else:        city1.append(coords[i][j])
problem.varmin = city2
problem.varmax = city1

# GA Parameters
params = structure()
params.maxit = 1000
params.npop = 50
params.beta = 1
params.pc = 1
params.gamma = 0.1
params.mu = 0.01
params.sigma = 0.1

# Run GA
out = GA.run(problem, params)

# Results
plt.plot(out.bestcost)
# plt.semilogy(out.bestcost)
plt.xlim(0, params.maxit)
plt.xlabel('Iterations')
plt.ylabel('Best Cost')
plt.title('Genetic Algorithm (GA)')
plt.grid(True)
plt.show()

