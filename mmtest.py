from torchvision import datasets
from torchvision.transforms import ToTensor
import torch

train_dataset = datasets.MNIST(
root = 'datasets',
train = True,
transform = ToTensor(),
download = True,
)

n = 100
counter = [0 for i in range(10)]
matrices = [[] for i in range(10)]

# temp = train_dataset[0]
# b = temp[0].reshape(1,-1).squeeze()

i = 0
skupaj = 0
while(True):
    if counter[train_dataset[i][1]] < n:
        counter[train_dataset[i][1]] += 1
        matrices[train_dataset[i][1]].append(train_dataset[i][0].reshape(1,-1).squeeze())
        skupaj += 1
    if skupaj == n * 10:
        break
    i += 1

matrices = [torch.stack(x) for x in matrices]

# solutions = [torch.linalg.lstsq(matrices[i].T, b).solution for i in range(10)]

# solutions = [sum(b - matrices[i].T @ solutions[i]) for i in range(10)]

# solutions.index(min(solutions))

test_dataset = datasets.MNIST(
root = 'datasets',
train = False,
transform = ToTensor()
)

pravilno = 0
narobe = 0
k = 0
for item in test_dataset:
    b = item[0].reshape(1,-1).squeeze()
    solutions = [torch.linalg.lstsq(matrices[i].T, b).solution for i in range(10)]
    solutions = [sum(abs(b - matrices[i].T @ solutions[i])) for i in range(10)]
    res = solutions.index(min(solutions))
    # print(res)
    # print(item[1])
    # print(solutions)
    if res == item[1]:
        pravilno += 1
    else:
        narobe += 1
    k += 1
    if k == 10:
        break

pravilno