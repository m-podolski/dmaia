import re

input_file = "1-Logic-and-Proofs/1-5-Nested-Quantifiers.md"

regex_patterns: dict[re.Pattern[str], str] = {
    # Clean
    # remove "- "-gaps
    re.compile(r"(?m)(\w)- (\w)"): r"\1\2",
    # remove asterisks from before numbers and put into parens
    re.compile(r"(?m)^(\∗{1,2}) ([\w\d]{1,2}[\.)])"): r"\2 (\1)",
    # remove leading, trailing and in-between whitespace from part-indexes
    re.compile(r"(?m)^\s?(\w) ?\) ?"): r"(\1) ",
    # Format
    # join lines
    re.compile(r"(?m)[\r\n](?!^\(\w\)|\d{1,2}\. )"): r" ",
    # add line above intro
    re.compile(r"(?m)^([\d]{1,2}[\.)])"): r"\n\1",
    # add bullets to part-indexes
    re.compile(r"(?m)^(\(\w\) )"): r"- \1",
}

with open(input_file, "r") as file:
    content: str = file.read()

for pattern, replacement in regex_patterns.items():
    content = re.sub(pattern, replacement, content)

with open(input_file, "w") as file:
    file.write(content)
