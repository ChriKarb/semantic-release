# semantic releases


## Conventions

Make sure your commit messages follow the Conventional Commits format, as semantic-release uses this format to determine the version number and generate release notes.

https://www.conventionalcommits.org/en/v1.0.0/#summary

- `fix:` a commit of the type fix patches a bug in your codebase (this correlates with PATCH in Semantic Versioning).
- `feat:` a commit of the type feat introduces a new feature to the codebase (this correlates with MINOR in Semantic Versioning).
- `BREAKING CHANGE:` a commit that has a footer `BREAKING CHANGE:`, or appends a `!` after the type/scope, introduces a breaking API change (correlating with `MAJOR` in Semantic Versioning). A `BREAKING CHANGE` can be part of commits of any type.
types other than `fix:` and `feat:` are allowed, for example @commitlint/config-conventional (based on the Angular convention) recommends `build:, chore:, ci:, docs:, style:, refactor:, perf:, test:`, and others.
footers other than `BREAKING CHANGE`: <description> may be provided and follow a convention similar to git trailer format.

Additional types are not mandated by the Conventional Commits specification, and have no implicit effect in Semantic Versioning (unless they include a `BREAKING CHANGE`). A scope may be provided to a commit’s type, to provide additional contextual information and is contained within parenthesis, e.g., `feat(parser):` add ability to parse arrays.

## Examples

- Commit message with description and breaking change footer 
```
feat: allow provided config object to extend other configs

BREAKING CHANGE: `extends` key in config file is now used for extending other config files
```

- Commit message with `!` to draw attention to breaking change
```
feat!: send an email to the customer when a product is shipped
```

- Commit message with scope and `!` to draw attention to breaking change
```
feat(api)!: send an email to the customer when a product is shipped
```

- Commit message with both `!` and `BREAKING CHANGE` footer
```
chore!: drop support for Node 6

BREAKING CHANGE: use JavaScript features not available in Node 6.
```

- Commit message with no body
```
docs: correct spelling of CHANGELOG
```

- Commit message with scope
```
feat(lang): add Polish language
```

- Commit message with multi-paragraph body and multiple footers
```
fix: prevent racing of requests

Introduce a request id and a reference to latest request. Dismiss
incoming responses other than from latest request.

Remove timeouts which were used to mitigate the racing issue but are
obsolete now.

Reviewed-by: Z
Refs: #123
```


## Why what how

- https://www.conventionalcommits.org/en/v1.0.0/#do-all-my-contributors-need-to-use-the-conventional-commits-specification
uae squash merges and change commit message accordingly !
- https://www.conventionalcommits.org/en/v1.0.0/#how-does-conventional-commits-handle-revert-commits
how to use this when doing reverts