magick -size 720x720 xc:white white.png
MKDIR original-glyphs
FOR %%f IN (cropped-icons\*.png) DO (
    magick composite %%f cropped-icons\999999.png -compose minus diff.png
    magick diff.png -channel RGB -separate +channel -evaluate-sequence add mask.png
    magick white.png -channel A mask.png -compose copyopacity -composite original-glyphs\%%~nf.png
)
DEL diff.png
DEL mask.png
DEL white.png