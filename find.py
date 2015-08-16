import re
import os

PAT_MD_FILE = re.compile(r'.*\.md')

# ![](/static/img/iotcookbook/weighingpad/assembly_final.jpg)
PAT_IMG_LINK1 = re.compile(r'!\[.*\]\((.*\.(jpg|png|svg))\)')

# src="../../static/img/iotcookbook/weighingpad/assembly_final.jpg"
PAT_IMG_LINK2 = re.compile(r'src="(.*\.(jpg|png|svg))"')


for root, dirs, files in os.walk('pages'):
    for name in files:
        if PAT_MD_FILE.match(name.lower()):
            fp = os.path.join(root, name)
            with open(fp) as fd:
                content = fd.read()
                for pat in [PAT_IMG_LINK1, PAT_IMG_LINK2]:
                    for match in re.finditer(pat, content):
                        print fp, match.groups()[0]
