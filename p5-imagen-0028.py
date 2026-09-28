import cv2
#leer la imagen con cv2 =computer vision
img = cv2.imread('images (1).jpg')
# determinar el tipo de imagen numpy.ndarray
print(type(img))
# mostrar pixeles (554, 554, 3)
print(img.shape)
# mostrando imagen en ventana barra de titulo perro dalmata
cv2.imshow('dalmata', img)
## tiempo de espera
cv2.waitKey(0)
# destruir todas las ventanas
cv2.destroyAllWindows()