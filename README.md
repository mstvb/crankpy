# crankpy

> Write Playdate games in Python. crankpy is an experimental toolchain that aims to translate a supported subset of Python into Lua for the official Playdate SDK.

**Status: early scaffold.** The package layout and project documentation are in place; Python-to-Lua compilation and packaging are not implemented yet. Do not expect to build or run games with this version.

## Table of contents

- [Project goals](#project-goals)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick start](#quick-start)
- [Project layout](#project-layout)
- [Development](#development)
- [Documentation](#documentation)
- [Project links](#project-links)

## Project goals

crankpy is intended to provide:

- A Python-facing API for common Playdate game features.
- A compiler for a documented, deliberately limited subset of Python that emits Lua.
- A command-line tool to build a game and launch it in the Playdate Simulator.
- Examples and tests that make the supported language and API clear.

The official Playdate SDK supports Lua and C. crankpy's planned approach is to generate Lua for the SDK rather than run Python on the device. Initially, arbitrary Python features and third-party Python packages will not be supported.

## Requirements

For development, use Python 3.10 or later. Building and running a Playdate game will also require the official Playdate SDK and Simulator. The compiler and SDK integration are not available in this scaffold yet.

## Installation

The package is not published to PyPI yet. From a clone of this repository, install it in editable mode:

```bash
python -m pip install -e ".[dev]"
```

## Quick start

The command-line entry point is scaffolded, but game compilation is not implemented yet. Check the available commands with:

```bash
crankpy --help
```

A future minimal game is planned under [`examples/hello_world`](examples/hello_world).

## Project layout

```text
src/crankpy/       Python package and CLI
examples/          Example game sources
 tests/             Automated tests
docs/              Design and usage documentation
```

## Development

```bash
python -m pip install -e ".[dev]"
pytest
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup, testing, and contribution guidance. Notable changes are recorded in [CHANGELOG.md](CHANGELOG.md).

## Documentation

- [Contributing guide](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)
- [Compiler design notes](docs/compiler-design.md)

## Project links

- Repository: <https://github.com/mstvb/crankpy>
- Issue tracker: <https://github.com/mstvb/crankpy/issues>
- Playdate developer documentation: <https://dev.play.date/>

The README, changelog, and contribution-guide structure is adapted from the documentation templates in these Gists: [27005d5eb90695ae3141386d276c0257](https://gist.github.com/mstvb/27005d5eb90695ae3141386d276c0257), [44cb3d9aeed7afa407b7b9765ac55173](https://gist.github.com/mstvb/44cb3d9aeed7afa407b7b9765ac55173), and [4122d0f3bbbcd2d77c23d52ce0617f3e](https://gist.github.com/mstvb/4122d0f3bbbcd2d77c23d52ce0617f3e). Wording and sections have been adapted for crankpy.
