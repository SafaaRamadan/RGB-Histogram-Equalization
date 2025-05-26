import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests

url = 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRVAzDu69PJJ_Esdiyex10BD1G_vtppUfRoJQOF_zmPybE2q3VE1fhGc89NphDuv4i3Qr6CI3lJPCIgNwE03NBHEA'

response = requests.get(url)
image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.axis('off')
plt.show()

plt.subplot(1, 3, 1)
plt.imshow(img[:,:,0], cmap='gray')
plt.subplot(1, 3, 2)
plt.imshow(img[:,:,1], cmap='gray')
plt.subplot(1, 3, 3)
plt.imshow(img[:,:,2], cmap='gray')
plt.show()
