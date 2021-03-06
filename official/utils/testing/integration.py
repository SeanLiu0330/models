# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Helper code to run complete models from within python.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import os
import shutil
import sys
import time


def run_synthetic(main, extra_flags=None):
  """Performs a minimal run of a model.

    This function is intended to test for syntax errors throughout a model. A
  very limited run is performed using synthetic data.

  Args:
    main: The primary function used to excercise a code path. Generally this
      function is "<MODULE>.main(argv)".
    extra_flags: Additional flags passed by the the caller of this function.
  """

  extra_flags = [] if extra_flags is None else extra_flags

  model_dir = "/tmp/model_test_{}".format(hash(time.time()))
  if os.path.exists(model_dir):
    shutil.rmtree(model_dir)

  args = [sys.argv[0], "--model_dir", model_dir, "--train_epochs", "1",
          "--epochs_per_eval", "1", "--use_synthetic_data",
          "--max_train_steps", "1"] + extra_flags

  try:
    main(args)
  finally:
    if os.path.exists(model_dir):
      shutil.rmtree(model_dir)
