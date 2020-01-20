# Comlipy - **Com**mit**li**nt for **Py**thon

**comlipy** is a little helper that makes it incredibly easy to check whether
your commit messages follow predefined or custom commit message 
standards. 

This means that after setting up `comlipy` in combination with 
a custom git `commit-msg` hook ([further information](https://git-scm.com/book/uz/v2/Customizing-Git-Git-Hooks))
`comlipy` takes care of the provided commit msg and warns you
whenever a message does not fit your style. 

By default `comlipy` follows the [conventional commit standards](https://conventionalcommits.org),
but you can easily change the configuration in order to fit your needs.

## Requirements
- python 3.7
- pip (pip3) & pipenv

## Installation
1. Make sure you have initialized git in your project. 
2. Install the repository by git cloning it and by installing it via pip/pip3
    ```bash
    # clone the repository
    git clone git@gitlab.com:slashplus-build/comlipy.git
    cd comlipy
    pip3 install .
    ```
3. Set up a commit-msg hook that checks the commit message before the 
    actual commit. An example `commit-msg` hook can be found [here](/docs/commit-msg.sample) 

    Tip:
    <br>
    It is recommended to set up a custom git hooks path, instead of 
    overriding the commit-msg hook directly. Learn more about it [here](https://git-scm.com/docs/githooks).
    
4. \[Optional:\] Configure `comlipy` by setting up a custom configuration yml file

See [docs](/docs) for further details.

## Configuration
It is possible to change the configuration values. This way you are able 
to change rule behaviour of all rules by providing values 
for `applicable`, `value`, `level` or you can change global settings
i.e. the help message. 

Therefore you must define a custom yml file with the rules to override and pass 
the custom config file path via parameter:

If a config rule is not set, the default value will be used instead.

Example config.yml
```yaml
## global definitions
global:
  debug: 0
  help: 'get help here: foo-bar-baz.abc'

rules:
  header-min-length:
    applicable: 'always'
    value: 0
    level: 1
  header-max-length: 
    applicable: 'always'
    value: 100
    level: 2
  scope-case:
    value: 'upper-case'
  scope-empty:
    applicable: never
    level: 2
```

## Tests

You can run unit.tests by following the python 3 unittest documentation.
For example:

```bash
python -m unittest comlipy.tests.ensure
```

### Credits
- [commitlint](https://github.com/conventional-changelog/commitlint)
- [conventional commit standards](https://conventionalcommits.org)

### Todos:

#### Tests:
- [ ] rules

### Rules:
- [ ] references-empty
- [ ] signed-off-by