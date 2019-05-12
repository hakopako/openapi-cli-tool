import argparse
import json

data = {
    'openapi': '3.0.0',
    'info': {'title': '', 'version': '', 'license': {'name': ''}},
    'servers': [{'url': ''}],
    'paths': {}
}


def data_input(message, default):
    try:
        return raw_input(message) or default
    except NameError:
        return input(message) or default


def __export(export_data):
    result = json.dumps(export_data, indent=2, ensure_ascii=False)
    print(result)


def scaffold():
    data['info']['title'] = data_input('Please enter title [""]: ', '')
    data['info']['version'] = data_input('Please enter version [v1.0]: ', 'v1.0')
    data['info']['license']['name'] = data_input('Please enter license [Apache 2.0]: ', 'Apache 2.0')
    data['servers'][0]['url'] = data_input('Please enter server url [http://example.com]: ', 'http://example.com')

    path_name = data_input('Please enter path [/]: ', '/')
    data['paths'][path_name] = dict()

    while len(data['paths'][path_name]) == 0 or \
            data_input('Add more request method for %s ? Y/n [n]: ' % path_name, 'n') == 'Y':
        path_method = ''
        while path_method not in ['get', 'post', 'put', 'delete', 'head', 'option', 'trace']:
            path_method = data_input('Please enter method for %s [get|post|put|delete|head|option|trace]: ' % path_name,
                                     '')
        path_desc = data_input('Please enter description for %s %s [""]: ' % (path_method, path_name), '')

        data['paths'][path_name][path_method] = {
            'description': path_desc,
            'responses': {}
        }
        print(len(data['paths'][path_name][path_method]['responses']))

        while len(data['paths'][path_name][path_method]['responses']) == 0 or \
                data_input('Add more response for %s %s ? Y/n [n]: ' % (path_method, path_name), 'n') == 'Y':
            response_code = data_input('Please enter response code for %s %s [200]: ' % (path_method, path_name), '200')
            response_desc = data_input('Please enter response description for %s: ' % response_code, '')
            response_content_type = data_input(
                'Please enter response content-type for %s %s [application/json]: ' % (path_method, path_name),
                'application/json')

            data['paths'][path_name][path_method]['responses'][response_code] = {
                'description': response_desc,
                'content': {
                    response_content_type: {"schema": {}}
                }
            }
    __export(data)
    return data


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('command', choices=['scaffold'])

    args = parser.parse_args()
    if args.command == 'scaffold':
        scaffold()


if __name__ == "__main__":
    main()
