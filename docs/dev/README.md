# Developer Documentation

## Running behaviour tests

To run all of the behaviour tests from the FreeCAD Gui Console:

``` python
from FreeCAD import Test
from freecad.robotpy.test import TestRobotPy, TestRobotPyGui
for cls in TestRobotPy + TestRobotPyGui:
    Test.runTestsFromClass(cls)


```

Use this command to run only the non-GUI tests from a terminal window. These will generally run faster, beacuse the load time of the full GUI is skipped

``` bash
freecad -c 'exec("""\nfrom FreeCAD import Test\nfrom freecad.robotpy.test import TestRobotPy\nfor cls in TestRobotPy:\n    Test.runTestsFromClass(cls)\n""")'

```
