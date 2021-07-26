#!/usr/bin/env bash

# instalando dependências em pasta temporária
pip3 install -r requirements.txt --target ./packages

# zip dependências
cd packages
zip -9mrv packages.zip .
mv packages.zip ..
cd ..

# removendo a pasta temporária
rm -rf packages

# adicionando utils ao zip de dependências
zip -ru9 packages.zip utils -x utils/__pycache__/\*

exit 0
