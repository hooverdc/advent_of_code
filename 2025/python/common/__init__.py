from argparse import ArgumentParser, Namespace
from pathlib import Path

# common

parser = ArgumentParser()
parser.add_argument("--input", type=Path, required=True)

class CliNamespace(Namespace):
    input: Path

def get_input() -> Path:
    return parser.parse_args(namespace=CliNamespace()).input
