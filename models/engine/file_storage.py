"""Creating a class that serializes instances to JSON and deserializes JSON to instance """
import json
from os.path import exists  # module to check if file exists


import json
from os.path import exists

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects if the file exists."""
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    class_instance = globals()[class_name]
                    obj_instance = class_instance(**obj_dict)
                    self.__objects[key] = obj_instance


# class FileStorage:
#     __file_path = "file.json"
#     __objects = {}
#
#     def all(self):
#         """Returns the dictionary __objects"""
#         return self.__objects
#     def new(self, obj):
#         obj = self.__objects.id