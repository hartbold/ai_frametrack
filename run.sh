#!/bin/bash

# Obtener el directorio del script
pushd $PWD >/dev/null
dir=`dirname $0`
cd $dir
base_dir=$PWD
popd >/dev/null

/usr/bin/python3 $base_dir/app.py


