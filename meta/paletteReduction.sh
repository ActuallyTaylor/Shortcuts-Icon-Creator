#!/bin/bash

for filename in ./original-glyphs/*.png; do
    echo "Reducing palette for $filename"
    newName="${filename##*/}"

    magick $filename +dither -remap palette.txt 4bit-glyphs/$newName
done