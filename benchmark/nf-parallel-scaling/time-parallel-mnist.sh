#!/bin/bash
#
# Runs neural-fortran MNIST training example
# with several different nprocs, for a total
# of five runs.

for run in {1..5}; do
    echo Run ${run}:
    for nproc in 1 2 3 4 5 6 8 10 12; do
        echo Running on $nproc cores
	cafrun -n $nproc ./example_mnist >> run${run}.txt
    done
done
