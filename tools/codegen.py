import glob
import os
from pathlib import Path

from grpc_tools import protoc


def clean() -> None:
    proto_files = glob.glob("src/*pb2*.py*", recursive=True)
    for file in proto_files:
        os.remove(file)


def gen() -> None:
    current_dir = Path.cwd()
    proto_dir = (current_dir / "proto").resolve()
    src_dir = (current_dir / "src").resolve()

    args = [
        "",
        f"--proto_path={proto_dir}",
        f"--python_out={src_dir}",
        f"--grpc_python_out={src_dir}",
        f"{proto_dir}/wireguard.proto",
        f"--mypy_out={src_dir}",
    ]

    protoc.main(args)
