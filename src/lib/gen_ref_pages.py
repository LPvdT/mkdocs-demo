from pathlib import Path

import mkdocs_gen_files

src = Path(__file__).parent.parent.joinpath("src")

for path in sorted(src.rglob("*.py")):
    module_path = path.relative_to(src).with_suffix("")
    doc_path = path.relative_to(src).with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = list(module_path.parts)

    match parts[-1]:
        case "__init__":
            parts = parts[-1]
        case "__main__":
            continue

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        identifier = ".".join(parts)
        print(f"::: {identifier}", file=fd)

    # TODO: Check if path is correct
    mkdocs_gen_files.set_edit_path(full_doc_path, path)
