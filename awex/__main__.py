from lib.sdaclient import SdaClient
import typer
import sys
from rich.progress import Progress, SpinnerColumn, TextColumn


def main():
    username = typer.prompt("Username")
    password = typer.prompt("Password", hide_input=True)
    client = None
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Logging in...", total=None)
        try:
            client = SdaClient(username, password)
        except Exception as e:
            print(e)
    if not client:
        sys.exit(1)

    print("Successfully logged in!")

if __name__ == "__main__":
    typer.run(main)
    username = typer.prompt("Username")
    password = typer.prompt("Password", hide_input=True)
