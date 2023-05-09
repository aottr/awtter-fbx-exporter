from awex.lib.sdaclient import SdaClient
import typer
from click import Choice
import sys
from rich.progress import Progress, SpinnerColumn, TextColumn
from os import path
from awex.lib.utils import get_application_path


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
    models = None

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Fetching models...", total=None)
        try:
            models = client.get_models()
        except Exception as e:
            print(e)

    print("Available Models")
    for i in range(len(models)):
        print(f"{i}\t{models[i]['name']}")
    click_choice = Choice([str(i) for i in range(len(models))])
    model_prompt = typer.prompt("Which model", "0", show_choices=True, type=click_choice)

    download_stream = client.download_stream_model(models[int(model_prompt)])

    with open(path.join(get_application_path(), 'temp.unitypackage'), 'wb') as f:
        for chunk in download_stream.iter_content(chunk_size=8192):
            f.write(chunk)

typer.run(main)
