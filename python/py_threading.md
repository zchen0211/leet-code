# Multi-Threading in Python

## With Library threading
```python
import threading

def worker(num=0):
  print('Worker %d' % num)
  return

if __name__ == '__main__':
  threads = []
  for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

  for i in range(5):
    threads[i].join()
```

## With Library multithreading
```python
from multiprocessing.dummy import Pool as ThreadPool 
pool = ThreadPool(4) 
results = pool.map(my_function, my_array)
```