



import os
import shutil

import mem
from mem import util
from mem._mem import Mem




@util.with_env(DESTDIR=".")
@mem.memoize
def install(source, DESTDIR):
    if DESTDIR is None:
        DESTDIR = Mem.instance().cwd
    mem.add_dep(source)

    target = os.path.join(DESTDIR, source.basename())
    source = mem.util.convert_cmd([source])[0]

    mem.util.ensure_dir(DESTDIR)

    def copier(*args, **kwargs):
        shutil.copy2(*args, **kwargs)
        return (0, "", "")


    if mem.util.run_return_output("Installing to %s" % DESTDIR,
                                  source,
                                  copier,
                                  source,
                                  target)[0]:
        mem.fail()

    return mem.nodes.File(target)

