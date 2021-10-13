import sys
import site
import inspect
import os

def _tool_name_site_dir_setup():
    dirname = os.path.dirname
    
    # Add site-packages to sys.path
    package_dir = dirname(dirname(dirname(dirname(inspect.getfile(inspect.currentframe())))))
    
    if package_dir not in sys.path:
        site.addsitedir(package_dir)

_tool_name_site_dir_setup()


try:
    import tool_name
    tool_name.startup()
except StandardError as e:
    print(e)
