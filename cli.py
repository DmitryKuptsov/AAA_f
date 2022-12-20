import click
from emoji import emojize


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """Готовит и доставляет пиццу"""
    click.echo("Приготовили за 2с!")
    if delivery:
        click.echo("Доставили за 1с!")


@cli.command()
def menu() -> None:
    """Выводит меню"""
    click.echo(emojize(
        "- Margherita:tomato:: tomato sauce, mozzarella, tomatoes")
        )
    click.echo(emojize(
        "- Pepperoni:pizza:: tomato sauce, mozzarella, pepperoni")
        )
    click.echo(emojize(
        "- Hawaiian:pineapple:: tomato sauce, mozzarella, chicken, pineapples")
        )


if __name__ == '__main__':
    cli()
