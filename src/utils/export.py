import json
import yaml
from tabulate import tabulate


def export_json(export_data):
    result = json.dumps(export_data, indent=2, ensure_ascii=False)
    print(result)


def export_yaml(export_data):
    result = yaml.safe_dump(export_data, default_flow_style=False)
    print(result)


def export_table(export_data, headers):
    print(tabulate(export_data, headers=headers))
