import io
import re

import docx

heading_re = re.compile(r'Heading (\d+)$')


def prepare_plain_text(
    doc_path: str,
    add_empty_lines: bool = False,
    add_tabs: bool = False,
    upper_headers: bool = False,
    headers_spacing: bool = False,
):
    doc = docx.Document(doc_path)
    out = io.StringIO()

    for par in doc.paragraphs:
        style_name = par.style.name
        if style_name.startswith('Heading'):
            print(file=out)
            if headers_spacing:
                print(file=out)

            h_text = par.text
            if upper_headers:
                h_text = h_text.upper()
            elif m := heading_re.match(style_name):
                level = int(m.group(1))
                for _ in range(level):
                    print('#', end='', file=out)
                print(' ', end='', file=out)
            else:
                print('# ', end='', file=out)

            print(h_text, file=out)
            if headers_spacing:
                print(file=out)
            continue

        if add_tabs:
            print('    ', end='', file=out)
        print(par.text, file=out)
        if add_empty_lines:
            print(file=out)

    print(out.getvalue())
