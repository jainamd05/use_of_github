import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
print(iris.head())
print(iris.describe())

print("HELLO WORLD!")
for i in range(3) :
    print(i)
print("DONE!")

print("I have leaarnt something new and tried implementing it...")
for i in range(10) :
    print(i*i)

print("Implementation is good!")
i = 0
while True :
    print("INFINITE LOOP!")
    i += 1
    if i == 25 :
        break
