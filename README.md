# pad-sequences-multi
pad variable length sequences with multiples features


## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Commands](#commands)
* [Support](#support)
* [Contributing](#contributing)


## Installation
The `pad-sequences-multi` [git repo](http://github.com/ulf1/pad-sequences-multi) 
is a private repo

```
pip install git+ssh://git@github.com/ulf1/pad-sequences-multi.git
```


## Usage

```
from pad_sequences_multi import pad_sequences_multi
import tensorflow as tf
# import torch

seq = []
seq.append([[1, 1, 1], [2, 2, 2]])
seq.append([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])

n_samples = len(seq)
n_features = len(seq[0][0])
n_timesteps = 3

# for input sequences
padded = pad_sequences_multi(seq, padding='pre', value=0, 
                             truncating='pre', maxlen=n_timesteps)

# for output sequences
# padded = pad_sequences_multi(seq, padding='post', value=0, 
#                              truncating='post', maxlen=n_timesteps)


X = tf.reshape(padded, [n_samples, n_timesteps, n_features])
# X = torch.reshape(torch.tensor(padded), [n_samples, n_timesteps, n_features])
```


Check the [examples](http://github.com/ulf1/pad-sequences-multi/examples) folder for notebooks.


## Commands
Install a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
pip3 install jupyterlab "tensorflow==2.0.0-beta1" "torch==1.1.0" "numpy>=1.14.5"
```

(If your git repo is stored in a folder with whitespaces, then don't use the subfolder `.venv`. Use an absolute path without whitespaces.)

Python commands

* Jupyter for the examples: `jupyter lab`
* Check syntax: `flake8 --ignore=F401 --exclude=$(grep -v '^#' .gitignore | xargs | sed -e 's/ /,/g')`
* Run Unit Tests: `pytest`
* Upload to PyPi with twine: `python setup.py sdist && twine upload -r pypi dist/*`

Clean up 

```
find . -type f -name "*.pyc" | xargs rm
find . -type d -name "__pycache__" | xargs rm -r
rm -r .pytest_cache
rm -r .venv
```


## Debugging
* Notebooks to profile python code are in the [profile](http://github.com/ulf1/pad-sequences-multi/profile) folder


## Support
Please [open an issue](https://github.com/ulf1/pad-sequences-multi/issues/new) for support.


## Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/ulf1/pad-sequences-multi/compare/).
