# Python Study

## Parsing Arguments
```python
import argparse

parser = argparse.ArgumentParser()

args = parser.parse_args()
```
-- Positional arguments (will throw error if missing)
```python
# positional parameters
parser.add_argument("echo")
```
-- Optional arguments (will throw error if missing)
```python
# 
parser.add_argument('-a', '--age')
```