import click

from toolkit.okd import okd_cli
from toolkit.ec2 import ec2_cli


@click.group()
@click.pass_context
def entry_point(ctx):
    pass


entry_point.add_command(okd_cli)
entry_point.add_command(ec2_cli)

if __name__ == '__main__':
    entry_point()
