This repository contains build recipes for a non-official Julia buildbot,
focused on testing packages which require an active GPU (which Travis and
the like don't support).

These recipes are not meant to be usable as-is, and contain hardcoded references
to non-public infrastructure. They are meant as a starting point for setting-up
GPU or ASAN buildbots.


GitHub hook
-----------

* Payload URL: `/change_hook/github` relative to the root
* Content Type: `application/x-www-form-urlencoded`
* Secret: same as `passwords.github['webhook']`
* Events: Push and Pull Request
