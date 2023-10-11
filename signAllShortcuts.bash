#!/bin/bash
for filename in ./generatedShortcuts/*.shortcut; do
    echo "Signing $filename"
    shortcuts sign --input $filename --output $filename;
done 