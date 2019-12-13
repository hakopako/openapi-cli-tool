from src.utils.repository import Repository
from src.utils.export import export_table


def list(paths):
    repository = Repository(paths)
    export_table(repository.routes.to_list(), ['Method', 'Path', 'File'])
