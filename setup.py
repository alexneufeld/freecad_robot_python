from setuptools import setup

__version__ = "0.0.0"  # FIXME

setup(
    name="freecad.robot_python",
    version=str(__version__),
    packages=["freecad", "freecad.robot_python"],
    maintainer="Alex Neufeld",
    maintainer_email="alex.d.neufeld@gmail.com",
    url="github.com/alexneufeld/freecad_robot_python/",
    description="A FreeCAD addon for simulating multi-axis robots",
    install_requires=[
        "PyKDL",
    ],
    include_package_data=True,
)
