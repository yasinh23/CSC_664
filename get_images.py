import argparse
from excav8r import Excva8r
import os
from PIL import Image
from app.backend.utils import randomize_mtime, gallery_as_path_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--keyword', type=str, required=True)
    parser.add_argument('--max', type=int, nargs='?', const=100, default=100)
    parser.add_argument('--dest', type=str, nargs='?', const='./gallery/', default='./gallery/')
    args = parser.parse_args()

    scraper = Excva8r()
    images = scraper.getDuckDuckGo(args.keyword, max=args.max, as_list=True)

    if not os.path.exists(args.dest):
        os.mkdir(args.dest)

    # randomize image creation data
    for i, image in enumerate(images):
        print(f'{args.dest}{args.keyword.replace(" ","_")}_{i}.jpeg')
        image.convert("RGB")
        image.save(f'{args.dest}{args.keyword.replace(" ","_")}_{i}.jpg')

    for im in gallery_as_path_list(args.dest):
        randomize_mtime(im)
