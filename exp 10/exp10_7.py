import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,25,30,40]

plt.plot(x,y)
plt.title("Line Plot")
plt.show()

plt.bar(x,y)
plt.title("Bar Chart")
plt.show()

plt.scatter(x,y)
plt.title("Scatter Plot")
plt.show()

data = [1,2,2,3,3,3,4,4,5]
plt.hist(data)
plt.title("Histogram")
plt.show()