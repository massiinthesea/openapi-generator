# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from petstore_api.models.creature_info import CreatureInfo
from typing import Optional, Set
from typing_extensions import Self

class UnnamedDictWithAdditionalModelListProperties(BaseModel):
    """
    UnnamedDictWithAdditionalModelListProperties
    """ # noqa: E501
    dict_property: Optional[Dict[str, List[CreatureInfo]]] = Field(default=None, alias="dictProperty")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["dictProperty"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UnnamedDictWithAdditionalModelListProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each value in dict_property (dict of array)
        _field_dict_of_array = {}
        if self.dict_property:
            for _key in self.dict_property:
                if self.dict_property[_key] is not None:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.dict_property[_key]
                    ]
            _dict['dictProperty'] = _field_dict_of_array
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict]) -> Optional[Self]:
        """Create an instance of UnnamedDictWithAdditionalModelListProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dictProperty": dict(
                (_k,
                        [CreatureInfo.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("dictProperty", {}).items()
            )
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


