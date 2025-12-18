"""
Setup script for nvdiffrec_render wheel building.
This builds the render utilities from NVlabs/nvdiffrec as a standalone package.
"""
from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import os

# Source files for renderutils CUDA extension
cuda_sources = [
    'nvdiffrec_render/renderutils/c_src/mesh.cu',
    'nvdiffrec_render/renderutils/c_src/loss.cu',
    'nvdiffrec_render/renderutils/c_src/bsdf.cu',
    'nvdiffrec_render/renderutils/c_src/normal.cu',
    'nvdiffrec_render/renderutils/c_src/cubemap.cu',
    'nvdiffrec_render/renderutils/c_src/common.cpp',
    'nvdiffrec_render/renderutils/c_src/torch_bindings.cpp',
]

setup(
    name='nvdiffrec_render',
    version='0.0.1',
    description='Render utilities from NVlabs/nvdiffrec for differentiable rendering',
    packages=find_packages(),
    package_data={
        'nvdiffrec_render': ['*.bin'],
    },
    include_package_data=True,
    ext_modules=[
        CUDAExtension(
            name='nvdiffrec_render.renderutils._C',
            sources=cuda_sources,
            extra_compile_args={
                'cxx': ['-O3', '-DNVDR_TORCH'],
                'nvcc': ['-O3', '-DNVDR_TORCH'],
            },
        ),
    ],
    cmdclass={'build_ext': BuildExtension},
    install_requires=[
        'torch',
        'numpy',
    ],
)
