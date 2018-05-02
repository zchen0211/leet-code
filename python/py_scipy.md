# Scipy and sklearn

## scipy
- A free and open-source Python library used for scientific computing and technical computing.
- https://www.scipy.org/
- Related document and papers: https://www.scipy.org/citing.html
- Core projects: **numpy, scipy, matplotlib, iPython, SymPy, Pandas**
- KD-Tree:
```python
from scipy import spatial

points = np.array([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
tree = spatial.KDTree(points)
```

## scikit-learn
- scikit-learn: Machine Learning in Python.
- Simple and efficient tools for data mining and data analysis;
- Accessible to everybody, and reusable in various contexts; Built on NumPy, SciPy, and matplotlib;
- Open source, commercially usable - BSD license.
- support **support vector machines, random forests, gradient boosting, k-means and DBSCAN**
```python
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier

### random forest classifier
x = [[0., 0.], [0.,1.], [1.,0.], [1.,1.]]
y = [1, 0, 0, 1]
clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(x, y)
```