JuliaGPU buildbot
=================

This repository contains build recipes for a non-official Julia buildbot,
focused on testing packages which require an active GPU (which Travis and the
like don't support).

These recipes are not meant to be usable as-is, and contain hardcoded references
to non-public infrastructure. They are meant as a starting point for setting-up
GPU or ASAN buildbots.


## How to: deploy

First, you need to provide multiple secrets:
- `worker.env`: define `WORKERNAME` and `WORKERPASS` environment variables (see
  `worker.env.sample`)
- `secrets/codecov.json`: JSON dict mapping package names (case-sensitive) to a
  Codecov token, skipping coverage if no entry is found
- `secrets/github.json`: JSON dict defining `client_id`, `client_secret`,
  `api_token` and `webhook`


## How to: use

The buildbot currently lives at `http://ci.maleadt.net:8010/`, use this as the
root for the URLs below.

### GitHub hook

When adding a GitHub webhook, register it as follows:

* Payload URL: `/change_hook/github` relative to the root
* Content Type: `application/x-www-form-urlencoded`
* Secret: same as `passwords.github['webhook']` in `private.py`
* Events: only Push and Pull Request
