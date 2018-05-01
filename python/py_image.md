# Image Handling

## support in scipy.misc
- read
```python
from scipy.misc import imread, imresize, imsave

im = imread('Poisson.jpg') 
plt.imshow(im)
plt.show()

# to read and show grey scale images
im = imread('Poisson.jpg', flatten=True) 
plt.imshow(im, cmap='gray')
plt.show()
```
- write
```python
imsave('test.jpg', im)
```
- resize
```python
im = imresize(im, (28,28), interp='nearest')
```

## support in PIL.Image
```python
from PIL import Image

# class 'PIL.Image.Image'
im = Image.open('Poisson.jpg').convert("L")
arr = np.asarray(im)
plt.imshow(im, cmap='gray')
plt.show()

im = Image.open('Poisson.jpg').convert("RGB")
```