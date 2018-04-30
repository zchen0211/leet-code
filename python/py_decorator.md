# Decorator

## A wrapper on a function:
- Some good materials: http://www.cnblogs.com/SeasonLee/articles/1719444.html, https://www.cnblogs.com/cicaday/p/python-decorator.html
```python
def debug(func):
    def wrapper(*args, **kwargs):  # fit any arguments passing
        print "[DEBUG]: enter {}()".format(func.__name__)
        print 'Prepare and say...',
        return func(*args, **kwargs)
    return wrapper  # return

@debug
def say(something):
    print "hello {}!".format(something)
```
- Decorator with arguments:
```python
def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print "[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__)
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say(something):
    print "say {}!".format(something)

# equal to
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do(something):
    print "do {}...".format(something)

if __name__ == '__main__':
    say('hello')
    do("my work")
```
