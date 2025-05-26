b, bins, patches = plt.hist(img.flatten(), 255)
plt.show()

colors = ['Red', 'Green', 'Blue']
for i, color in enumerate(colors):
    plt.subplot(1, 3, i+1)
    plt.hist(img[:, :, i].flatten(), 255, color=color.lower())
    plt.title(f'{color}')

plt.tight_layout()
plt.show()

