# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=relative-beyond-top-level

import tensorflow as tf
tf.compat.v1.enable_eager_execution()

from util import logging as logutil


logger = logutil.Logger(loggee="networks/base")


class Network:
    def __init__(self):
        self.layers = []

    def __call__(self, x):
        raise NotImplementedError

    @staticmethod
    def str2none(str_):
        """Mostly to overcome there being no `config.getnone()` method.
        """
        assert isinstance(str_, str), "Call this only on strings"
        if str_.lower() == 'none':
            return None
        return str_
