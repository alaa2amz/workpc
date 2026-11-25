from pathlib import Path
import yaml
from pprint import pp
import sys
from cas import Skell
import json
import subprocess

var_prefix = "var"
data_prefix = "data"
skell_spec_name = data_prefix + "/" + "skell_spec.yaml"
skell_script_name = var_prefix + "/" + "skell.tcl"


def main():
    Path("var").mkdir(parents=True, exist_ok=True)
    Path("var/skell").mkdir(parents=True, exist_ok=True)
    Path("var/equips").mkdir(parents=True, exist_ok=True)
    Path("var/piping").mkdir(parents=True, exist_ok=True)
    gen_skell()


def gen_skell():
    with open(skell_spec_name) as skell:
        skell_dict = yaml.safe_load(skell)
    # pp(skell_dict,)
    skell = Skell(skell_dict)
    stdout_orig = sys.stdout
    with open(skell_script_name, "w+") as f, open("ll", "w") as l:
        sys.stdout = f
        skell.insert()
        f.flush()
        f.seek(0)
        sys.stdout = stdout_orig
        p = subprocess.run(
            ["mged", "-c", "site.g"], stdin=f, stdout=l, stderr=subprocess.STDOUT
        )
        pp(p.__dict__)


if __name__ == "__main__":
    main()
