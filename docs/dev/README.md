# Developer Documentation

## Running behaviour tests

To run all of the behaviour tests from the FreeCAD Gui Console:

``` python
from FreeCAD import Test
from freecad.robotpy.test import TestRobotPy, TestRobotPyGui
for cls in TestRobotPy + TestRobotPyGui:
    Test.runTestsFromClass(cls)


```

Use this command to run only the non-GUI tests from a terminal window. These will generally run faster, because the load time of the full GUI is skipped.

``` bash
freecad -c 'exec("""\nfrom FreeCAD import Test\nfrom freecad.robotpy.test import TestRobotPy\nfor cls in TestRobotPy:\n    Test.runTestsFromClass(cls)\n""")'

```


## Compiling PyKDL

We'll need these bindings to access the robot kinematic solver. Begin by downloading the code from the [Github Repository](https://github.com/orocos/orocos_kinematics_dynamics)

``` bash
git clone git@github.com:orocos/orocos_kinematics_dynamics.git
cd orocos_kinematics_dynamics/
git submodule update --init # init pybind11 submodule
```

Build the c++ library first.

I chose to override the default installation folder to avoid installing to my `/usr` folder, which requires root permissions.

``` bash
cd orocos_kdl/
mkdir build
cd build/
cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local ..
make -j$(nproc)
make install # installs liborocos-kdl.so.1.5 to $HOME/.local/lib
```

For non Debian-based systems, override the `dist-packages` install directory convention (see [StackOverflow](https://stackoverflow.com/questions/9387928/whats-the-difference-between-dist-packages-and-site-packages) for details):

``` bash
ln -s $HOME/.local/lib/python3.x/site-packages $HOME/.local/lib/python3.x/dist-packages
```

Now build the python bindings:

``` bash
cd ../../python_orocos_kdl
mkdir build
cd build/
cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local ..
make -j$(nproc)
make install # installs PyKDL.so to $HOME/.local/lib/python3.x/dist-packages
```



We'll also need to create a symbolic link to site-packages in the FreeCAD Mod folder, to allow it to find our freshly built .so file:

``` bash
ln $HOME/.local/lib/python3.x/site-packages $HOME/.local/share/FreeCAD/python_site_packages
> $HOME/.local/share/FreeCAD/python_site_packages/init.py
```


run FreeCAD from the command line, appending to LD_LIBRARY_PATH so that PyKDL.so links correctly:
``` bash
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.local/lib freecad
```
