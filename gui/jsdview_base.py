from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QMainWindow

from dataclasses import dataclass

@dataclass
class GroupBoxData:
    _file_infos = []
    _category_info = {
        'current_text': None,
        'current_index': None,
        'category_list': [],
    }

    @property
    def file_infos(self):
        return self._file_infos

    def get_file_infos(self):
        return self._file_infos

    def append_file_info(self, file_info: dict):
        file_info['checked'] = file_info.get('checked', True)
        self._file_infos.append(file_info)
        # TODO: Update the category list too?

    @property
    def category_info(self):
        return self._category_info

    def get_category_info(self):
        return self._category_info

    def update_category_list(self, categorylist, categoryindex):
        self._category_info = {
            'current_text': categorylist[categoryindex],
            'current_index': categoryindex,
            'category_list': categorylist,
        }

    def update_category_index(self, categoryindex):
        self._category_info['current_index'] = categoryindex
        self._category_info['current_text'] = self._category_info['category_list'][categoryindex]

    def update_category_text(self, categorytext):
        category_list = self._category_info['category_list']
        if categorytext in category_list:
            self._category_info['current_text'] = categorytext
            self._category_info['current_index'] = category_list.index(categorytext)


class JsdViewBase(QObject):
    add_data_source = Signal(dict)

    def __init__(self):
        if not isinstance(self, QMainWindow):
            super().__init__()
        self.update_view_on_controller_initialization = True
        self._dataselectiongroupbox = GroupBoxData()

    @property
    def dataselectiongroupbox(self):
        return self._dataselectiongroupbox

    def open_excel_file(self, data_source_dict):
        self._dataselectiongroupbox.append_file_info({
            'description': data_source_dict['description'],
            'source_id': data_source_dict['name'],
            'index': len(self._dataselectiongroupbox.file_infos),
            'checked': True,
        })

    def update_pie_chart_dock(self, sheet_dict):
        pass

    def update_spider_chart(self, spider_plot_values_dict):
        pass

    def update_jsd_timeline_plot(self, jsd_model):
        pass

    def update_area_chart(self, sheet_dict):
        pass