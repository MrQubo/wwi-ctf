from contextlib import contextmanager
from importlib.machinery import SourceFileLoader
import os
import sys

from ruamel.yaml import YAML

yaml = YAML(typ="safe")


@contextmanager
def pushd(new_dir):
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    yield
    os.chdir(previous_dir)


def main():
    task_name = sys.argv[1]
    task_dir = sys.argv[2]
    solution_dir = os.path.join(task_dir, './solution/')
    solve_path = os.path.join(solution_dir, './solve.py')
    config_path = os.path.join(task_dir, './task.yml')

    env = os.environ['CTFT_ENV']

    with open(config_path) as f:
        config = yaml.load(f)
    flag = config['flag']

    if env != 'prod' and config.get('solution', {}).get('prod_only', False):
        print(f'Solution for task "{task_name}": prod_only')
        exit(0)

    solve = SourceFileLoader('solve', solve_path).load_module()
    with pushd(solution_dir):
        res = ''.join(solve.solve())

    if flag in res:
        exit(0)
    else:
        print(f'Solution for task "{task_name}": wrong!!!')
        exit(1)


if __name__ == '__main__':
    main()
