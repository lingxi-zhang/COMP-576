import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Example Line Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.savefig('example_graph.png')
plt.show()
