import wsgiref.simple_server
import re


def load_template_file(file_name, sub_dict):
    with open(file_name) as my_file:
        template_str = my_file.read()
        for key, value in sub_dict.items():
            template_str = re.sub('\$%s\$' % key, value, template_str)
        return bytes(template_str, 'utf-8')


def core_provider(environ, start_response):
    start_response('200 OK', [("Content-Type", "text/yaml")])
    return[load_template_file('/home/psb/coreos/cloud',
                              dict(ip=environ['REMOTE_ADDR']))]

srv = wsgiref.simple_server.make_server('0.0.0.0', 8080, core_provider)
srv.serve_forever()
