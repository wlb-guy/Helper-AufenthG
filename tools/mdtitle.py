import os
import re
import sys

os.chdir(sys.path[0])

input_path = "../output/ResidenceLawOrigin-remove.md"
out_path = "../output/ResidenceLaw.md"

with open(input_path, "r", encoding="utf-8") as f:
    input_text = f.read()


# Chapter 
pattern = re.compile(
    r'\nChapter\s+(\d+)\s*\n\s*(.+)',
    re.IGNORECASE
)

input_text1 = pattern.sub(r'\n## Chapter \1 \2', input_text)

# Section
pattern = re.compile(
    r'\nSection\s+(\d+)\s*\n\s*(.+)',
    re.IGNORECASE
)

output_text = pattern.sub(r'\n### Section \1 \2', input_text1)

with open(out_path, "w", encoding="utf-8") as f:
    f.write(output_text)

print("done!")

