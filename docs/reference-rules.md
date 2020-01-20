# Rules

Rules are made up by a name and a configuration list. The configuration list contains:
* **Level** `[0..2]`: `0` disables the rule. For `1` it will be considered a warning for `2` an error.
* **Applicable** `always|never`: `never` inverts the rule.
* **Value**: value to use for this rule.

Rule configurations are of type `list` residing on a key with the rule's name as key on the rules configuration settings.
Examples:

```yaml
  rules: 
    header-max-length: 
      level: 0
      applicable: 'always'
      value: 72
  
```

also valid:
```yaml
  rules: 
    type-enum:
      applicable: 'always'
      value:
        - 'build'
        - 'chore'
        - 'ci'
        - 'docs'
        - 'feat'
        - 'fix'
        - 'improvement'
        - 'perf'
        - 'refactor'
        - 'revert'
        - 'style'
        - 'test'
```

### Available rules
#### body-leading-blank
* **condition**: `body` begins with blank line
* **rule**: `always`

#### body-max-length
* **condition**: `body` has `value` or less characters
* **rule**: `always`
* **value**
```yaml
  Infinity
```

#### body-max-line-length
* **condition**: `body` lines has `value` or less characters
* **rule**: `always`
* **value**
```yaml
  Infinity
```

#### body-min-length
* **condition**: `body` has `value` or more characters
* **rule**: `always`
* **value**
```yaml
  0
```

#### footer-leading-blank
* **condition**: `footer` begins with blank line
* **rule**: `always`

#### footer-max-length
* **condition**: `footer` has `value` or less characters
* **rule**: `always`
* **value**
```yaml
  Infinity
```

#### footer-max-line-length
* **condition**: `footer` lines has `value` or less characters
* **rule**: `always`
* **value**
```yaml
  Infinity
```

#### footer-min-length
* **condition**: `footer` has `value` or more characters
* **rule**: `always`
* **value**
```yaml
  0
```

#### header-case
* **condition**: `header` is in case `value`
* **rule**: `always`
```yaml
  'lowerCase'
```
* **possible values**
```yaml
  - 'lower-case' # default
  - 'upper-case' # UPPERCASE
  - 'camel-case' # camelCase
  - 'kebab-case' # kebab-case
  - 'pascal-case' # PascalCase
  - 'sentence-case' # Sentence case
  - 'snake-case' # snake_case
  - 'start-case' # Start Case
```

#### header-full-stop
* **condition**: `header` ends with `value`
* **rule**: `never`
* **value**
```yaml
  '.'
```

#### header-max-length
* **condition**: `header` has `value` or less characters
* **rule**: `always`
* **value**
```yaml
  72
```

#### header-min-length
* **condition**: `header` has `value` or more characters
* **rule**: `always`
* **value**
```yaml
  0
```

#### scope-enum
* **condition**: `scope` is found in value
* **rule**: `always`
* **value**
```yaml
[]
```

#### scope-case
* **condition**: `scope` is in case `value`
* **rule**: `always`
```yaml
  'lowerCase'
```
* **possible values**
```yaml
  - 'lower-case' # default
  - 'upper-case' # UPPERCASE
  - 'camel-case' # camelCase
  - 'kebab-case' # kebab-case
  - 'pascal-case' # PascalCase
  - 'sentence-case' # Sentence case
  - 'snake-case' # snake_case
  - 'start-case' # Start Case
```

#### scope-empty
* **condition**: `scope` is empty
* **rule**: `never`

#### scope-max-length
* **condition**: `scope` has `value` or less characters
* **rule**: `always`
* **value**
```yaml
  Infinity
```

#### scope-min-length
* **condition**: `scope` has `value` or more characters
* **rule**: `always`
* **value**
```yaml
  0
```

#### subject-case
* **condition**: `subject` is in case `value`
* **rule**: `always`
```yaml
  'lowerCase'
```
* **possible values**
```yaml
  - 'lower-case' # default
  - 'upper-case' # UPPERCASE
  - 'camel-case' # camelCase
  - 'kebab-case' # kebab-case
  - 'pascal-case' # PascalCase
  - 'sentence-case' # Sentence case
  - 'snake-case' # snake_case
  - 'start-case' # Start Case
```

#### subject-empty
* **condition**: `subject` is empty
* **rule**: `never`

#### subject-full-stop
* **condition**: `subject` ends with `value`
* **rule**: `never`
* **value**
```yaml
  '.'
```

#### subject-max-length
* **condition**: `subject` has `value` or less characters
* **rule**: `always`
* **value**
```yaml
  Infinity
```

#### subject-min-length
* **condition**: `subject` has `value` or more characters
* **rule**: `always`
* **value**
```yaml
  0
```

#### type-enum
* **condition**: `type` is found in value
* **rule**: `always`
* **value**
```yaml
  - 'feat'
  - 'fix'
  - 'docs'
  - 'style'
  - 'refactor'
  - 'test'
  - 'revert'
```

#### type-case
* **description**: `type` is in case `value`
* **rule**: `always`
* **value**
  ```yaml
    'lower-case'
  ```
* **possible values**
```yaml
  - 'lower-case' # default
  - 'upper-case' # UPPERCASE
  - 'camel-case' # camelCase
  - 'kebab-case' # kebab-case
  - 'pascal-case' # PascalCase
  - 'sentence-case' # Sentence case
  - 'snake-case' # snake_case
  - 'start-case' # Start Case
```

#### type-empty
* **condition**: `type` is empty
* **rule**: `never`

#### type-max-length
* **condition**: `type` has `value` or less characters
* **rule**: `always`
* **value**
```yaml
  Infinity
```

#### type-min-length
* **condition**: `type` has `value` or more characters
* **rule**: `always`
* **value**
```yaml
  0
```