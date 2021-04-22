import argparse
import pyexiv2

def ClearAllMetadata(filename, preserve):
    img = pyexiv2.Image('r',filename)
    img.clear_comment()
    img.close()

def AddComment(filename):
    with pyexiv2.Image(filename) as img:
        valueMsg = input("Input your msg  (q to quit) =" )
        if not valueMsg == 'q':
            if valueMsg != '':
                img.modify_comment(valueMsg)

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("img", help = "Image file to add msg in the metadata")
    parser.add_argument("--clear","-c", help ="Clear all metadata from the file", action="store_true")
    args = parser.parse_args()
    if args.img:
        if args.clear:
            ClearAllMetadata(args.img, args.preserve)
        else:
            AddComment(args.img)
    else:
        print(parser.usage)

if __name__ == "__main__":
    Main()
