import sys
from . import ui_utils
from .ui_utils import QtCore, QtWidgets

from . import tool_name_system

        
class ToolNameWindow(ui_utils.ToolWindow):
    def __init__(self):
        super(ToolNameWindow, self).__init__()
        
        # add simple button example
        self.add_button("Example Button", self.example_action)
    
    def example_action(self):
        print("Example button triggered")


def main(refresh=False):
    existing_app = QtWidgets.QApplication.instance()
    
    # if running in standalone, create app
    standalone_app = None
    if not existing_app:
        standalone_app = QtWidgets.QApplication(sys.argv)
    
    win = ToolNameWindow()
    win.main(refresh=refresh)
    
    if standalone_app:
        sys.exit(standalone_app.exec_())


if __name__ == "__main__":
    main()
