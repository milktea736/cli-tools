import click

from toolkit.okd.working_status_manager import WorkingStatusManger

USERS = ['Ivan', 'Jacky', 'Amber', 'Square']

@click.group()
def entry_point():
    pass

@click.group()
def okd():
    pass

@okd.command()
@click.option('--user', type=click.Choice(USERS, case_sensitive=True), required=True)
def start(user: str):
    wsm.udpate(user, True)


@okd.command()
@click.option('--user', type=click.Choice(USERS, case_sensitive=True), required=True)
def stop(user: str):
    wsm.udpate(user, False)


@okd.command()
def force_stop():
    wsm.force_shutdown()


@okd.command()
def working():
    wsm.show_working_status()


wsm = WorkingStatusManger()
entry_point.add_command(okd)

if __name__ == '__main__':
    entry_point()
