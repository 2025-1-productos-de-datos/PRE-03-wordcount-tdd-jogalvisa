import os


def read_all_lines(input_folder):
    pass
    """Read all lines from files in the input folder."""
    lines = []
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as f:
                lines.extend(f.readlines())
    return lines