# How to use the remove function

## Load the Image
```python
from remove_bg import remove_byte,remove_direct,remove_cv2,remove_path

input_path = "path/to/input"
output_path = "path/to/output"
```
## Removing the background

### With Byte Architecture
```python
success = remove_byte(input_path:str,output_path:str)
print(success)
```

### With direct
```python
success = remove_direct(input_path:str,output_path:str)
print(success)
```

### With cv2
```python
success = remove_cv2(input_path:str,output_path:str)
print(success)
```

### With path
```python
success = remove_path(input_path:str,output_path:str)
print(success)
```


## Authors

- [@MyFaduGame](https://www.github.com/myfadugame)

