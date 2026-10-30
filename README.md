<!-- Generated from private documentation source. Do not edit directly. Source SHA256: 0fa864de082d5dd14dbf31707b1497c8e345bca2c9d195221f82c04ac718b9fc -->

# gdam Godot fixture

Empty Godot consumer fixture for addon tooling. It has no game scene or export preset.

Install [mise](https://mise.jdx.dev/) and run `mise install`, then run `mise run check`. The gate validates the project and imports a disposable copy with the verified engine, leaving authored resources unchanged. Export templates are unnecessary for this fixture.

For the shared engine installer, check out the reviewed helper source first:

```sh
git clone https://github.com/nicodes/tools.git .ci-tools
git -C .ci-tools checkout --detach f7e243524ce2aa29f299e4c79db33001f72f4a30
```

Declared tests produce source evidence from the current verification session in `.artifacts/verification`.
