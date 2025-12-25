import os
import re
import sys
from functools import reduce  # pipeline

os.chdir(sys.path[0])

input_path = "../output/ResidenceLawOrigin-remove.md"
out_path = "../output/ResidenceLaw.md"

def chapter(input_text:str):
    # Chapter 
    pattern = re.compile(
        r'\nChapter\s+(\d+)\s*\n\s*(.+)',
        re.IGNORECASE
    )

    output_text = pattern.sub(r'\n## Chapter \1 \2', input_text)
    return output_text

def division(input_text:str):
    # Division
    pattern = re.compile(
        r'\Division\s+(\d+)\s*\n\s*(.+)',
        re.IGNORECASE
    )

    output_text = pattern.sub(r'\n### Division \1 \2', input_text)
    return output_text

def section(input_text:str):
    # Section
    pattern = re.compile(
        r'\nSection\s+(\d+)\s*\n\s*(.+)',
        re.IGNORECASE
    )

    output_text = pattern.sub(r'\n#### Section \1 \2', input_text)
    return output_text

def sub_section(input_text:str):
    # Section 1[abc]
    pattern = re.compile(
        r'\nSection\s+(\d+[a-z]?)\s*\n\s*(.+)',
        re.IGNORECASE
    )

    output_text = pattern.sub(r'\n##### Section \1 \2', input_text)
    return output_text

def apply_pipeline(input_text:str):
    return reduce(lambda x, fun: fun(x), pipeline, input_text)

if __name__ == "__main__":
    pipeline = [chapter, division, section, sub_section]

    with open(input_path, "r", encoding="utf-8") as f:
        input_text = f.read()

    output_text = apply_pipeline(input_text)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output_text)

    print("done!")

