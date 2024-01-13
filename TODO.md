# Tasks

- [Tasks](#tasks)
  - [Open](#open)
  - [Closed](#closed)

## Open

+ [ ] Do additional [site configuration](https://squidfunk.github.io/mkdocs-material/creating-your-site/).
+ [ ] CI/CD with `GitHub Actions`.
+ [ ] Include `Makefile` alternative, instead of janky `Poetry` scripts.

## Closed

+ [x] Write tests.
  + Could include some more, but not really the point of the project.
+ [x] Structure code:
  + [x] Do not only use `lib/`.
  + [x] Add some more code to generate documentation from.
+ [x] [Basic mkdocs Material](https://squidfunk.github.io/mkdocs-material/creating-your-site/#minimal-configuration-visual-studio-code)
+ [x] [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings/tree/main)
+ [x] Refactor lib scripts to make use of a factory (e.g. pass command and create new func).
+ [x] Pre-commit hooks.
+ [x] MkDocstrings site configuration
+ [x] Ideally you want the following output structure for `reference/`:
  ```shell
  site/reference/
  ├── main_package/
  │   ├── constants/
  │   ├── lib/
  │   ├── mkdocs_testing/
  │   ├── scripts/
  │   └── index.html
  └── SUMMARY.html
  ```
