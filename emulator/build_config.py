import os

folder = os.path.realpath(os.path.dirname(__file__))
with open(os.path.join(folder, 'slapd.conf.dist')) as fp:
    config = fp.read()
    config = config.replace('__SCHEMADIR__', os.path.join(folder, 'schema'))

with open(os.path.join(folder, 'slapd.conf'), 'w') as fp:
    fp.write(config)
