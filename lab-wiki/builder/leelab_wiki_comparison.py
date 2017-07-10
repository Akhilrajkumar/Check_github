"""compare the summary info of two builds of websites, based on their summary.json"""

import json
from sys import argv, version_info

assert version_info >= (3, 6), "Python 3.6 or later to run this program!"

_result_dict = {
    'added': 0,
    'removed': 0,
}


def main():
    file_old, file_new = argv[1:]
    with open(file_old, 'r', encoding='utf-8') as f_old:
        content_old = f_old.read()
        if not content_old:
            content_old = "{}"
        dict_old = json.loads(content_old)

    with open(file_new, 'r', encoding='utf-8') as f_new:
        content_new = f_new.read()
        if not content_new:
            content_new = "{}"
        dict_new = json.loads(content_new)

    # time to show their differences.
    compare_summary(dict_old, dict_new)
    print(_result_dict)


def compare_summary(dict_old, dict_new):
    keys_all = dict_old.keys() | dict_new.keys()

    # then let's run through them one by one.
    for key in sorted(keys_all):
        print(key)
        print('=' * 40)
        compare_subsummary(dict_old.get(key, {}), dict_new.get(key, {}))
        print('=' * 40)


def compare_subsummary(dict_old, dict_new):
    keys_all = dict_old.keys() | dict_new.keys()
    for key in sorted(keys_all):
        print(key)
        print('=' * 20)
        bib_ids_old = set(dict_old.get(key, []))
        bib_ids_new = set(dict_new.get(key, []))
        only_in_old = bib_ids_old - bib_ids_new
        only_in_new = bib_ids_new - bib_ids_old
        if only_in_old:
            print('only in old', sorted(only_in_old))
            _result_dict['removed'] += len(only_in_old)
        if only_in_new:
            print('only in new', sorted(only_in_new))
            _result_dict['added'] += len(only_in_new)
        print('=' * 20)


if __name__ == '__main__':
    main()
