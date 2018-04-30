# Python Environment

## Variables
```python
a = None
del a
```
- Check all variables in the memory
```python
print(dir())
```
- Local and global variables in the current scope
```python
globals()
locals()
```

## Parse from os.envirson
- A bash run like:
```bash
root=xxx game=elfgames.go.game model_file=elfgames.go.df_model3 python3 -u df_selfplay.py
```
- library os will parse environment variables as strings, envs will be a dictrionary:
```python
import os
envs = os.environ

# we will have
envs["root"] = "xxx"
envs["game"] = "elfgames.go.game"
...
```

## Load Modules by Name
- python 3.6 importlib library
```python
import importlib
module = importlib.import_module("argparse")

# module is now numpy
module = importlib.import_module("numpy")
module.zeros([2, 4])
```