import click
import sys

from planemo.cli import pass_context

from planemo import options
from planemo import shed


@click.command("shed_init")
@options.optional_project_arg()
@click.option(
    "--from_workflow",
    type=click.Path(exists=True, file_okay=True, resolve_path=True),
    help=('Attempt to generate repository dependencies from specified '
          'workflow.')
)
@click.option(
    "--description",
    help='Specify repository description for .shed.yml.'
)
@click.option(
    "--long_description",
    help='Specify repository long_description for .shed.yml.'
)
@click.option(
    "--remote_repository_url",
    help='Specify repository remote_repository_url for .shed.yml.'
)
@click.option(
    "--homepage_url",
    help='Specify repository homepage_url for .shed.yml.'
)
@click.option(
    "--category",
    multiple=True,
    help='Specify repository category for .shed.yml (may specify multiple).',
    type=click.Choice(shed.CURRENT_CATEGORIES)
)
@options.shed_owner_option()
@options.shed_name_option()
@options.force_option()
@pass_context
def cli(ctx, path, **kwds):
    """Bootstrap a new Tool Shed configuration (.shed.yml) file.

    This file is used by other ``planemo`` commands such as ``shed_lint``,
    ``shed_create``, ``shed_upload``, and ``shed_diff`` to manage repositories
    in a Galaxy Tool Shed.
    """
    exit_code = shed.shed_init(ctx, path, **kwds)
    sys.exit(exit_code)