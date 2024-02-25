# Tasks

- [Tasks](#tasks)
  - [Open](#open)
  - [Closed](#closed)

## Open

+ [ ] Use workflows from [this repo](https://github.com/ajndkr/lanarky/blob/main/Makefile) as inspiration. Also:
  + [ ] `.pre-commit-config.yaml`
  + [x] `Makefile`
  + [x] `ISSUE_TEMPLATE`
  + [x] Etc.
+ [x] Move these to-do's to their own file.
+ [ ] Include proper readme and populate it.
+ [x] Add `LICENSE`
+ [ ] Auto-add the `ci-cd.yaml` to the *CI/CD* page, and provide the annotation markers in the source file (if this counts as valid YAML).
+ [ ] Update *Make* page for the changes to `Makefile`.
+ [ ] Check fonts.
+ [ ] Fix versioning.
+ [ ] Write accompanying article on LinkedIn.

## Closed

+ [x] Include `Makefile` to setup project.
  + [x] Create template `Makefile`.
  + [x] Enable poetry env plugin.
  + [x] Install project.
  + [x] Update pre-commit hooks.
  + [x] Install pre-commit hooks.
+ [x] Add `site_url` to `mkdocs.yml`.
+ [x] Create repo on GitHub.
+ [x] CI/CD with `GitHub Actions`.
+ [x] Add some more pages for in navigation.
  + [x] Project layout in file.
  + [x] Home in file.
  + [x] Write some content for Home.
  + [x] Throw in some admonitions for fancy graphics.
+ [x] Add stubgen script.
+ [x] Check serve preview for mistakes in docstrings.
+ [x] Do additional [site configuration](https://squidfunk.github.io/mkdocs-material/creating-your-site/).
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
