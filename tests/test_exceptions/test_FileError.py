import click


def test_file_error_surrogates():
    message = click.FileError(filename="\udcff").format_message()
    assert message == "Could not open file '�': unknown error"
