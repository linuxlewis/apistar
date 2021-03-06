import click


def create_tables():
    """
    Create SQLAlchemy tables.
    """
    from apistar.main import get_current_app
    from apistar.backends import DjangoBackend
    app = get_current_app()
    db_backend = DjangoBackend.build(settings=app.settings)
    db_backend.create_tables()
    click.echo("Tables created")
