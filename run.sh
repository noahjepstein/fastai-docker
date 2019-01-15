#!/bin/bash

RUN_JUPYTER="jupyter notebook --ip=0.0.0.0 --no-browser --allow-root"

ln -s /storage /notebooks/course-v3/nbs/dl1/data
tmux new-session -s jupyter $RUN_JUPYTER
