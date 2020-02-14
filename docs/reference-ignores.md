# Ignores

Ignores allow you to skip the entire validation process by defining regex pattern.
Whenever at least one of the provided patterns match the 'header' string, 
the validation will stop and comlipy will exit with exitcode 0 (success).

By default all typical git buzzwords/buzzlines will be ignored.

Defaults:

```yaml
ignores:
    - '^((Merge pull request)|(Merge (.*?) into (.*?)|(Merge branch (.*?)))(?:\r?\n)*$)'
    - '^(R|r)evert .*'
    - '^(fixup|squash)!'
    - '^Merged .*?(in|into) .*'
    - '^Merge remote-tracking branch .*'
    - '^Automatic merge.*'
    - '^Auto-merged .*? into .*'
```

## Custom ignores
It is possible to add custom ignores, by setting one or a list of regex pattern strings 
in a configuration yaml. The regex pattern should follow the Python 3 re module syntax.

Example:

```yaml
ignores:
    - '^IGNORE .*'
```