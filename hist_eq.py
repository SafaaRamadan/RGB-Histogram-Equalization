r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]

# Apply histogram equalization
r_eq = cv2.equalizeHist(r)
g_eq = cv2.equalizeHist(g)
b_eq = cv2.equalizeHist(b)

# Show equalized channels
plt.figure(figsize=(10, 4))
plt.subplot(1, 4, 1)
plt.imshow(r_eq, cmap='gray')
plt.title('Equalized Red')

plt.subplot(1, 4, 2)
plt.imshow(g_eq, cmap='gray')
plt.title('Equalized Green')

plt.subplot(1, 4, 3)
plt.imshow(b_eq, cmap='gray')
plt.title('Equalized Blue')


# Merge equalized channels
equalized_img = cv2.merge((r_eq, g_eq, b_eq))
plt.subplot(1, 1, 1)
plt.imshow(equalized_img)
plt.title('Equalized RGB')
plt.axis('off')
plt.tight_layout()
plt.show()
