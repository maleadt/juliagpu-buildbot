This repository contains build recipes for two non-official Julia buildbots.
- `juliacpu`: regular CPU builds, both per-commit and daily ASAN build
- `juliagpu`: GPU toolchain integration testing, pulling code from julia, LLVM.jl,
   CUDAdrv.jl and CUDAnative.jl

These recipes are not meant to be usable as-is, and contain hardcoded references
to non-public infrastructure. They are meant as a starting point for setting-up
GPU or ASAN buildbots.


Redesign
--------

Have a unified bot that builds all relevant recipes:

1) Julia from the release branches
- release-0.5
- release-0.6
- master

These should generate dist archives (including `llvm-config` and the like, so just tarring
`usr`), and upload it to the master.


2) Package builders

eg. for LLVM, CUDAdrv

These track a package repo, take a Julia version name, and test the package much like it is
done on Travis now.

These should optionally allow to check-out certain dependencies from `master` (eg.
CUDAnative package builder should probably use CUDAdrv and LLVM from master -- but maybe
also have a tag builder with normal check-outs).


GitHub hook
-----------

* Payload URL: `/change_hook/github` relative to the root
* Content Type: `application/x-www-form-urlencoded`
* Secret: same as `passwords.github['webhook']`
* Events: Push and Pull Request
