#!/bin/bash

magick -size 720x720 xc:white white.png
mkdir original-glyphs

for filename in ./cropped-icons/*.png; do
    echo "Removing BG for $filename"
    newName="${filename##*/}"

    magick composite $filename cropped-icons/999999.png -compose minus diff.png
    magick diff.png -channel RGB -separate +channel -evaluate-sequence add mask.png
    magick white.png -channel A mask.png -compose copyopacity -composite original-glyphs/$newName
done 

rm diff.png
rm mask.png
rm white.png

