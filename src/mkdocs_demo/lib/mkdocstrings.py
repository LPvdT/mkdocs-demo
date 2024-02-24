"""This module contains code for auto-generating the codebase documentation."""

from pathlib import Path
from typing import Literal

import mkdocs_gen_files

from mkdocs_demo.config.config import RefGenConfig


def gen_ref_pages(config: type[RefGenConfig]) -> Literal[True]:
    """
    The `gen_ref_pages` function generates reference pages for Python modules
    and creates a navigation structure for them.

    Parameters
    ----------
    `config` : `type`[`RefGenConfig`]
        The `config` parameter is of type `RefGenConfig`. It is used to provide configuration settings for
        generating reference pages.
    """

    nav = mkdocs_gen_files.Nav()
    src = Path(__file__).parent.parent.parent

    # Get paths for the give language handler
    for path in sorted(src.rglob(config.handler.value)):
        module_path = path.relative_to(src).with_suffix("")
        doc_path = path.relative_to(src).with_suffix(".md")
        full_doc_path = config.out_dir.joinpath(doc_path)

        parts = tuple(module_path.parts)

        match parts[-1]:
            case "__init__":
                parts = parts[:-1]
                doc_path = doc_path.with_name("index.md")
                full_doc_path = full_doc_path.with_name("index.md")
            case "__main__":
                continue

        nav[parts] = doc_path.as_posix()

        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            identifier = ".".join(parts)
            fd.write(f"::: {identifier}")

        mkdocs_gen_files.set_edit_path(full_doc_path, path)

    with mkdocs_gen_files.open(config.out_dir.joinpath("SUMMARY.md"), "w") as nav_file:
        nav_file.writelines(nav.build_literate_nav())

    return True
