# Compiler design (initial notes)

## Goal

Translate a documented subset of Python source into Lua that can run with the official Playdate SDK. crankpy is not intended to embed a general-purpose Python interpreter on the device or support every Python feature.

## Initial implementation milestones

1. Parse source with Python's built-in `ast` module and report syntax errors with useful locations.
2. Define a small supported subset and reject unsupported syntax explicitly.
3. Generate readable Lua for supported constructs, with focused unit tests for each construct.
4. Add a crankpy game API and map its calls to Playdate SDK APIs.
5. Package generated Lua and assets into a `.pdx` game bundle, then add Simulator integration.

## Candidate first subset

The exact subset is not finalized. A useful starting point may include constants, assignments, arithmetic and comparisons, function definitions, conditionals, bounded loops, and calls to a small crankpy API. Python's dynamic features, reflection, arbitrary imports, exceptions, and general-purpose third-party packages are out of scope unless explicitly designed later.

## Design principles

- Fail clearly when source uses unsupported syntax; do not silently generate incorrect behavior.
- Keep generated Lua deterministic and readable to help debugging.
- Separate Python syntax translation from Playdate API/runtime helpers.
- Test translations with both expected Lua output and, when available, the Playdate Simulator.
- Treat API and language-subset changes as compatibility decisions and document them.

## Open questions

- Which Python constructs are essential for the first playable example?
- Should users write one Python file or a small project with assets and metadata?
- How should source locations map into Lua errors and debugging output?
- Which SDK version and Simulator discovery mechanisms should be supported?
