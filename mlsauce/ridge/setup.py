import os


def configuration(parent_package="", top_path=None):
    import numpy
    from numpy.distutils.misc_util import Configuration

    config = Configuration("ridge", parent_package, top_path)

    libraries = []
    if os.name == "posix":
        libraries.append("m")

    config.add_extension(
        "_ridgec",
        sources=["_ridgec.pyx"],
        include_dirs=numpy.get_include(),
        libraries=libraries,
    )

    return config


if __name__ == "__main__":
    from numpy.distutils.core import setup

    setup(**configuration(top_path="").todict())
