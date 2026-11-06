"""Command-line interface for crankpy."""

from __future__ import annotations

import argparse

from crankpy import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="crankpy",
        description="Author Playdate games in Python (compiler under development).",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("compile", help="Compile a Python game (not implemented yet)")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "compile":
        parser.error("the Python-to-Lua compiler is not implemented yet")
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
