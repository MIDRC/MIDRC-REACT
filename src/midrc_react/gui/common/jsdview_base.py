#  Copyright (c) 2025 Medical Imaging and Data Resource Center (MIDRC).
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

"""
This module contains the JsdViewBase class, which serves as a base class for JSD views.
"""

from typing import List, Optional, Union

from pydantic import BaseModel, Field
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMainWindow


class FileInfo(BaseModel):
    description: Optional[str] = None
    source_id: Optional[str] = None
    index: Optional[int] = None
    checked: bool = True

FileInfoList = List[FileInfo]

class CategoryInfo(BaseModel):
    current_text: Optional[str] = None
    current_index: Optional[int] = None
    category_list: List[str] = Field(default_factory=list)

class GroupBoxData(BaseModel):
    """
    This class represents a group box widget for data selection. It provides functionality for creating labels and
    combo boxes for data files and a category combo box. The class has methods for setting up the layout,
    updating the category combo box, and initializing the widget.

    Attributes:
        file_infos (list): A list of file information dictionaries.
        category_info (dict): A dictionary containing information about the selected category.
    """
    file_infos: FileInfoList = Field(default_factory=list)
    category_info: CategoryInfo = Field(default_factory=CategoryInfo)

    def get_file_infos(self) -> FileInfoList:
        """
        Get the file information dictionaries.

        Returns:
            list: A list of file information dictionaries.
        """
        return self._file_infos

    def append_file_info(self, file_info: Union[dict, FileInfo]):
        """
        Appends a file information dictionary to the list of file information dictionaries.

        Args:
            file_info (dict): file information dictionary to append to the list
        """
        if isinstance(file_info, dict):
            file_info.setdefault('checked', True)
            file_info = FileInfo(**file_info)
        elif isinstance(file_info, FileInfo):
            # ensure checked is set
            file_info.checked = bool(file_info.checked)
        self.file_infos.append(file_info)
        # TODO: Update the category list too?

    def get_category_info(self) -> CategoryInfo:
        """
        Get the category information dictionary.

        Returns:
            dict: A dictionary containing information about the selected category.
        """
        return self.category_info

    def update_category_list(self, categorylist: List[str], categoryindex: int):
        """
        Updates the category information dictionary with the given category list and index.

        Args:
            categorylist (list(str)): List of categories to add to the information dictionary
            categoryindex (int): Index to set the current index to (and item in the category list)

        Returns:
            None
        """
        self.category_info = CategoryInfo(
            current_text = categorylist[categoryindex],
            current_index = categoryindex,
            category_list = categorylist,
        )

    def update_category_index(self, categoryindex: int):
        """
        Updates the category information dictionary with the given category index.

        Args:
            categoryindex (int): Index to set the current category to

        Returns:
            None
        """
        self.category_info.current_index = categoryindex
        if 0 <= categoryindex < len(self.category_info.category_list):
            self.category_info.current_text = self.category_info.category_list[categoryindex]
        else:
            self.category_info.current_text = None

    def update_category_text(self, categorytext: str):
        """
        Updates the category information dictionary with the given category text.

        Args:
            categorytext (str): The category to set the current category text (and current index) to

        Returns:
            None
        """
        if categorytext in self.category_info.category_list:
            self.category_info.current_text = categorytext
            self.category_info.current_index = self.category_info.category_list.index(categorytext)


class JsdViewBase(QObject):
    """
    This class represents a base class for JSD views. It provides functionality for creating a data selection group box,
    updating the category combo box, and initializing the widget.

    Attributes:
        _data_selection_group_box (GroupBoxData): A data selection group box.
        _controller (JSDController): A JSDController object.
        update_view_on_controller_initialization (bool): A flag indicating whether the view should be updated on
                                                         controller initialization.
    """
    _data_selection_group_box = GroupBoxData()
    _controller = None
    update_view_on_controller_initialization = True
    add_data_source = Signal(dict)

    def __init__(self):
        """
        Initialize the JsdViewBase.
        """
        if not isinstance(self, QMainWindow):
            super().__init__()
        self.update_view_on_controller_initialization = True
        self._dataselectiongroupbox = GroupBoxData()

    @property
    def dataselectiongroupbox(self):
        """
        Get the data selection group box.

        Returns:
            GroupBoxData: The data selection group box.
        """
        return self._dataselectiongroupbox

    def open_excel_file(self, data_source_dict):
        """
        Opens an Excel file and adds it to the data selection group box.

        Args:
            data_source_dict (DataSource): The data source dictionary.
        """
        self._dataselectiongroupbox.append_file_info(FileInfo(
            description = data_source_dict.description,
            source_id = data_source_dict.name,
            index = len(self._dataselectiongroupbox.file_infos),
            checked = True,
        ))

    def update_pie_chart_dock(self, sheet_dict):
        """
        Updates the pie chart dock with the given sheet dict.

        Args:
            sheet_dict (dict): A dictionary of index keys and sheets.
        """
        pass  # pylint: disable=unnecessary-pass

    def update_spider_chart(self, spider_plot_values_dict):
        """
        Updates the spider chart with new values.

        Args:
            spider_plot_values_dict (dict): A dictionary of dictionaries where each dictionary contains
                the values for one series on the spider chart.
        """
        pass  # pylint: disable=unnecessary-pass

    def update_jsd_timeline_plot(self, jsd_model):
        """
        Updates the JSD timeline plot with the specified JSD model.

        Args:
            jsd_model (JSDTableModel): The JSDTableModel that contains the data for generating the timeline plot.
        """
        pass  # pylint: disable=unnecessary-pass

    def update_area_chart(self, category):
        """
        Updates the area chart with new data.

        Args:
            category: The category to use for updating the area charts.
        """
        pass  # pylint: disable=unnecessary-pass
