import glob
import os


def get_abs_paths(root_path: str, ext_filter: str = None) -> list:
    if not os.path.exists(os.path.dirname(root_path)):
        print("Error: path does not exist")
        raise ValueError
    if ext_filter[0] != ".":
        print("Error: ext_filter must start with a dot (.)")
        raise ValueError

    out = glob.glob(os.path.join(root_path, "**", f"*{ext_filter}"), recursive=True)

    for i in out:
        i = f"{os.getcwd()}" + i
    out = sorted(out)
    return out
