from server.server import run_server
from server.tools import parse_config

DEFAULT_CONFIG_PATH = 'httpd.conf'

if __name__ == '__main__':
    config = parse_config(DEFAULT_CONFIG_PATH)
    print('Config data: ', config)
    run_server(**config)
