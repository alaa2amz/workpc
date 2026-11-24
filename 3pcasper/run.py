from pathlib import Path
import yaml
from pprint import pp
import sys
from cas import Skell

var_prefix = "var"
data_prefix = "data"
skell_file_name = "skell_spec.yaml"
skell_script_name = var_prefix + "/" + "skell.tcl"


def main():
    Path("var").mkdir(parents=True, exist_ok=True)
    gen_skell()


def gen_skell():
    skell_path = Path(data_prefix) / Path(skell_file_name)
    with skell_path.open() as skell:
        skell_dict = yaml.safe_load(skell)
    pp(skell_dict)
    skell = Skell(skell_dict)
    stdout_orig = sys.stdout
    with open(skell_script_name, "w") as f:
        sys.stdout = f
        skell.insert()
        sys.stdout = stdout_orig


if __name__ == "__main__":
    main()
