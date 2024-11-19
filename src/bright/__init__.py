import subprocess

import click


@click.command()
@click.argument("brightness", default=-1, type=int)
def cli(brightness):
    """Set/get the brightness of your monitor via a CLI.

    Usage:
        Set the brightness to 75%: `bright 75`
        Get the brightness: `bright`

    """
    if brightness == -1:  # get and print
        answer = subprocess.run(["ddcutil", "getvcp", "10"], capture_output=True)
        # try to decode the answer and parse
        brightness = answer.stdout.decode("utf-8").split("=")
        try:
            assert "current value" in brightness[0]
            comma_pos = brightness[1].find(",")
            brightness = brightness[1][:comma_pos].strip()
            click.secho(f"Brightness: {brightness}%")
        except AssertionError:
            click.secho(answer.stdout)
    else:  # set
        if brightness < 0 or brightness > 100:
            click.secho("Brightness must be between 0 and 100")
            return
        subprocess.run(["ddcutil", "setvcp", "10", str(brightness)])
