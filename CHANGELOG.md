## [1.2.1] - 2020-07-08
### Fixed
- Fix brew Formula (see issue #8)

## [1.2.0] - 2020-06-17
### Added
- Add comlipy-install to easily create commit-msg hook (see issue #5)
- Add configuration setting in order to allow custom ignores
- Add poetry (see issue #6)

### Changed
- Change default rule `subject-case` to always lower-case
- Remove all Pipenv files (now poetry)

### Fixed
- Fix ansi color sequences in IDE commit errors (hide if color not supported) (see issue #4)
- Fix minor typos & misc bugs 

### Removed
- Remove pipenv (replaced with poetry) (see issue #6)

## [1.1.2] - 2020-02-14
### Added
- Add default ignores
- Add configuration setting in order to allow custom ignores

### Fixed
- Fix error when auto-merging and similar git commits (see issue #3)

## [1.1.1] - 2020-02-14
### Fixed
- Fix header parsing error when parsing an empty message (see issue #2)

## [1.1.0] - 2020-02-04
### Added
- Add monochrome output option
- Add verbose output option

### Fixed
- Fix parsing of subject (see issue #1)

### Changed
- Change comlipy name (description)
- Change comlipy example svg path
- Change config-comlipy.yml defaults (remove useless configs)

## [1.0.0] - 2020-01-20
- Initial release

## [1.0.0-rc2] - 2020-01-20

### Added
- Add colors module
- Add rule name in messages  
- Add changelog

### Changed
- Change info icon
- Change message grey colors

### Removed
- Remove dependency of `termcolor` in favor of simple colors module 

## [1.0.0-rc1] - 2020-01-19
### Added
- Add brew formula

## [1.0.0-rc0] - 2020-01-18
- Initial wip release