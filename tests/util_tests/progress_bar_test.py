#!/usr/bin/env python
# encoding:utf8

import os
import sys
import require
from utils.progress_bar_util import ProgressBarUtil

progressBar = ProgressBarUtil("请求中", 1)
progressBar.refresh(0.1)
progressBar.refresh(0.2)
progressBar.refresh(0.3)


