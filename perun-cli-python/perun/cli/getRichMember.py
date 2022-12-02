from perun_openapi import ApiException
from rich import print
from rich.console import Console
from rich.table import Table
from perun.cli import PerunException
import perun.cli
import typer


def get_rich_member(user_id: int = typer.Option(3197, '-u', '--user_id', help='user ID'),
                    vo_name: str = typer.Option("meta", '-v', '--voShortName', help='short name of VO')) -> None:
    """ tests getting complex object of RichMember """
    rpc = perun.cli.rpc
    try:
        user = rpc.users_manager.get_user_by_id(user_id)
        vo = rpc.vos_manager.get_vo_by_short_name(vo_name)
        member = rpc.members_manager.get_member_by_user(vo=vo.id, user=user.id)
        rich_member = rpc.members_manager.get_rich_member(member.id)
        console = Console()
        # print user
        table = Table(title="user")
        table.add_column("id", justify="right")
        table.add_column("first_name")
        table.add_column("last_name")
        table.add_column("createdAt")
        table.add_row(str(rich_member.user.id), rich_member.user.first_name, rich_member.user.last_name,
                      str(rich_member.user.createdAt))
        console.print(table)
        # print member
        table = Table(title="member")
        table.add_column("id", justify="right")
        table.add_column("VO")
        table.add_column("status")
        table.add_column("createdAt")
        table.add_row(str(rich_member.id), vo.name, rich_member.status, str(rich_member.createdAt))
        console.print(table)
        # print table of ues
        table = Table(title="userExtSources")
        table.add_column("id", justify="right")
        table.add_column("last_access")
        table.add_column("login")
        table.add_column("extSource")
        for ues in rich_member.user_ext_sources:
            table.add_row(str(ues.id), ues.last_access, ues.login, ues.ext_source.name)
        console.print(table)
    except ApiException as ex:
        print('error name:', PerunException(ex).name)
        print('error message:', PerunException(ex).message)
    raise typer.Exit(code=1)
