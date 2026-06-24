# Cursor Plugins (Optional)

Not required for the four-hour workshop. Use when you want bundled hooks, skills, or doc-sync helpers.

## Examples

| Plugin / pattern | Purpose |
| --- | --- |
| [Cursor superpowers](https://github.com/obra/superpowers) (marketplace) | Brainstorming, TDD, verification hooks |
| `cursor-docs-sync` | Align course wording with cursor.com/docs (instructor) |

## Install (verify in your Cursor version)

1. Open Cursor Settings → Plugins / Marketplace.
2. Install from a known marketplace entry only.
3. Review what files the plugin adds under `.cursor/` or user config.

## Settings snippet (optional)

```json
{
  "plugins": {
    "example-plugin@marketplace": true
  }
}
```

Do not enable plugins that send repository contents to unknown endpoints without institutional approval.
