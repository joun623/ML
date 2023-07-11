import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/kion10y.csv", encoding="utf-8")

g = df.groupby(['tuki'])["kion"]
gg = g.sum() / g.count()

print(gg)
gg.plot()
plt.savefig("data/tenki0heikin-tuki.png")
plt.show()

# md = {}

#
# for i, row in df.iterrows():
#     m, d, v = (int(row['tuki']), int(row['hi']), float(row['kion']))
#     key = str(m) + "/" + str(d)
#     if not(key in md):
#         md[key] = []
#     md[key] += [v]
#
# avs = {}
# for key in md:
#     v = avs[key] = sum(md[key]) / len(md[key])
#     print("{0}: {1}".format(key, v))
