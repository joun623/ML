import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/kion10y.csv', encoding="utf-8")

atui_bool = (df["kion"] > 30)

atui = df[atui_bool]

cnt = atui.groupby("nen")["nen"].count()

print(cnt)
cnt.plot()
plt.savefig("tenki-over30.png")
plt.show()
