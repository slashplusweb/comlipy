# comlipy by slashplus - lint commit messages with python

<div align="center">
  <img width="800" src="https://gitlab.com/slashplus-build/comlipy/raw/master/docs/assets/comlipy.svg">
</div>

Demo generated with [svg-term-cli](https://github.com/marionebl/svg-term-cli) 

**comlipy** is a helper that makes it incredibly easy to check whether
your commit messages follow predefined or custom commit message 
standards or not. 

This means that after setting up `comlipy` in combination with 
a custom git `commit-msg` hook ([further information](https://git-scm.com/book/uz/v2/Customizing-Git-Git-Hooks)),
`comlipy` takes care of the provided commit msg and warns you
whenever a message does not fit your style. 

By default `comlipy` follows the [conventional commit standards](https://conventionalcommits.org),
but you can easily change the configuration in order to fit your needs.

## Requirements

- python 3.7
- pip (pip3) & pipenv

## Installation

### Installation with brew (recommended)

```bash
# Add the source
brew tap slashplus/comlipy git@gitlab.com:slashplus-build/comlipy.git

# Install comlipy
brew install comlipy
```

### Installation with pip

```bash
pip3 install comlipy
```

### Development installation

Install the repository by git cloning it and by setting up a 
virtual environment using pipenv:

```bash
git clone git@gitlab.com:slashplus-build/comlipy.git
cd comlipy/
pipenv install

# OR optional: install the current version globally
# pip3 install .
```

Run comlipy:
```bash
pipenv shell
```
    
## Usage

### Setting up a git commit-msg hook (optional)
Comlipy comes with a simple git commit-msg hook installer. 
This sets up a commit-msg hook that checks the commit message before the 
actual commit. <br>
An example `commit-msg` hook can be found [here](/docs/commit-msg.sample) 

Make sure you have initialized `git` in your project. 
And then just run `comlipy-install`, or  `comlipy-install -c 'PATH/TO/CUSTOM/CONFIGFILE.yml'` 
if you want to set a default config override.

**Note:** <br>
Don't worry, the installer will _not_ automatically override an existing commit-msg hook. 
In case such file already exists, you will be asked if you want to override it.

**Tip:**<br>
Sometimes it can be useful to to set up a custom git hooks path, instead of 
overriding the commit-msg hook directly. <br>
Learn more about it [here](https://git-scm.com/docs/githooks).

### Setting up a a custom configuration override (optional)

Its on you to configure `comlipy` so it perfectly fits your needs 
by setting up and passing a custom configuration yml file. By doing this, you can
override the default configuration i.e. enable or disable rules or changing the
message behaviour (none, warning, error). 

See [docs](/docs/) for further details.

## Documentation

Documentation is currently not finished. Following a list of available 
references:

- [docs](/docs/): ALL documents 
- [rules](/docs/reference-rules.md): Reference of all available validation rules with
 configuration values
- [ignores](/docs/reference-ignores.md): Reference of default validation ignores and how 
to add custom ignores 
- [commit-msg sample hook](/docs/commit-msg.sample): Example git `commit-msg` hook
- [cli](/docs/reference-cli.md): List of available cli flags

## Configuration

It is possible to change the configuration values. This way you are able 
to change rule behaviour of all rules by providing values 
for `applicable`, `value`, `level` or you can change global settings
i.e. the help message. 

Therefore you must define a custom YAML file with the rules to override 
and pass the custom config file path via parameter:

If a config rule is not set, the default value will be used instead.

Example `config-comlipy.yml

```yaml
## global definitions
global:
  help: 'get help here: foo-bar-baz.abc'

rules:
  header-min-length:
    applicable: 'always'
    value: 0
    level: 1
  header-max-length: 
    applicable: 'always'
    value: 123
    level: 2
  scope-case:
    value: 'upper-case'
  scope-empty:
    applicable: 'never'
    level: 2
ignores:
    - '^SKIPME' #skip validations where header starts with "SKIPME"
```

## Tests

You can run unit.tests by following the python 3 unittest documentation.
For example:

```bash
python -m unittest comlipy.tests.lib.test_ensure
python -m unittest comlipy.tests.lib.test_rule_checker
```

or run all tests in batch:
```bash
# optionally run it in verbose mode (-v)
python -m unittest -v comlipy.tests.suite
```

### Credits & inspiration

- [commitlint](https://github.com/conventional-changelog/commitlint)
- [conventional commit standards](https://conventionalcommits.org)
