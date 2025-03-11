#  Copyright (c) 2024 Medical Imaging and Data Resource Center (MIDRC).
#
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#
#
#  This work was supported in part by The Medical Imaging and Data Resource
#  Center (MIDRC), which is funded by the National Institute of Biomedical
#  Imaging and Bioengineering (NIBIB) of the National Institutes of Health under
#  contract 75N92020D00021/5N92023F00002 and through the Advanced Research
#  Projects Agency for Health (ARPA-H).

"""
This module contains the main function to launch the MIDRC-REACT application.
"""

from midrc_react.gui.pyside6.launch_react import launch_react


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    launch_react()
