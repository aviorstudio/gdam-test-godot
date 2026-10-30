<!-- Generated from private documentation source. Do not edit directly. Source SHA256: 31cdbd43f05b6f8cf0d0f0d7407b9e2e300314b91cbae6d595d33aa1f7b9d7a5 -->

# gdam Godot fixture

Empty Godot consumer fixture for addon tooling. It has no game scene or export preset.

Install [mise](https://mise.jdx.dev/) and run `mise install`, then run `mise run check`. The gate validates the project and imports a disposable copy with the verified engine, leaving authored resources unchanged. Export templates are unnecessary for this fixture.

For the shared engine installer, check out the reviewed helper source first:

```sh
git clone https://github.com/nicodes/tools.git .ci-tools
git -C .ci-tools checkout --detach 7dd151b7c2cac851d46591cad4a14d74d923dd77
```
