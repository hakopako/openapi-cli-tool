from src.utils.export import export_json


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


def run_scaffold():
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
    return data


def scaffold():
    result = run_scaffold()
    export_json(result)
