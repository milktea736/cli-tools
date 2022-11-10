import click

from toolkit.okd.working_status_manager import WorkingStatusManger, USERS


@click.group(name='okd')
@click.pass_context
def okd_cli(ctx):
    ctx.obj = WorkingStatusManger()


@okd_cli.command()
@click.pass_obj
@click.option('--user', type=click.Choice(USERS, case_sensitive=True), required=True)
def start(obj, user: str):
    obj.udpate(user, True)


@okd_cli.command()
@click.pass_obj
@click.option('--user', type=click.Choice(USERS, case_sensitive=True), required=True)
def stop(obj, user: str):
    obj.udpate(user, False)


@okd_cli.command()
@click.pass_obj
def force_stop(obj):
    obj.force_shutdown()


@okd_cli.command()
@click.pass_obj
def working(obj):
    obj.show_working_status()
