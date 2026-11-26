from pathlib import Path

contents = "I love programing.\n"
contents += "I love creating new games.\n"
contents += "I also love working whith data.\n"

path = Path('programming.txt')
path.write_text(contents)
