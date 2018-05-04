# Python Package and Environment

## conda
- conda self
```
conda --version
conda update conda
```
- Environment
    - List all envs
```
conda info --envs
```
    - Create an environment
```
conda create --name snowflake biopython
source activate snowflakes

source deactivate
```
    - Clone an environment
```
conda create -n flowers --clone snowflakes
```
    - Remove an environment
```
conda remove -n flowers 
```
- Packages
    - List packages
```
conda list
```
    - Install a package
```bash
conda install --name bunnies beautifulsoup4
# same as
activate bunnies
conda install beautifulsoup4

# install from Anaconda.org
conda install--channel https：//conda .anaconda.ort/pandas bottleneck

# check online at pypi for packages
pip install xxx

# from source
python setup.py install
```
- To remove:
```
# To remove a package
conda remove -n bunnies iopro

# To remove an environment
conda remove -n snakes --all

# remove conda
rm -rf ~/miniconda 
```
