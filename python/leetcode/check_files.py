import os

fnames = []
for dirpath, dirnames, fname in os.walk("."):
    for item in fname:
        fnames.append(item)
        # print(item)

n_set = set()
for fname in fnames:
    if fname.endswith(".py"):
        no_ = fname.split("_")
        try:
            no_ = int(no_[0])
            assert (no_ not in n_set, no_)
            n_set.add(no_)
            # print(no_)
        except ValueError:
            pass

print("%d problems checked in." % len(n_set))
# print(n_set)
missing = []
for i in range(1, 725):
    if i not in n_set:
        missing.append(i)
print("%d problems missing." % len(missing))
print(missing)
