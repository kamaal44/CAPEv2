# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from __future__ import absolute_import
import os
import shutil
import logging

from lib.common.abstracts import Package

log = logging.getLogger(__name__)

class Shellcode_x64(Package):
    """DLL analysis package."""
    #PATHS = [
    #    ("SystemRoot", "system32"),
    #]

    def start(self, path):
        loaderpath = "bin\\loader_x64.exe"
        arguments = "shellcode " + path

        # we need to move out of the analyzer directory
        # due to a check in monitor dll
        basepath = os.path.dirname(path)
        newpath = os.path.join(basepath, os.path.basename(loaderpath))
        shutil.copy(loaderpath, newpath)

        log.info("[-] newpath : "+newpath)
        log.info("[-] arguments : "+arguments)

        return self.execute(newpath, arguments, newpath)
