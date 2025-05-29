import ttkbootstrap as ttkb
from gui import DentalApp
if __name__ == "__main__":
    root = ttkb.Window()
    app = DentalApp(root)
    root.mainloop()