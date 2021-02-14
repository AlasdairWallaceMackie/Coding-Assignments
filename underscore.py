class Underscore:
    def map(self, iterable, callback):
        new_iterable = []
        for i in range ( len(iterable) ):
            new_iterable.append( callback( iterable[i] ) )
        return new_iterable

    def find(self, iterable, callback):
        for i in range ( len(iterable) ):
            if callback(iterable[i]) == True:
                return iterable[i]
        return None

    def filter(self, iterable, callback):
        new_iterable = []
        for i in range ( len(iterable) ):
            if callback(iterable[i]) == True:
                new_iterable.append(iterable[i])
        return new_iterable

    def reject(self, iterable, callback):
        new_iterable = []
        for i in range ( len(iterable) ):
            if callback(iterable[i]) == False:
                new_iterable.append( iterable[i] )
        return new_iterable
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print (evens)
# should return [2, 4, 6] after you finish implementing the code above

first_even = _.find([1,2,3,4,5,6], lambda x: x % 2 == 0)
print (first_even)

non_evens = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print (non_evens)

squares = _.map([1,2,3,4,5,6], lambda x: x * x)
print (squares)