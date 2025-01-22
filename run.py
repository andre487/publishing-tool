#!/usr/bin/env python3
import click

import logic


@click.group()
def main():
    pass


@main.command()
@click.option('--add-empty-lines', '-l', is_flag=True)
@click.option('--add-tabs', '-t', is_flag=True)
@click.option('--upper-headers', '-H', is_flag=True)
@click.option('--headers-spacing', '-s', is_flag=True)
@click.argument('doc_path', type=click.Path(exists=True, file_okay=True, dir_okay=False))
def plain_text(
    doc_path: str,
    add_empty_lines: bool,
    add_tabs: bool,
    upper_headers: bool,
    headers_spacing: bool,
):
    logic.prepare_plain_text(
        doc_path,
        add_empty_lines=add_empty_lines,
        add_tabs=add_tabs,
        upper_headers=upper_headers,
        headers_spacing=headers_spacing,
    )


@main.command()
@click.argument(
    'doc_path',
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    required=True,
)
@click.argument(
    'out_dir',
    type=click.Path(exists=False, file_okay=False, dir_okay=True),
    required=True,
)
def partition(doc_path: str, out_dir: str):
    logic.partition(doc_path, out_dir)


if __name__ == '__main__':
    main()
