## Context managers
-Write own context manager which main purpose is works only with CSV files in append mode.
-Reimplement previous context manager with contextmanager decorator (search in contextlib)

## OOP
- Write a class for creating completely generic objects: its `__init__` function should accept any number of keyword parameters, and set them on the object as attributes with the keys as names. Write a `__str__` method for the class – the string it returns should include the name of the class and the values of all the object’s custom instance attributes.
- Create a class called `Arithmetic`, which has a class constant attribute called MULTIPLIER, and a constructor which takes the parameters x and y (these should all be integers).
    - Write a method called divide which returns the division of the attributes x and y.
    - Write a class method called multiply, which takes a single number parameter x and returns the product of a and MULTIPLIER.
    - Write a static method called operation, which takes operation type (add or subtract) and two number parameters, a and b, and returns b - a.
    - Write a method called value which returns a tuple containing the values of x and y. Make this method into a property, and write a setter.
- Create a base class `Polygon`, which has two methods - a method for calculating the area of a figure and a method for calculating the perimeter of a figure.
- Create a `Triangle` class that implements methods for calculating the area and perimeter of the shape. Write methods that determine whether a given triangle is rectangular or equilateral.
- Create a class `Rectangle` that implements methods for calculating the area and perimeter of the shape. Write a method that determines whether a given rectangle is a square.
- Create a `Circle` class that implements a method for calculating the area of a shape.

# Updates
Create abstract class Application, which initializes with attributes - `name`, `release date` and `version` (remember how usually version are marked). Prevent creation unnecessary attributes using slots (research into that).
   - Implement `__str__` and `__repr__` methods
   - Add possibility to compare class instances, like `app1 > app2, app1 < app2, app1 == app2` by year and version
- Create class `AndroidApplication` inherited of `Application`.
    - Add method to get application `link in Google Play Market`
    - Add methods to get and set list of compatible `Android versions`
- Create class `IOSApplication` inherited of `Application`
    - Add method to get application `link in AppStore`
- Create class `DesktopApplication` inherited of `Application`
    - Add method to get and set `platform attribute`. Available platforms is `windows, linux, macos`. Attribute must be set as a list of available platforms
- Add attribute `Description` which must not contain more that 250 symbols
- Add method `short description` which returns first 10 words if description more than 50 symbols
- Add class `JSONSerializable` with one method to_json() which convert class instance to JSON object. All previous classes must be inherited from this class to add `JSON serialization functionality`