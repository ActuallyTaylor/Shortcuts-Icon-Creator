# 59392 - 61588
import os

def resetFolders():
    print("=== Resetting Folders ===")
    os.system("rm -rf ./generatedShortcuts")
    os.system("mkdir generatedShortcuts")
    print("=== Done Resetting Folders ===")

def create_shortcuts_files():
    print("=== Creating Shortcuts File ===")
    shortcut_id_range = range(57344, 63744)
    blank_shortcut = open("blank.shortcut", "r").read()

    for id in shortcut_id_range:
        filled_shortcut = blank_shortcut.replace("{ID}", f"{id}")
        f = open(f"./generatedShortcuts/{id}.shortcut", "x")
        f.write(filled_shortcut)
        f.close()
    print("=== Done Creating Shortcuts Files ===")

def sign_shortcuts():
    print("=== Signing Shortcuts ===")
    os.system("./signAllShortcuts.bash")
    print("=== Done Signing Shortcuts ===")

def part_1():
    resetFolders()
    create_shortcuts_files()
    sign_shortcuts()

def part_2():
    print("=== Retrieving All Icons ===")
    os.system('shortcuts run "Icon Ripper (Library)"')
    print("=== Done Retrieving All Icons ===")

def optimize_icons():
    print("=== Optimizing Icons ===")
    os.system('./meta/optimizeIcons.cmd')
    print("=== Done Optimizing Icons ===")

def crop_icons():
    print("=== Cropping Icons ===")
    os.system('./meta/crop.cmd')
    print("=== Done Cropping Icons ===")

def remove_background():
    print("=== Removing Backgrounds From Icons ===")
    os.system('./meta/removeBG.cmd')
    print("=== Done Removing Backgrounds From Icons ===")

def palette_reduction():
    print("=== Reducing Icon Palette ===")
    os.system('./meta/paletteReduction.cmd')
    print("=== Done Reducing Icon Palette ===")

def optimize_glyphs():
    print("=== Optimizing Icons ===")
    os.system('./meta/optimizeGlyphs.cmd')
    print("=== Done Optimizing Icons ===")

def part_3():
    if os.name != 'nt':
        print("Please run this part on a windows machine.")
        exit(1)
    optimize_icons()
    crop_icons()
    remove_background()
    palette_reduction()
    optimize_glyphs()

def main():
    part = input("Which Part? (1, 2, 3): ")
    if int(part) == 1:
        part_1()
    elif int(part) == 2:
        part_2()
    elif int(part) == 3:
        part_3()

if __name__=="__main__":
    main()