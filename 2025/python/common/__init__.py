from argparse import ArgumentParser, Namespace
from pathlib import Path
import time
from contextlib import contextmanager

# common

parser = ArgumentParser()
parser.add_argument("--input", type=Path, required=True)

class CliNamespace(Namespace):
    input: Path

def get_input() -> Path:
    return parser.parse_args(namespace=CliNamespace()).input

@contextmanager
def timer():
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    print(f"Execution time: {(end - start) * 1000:.2f} ms")
