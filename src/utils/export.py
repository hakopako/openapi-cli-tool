import json
from tabulate import tabulate


def export_json(export_data):
    result = json.dumps(export_data, indent=2, ensure_ascii=False)
    print(result)


def export_table(export_data, headers):
    print(tabulate(export_data, headers=headers))
