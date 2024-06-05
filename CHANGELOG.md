# Changelog

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). See
[conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit guidelines.

## [Unreleased](https://github.com/afuetterer/python-re3data/compare/0.5.0...main)

## [0.5.0](https://github.com/afuetterer/python-re3data/compare/0.4.0...0.5.0) (2024-06-05)

### Breaking Changes

- set up resources (#109) ([`0d766d2`](https://github.com/afuetterer/python-re3data/commit/0d766d24f46d6ec9182ac89a743ed5fa88b6a274))

### Features

- **cli:** add print_error function to highlight errors in console (#123) ([`f242b10`](https://github.com/afuetterer/python-re3data/commit/f242b1050ab4d6c8b34874e10e170463a59cab10))
- add cli parameters for return_type selection (#113) ([`15668bc`](https://github.com/afuetterer/python-re3data/commit/15668bc833cc147b4c30fc0a096526ef0be8cb46))
- set up custom exceptions (#108) ([`a2fa099`](https://github.com/afuetterer/python-re3data/commit/a2fa099f41114ed50f8a9a64a7530cbe23d65a79))

### Code Refactoring

- **cli:** use rich.console instead of rich.print (#122) ([`a4efea0`](https://github.com/afuetterer/python-re3data/commit/a4efea0d222779642e440a6b486f17235856e721))
- add is_eager argument to version_callback (#106) ([`eab6579`](https://github.com/afuetterer/python-re3data/commit/eab6579d3205e98b0bba4a70e3666008ade60795))

### Testing

- add respx mock route for /repository{id} endpoint (#114) ([`070bbf6`](https://github.com/afuetterer/python-re3data/commit/070bbf67f219a5deb04b3fbaf41ac0845553c76e))

## [0.4.0](https://github.com/afuetterer/python-re3data/compare/0.3.0...0.4.0) (2024-05-28)

### Features

- set up dockerfile (#87) ([`75d85b5`](https://github.com/afuetterer/python-re3data/commit/75d85b5ef08b6ffbda6baddd87da005d1f0481d7))

### Code Refactoring

- **client:** move guard clause to top of _request method (#78) ([`f3eef8b`](https://github.com/afuetterer/python-re3data/commit/f3eef8b7b4316c45a56481e68e1683855c116e35))

### Documentation

- add extra css for prompt (#85) ([`16545d7`](https://github.com/afuetterer/python-re3data/commit/16545d74fc7a308a2cb9144465a50b771fabb5a5))
- add outdated message (#84) ([`7218b47`](https://github.com/afuetterer/python-re3data/commit/7218b47a027d2cc6b043417a59dca7ee458b0fa2))
- add reference level in navigation (#80) ([`6a41547`](https://github.com/afuetterer/python-re3data/commit/6a415478032210e960d6f7ec7a8c8e840ffb84cf))

## [0.3.0](https://github.com/afuetterer/python-re3data/compare/0.2.0...0.3.0) (2024-05-26)

### Features

- **cli:** set up repository list and get commands (#76) ([`44987e6`](https://github.com/afuetterer/python-re3data/commit/44987e6ba20f51181dbea2c2d3794a3a96ddf6a5))

### Testing

- add respx mock route for /repositories endpoint (#75) ([`59f7d58`](https://github.com/afuetterer/python-re3data/commit/59f7d58e65d91575c571e6bbea51957900424fdc))
- set up zenodo_id fixture for re-use (#72) ([`e926c07`](https://github.com/afuetterer/python-re3data/commit/e926c07419f2720d7d3f9c97f01285e52a52863e))

### Documentation

- add doi to citation.cff and badge to readme (#66) ([`2fde7ee`](https://github.com/afuetterer/python-re3data/commit/2fde7ee3e2afa7c1dbbd44bf26c8e918d6e79396))

## [0.2.0](https://github.com/afuetterer/python-re3data/compare/0.1.0...0.2.0) (2024-05-23)

### Features

- set up client (#64) ([`62300bc`](https://github.com/afuetterer/python-re3data/commit/62300bcf2fa2dd7f1a4c8bbaf7b7ae6bab4e9e77))

### Documentation

- **readme:** remove table of contents (#62) ([`8f224e8`](https://github.com/afuetterer/python-re3data/commit/8f224e8ec1819a2cbf74738af7b4e84d34d663bf))
- **readme:** add status badge (#56) ([`cfc9f5a`](https://github.com/afuetterer/python-re3data/commit/cfc9f5a5d2b993690c5d4507603ca5bb7dac0f5e))
- add api reference (#47) ([`9e455c4`](https://github.com/afuetterer/python-re3data/commit/9e455c490183109ca3fb7026e554ca53c7bcad12))
- add changelog to docs (#43) ([`a167c46`](https://github.com/afuetterer/python-re3data/commit/a167c46b2b80cbefa2b7a6aee2bc0ccdbb0f6459))
- **readme:** add pypi badges (#37) ([`f4b31a9`](https://github.com/afuetterer/python-re3data/commit/f4b31a92c2c2cc9db6c7ee484abf3e8ba6a02860))

## 0.1.0 (2024-05-20)

### Features

- add initial cli (#32) ([`0b5b2c4`](https://github.com/afuetterer/python-re3data/commit/0b5b2c4a855656196d0c502de93752c780be6c40))

### Documentation

- **readme:** add short project description (#28) ([`c20f23e`](https://github.com/afuetterer/python-re3data/commit/c20f23e7b682c10c0749043e851b81cf0ec80f61))
- **readme:** add similar projects (#23) ([`7e3e919`](https://github.com/afuetterer/python-re3data/commit/7e3e919d512d9f8556a3c45e7a6f164b9e19be9a))
- set up python-semantic-release templates (#21) ([`bcd976a`](https://github.com/afuetterer/python-re3data/commit/bcd976aa4dcc25188dcf16f82d2a5cee475c5983))
- **readme:** add codeql badge (#18) ([`ee6f6aa`](https://github.com/afuetterer/python-re3data/commit/ee6f6aa7dfb1f2b8b6e4d8e10bbe67b10af00c04))

