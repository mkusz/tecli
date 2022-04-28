import typer
import pyperclip
import json
from time import sleep
from pprint import pprint
from functools import wraps
from faker import Faker

app = typer.Typer()
faker = Faker()


def clipboard(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        typer.echo(result)
        pyperclip.copy(result)
        return result
    return wrapper


@app.command()
@clipboard
def first_name():
    return faker.first_name()


@app.command()
@clipboard
def last_name():
    return faker.last_name()


@app.command()
@clipboard
def name():
    return faker.name()


@app.command()
def person(
        save: bool = typer.Option(True, help="Save to file"),
        filename: str = typer.Option("person.json", help="JSON filename")
):
    profile = faker.profile()
    profile['current_location'] = (str(profile['current_location'][0]),
                                   str(profile['current_location'][1]))
    profile['birthdate'] = profile['birthdate'].strftime("%Y.%m.%d")
    pprint(profile)

    if save:
        with open(filename, 'w') as json_file:
            json.dump(profile, json_file, indent=4)


@app.command()
def watcher():
    generators = {'first_name': faker.first_name,
                  'last_name': faker.last_name,
                  'name': faker.name}
    while True:
        try:
            clipboard_input = pyperclip.paste()
            if clipboard_input.startswith('__gen__'):
                clipboard_output = clipboard_input.replace('__gen__', '')
                if clipboard_output in generators:
                    clipboard_output = generators[clipboard_output]()
                typer.echo(f"Replace '{clipboard_input}' with '{clipboard_output}'")
                pyperclip.copy(clipboard_output)
            sleep(1)
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    app()


