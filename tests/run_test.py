from importlib.machinery import SourceFileLoader
import os
import sys

from ruamel.yaml import YAML

yaml = YAML(typ="safe")


def main():
    task_dir = sys.argv[1]
    solve_path = os.path.join(task_dir, './solution/solve.py')
    config_path = os.path.join(task_dir, './task.yml')

    env = os.environ['CTFT_ENV']

    with open(config_path) as f:
        config = yaml.load(f)
    flag = config['flag']

    if env != 'prod' and flag['solution'] and flag['solution']['prod_only']:
        print('prod_only')
        exit(0)

    solve = SourceFileLoader('solve', solve_path).load_module()
    res = ''.join(solve.solve())

    if flag in res:
        print('successful.')
        exit(0)
    else:
        print('wrong!!!')
        exit(1)


if __name__ == '__main__':
    main()
