# -*- coding: utf-8 -*-
"""Práctica1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DS5YUDVB9NG8spXFmgepUZUPi040gWSQ

# **Actividad 1**

Asignaremos valores a dos variables y después las sumaremos.
"""

a = 90;
b = 7;
A = 25;

c = a+b;
d = A+b;

print("a + b = ", c);
print("A + b = ", d);

"""Ahora cambiaremos los valores de las siguientes variables y probaremos distintos resultados."""

f = 63;
g = 132;
x = f+g*g;

print("f + g * g = ",x);

"""**Llamadas a funciones**

Usaremos funciones definidas en la biblioteca math. Usaremos el import math.
"""

import math;

a = math.factorial(5);
b = math.sqrt(4);
c = math.ceil(4.12);

print("Factorial de 5 =", a);
print("La raíz cuadrada de 4 =", b);
print("El techo de 4.12 =", c);

"""Indica para que se usan las siguientes funciones:"""

import math;

x = 7.2;
i= 3.4;

a = math.floor(x)  # Devuelve el mayor entero menor o igual a x
b = math.fmod(x, i)  # Devuelve el resto de dividir x entre i
c = math.pow(x, i)  # Calcula x elevado a la potencia i
d = math.atan(x)  # Calcula el arco tangente de x en radianes

# Imprimir resultados
print("Mayor entero menor o igual a", x, "=", a)
print("Resto de", x, "dividido entre", i, "=", b)
print("Potencia de", x, "elevado a", i, "=", c)
print("Arco tangente de", x, "=", d)

"""**Listas**

Colección ordenada de elementos. Los items deben definirse dentro de corchetes. Una vez definida una lista, es posible agregar, eliminar y buscar items en la lista.
"""

l = [1,2,3,4,5];
print(l);

l2 = [5,8,"a"];
print(l2);

print(l[0]);
print(l2[0:2]);

listaCompras = ["manzanas","mango","zanahorias","platano"];
print(listaCompras[1:3]);

listaCompras.append("jugo");
print(listaCompras);

listaCompras.sort();
print(listaCompras);

a = [1,2,3];
c = math.sqrt(a); #Se espera error porque debe usarse numpy
print(a);

"""**Numpy**"""

import numpy as np;

a = np.array([1,2,3,4]);
print(a);
b = np.sqrt(a);
print(b);

a = np.array([[1.0,0.0,0.01],[1.1,0,2]]);
print(a);

print(a.shape);

a = np.zeros([2,3]);
print(a);
b = np.ones([2,4,6]);
print(b);

a[1,1] = 2;
print(a);

b[:,1:3,1:5] = 2;
print(b);

"""Matriz aleatoria con shape (4,5) e imprimiremos la raíz cuadrada de todos los elementos."""

import numpy as np

matriz = np.random.rand(4, 5)

raiz_cuadrada = np.sqrt(matriz)

print("Matriz original:")
print(matriz)
print("\nRaíz cuadrada de cada elemento:")
print(raiz_cuadrada)

"""**Matploblib**"""

import matplotlib.pyplot as plt
from numpy import pi

x = np.linspace(0,2*pi,100)
y = np.sin(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""# **Actividad 2**"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
cv2.__version__

img = cv2.imread('./img/toki.jpg')
imgShape = img.shape
print(imgShape)

img = img[:,:,::-1]
plt.imshow(img)
plt.show()

edgesImg = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Imagen original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edgesImg,cmap = 'gray')
plt.title('Imagen filtrada con los bordes'), plt.xticks([]), plt.yticks([])

plt.show()

cv2.imwrite('./img/ciao.jpg',edgesImg)

import cv2
import numpy as np
from matplotlib import pyplot as plt
cv2.__version__

img = cv2.imread('./img/toki.jpg')
imgShape = img.shape
print(imgShape)
img = img[:,:,::-1]
plt.imshow(img)
plt.show()

img2 = cv2.imread('./img/doki.jpg')
img2Shape = img2.shape
print("Forma de la imagen original= ",img2Shape)
img2 = img2[:,:,::-1]
plt.imshow(img2)
plt.show()

img2Resized = cv2.resize(img2, (400, 400))
img2ResizedShape = img2Resized.shape
print("Forma de la imagen despues del resize = ",img2ResizedShape)
plt.imshow(img2Resized)
plt.show()

imgResized = cv2.resize(img, (400,400))
imgResized = imgResized.shape
print("Forma de la imagen despues del resize = ",imgResized)
plt.imshow(imgResized)
plt.show()



#imagenMezclada = cv2.add(img,img2Resized)
imagenMezclada = cv2.addWeighted(imgResized,0.7,img2Resized,0.3,0)
plt.imshow(imagenMezclada)
plt.show()

"""# **Actividad 3**"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

#Se cargan los modelos para detectar rostros y ojos. NOTA: Estos modelos ya fueron entrenados previamente, solo los estamos usando
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Revisa que este archivo está en tu carpeta
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') #Revisa que este archivo está en tu carpeta

#Se lee la imagen
img = cv2.imread('./img/toki.jpg')

#Se convierte a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgToShow =  img[:,:,::-1]

#Se muestra la imagen
plt.imshow(imgToShow)
plt.show()

#Se utiliza el modelo detector de rostros que ya cargamos anteriormente
faces = face_cascade.detectMultiScale(gray, 1.3, 5)  #Indicamos los parámetros
#faces = face_cascade.detectMultiScale(gray, 1.01, 1)
for (x,y,w,h) in faces: #iterando en las coordenadas en donde se detectaron rostros con el modelo
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #Se dibujan los rectángulos en donde se encontraron rostros
    roi_gray = gray[y:y+h, x:x+w]  #region de interés de la imagen en gris
    roi_color = img[y:y+h, x:x+w]  #region de interés de la imagen a color
    #Se utiliza el detector de ojos que ya cargamos anteriormente
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes: #Iterando en las coordenadas de los ojos encontrados
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) #Se dibujan rectángulos en donde se encontraron ojos

plt.imshow(img)
plt.show()
#cv2.imshow('img',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Se crea un arreglo numpy
a = np.array([1, 3, 4, 5, 6 ,7])
print("Arreglo a original: ", a)
#Se crea el arreglo b con un segmento de a
b = a[:3]
#Se modifica un elemento de b
b[0]=9
#Como los valores se pasaron como referencia, también se modifica a
print("Arreglo b: ", b)
print("Arreglo a modificado: ", a)