class plotthings(object):
# This is a class, which is a convenient way of organizing functions and 
# reusing the same functions many times "cleanly".
# More about what "cleanly" means below.

    def __init__(self,ending,numofpoints):
        # This is an example of a dunder method, one which is reserved by Python.
        # __init__ will run first thing no matter what when accessing the "plottings" class.
        # The 'self' keyword is CRUCIAL. DO NOT OMIT. ALSO KEEP IT AS THE FIRST ARGUMENT.
        # Also, by convention, use the name "self", though you can also say "banana" or "astronaut" or whatever.
        self.arr = np.linspace(0,ending,numofpoints)
        # kinda similar to MATLAB, eh? Notice that "linspace" belongs to Numpy (shown as np), 
        # so you can't just ingnore "np".

    def sinefxn(self):
        # Notice here how "arr" is fully contained within "self", so i don't need to say self.arr
        # because Python knows what is inside of what.
        print("here's a sine!")
        self.sinusoid = np.sin(self.arr)
        plt.plot(self.arr, self.sinusoid, color='r', linewidth=0.25)
        plt.show()
        # if you ignore plt.plot nothing will show up.

    def linearfxn(self):
        print("here's a straight line!")
        self.linear = self.arr - 10
        plt.plot(self.arr, self.linear, color='b', linewidth=2)
        plt.show()

if __name__ == "__main__":
    # the whole __name__ thing is just a good convention to follow.
    import numpy as np
    import matplotlib.pyplot as plt
    # just because you installed something doesn't mean it imported (i.e. usable in this script)!
    # you don't need the "as np" part, but it makes life easier.

    try:
    # try-except is good to have. if an error occurs in the "try" block, instead of the compiler quitting
    # the "except" block will run, which is good because it's a clean way of doing things wrong.
        userchoice = int(input("do you want a sine(0) or straight line(1)? "))
        if userchoice == 0:
            wavy = plotthings(np.pi,100)
            # IMPORTANT: "wavy" and "straight" don't know each other. In fact, within this "if" statement
            # I could have additionally added another class instance, but it would be completely separate from 
            # any other instance. This is why classes can be re-used many times, because each instance
            # is an independent instance, though they use the same code.
            wavy.sinefxn()
            # Now I call the function within the instantiated class outside of the class. 
            # I could have also called self.sinefxn() inside the class.
        elif userchoice == 1:
            straight = plotthings(25,100)
            straight.linearfxn()
        else:
            print("not a valid input")
    except:
        print("input error")