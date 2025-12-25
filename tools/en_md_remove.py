import os
import re
import sys

os.chdir(sys.path[0])

input_path = "../ResidenceLawOrigin.md"
out_path = "../output/ResidenceLawOrigin-remove.md"

with open(input_path, "r", encoding="utf-8") as f:
    origin_text = f.read()


pattern = re.compile(
    r'^\s*\[table of contents\]\(https?://[^)\s]+\)\s*$',
    re.MULTILINE
)

cleaned_text = re.sub(pattern, '', origin_text)

with open(out_path, "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print("done!")