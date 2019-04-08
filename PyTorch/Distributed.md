# Distributed Training

## Typical Setup
- Backend
	- GLOO (default for CPU)
	- MPI (optional)
	- NCCL (GPU)
- Distributed URL:
	- "env://" style:
	- "TCP" style:
- World Size: how many nodes

## Launch job
- In the main loop
```python
import torch.multiprocessing as mp

args.world_size = ngpus_per_node * args.world_size
mp.spawn(main_worker,
	nprocs=ngpus_per_node,
	args=(ngpus_per_node, args))
```
- In the function (main_worker in our case)
```python
import torch.distributed as dist

dist.init_process_group(backend="nccl",
	init_method=args.dist_url,
	world_size=args.world_size,
	rank=args.rank)

model = torch.nn.parallel.DistributedDataParallel(model)
```
- Single machine, multiple cards:
```python
model = torch.nn.DataParallel(model).cuda()
```
- Dataloader:
```python
train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset)

train_loader = torch.utils.data.DataLoader(
        train_dataset, batch_size=args.batch_size, shuffle=(train_sampler is None),
        num_workers=args.workers, pin_memory=True, sampler=train_sampler)
```
- Training:
```python
if args.distributed: train_sampler.set_epoch(epoch)
```
- Checkpointing:
```python
if args.rank % ngpus_per_ndoe == 0:
	torch.save(...)
```