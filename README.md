# nvdiffrec_render-wheels

Pre-built Python wheels for `nvdiffrec_render` (rendering utilities from [NVlabs/nvdiffrec](https://github.com/NVlabs/nvdiffrec)).

## Install

```bash
pip install nvdiffrec_render --find-links https://PozzettiAndrea.github.io/nvdiffrec_render-wheels/
```

## Supported Configurations

| CUDA | PyTorch | Python Versions |
|------|---------|-----------------|
| 12.4 | 2.5.1 | 3.10, 3.11, 3.12 |
| 12.6 | 2.6.0 | 3.10, 3.11, 3.12, 3.13 |
| 12.6 | 2.8.0 | 3.10, 3.11, 3.12, 3.13 |
| 12.8 | 2.8.0 | 3.10, 3.11, 3.12, 3.13 |
| 12.8 | 2.9.1 | 3.10, 3.11, 3.12, 3.13 |

**Platforms:** Linux (x86_64), Windows (amd64)

**GPU Support:** RTX 20/30/40/50 series (SM 7.5+)

## Building Manually

To trigger a build for a specific configuration, go to Actions and run the corresponding workflow.

## License

The nvdiffrec rendering utilities are under NVIDIA Source Code License. See the original repository for details.
