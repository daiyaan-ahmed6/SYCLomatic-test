# ====------ do_test.py---------- *- Python -* ----===##
#
# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
#
#
# ===----------------------------------------------------------------------===#
import subprocess
import platform
import os
import sys

from test_utils import *

def setup_test():
    change_dir(test_config.current_test)
    return True

def migrate_test():
    call_subprocess(test_config.CT_TOOL + " test.cu --out-root=out --cuda-include-path=" + test_config.include_path + " --extra-arg=-xc++")
    return not is_sub_string("warning: '-x c' after last input file has no effect [-Wunused-command-line-argument]", test_config.command_output)

def build_test():
    return call_subprocess("icpx -fsycl out/test.dp.cpp")

def run_test():
    return True