# To do

+ [ ] Structure code:
  + Do not only use `lib/`.
  + Add some more code to generate documentation from.
+ [ ] Do some [site configuration](https://squidfunk.github.io/mkdocs-material/creating-your-site/).
+ [ ] CI/CD with `GitHub Actions`.
+ [ ] Eventually use `Makefile` instead of janky `Poetry` scripts.
+ [ ] Ideally you want the following output structure for `reference/`:
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

# Done

+ [x] [Basic mkdocs Material](https://squidfunk.github.io/mkdocs-material/creating-your-site/#minimal-configuration-visual-studio-code)
+ [x] [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings/tree/main)
+ [x] Refactor lib scripts to make use of a factory (e.g. pass command and create new func).
+ [x] Pre-commit hooks.
