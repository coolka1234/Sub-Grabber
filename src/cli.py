
import typer
from src.app_info import __app_name__, __app_version__, __app_description__

app = typer.Typer()
def version_callback(value: bool):
    if value: 
        typer.echo(f"{__app_name__} version {__app_version__}")
        raise typer.Exit()


@app.callback()
def main_version(
    version: bool = typer.Option(
        None, "--version", 
        "-v", 
        callback=version_callback,
        is_eager=True)
):
    pass