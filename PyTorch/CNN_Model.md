# General Paradigm

## Components
- Loss
```python
criterion = nn.CrossEntropyLoss().cuda(args.gpu=None)
```
- Optimizer
```python
optimizer = torch.optim.SGD(model.parameters(), args.lr,
                                momentum=args.momentum,
                                weight_decay=args.weight_decay)
```
- Resume checkpoint
```python
checkpoint = torch.load(args.resume)
model.load_state_dict(checkpoint['state_dict'])
optimizer.load_state_dict(checkpoint['optimizer'])
```

## Hogwild
- Support both CPU and GPU:
```python
use_cuda = args.cuda and torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")
dataloader_kwargs = {'pin_memory': True} if use_cuda else {}
```
- Multiprocessing
```python
import torch.multiprocessing as mp

mp.set_start_method('spawn')

model = Net().to(device)
model.share_memory() # gradients are allocated lazily, so they are not shared here
```
- 
```python
processes = []
for rank in range(args.num_processes):
    p = mp.Process(target=train, args=(rank, args, model, device, dataloader_kwargs))
    # We first train the model across `num_processes` processes
    p.start()
    processes.append(p)

for p in processes:
    p.join()
```