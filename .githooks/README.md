# .githooks

Git hooks for this repository. Committed so every contributor gets them automatically after one setup command.

## Activate

```sh
git config core.hooksPath .githooks
```

Run once after cloning. The hooks take effect immediately — no restart needed.

## Hooks

| Hook | Fires on | Checks |
|---|---|---|
| `pre-commit` | `git commit` | git config identity, `GIT_AUTHOR_*` / `GIT_COMMITTER_*` env vars, OS fallback, staged file content |
| `commit-msg` | `git commit` | commit message text, identity (belt-and-suspenders) |
| `tag` | `git tag -a` | tag name, tagger identity (requires git ≥ 2.24) |
| `pre-push` | `git push` | annotated tag tagger/message, commit author/committer in push range |

## What is blocked

Each hook blocks commits, tags, and pushes that contain identifiers from an encoded block list. The encoded values are baked into the hooks; no external file is needed.

## Fix a blocked commit

```sh
git config user.name  "Developer"
git config user.email "<handle>@users.noreply.github.com"
```

Then re-run the failing git command.

## Fix a blocked annotated tag

```sh
git tag -d <tag-name>
git config user.email "<handle>@users.noreply.github.com"
git tag -a <tag-name> -m "<message>"
```
