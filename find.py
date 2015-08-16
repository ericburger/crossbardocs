# Searches through all Markdown files in subfolder "pages", looking
# for image links (either Markdown syntax or HTML syntax).
# The list of found image links is printed.

import re
import os

PAT_MD_FILE = re.compile(r'.*\.md')

# ![](/static/img/iotcookbook/weighingpad/assembly_final.jpg)
PAT_IMG_LINK1 = re.compile(r'!\[.*\]\((.*\.(jpg|png|svg))\)')

# src="../../static/img/iotcookbook/weighingpad/assembly_final.jpg"
PAT_IMG_LINK2 = re.compile(r'src="(.*\.(jpg|png|svg))"')

found = {}

for root, dirs, files in os.walk('pages'):
    for name in files:
        if PAT_MD_FILE.match(name.lower()):
            fp = os.path.join(root, name)
            with open(fp) as fd:
                content = fd.read()
                for pat in [PAT_IMG_LINK1, PAT_IMG_LINK2]:
                    for match in re.finditer(pat, content):
                        img_path = match.groups()[0]
                        if img_path not in found:
                            found[img_path] = set()
                        if fp not in found[img_path]:
                            found[img_path].add(fp)

for img_fp in sorted(found.keys()):
    print("{}".format(img_fp))
    if False:
        for md_fp in sorted(found[img_fp]):
            print("          {}".format(md_fp))
