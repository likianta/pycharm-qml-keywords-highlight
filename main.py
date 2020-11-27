from lk_utils.read_and_write import dumps, loads


# noinspection PyUnusedLocal
def main(
        ifile='data/pyml_import_namespaces.json',
        ofile1='data/qml_modules.txt',
        ofile2='data/qml_widgets.txt',
        ofile3='data/qml_properties.txt',
):
    rdata = loads(ifile)  # type: dict
    ''' The json file comes from my another project (yet it is under
        construction).
        The dict structure is:
            {
                module: {
                        module (str): e.g. 'pyml.qtquick', 'pyml.qtquick
                            .controls', 'pyml.qtquick.window', etc.
                    widget: {
                            widget (str): e.g. 'Rectangle', 'TextArea', etc.
                        'props': [prop, ...], ...
                            prop (str): Note this is lower case with undersores,
                                we should convert it to camelCase.
                    }, ...
                }, ...
            }
    '''
    
    # dumps(indexing_modules(rdata), ofile1)  # FIXME
    dumps(indexing_widgets(rdata), ofile2)
    dumps(indexing_properties(rdata), ofile3)


# noinspection PyUnusedLocal
def indexing_modules(rdata: dict):
    
    # noinspection PyUnusedLocal
    def convert_k1_to_qml_module(k1):
        """ Convert pyml module name to qml.

        Examples:
            'pyml.qtquick.controls' -> 'QtQuick.Controls'
        """
        # TODO: Refer to pyml project source code.
    
    for k1 in rdata.keys():
        pass


def indexing_widgets(rdata: dict):
    wdata = set()

    for v1 in rdata.values():
        wdata.update(v1.keys())
    
    wdata = list(wdata)
    wdata.sort()
    return wdata


def indexing_properties(rdata: dict):
    wdata = set()

    def handle_each_part(part: str):
        x = part.split('_')
        out = x[0] + ''.join(y.title() for y in x[1:])
        return out
        
    for i, p in rdata.items():
        for j, q in p.items():
            for k in q['props']:
                parts = k.split('.')
                name = '.'.join(map(handle_each_part, parts))
                wdata.add(name)
    
    wdata = list(wdata)
    wdata.sort()
    return wdata


if __name__ == '__main__':
    main()
