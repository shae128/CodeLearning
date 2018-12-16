class One:
        def doit(self):
                print("doit from One")
        def doanything(self):
                self.doit()


class Two(One):
        def doit(self):
                print("doit from Two")


one = One()
two = Two()

one.doanything()
two.doanything()
