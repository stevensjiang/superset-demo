# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Tests for superset.views.utils module"""

from superset.views.utils import (
    JS_CONTROL_FORM_DATA_KEYS,
    REJECTED_FORM_DATA_KEYS,
)


def test_js_control_lists_are_empty_after_removal() -> None:
    """JS-based controls have been removed; both lists should be empty."""
    assert JS_CONTROL_FORM_DATA_KEYS == []
    assert REJECTED_FORM_DATA_KEYS == []
