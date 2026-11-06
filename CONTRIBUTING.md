# Contributing to crankpy

Thanks for your interest in contributing! crankpy is at an early stage, so design discussions and small, focused contributions are especially useful.

## Before you start

- Check existing [issues](https://github.com/mstvb/crankpy/issues) before starting substantial work.
- For a larger feature, open an issue first to agree on the supported Python subset, generated Lua behavior, or public API.
- Keep generated Lua compatible with the official Playdate SDK and document any limitations.

## Setup

1. Install Python 3.10 or later.
2. Clone the repository and enter its directory.
3. Install the package and development dependencies:

   ```bash
   python -m pip install -e ".[dev]"
   ```

4. Confirm the command is available:

   ```bash
   crankpy --help
   ```

The official Playdate SDK is only needed for work involving Simulator or device integration. It is not currently required for the scaffold's tests.

## Testing

Run the test suite from the repository root:

```bash
pytest
```

Add or update tests for changes to the compiler, CLI, or game API. If a change depends on the Playdate SDK, explain how it was verified and note any SDK-specific prerequisites.

## Documentation

Update the README, compiler design notes, and changelog when behavior or project direction changes. Prefer documenting unsupported language constructs explicitly rather than implying full Python compatibility.

## Pull requests

- Keep changes focused and use descriptive commit messages.
- Include tests and documentation where applicable.
- Clearly state what was tested and what remains incomplete.
- Do not commit generated build artifacts or local SDK paths.

## Code of conduct

Be respectful and constructive in discussions and reviews. Report unacceptable behavior to the project maintainers.
