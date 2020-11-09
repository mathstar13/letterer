Letterer is more string methods.
To install, use:
```
pip install letterer
```
Letterer includes the methods:  
__isfirstwordtitle__ checks to see if the first word is title:
```python
from letterer import isfirstwordtitle
txt = 'YAY'
isfirstwordtitle(txt) #returns True
txt = 'yAY'
isfirstwordtitle(txt) #returns False
```
__islower__ checks if the string is lower:
```python
from letterer import islower
txt = 'yay'
islower(txt) #returns True
txt = 'Yay'
islower(txt) #returns False
```
__istitle__ checks if an entire string is title:
```python
from letterer import istitle
txt = 'YAY Yay'
istitle(txt) #returns True
txt = 'yAY yay'
istitle(txt) #returns False
```
__isupper__ checks if a string is in upper:
```python
from letterer import isupper
txt = 'YAY YAY'
isupper(txt) #returns True
txt = 'YAY YaY'
isupper(txt) #returns False
```
__getupper__ gets the character location for uppercase letters:
```python
from letterer import getupper
txt = 'YAY YAY'
getupper(txt) #returns [1, 2, 3, 5, 6, 7]
txt = 'YAY YaY'
getupper(txt) #returns [1, 2, 3, 5, 7]
```
