"""Python-to-Lua compiler entry points (implementation not yet available)."""

from __future__ import annotations

from pathlib import Path


def compile_file(source: Path, output: Path) -> None:
    """Compile a crankpy source file to Lua.

    This is a placeholder for the planned compiler. The supported Python subset
    and code generation behavior are described in ``docs/compiler-design.md``.
    """
    raise NotImplementedError("Python-to-Lua compilation is not implemented yet")
