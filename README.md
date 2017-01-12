This repository contains build recipes for two non-official Julia buildbots.
- `juliacpu`: regular CPU builds, both per-commit and daily ASAN build
- `juliagpu`: GPU toolchain integration testing, pulling code from julia, LLVM.jl,
   CUDAdrv.jl and CUDAnative.jl

These recipes are not meant to be usable as-is, and contain hardcoded references
to non-public infrastructure. They are meant as a starting point for setting-up
GPU or ASAN buildbots.
