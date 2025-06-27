# DiskGen
# Simple radial profile generator for synthetic protoplanetary disks

## Requirements
- Python 3.8+
- see `requirements.txt`


## Project Structure

- `src/diskgen/`: Main source code
- `Notebooks/`: Jupyter notebook tests and experiments
- `Notebooks/Output/`: Automatically generated FITS images (ignored in git)

## Features

- Create radial intensity profiles with power laws
- Add Gaussian-shaped rings
- Generate 2D disk images
- Export to FITS format

## Setup
```bash
git clone https://github.com/TomLostInSpace/DiskGen.git
cd DiskGen

```bash
pip install -r requirements.txt
pip install -e .