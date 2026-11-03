<!-- Generated from private documentation source. Do not edit directly. Source SHA256: 335107cf8b64b078b15cc033002f8c97ef32da68c3517ba3599b2b8cd710f46c -->

# gdam Godot fixture

Empty Godot consumer fixture for addon tooling. It has no game scene or export preset.

Install [mise](https://mise.jdx.dev/) and run `mise install`, then run `mise run check`. The gate validates the project and imports a disposable copy with the verified engine, leaving authored resources unchanged. Export templates are unnecessary for this fixture.

For the shared engine installer, check out the reviewed helper source first:

```sh
git clone https://github.com/nicodes/tools.git .ci-tools
git -C .ci-tools checkout --detach f7e243524ce2aa29f299e4c79db33001f72f4a30
```

Declared tests produce source evidence from the current verification session in `.artifacts/verification`.

## Contributor task interface

Contributor tool versions and task entry points live in the native Mise configuration. Use `mise run lint` for source checks, `mise run test` for the applicable behavioral tests, and `mise run check` for the complete supported gate. `mise run clean` removes declared generated outputs while preserving source, credentials and retained data. This package has no application development service.
