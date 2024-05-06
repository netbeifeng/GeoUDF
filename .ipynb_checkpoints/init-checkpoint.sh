# /bin/bash

source $CONDA_PREFIX/etc/profile.d/conda.sh

# Delete if already exists
conda env remove -n geoudf -y

conda create -n geoudf python=3.8 -y
conda activate geoudf 
conda install -y cudatoolkit=11.3 -c nvidia
conda install -y pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 -c pytorch 

pip install fvcore
pip install --no-index --no-cache-dir pytorch3d -f https://dl.fbaipublicfiles.com/pytorch3d/packaging/wheels/py38_cu113_pyt1110/download.html
pip install open3d
pip install point-cloud-utils
pip install trimesh
pip install numba
pip install networkx
cd pointnet2_ops_lib   
python setup.py install
