# Some Popular Libraries

## mock
```pyhon
import mock

class Foo(object):
  def echo(self, *args):
    return "hello"

foo = Foo()
foo.echo = mock.MagicMock()
foo.echo.return_value = "mock value"

foo.echo() # 'mock value'
```
- Mock with patch
```python
def my_func():
  # tf.get_variable() called
  # ...
  
def custom_get_variable(*args, **kwargs):
  # do something...

with mock.patch('tensorflow.get_variable', custom_get_variable):
  return my_func()
```

## tqdm
- Usage: just wrap iteration with tqdm, then progress bar will show:
- A good article: http://skyrover.me/2017/08/08/tqdm%20%E8%AF%A6%E8%A7%A3/
```python
from tqdm import tqdm

for i in tqdm(range(10000)):
    ...
```
- Inside tqdm
```python
def tqdm(iterable, desc='', total=None, leave=False, file=sys.stderr,
         mininterval=0.5, miniters=1):

# control progress bar printing
def format_meter(n, total, elapsed):
```