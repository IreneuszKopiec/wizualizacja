import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.linspace(-4, 4, 100)
y = np.sin(2*x)
y1 = 2*np.sin(x)
y2 = np.sin(x)
plt.plot(x, y2, 'blue', linestyle="-", label="sin(x)")
plt.plot(x, y1, 'red', linestyle=":", label="2sin(x)")
plt.plot(x, y, 'green', linestyle="--", label="sin(2x)")
plt.legend(title='Wykres')
plt.show()
x1 = np.linspace(-10, 10, 100)
y3 = 1/(1+x**2)
plt.plot(x1, y3)
plt.show()
zero3 = np.linspace(0, 3, 100)
zero4 = np.linspace(0, 4, 100)
y4 = zero3**2
y5 = np.exp(zero3)
y6 = zero3**zero3
plt.plot(zero3, y4, 'blue', linestyle="dashed", label="x^2")
plt.plot(zero3, y5, 'red', linestyle="dotted", label="e^x")
plt.plot(zero3, y6, 'green', linestyle="-", label="x^x")
plt.legend(title='Wykres')
plt.show()
y7 = zero4**2
y8 = np.exp(zero4)
y9 = zero4**zero4
plt.plot(zero4, y4, 'blue', linestyle="dashed", label="x^2")
plt.plot(zero4, y5, 'red', linestyle="dotted", label="e^x")
plt.plot(zero4, y6, 'green', linestyle="-", label="x^x")
plt.legend(title='Wykres')
plt.show()
plt.subplot(3, 1, 1)
plt.plot(zero4, y4, 'blue', linestyle="dashed", label="x^2")
plt.subplot(3, 1, 2)
plt.plot(zero4, y5, 'red', linestyle="dotted", label="e^x")
plt.subplot(3, 1, 3)
plt.plot(zero4, y6, 'green', linestyle="-", label="x^x")
plt.tight_layout()
plt.legend(title='Wykres', loc='upper center')
plt.show()


def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 5):
        plt.plot(x, np.sin(x+i*.5)*(7-i)*flip)


sns.set_style("whitegrid")
sns.set_palette("husl")
sinplot()
print(sns.axes_style())
plt.show()


def xplot():
    p1 = np.linspace(-2, 2, 100)
    p2 = np.linspace(0, 2, 100)
    for i in range(1, 4):
        plt.plot(p1, p1**i)
        if i == 1:
            plt.plot(p2, np.sqrt(p2))
        if i == 3:
            plt.plot(p2, p2**(1/3))


sns.set_style("whitegrid")
sns.set_palette("husl")
xplot()
print(sns.axes_style())
plt.show()
