import scipy.misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#lena = scipy.misc.lena()
#plt.gray()
lena = mpimg.imread('girl.png')
plt.imshow(lena)
plt.colorbar()
plt.show()
