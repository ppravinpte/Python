'''Class Inheritance :Inheritance allows one class to take some methods and 
properties from another class using super(). 
In below, Printer inherits methods of Device class and can also add new methods 
in it's class which are only limited to it's own.'''
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
     
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"
        #note:!r add quotes in o/p => Device 'Printer' (USB)
        #return f"Device {self.name} ({self.connected_by})"
     
    def disconnect(self):
        self.connected = False
        print ("Disconnected.")

printer = Device("Printer", "USB")
print(printer) # o/p: Device 'Printer' (USB)

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        #super class - it gets parent classs "Device" and calls the init method.
        super().__init__(name, connected_by)
        # below is new parameter only present and accessible for this class
        self.capacity = capacity # maximum pages
        self.remaining_pages = capacity # remaining pages
    
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages

printer =  Printer("Printer", "USB", 500)  # o/p: Device 'Printer' (USB)
printer.print(20)       # o/p: Printing 20 pages.

print(printer)          # o/p: Device 'Printer' (USB) (480 pages remaining)
printer.disconnect()    # o/p: Disconnected.
printer.print(30)       # o/p: Your printer is not connected!
