## Add Comment to Metadata


how to use:

write comment
```
python3 add_meta.py -w cat.jpg
```

read comment

```
python3 add_meta.py -r cat.jpg
```




install terlebih dahulu pyexiv2

```
pip3 install pyexiv2
```
kemudian import kedalam python

```
import pyexiv2

```

1. Read file image

```
img = pyexiv2.Image(filename)
```
2. Modify Comment

```
img.modify_comment('text comment')
```
3. Read Comment
there are 2 way to read comment:
* with bash
```
exiftool
```
* with python3
```
img.read_comment()
```




next update:
1. Encryption the comment
2. Decryption the comment
3. Add file into Image
