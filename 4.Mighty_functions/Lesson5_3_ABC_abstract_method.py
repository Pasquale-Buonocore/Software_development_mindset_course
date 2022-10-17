'''
When dealing with classes and inheritance, it could be needed to CONSTRAINT the presence of some methods.
We can do it having a super class of ABC class type, whose methods are decorated with the @abstractmethod property.

In the example below:
- Animal is defined as a class of ABC with method __repr__ and feed as @abstractmethod.
- The Lion class inherit from Animal. What does it mean?

It means that the Lion class SHALL have the __repr__ and feed method, otherwise it will not be possible to instanciate a Lion class.
We can use that when we want to be sure that the class have specific method.

It can also be used to specify an attribute?

'''

from abc import ABC, abstractmethod 

class Animal(ABC): # Inherit from ABC(Abstract base class)
    
    @abstractmethod
    def __repr__(self) -> None:
        pass

    @abstractmethod # decorator to define an abstract method
    def feed(self) -> None:
        pass

    #####################
    ## PROPERTY START ###
    #####################
    @property                 
    def food_eaten(self):     
        return self._food

    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self._food = food
        else:
            raise ValueError(f"You can't feed this animal with {food}.")

    @property
    @abstractmethod
    def diet(self):
        pass

    #####################
    ## PROPERTY END ###
    #####################

class Lion(Animal):
    
    @property                 
    def diet(self):     
        return ["antelope", "cheetah", "buffaloe"]

    def __repr__(self) -> str:
        return 'Lion'

    def feed(self) -> None:
        print(f"Feeding the animal " + self.__repr__())


if __name__ == '__main__':
    Lion = Lion()
    Lion.feed()
    Lion.food_eaten = 3
    print(Lion.food_eaten)
