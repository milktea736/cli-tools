import boto3
import click


# INSTANCES = {'instance_nick_name': 'ec2_instance_id'}
INSTANCES = {}


@click.group(name='client')
@click.pass_context
def ec2_cli(ctx):
    ctx.obj = boto3.resource('ec2')


@ec2_cli.command()
@click.pass_obj
@click.option('--name', type=click.Choice(INSTANCES.keys(), case_sensitive=True), required=True)
def start(obj, name: str):
    obj.Instances(INSTANCES[name]).start()


@ec2_cli.command()
@click.pass_obj
@click.option('--name', type=click.Choice(INSTANCES.keys(), case_sensitive=True), required=True)
def stop(obj, name: str):
    obj.Instances(INSTANCES[name]).stop()


@ec2_cli.command()
@click.pass_obj
def state(obj):
    for name, val in INSTANCES.items():
        print(f'{name}: {obj.Instance(val).state["Name"]}')
