import os
import re
import sys
from functools import reduce  # pipeline

os.chdir(sys.path[0])

input_path = "../AufenthGOrigin.md"
out_path = "../output/AufenthG.md"

def link(input_text:str):
    pattern = re.compile(
        r'^\s*\[Nichtamtliches Inhaltsverzeichnis\]\(https?://[^)\s]+\)\s*$',
        re.MULTILINE
    )

    output_text = pattern.sub('', input_text)
    return output_text

def blank_list(input_text:str):
    pattern = re.compile(
        r'\n(\d+\.)\n\n',
        re.MULTILINE
    )

    output_text = pattern.sub(r'\n\1 ', input_text)
    return output_text


def apply_pipeline(input_text:str):
    return reduce(lambda x, fun: fun(x), pipeline, input_text)

if __name__ == "__main__":
    pipeline = [link,blank_list]

    with open(input_path, "r", encoding="utf-8") as f:
        input_text = f.read()

    output_text = apply_pipeline(input_text)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output_text)

    print("done!")

