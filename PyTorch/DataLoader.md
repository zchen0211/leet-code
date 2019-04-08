# Data Loader, Dataset

## Data Loader
- Create dataset on your own
```python
import torchvision.datasets

normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])

train_dataset = datasets.ImageFolder(
        traindir,
        transforms.Compose([
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            normalize,
        ]))

train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset)
```
- In the dataset, data.Dataset is an abstract class and you need to implement:
```python
class DatasetFolder(data.Dataset):
	def __init__(self, ...):

	def __getitem__(self, index):
		return sample target

	def __len__(self):
		return len(...)

	def __repr__(self): # optional
```
- cifar style:
```python
img, target = self.data[index], self.targets[index]

# doing this so that it is consistent with all other datasets
# to return a PIL Image
img = Image.fromarray(img)

if self.transform is not None:
    img = self.transform(img)

if self.target_transform is not None:
    target = self.target_transform(target)

return img, target
```
- Wrap a loader
```python
train_loader = torch.utils.data.DataLoader(
    train_dataset, batch_size=args.batch_size, shuffle=(train_sampler is None),
        num_workers=args.workers, pin_memory=True, sampler=train_sampler)
```