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

"""
This module contains the JSDConfig class, which loads and stores data from a YAML file.
"""

import os
from typing import List, Optional, Dict, Union, Any

from pydantic import BaseModel, Field, ValidationError
from pydantic.dataclasses import dataclass
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class NumericColumnConfig(BaseModel):
    """
    NumericColumnConfig model to represent numeric column configurations in the YAML configuration.
    """
    raw_column: str = Field(..., alias='raw column')
    bins: List[float]
    labels: Optional[List[str]] = None
    adjust_outliers: bool = Field(False, alias='adjust outliers')

class DataSourceConfig(BaseModel):
    """
    DataSource model to represent individual data sources in the YAML configuration.
    """
    name: str
    description: Optional[str] = None
    data_type: str = Field(..., alias='data type')
    filename: str
    columns: Optional[List[str]] = None
    numeric_cols: Optional[Dict[str, NumericColumnConfig]] = None
    plugin: Optional[str] = None
    date: Optional[str] = None
    date_column: Optional[str] = Field('date', alias='date column')
    remove_column_name_text: Optional[List[str]] = Field(None, alias='remove column name text')

    content: Optional[Any] = None  # Placeholder for loaded content
    content_type: Optional[str] = None  # Placeholder for content type after loading

    class Config:
        validate_by_name = True
        extra = 'allow'

DataSourceConfigList = List[DataSourceConfig]

class ConfigData(BaseModel):
    """
    ConfigData model to represent the structure of the YAML configuration data.
    """
    # Define fields based on expected YAML structure
    data_sources: DataSourceConfigList = Field(..., alias='data sources')
    custom_age_ranges: Optional[Dict[str, List[Union[int, float]]]] = Field(None, alias='custom_age_range')

    class Config:
        validate_by_name = True
        # accept extra fields in the YAML
        extra = 'allow'


class JSDConfig:
    """
    The JSDConfig class loads and stores data from a YAML file.

    Attributes:
        filename (str): The name of the YAML file to load. Default is 'jsdconfig.yaml'.
        data (dict): The loaded data from the YAML file.

    Methods:
        __init__(self, filename='jsdconfig.yaml'): Initializes a new instance of JSDConfig.
        _load_data(self): Loads the YAML data from the current filename.
        set_filename(self, new_filename): Sets a new filename and reloads the data.
    """
    filename: str
    data: Optional[ConfigData]

    def __init__(self, filename: str = 'jsdconfig.yaml'):
        """Load the YAML data from the current filename."""
        self.filename = filename
        self.data = None
        # os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
        self._load_data()

    def _load_data(self):
        """Load the YAML data from the current filename."""
        if not os.path.exists(self.filename):
            print(f"File {self.filename} does not exist. Skipping load.")
            print(f"Current working directory: {os.getcwd()}")
            self.data = None
            return

        with open(self.filename, 'r', encoding='utf-8') as stream:
            raw = load(stream, Loader=Loader)
        try:
            self.data = ConfigData(**raw)
        except ValidationError as e:
            self.data = None
            raise
        # print(dump(self.data))

    def set_filename(self, new_filename: str):
        """
        Set a new filename and reload the data.

        Args:
            new_filename (str): The new filename to load.
        """
        self.filename = new_filename
        self._load_data()
