# Changelog

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). See
[conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit guidelines.

## [Unreleased](https://github.com/afuetterer/python-re3data/compare/0.10.0...main)

<!-- releases -->

## [0.10.0](https://github.com/afuetterer/python-re3data/compare/0.9.0...0.10.0) (2024-12-11)

### Features

- Add return_type csv ([#182](https://github.com/afuetterer/python-re3data/pull/182),
  [`4123823`](https://github.com/afuetterer/python-re3data/commit/4123823353be1fe9fc018328dd0c0542afc80ab3))

### Documentation

- Update uv installation instructions ([#227](https://github.com/afuetterer/python-re3data/pull/227),
  [`d83fe84`](https://github.com/afuetterer/python-re3data/commit/d83fe8488568ab2632ecde299da9447d680d2bee))

## [0.9.0](https://github.com/afuetterer/python-re3data/compare/0.8.0...0.9.0) (2024-07-06)

### Features

- **cli**: Add --outfile option for saving results to disk
  ([#166](https://github.com/afuetterer/python-re3data/pull/166),
  [`1e689e8`](https://github.com/afuetterer/python-re3data/commit/1e689e850b6f5c117887eb1938b1a336422e5418))
- **client**: Add repository counting ([#158](https://github.com/afuetterer/python-re3data/pull/158),
  [`c1cba53`](https://github.com/afuetterer/python-re3data/commit/c1cba53a408505c673de2aa8b4f6caddcb91cadd))

### Documentation

- Add features page ([#157](https://github.com/afuetterer/python-re3data/pull/157),
  [`2348b01`](https://github.com/afuetterer/python-re3data/commit/2348b013ad16cacd8a85b72d9f6d488df1ab7f7e))
- **readme**: Update key features in readme ([#165](https://github.com/afuetterer/python-re3data/pull/165),
  [`2396cf5`](https://github.com/afuetterer/python-re3data/commit/2396cf59b1f2d62e917e9b335d8596aa4d3b38d6))

## [0.8.0](https://github.com/afuetterer/python-re3data/compare/0.7.0...0.8.0) (2024-07-03)

### Features

- Add return_type dict ([#153](https://github.com/afuetterer/python-re3data/pull/153),
  [`5894329`](https://github.com/afuetterer/python-re3data/commit/5894329ed52fb014ca4d08a0941e71a66146d446))
- Add return_type json ([#156](https://github.com/afuetterer/python-re3data/pull/156),
  [`f948d6b`](https://github.com/afuetterer/python-re3data/commit/f948d6bef533314327394dbaa250a8518af6b248))

## [0.7.0](https://github.com/afuetterer/python-re3data/compare/0.6.0...0.7.0) (2024-07-03)

### Features

- Add repository filtering based on query string ([#152](https://github.com/afuetterer/python-re3data/pull/152),
  [`713d4d1`](https://github.com/afuetterer/python-re3data/commit/713d4d1cd581426a95fd8d6a84f5fa4f4fff1564))

## [0.6.0](https://github.com/afuetterer/python-re3data/compare/0.5.0...0.6.0) (2024-07-02)

### Features

- Add async client ([#139](https://github.com/afuetterer/python-re3data/pull/139),
  [`b0c4a48`](https://github.com/afuetterer/python-re3data/commit/b0c4a48b03bc42bec194f4b6c8aa4f1f54d75231))

### Documentation

- Add installation guide ([#129](https://github.com/afuetterer/python-re3data/pull/129),
  [`0de3b5e`](https://github.com/afuetterer/python-re3data/commit/0de3b5e2f93bf162f3c94b1b3eb18cf522962725))
- Enable permalinks for headings ([#132](https://github.com/afuetterer/python-re3data/pull/132),
  [`89d0a3d`](https://github.com/afuetterer/python-re3data/commit/89d0a3d2434db5eab1323843a25d6fcb1f903703))

## [0.5.0](https://github.com/afuetterer/python-re3data/compare/0.4.0...0.5.0) (2024-06-05)

### Breaking Changes

- Set up resources ([#109](https://github.com/afuetterer/python-re3data/pull/109),
  [`0d766d2`](https://github.com/afuetterer/python-re3data/commit/0d766d24f46d6ec9182ac89a743ed5fa88b6a274))

### Features

- Add cli parameters for return_type selection ([#113](https://github.com/afuetterer/python-re3data/pull/113),
  [`15668bc`](https://github.com/afuetterer/python-re3data/commit/15668bc833cc147b4c30fc0a096526ef0be8cb46))
- Set up custom exceptions ([#108](https://github.com/afuetterer/python-re3data/pull/108),
  [`a2fa099`](https://github.com/afuetterer/python-re3data/commit/a2fa099f41114ed50f8a9a64a7530cbe23d65a79))
- **cli**: Add print_error function to highlight errors in console
  ([#123](https://github.com/afuetterer/python-re3data/pull/123),
  [`f242b10`](https://github.com/afuetterer/python-re3data/commit/f242b1050ab4d6c8b34874e10e170463a59cab10))

### Refactoring

- Add is_eager argument to version_callback ([#106](https://github.com/afuetterer/python-re3data/pull/106),
  [`eab6579`](https://github.com/afuetterer/python-re3data/commit/eab6579d3205e98b0bba4a70e3666008ade60795))
- **cli**: Use rich.console instead of rich.print ([#122](https://github.com/afuetterer/python-re3data/pull/122),
  [`a4efea0`](https://github.com/afuetterer/python-re3data/commit/a4efea0d222779642e440a6b486f17235856e721))

### Testing

- Add respx mock route for /repository{id} endpoint ([#114](https://github.com/afuetterer/python-re3data/pull/114),
  [`070bbf6`](https://github.com/afuetterer/python-re3data/commit/070bbf67f219a5deb04b3fbaf41ac0845553c76e))

## [0.4.0](https://github.com/afuetterer/python-re3data/compare/0.3.0...0.4.0) (2024-05-28)

### Features

- Set up dockerfile ([#87](https://github.com/afuetterer/python-re3data/pull/87),
  [`75d85b5`](https://github.com/afuetterer/python-re3data/commit/75d85b5ef08b6ffbda6baddd87da005d1f0481d7))

### Refactoring

- **client**: Move guard clause to top of _request method ([#78](https://github.com/afuetterer/python-re3data/pull/78),
  [`f3eef8b`](https://github.com/afuetterer/python-re3data/commit/f3eef8b7b4316c45a56481e68e1683855c116e35))

### Documentation

- Add extra css for prompt ([#85](https://github.com/afuetterer/python-re3data/pull/85),
  [`16545d7`](https://github.com/afuetterer/python-re3data/commit/16545d74fc7a308a2cb9144465a50b771fabb5a5))
- Add outdated message ([#84](https://github.com/afuetterer/python-re3data/pull/84),
  [`7218b47`](https://github.com/afuetterer/python-re3data/commit/7218b47a027d2cc6b043417a59dca7ee458b0fa2))
- Add reference level in navigation ([#80](https://github.com/afuetterer/python-re3data/pull/80),
  [`6a41547`](https://github.com/afuetterer/python-re3data/commit/6a415478032210e960d6f7ec7a8c8e840ffb84cf))

## [0.3.0](https://github.com/afuetterer/python-re3data/compare/0.2.0...0.3.0) (2024-05-26)

### Features

- **cli**: Set up repository list and get commands ([#76](https://github.com/afuetterer/python-re3data/pull/76),
  [`44987e6`](https://github.com/afuetterer/python-re3data/commit/44987e6ba20f51181dbea2c2d3794a3a96ddf6a5))

### Testing

- Add respx mock route for /repositories endpoint ([#75](https://github.com/afuetterer/python-re3data/pull/75),
  [`59f7d58`](https://github.com/afuetterer/python-re3data/commit/59f7d58e65d91575c571e6bbea51957900424fdc))
- Set up zenodo_id fixture for re-use ([#72](https://github.com/afuetterer/python-re3data/pull/72),
  [`e926c07`](https://github.com/afuetterer/python-re3data/commit/e926c07419f2720d7d3f9c97f01285e52a52863e))

### Documentation

- Add doi to citation.cff and badge to readme ([#66](https://github.com/afuetterer/python-re3data/pull/66),
  [`2fde7ee`](https://github.com/afuetterer/python-re3data/commit/2fde7ee3e2afa7c1dbbd44bf26c8e918d6e79396))

## [0.2.0](https://github.com/afuetterer/python-re3data/compare/0.1.0...0.2.0) (2024-05-23)

### Features

- Set up client ([#64](https://github.com/afuetterer/python-re3data/pull/64),
  [`62300bc`](https://github.com/afuetterer/python-re3data/commit/62300bcf2fa2dd7f1a4c8bbaf7b7ae6bab4e9e77))

### Documentation

- Add api reference ([#47](https://github.com/afuetterer/python-re3data/pull/47),
  [`9e455c4`](https://github.com/afuetterer/python-re3data/commit/9e455c490183109ca3fb7026e554ca53c7bcad12))
- Add changelog to docs ([#43](https://github.com/afuetterer/python-re3data/pull/43),
  [`a167c46`](https://github.com/afuetterer/python-re3data/commit/a167c46b2b80cbefa2b7a6aee2bc0ccdbb0f6459))
- **readme**: Add pypi badges ([#37](https://github.com/afuetterer/python-re3data/pull/37),
  [`f4b31a9`](https://github.com/afuetterer/python-re3data/commit/f4b31a92c2c2cc9db6c7ee484abf3e8ba6a02860))
- **readme**: Add status badge ([#56](https://github.com/afuetterer/python-re3data/pull/56),
  [`cfc9f5a`](https://github.com/afuetterer/python-re3data/commit/cfc9f5a5d2b993690c5d4507603ca5bb7dac0f5e))
- **readme**: Remove table of contents ([#62](https://github.com/afuetterer/python-re3data/pull/62),
  [`8f224e8`](https://github.com/afuetterer/python-re3data/commit/8f224e8ec1819a2cbf74738af7b4e84d34d663bf))

## 0.1.0 (2024-05-20)

### Features

- Add initial cli ([#32](https://github.com/afuetterer/python-re3data/pull/32),
  [`0b5b2c4`](https://github.com/afuetterer/python-re3data/commit/0b5b2c4a855656196d0c502de93752c780be6c40))

### Documentation

- Set up python-semantic-release templates ([#21](https://github.com/afuetterer/python-re3data/pull/21),
  [`bcd976a`](https://github.com/afuetterer/python-re3data/commit/bcd976aa4dcc25188dcf16f82d2a5cee475c5983))
- **readme**: Add codeql badge ([#18](https://github.com/afuetterer/python-re3data/pull/18),
  [`ee6f6aa`](https://github.com/afuetterer/python-re3data/commit/ee6f6aa7dfb1f2b8b6e4d8e10bbe67b10af00c04))
- **readme**: Add short project description ([#28](https://github.com/afuetterer/python-re3data/pull/28),
  [`c20f23e`](https://github.com/afuetterer/python-re3data/commit/c20f23e7b682c10c0749043e851b81cf0ec80f61))
- **readme**: Add similar projects ([#23](https://github.com/afuetterer/python-re3data/pull/23),
  [`7e3e919`](https://github.com/afuetterer/python-re3data/commit/7e3e919d512d9f8556a3c45e7a6f164b9e19be9a))
