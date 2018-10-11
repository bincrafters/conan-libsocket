#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cpt.packager import ConanMultiPackager
import os

if __name__ == "__main__":
	builder = ConanMultiPackager(username='bincrafters',
					login_username=os.environ.get('CONAN_LOGIN_USERNAME'),
					upload=os.environ.get('CONAN_UPLOAD'),
					password=os.environ.get('CONAN_PASSWORD'),
					channel='testing'
					)
	
	builder.add_common_builds()
	builder.run()
