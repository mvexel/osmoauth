"""OSM helper types"""

import xml.etree.ElementTree as ET
import json

class User:
    """An OSM user"""
    def __init__(self, osm_id, display_name):
        self.osm_id = osm_id
        self.display_name = display_name

    @classmethod
    def from_xml(cls, xml):
        """Parse OSM API XML response to create user"""
        root = ET.fromstring(xml)
        user = root.find("user")
        attrib = user.attrib
        osm_id = attrib.get("id")
        display_name = attrib.get("display_name")
        user = cls(osm_id, display_name)
        return user

    def json(self):
        """dump obj as json"""
        return json.dumps({
            "osm_id": self.osm_id,
            "display_name": self.display_name})