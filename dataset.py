from tabulate import tabulate
import requests


def convert_capacity(capacity_str):
    unit = capacity_str[-1].upper()
    value = float(capacity_str[:-1])

    if capacity_str == '0B':
        return 0
    if unit == 'T':
        return value * 1024 * 1024
    elif unit == 'G':
        return value * 1024
    elif unit == 'M':
        return value

def format_capacity(value):
    if value >= 1024 * 1024:
        return f"{value / (1024 * 1024):.2f}T"
    elif value >= 1024:
        return f"{value / 1024:.2f}G"
    else:
        return f"{value:.2f}M"


def get_pool_dataset(host, auth):
    url = f'{host}/api/v2.0/pool/dataset'
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {auth}'
    }

    response = requests.get(url, headers=headers).json()
    table_data = []
    for item in response:
        if '/' not in item['id']:  # Filter out nodes without '/'
            name = item['name']
            used = item['used']['value']
            available = item['available']['value']
            usable_capacity = format_capacity(convert_capacity(used) + convert_capacity(available))
            table_data.append([name, usable_capacity, used, available])

    table_headers = ["Name", "Usable Capacity", "Used", "Available"]
    table = tabulate(table_data, headers=table_headers, tablefmt="pipe")

    print(table)
