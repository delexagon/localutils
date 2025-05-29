import pathlib
import os
import importlib.machinery
import sys

class LocalFinder(importlib.machinery.PathFinder):
    def __init__(self, parent_module, folder):
        self.parent_module = parent_module
        self.folder = folder

    def find_spec(self, module_path, a, b):
        if module_path.startswith(f'{self.parent_module}.'):
            script = module_path.split('.',1)[1]
            full_path = self.folder/f'{script}.py'
            if not full_path.is_file():
                return None
            loader = importlib.machinery.SourceFileLoader(module_path, str(full_path))
            return importlib.machinery.ModuleSpec(module_path, loader)
        return None

sys.meta_path.append(LocalFinder('localutils', pathlib.Path('/etc/python_utils')))
sys.meta_path.append(LocalFinder('localutils', pathlib.Path.home()/'.python_utils'))
