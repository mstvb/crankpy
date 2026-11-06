from crankpy import __version__


def test_version_is_defined() -> None:
    assert __version__


def test_cli_help(capsys) -> None:
    from crankpy.cli import main

    assert main() == 0
    assert "usage:" in capsys.readouterr().out.lower()
