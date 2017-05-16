import numpy as np
from skimage import data
from skimage import io
from skimage.viewer import ImageViewer
import matplotlib.pyplot as plt

coins = data.coins()
viewer = ImageViewer(coins)
#viewer.show()
histo = np.histogram(coins, bins=np.arange(0, 256))
plt.bar(histo, align='center')
plt.show()

from skimage.filter import canny
edges = canny(coins/255.)
viewer = ImageViewer(edges)
#viewer.show()
from scipy import ndimage as ndi
fill_coins = ndi.binary_fill_holes(edges)
viewer = ImageViewer(fill_coins)
#viewer.show()


label_objects, nb_labels = ndi.label(fill_coins)
sizes = np.bincount(label_objects.ravel())
mask_sizes = sizes > 20
mask_sizes[0] = 0
coins_cleaned = mask_sizes[label_objects]

markers = np.zeros_like(coins)
markers[coins < 30] = 1
markers[coins > 150] = 2

from skimage.filter import sobel
elevation_map = sobel(coins)
viewer = ImageViewer(elevation_map)
#viewer.show()

markers = np.zeros_like(coins)
markers[coins < 30] = 1
markers[coins > 150] = 2

from skimage.morphology import watershed
segmentation = watershed(elevation_map, markers)


segmentation = ndi.binary_fill_holes(segmentation - 1)

labeled_coins, _ = ndi.label(segmentation)

viewer = ImageViewer(segmentation)
viewer.show()