from pythonforandroid.toolchain import shprint, current_directory
from pythonforandroid.recipe import Recipe
from multiprocessing import cpu_count
from os.path import exists,join
import sh
import os

class LibudevRecipe(Recipe):
    version = 'master'
    url = 'https://github.com/gentoo/eudev/archive/master.zip'
    call_hostpython_via_targetpython = False
    # depends=['libc']
    def build_arch(self, arch):
        super(LibudevRecipe, self).build_arch(arch)
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            shprint(sh.Command('./autogen.sh'),
            '--host=arm-linux')
            shprint(sh.Command('./configure'),
            '--host=arm-linux',
            '--prefix=' + self.ctx.get_python_install_dir(),
            _env=env)
            shprint(sh.make, _env=env)

recipe = LibudevRecipe()
