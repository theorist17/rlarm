# RLARM

RLARM is a Python library for 3d printed arm robot.

## Installation

Use the package manager [conda](https://docs.conda.io/en/latest/) to install RLARM.

```bash
git clone https://github.com/theorist17/rlarm/
cd rlarm
conda create -f environment.yaml --name rlarm
conda activate rlarm
cd gym_rlarm
python setup.py install
cd ..
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
