# Utils
For every python programmer arrive the moment to create his packages.
This is my utils repo.

## Includes:

## Preprocessing:
Some preprocessing util functions:

* Features matrix
    - Standardize (numpy, pytorch)
    - Normalize   (numpy, pytorch)

## PCA
Calculate the PCA (numpy, pytorch)

## Scraper
Wrapper for manager a FireFox browser with selenium library.


email:  marcotreglia1@gmail.com


# Usage
* Preprocessing

```python
from mark_utils.preprocessing import Standardize, Normalize

# Numpy
x = np.random.rand(100,5)
x = Standardize.numpy(x)
x = Normalize.numpy(x)

# Pytorch (cuda enable)
x = torch.randn(100,5)
x = Standardize.torch(x)
x = Normalize.torch(x)
```

* PCA

```python
from mark_utils.pca import PCA

# Numpy
x = np.random.rand(100,5)
x_pca = PCA.numpy(x)

# Pytorch (cuda enable)
x = torch.randn(100,5)
x_pca = PCA.torch(x)
```

* Scraper

```python
from mark_utils.scraper import Scraper

# Init the browser
s = Scraper()

# Open url (For fun let's scrab some rocks!)
s.openUrl('http://www.radiofreccia.it/fm/')

# set target (In this case is the artist of the current song)
# create a dictionary with :  
# type: [xpath, class, id, tag, link] |  name : 'respectively target'

artist = dict(type='xpath', name='(//*[@class="white first-line"])[1]')

# Get the element from the webBrowser
element = s.get_element_BY(title)
print(artist_element.text)
'Imagine Dragons'

# Or if you want multiple element you can do :
title = dict(type='xpath',name='(//*[@class="white second-line"])[1]')
target_list = [artist, title ]
elements = s.get_element_BY(target_list)
for e in elements:
  print(e.text)

'Imagine Dragons'
'Thunder'

```

versione: 0.1.1
