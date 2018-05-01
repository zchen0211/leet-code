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