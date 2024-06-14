import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = r"C:\Users\andre\Documents\MSDS\MSDSOrientation\MSDSOrientationPython\MSDS-Orientation-Computer-Survey(in).csv";
data = pd.read_csv(path)

cycle = data.loc[:,"CPU Cycle Rate (in GHz)"]
print(data.get("CPU Cycle Rate (in GHz)"))

plt.hist(data.get("CPU Cycle Rate (in GHz)"), range=[0, 5], bins=30, color='skyblue', edgecolor='black')

plt.xlabel('Cycle Rates')
plt.ylabel('Frequency')
plt.title('Cycle Rates of Data Science Students')
plt.savefig(f"fig.png")
# Display the plot
plt.show()

