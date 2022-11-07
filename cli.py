import click

from toolkit.okd.working_status_manager import WorkingStatusManger

USERS = ['Ivan', 'Jacky', 'Amber', 'Square']


@click.group()
def cli():
    pass


@cli.command()
@click.option('--user', type=click.Choice(USERS, case_sensitive=True), required=True)
def start(user: str):
    wsm.udpate(user, True)


@cli.command()
@click.option('--user', type=click.Choice(USERS, case_sensitive=True), required=True)
def stop(user: str):
    wsm.udpate(user, False)


@cli.command()
def force_stop():
    wsm.force_shutdown()


@cli.command()
def working():
    wsm.show_working_status()


if __name__ == '__main__':
    wsm = WorkingStatusManger()
    cli()
