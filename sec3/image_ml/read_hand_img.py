import matplotlib.pyplot as plt

from sklearn import datasets
digits = datasets.load_digits()

# for i in range(15):
#     plt.subplot(3, 5, i+1)
#     plt.axis("off")
#     plt.title(str(digits.target[i]))
#     plt.imshow(digits.images[i], cmap="gray")
#
# plt.show()


d0 = digits.images[0]
plt.imshow(d0, cmap="gray")
plt.show()
print(d0)
