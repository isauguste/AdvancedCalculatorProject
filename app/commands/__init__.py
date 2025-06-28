import importlib
import os

def load_commands():
    commands = {}
    package_dir = os.path.dirname(__file__)
    
    for filename in os.listdir(package_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"app.commands.{filename[:-3]}"
            module = importlib.import_module(module_name)
            for attr in dir(module):
                obj = getattr(module, attr)
                if hasattr(obj, "name") and hasattr(obj, "execute"):
                    commands[obj.name] = obj.execute
    return commands
