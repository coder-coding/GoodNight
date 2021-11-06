from PIL import Image
import numpy as np
from goodnight import GN

gn = GN('Adv1')
gn.init('http://23.105.196.211:9999/post/')

img = Image.open('./Samoyed.jpg')
img = np.array(img)
# gn.mix([('text', '图片1'), ('img', img), ('text', 'end...')])
# gn.text("remote test2")
print(type(img),img.shape)