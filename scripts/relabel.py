"""
Scripts ro relabel issues within the RVD repository
Run:
    python3 summary.py
"""

from import_base import RVDImport
from github import Label
from time import gmtime, strftime
import click

@ade.command('remove')
              help='The person to greet.')
# @click.option('--create/--no-create', help='Create .alurityhome file automatically and relaunch configuration',
              # default=False)
def relabel_init(package):
    """
    TODO
    """
    pass

              
def relabel(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    relabel()