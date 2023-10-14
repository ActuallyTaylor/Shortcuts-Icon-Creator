#!/bin/bash
mkdir cropped-icons

for filename in ./original-icons/*.png; do
    echo "Cropping $filename"
    newName="${filename##*/}"
    magick $filename -crop 720x720+152+152 cropped-icons/$newName
done 