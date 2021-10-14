"""
Requirements:
    lk-utils
"""
from lk_utils import dumps
from lk_utils import loads


# noinspection PyUnusedLocal
def main(
        file_i='data/pyml-import-namespaces.json',
        file_o1='data/qml-modules.txt',
        file_o2='data/qml-components.txt',
        file_o3='data/qml-properties.txt',
):
    data_r = loads(file_i)  # type: dict
    ''' The json file is come from my another project (declare-qml).
        The dict structure is:
            {
                <module: str>: {
                    #   e.g. 'pyml.qtquick', 'pyml.qtquick.controls', 'pyml
                    #       .qtquick.window', etc.
                    <widget: str>: {
                        #   e.g. 'Rectangle', 'TextArea', etc.
                        'props': [prop, ...], ...
                        #   prop (str): Note this is lower case with undersores,
                        #       we should convert it to camelCase.
                    }, ...
                }, ...
            }
    '''
    # dumps(indexing_modules(data_r), ofile1)  # FIXME
    dumps(indexing_components(data_r), file_o2)
    dumps(indexing_properties(data_r), file_o3)


# noinspection PyUnusedLocal
def indexing_modules(data_r: dict):
    # noinspection PyUnusedLocal
    def convert_k1_to_qml_module(k1):
        """ Convert pyml module name to qml.

        Examples:
            'pyml.qtquick.controls' -> 'QtQuick.Controls'
        """
        # TODO: Refer to pyml project source code.
    
    for k1 in data_r.keys():
        pass


def indexing_components(data_r: dict):
    data_w = set()
    
    for v1 in data_r.values():
        data_w.update(v1.keys())
    
    data_w = list(data_w)
    data_w.sort()
    return data_w


def indexing_properties(data_r: dict):
    data_w = set()
    
    def handle_each_part(part: str):
        x = part.split('_')
        out = x[0] + ''.join(y.title() for y in x[1:])
        return out
    
    for i, p in data_r.items():
        for j, q in p.items():
            for k in q['props']:
                parts = k.split('.')
                name = '.'.join(map(handle_each_part, parts))
                data_w.add(name)
    
    data_w = list(data_w)
    data_w.sort()
    return data_w


if __name__ == '__main__':
    main()
