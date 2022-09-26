from Lesson4_before_data_class_usage import FuelType, Accessory
from dataclasses import dataclass, field
'''
The code is refactoring introducing the concept of data classes.
If to role of a class is storing data, the @dataclass decorator might be useful!

What does that decarator do?
Data classes provide basic implementation of what a more oriented class could be like and remove useless code.

The Vehicle class has no methods and it is just used to store information.
'''

# It was before:
class Vehicle_before:
    def __init__(
        self,
        brand: str,
        model: str,
        color: str,
        license_plate: str,
        fuel_type: FuelType = FuelType.ELECTRIC,
        accessories: list[Accessory] = [],
    ) -> None:
        self.brand = brand
        self.model = model
        self.color = color
        self.fuel_type = fuel_type
        self.license_plate = license_plate
        self.accessories = accessories

# Using data classes it becomes
@dataclass(frozen=True)
class Vehicle:
    brand: str
    model: str
    color: str
    license_plate: str
    fuel_type: FuelType = FuelType.ELECTRIC
    accessories: list[Accessory] = field(default_factory=lambda: [Accessory.AIRCO])
'''
How does the accessories attribute is defined? Why not using just accessories: list[Accessory] = []?
Because @dataclasse would not allow it since datatype list is a mutable data type.
The default variable cannot be a mutable element.

We can use the field function having as argumento the default_factory.
accessories: list[Accessory] = field(default_factory = list)

if you do not want accessories to be initiable when creating an object, you could also:
accessories: list[Accessory] = field(default_factory = list, init = False)

Imagine that you want to initialize a value at object definition without allowing the user to set the accessories attributes.
You want to initialize accessories based on other init attribute. How do to so?

Defining the function __post_init__(self) which is called just before leaving the object creation class.
'''

# Let's do the example using the license_plate attributes
@dataclass()
class Vehicle_ex2:
    brand: str
    model: str
    color: str
    license_plate: field(init = False)
    fuel_type: FuelType = FuelType.ELECTRIC
    accessories: list[Accessory] = field(default_factory=lambda: [Accessory.AIRCO])

    def __post_init__(self):
        self.license_plate = '23123123'
        if self.brand == 'Tesla':
            self.license_plate += "-t"

'''
When defining a @dataclass what does frozen = True means?
That each object created for such class cannot be modified after initialization.
That means that we cannot use the frozen property and then the __post_init__ function.


Encapsulation -> hide implementation to the user
'''
if __name__ == '__main__':
    a = field(default_factory=lambda: [Accessory.AIRCO])
    ciao = 1