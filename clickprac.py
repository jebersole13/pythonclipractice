import click

@click.command()
def hello():
    click.echo('What up son?')

if __name__ == '__main__':
    hello()