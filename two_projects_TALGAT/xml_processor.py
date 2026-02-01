from pymongo import MongoClient
import xml.etree.ElementTree as ET
import os
from datetime import datetime

class XMLProcessor:
    def __init__(self):
        self.client = None
        self.database = None
        self.schemas_collection = None
        self.search_results_collection = None
        self.database_connection_active = False
        self.current_document_data = None
        self.setup_database_connection()

    def setup_database_connection(self):
        try:
            self.client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
            self.client.server_info()
            self.database = self.client['talgat_db']
            self.schemas_collection = self.database['schemas']
            self.search_results_collection = self.database['search_results']
            self.database_connection_active = True
        except Exception:
            self.database_connection_active = False

    def load_and_process_xml(self, file_path):
        if not os.path.exists(file_path):
            return False

        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            parsed_elements = []
            counts = [0] * 10

            for elem in root.findall('.//Elements/*'):
                if not elem.tag.startswith('element'):
                    continue
                    
                name = elem.get('name', '')
                value = elem.get('value', '')
                typ = elem.get('type', '')
                x = elem.get('x', '')
                y = elem.get('y', '')

                if not name:
                    continue

                type_names = {
                    "0": "резистор", "1": "конденсатор", "2": "индуктивность",
                    "3": "источник напряжения", "4": "линия передачи", "5": "узел",
                    "6": "источник тока", "7": "сигнальная земля", "8": "земля", "9": "пробник"
                }

                type_name = type_names.get(typ, name)
                
                parsed_elements.append({
                    'name': name, 'type': type_name, 'value': value,
                    'x': x, 'y': y, 'filename': os.path.basename(file_path)
                })

                if typ.isdigit():
                    idx = int(typ)
                    if 0 <= idx < len(counts):
                        counts[idx] += 1

            self.current_document_data = {
                'filename': os.path.basename(file_path),
                'upload_date': datetime.now(),
                'parsed_elements': parsed_elements,
                'total_elements_count': len(parsed_elements),
                'resistors_count': counts[0], 'transmission_lines_count': counts[4],
                'voltage_sources_count': counts[3], 'capacitors_count': counts[1],
                'inductors_count': counts[2], 'nodes_count': counts[5],
                'current_sources_count': counts[6], 'signal_grounds_count': counts[7],
                'grounds_count': counts[8], 'probes_count': counts[9]
            }
            return True

        except Exception:
            return False

    def get_file_info(self):
        return self.current_document_data['filename'] if self.current_document_data else "файл не выбран"

    def get_upload_date(self):
        return self.current_document_data['upload_date'].strftime("%d.%m.%Y %H:%M") if self.current_document_data else ""

    def get_statistics(self):
        if not self.current_document_data:
            return ["нет данных"]

        data = self.current_document_data
        return [
            f"всего элементов: {data['total_elements_count']}",
            f"резисторы: {data['resistors_count']}", f"линии передачи: {data['transmission_lines_count']}",
            f"источники напряжения: {data['voltage_sources_count']}", f"конденсаторы: {data['capacitors_count']}",
            f"индуктивности: {data['inductors_count']}", f"узлы: {data['nodes_count']}",
            f"источники тока: {data['current_sources_count']}", f"сигнальные земли: {data['signal_grounds_count']}",
            f"земли: {data['grounds_count']}", f"пробники: {data['probes_count']}"
        ]

    def get_elements_for_table(self):
        return self.current_document_data.get('parsed_elements', []) if self.current_document_data else []

    def save_to_db(self):
        if not self.current_document_data or not self.database_connection_active:
            return False, "нет данных для сохранения или нет подключения к базе данных"

        try:
            self.current_document_data['upload_date'] = datetime.now()
            result = self.schemas_collection.insert_one(self.current_document_data)
            return True, f"сохранено с ID: {result.inserted_id}"
        except Exception as e:
            return False, f"ошибка сохранения: {e}"

    def search_elements_in_current(self, search_text):
        if not self.current_document_data:
            return []

        found_elements = []
        for element in self.current_document_data.get('parsed_elements', []):
            if (search_text.lower() in element.get('name', '').lower() or 
                search_text.lower() in element.get('type', '').lower() or 
                search_text.lower() in element.get('value', '').lower()):
                
                found_elements.append({
                    'filename': self.current_document_data.get('filename', 'текущая схема'),
                    'name': element.get('name', ''), 'type': element.get('type', ''),
                    'value': element.get('value', ''), 'x': element.get('x', ''),
                    'y': element.get('y', ''), 'search_text': search_text,
                    'search_date': datetime.now(), 'search_id': len(found_elements) + 1
                })
        return found_elements

    def search_elements_in_all(self, search_text):
        if not self.database_connection_active:
            return []

        found_elements = []
        for schema in self.schemas_collection.find({}):
            for element in schema.get('parsed_elements', []):
                if (search_text.lower() in element.get('name', '').lower() or 
                    search_text.lower() in element.get('type', '').lower() or 
                    search_text.lower() in element.get('value', '').lower()):
                    
                    found_elements.append({
                        'filename': schema.get('filename', 'неизвестно'),
                        'name': element.get('name', ''), 'type': element.get('type', ''),
                        'value': element.get('value', ''), 'x': element.get('x', ''),
                        'y': element.get('y', ''), 'search_text': search_text,
                        'search_date': datetime.now(), 'search_id': len(found_elements) + 1
                    })
        return found_elements

    def save_sorted_results(self, elements, description=""):
        if not self.database_connection_active:
            return False, "нет подключения к базе данных"
        
        try:
            sorted_document = {
                'filename': f"sorted_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                'creation_date': datetime.now(), 'total_elements': len(elements),
                'elements': elements, 'description': description
            }
            result = self.search_results_collection.insert_one(sorted_document)
            return True, f"отсортированные результаты сохранены с ID: {result.inserted_id}"
        except Exception as e:
            return False, f"ошибка сохранения: {e}"

    def get_all_schemas(self):
        if not self.database_connection_active:
            return []

        schemas = []
        for schema in self.schemas_collection.find({}, {'filename': 1, 'upload_date': 1, 'total_elements_count': 1}).sort('upload_date', -1):
            schemas.append({
                'filename': schema.get('filename', 'неизвестно'),
                'date': schema.get('upload_date', datetime.now()).strftime("%d.%m.%Y %H:%M"),
                'element_count': schema.get('total_elements_count', 0)
            })
        return schemas

    def load_schema_from_db(self, filename):
        if not self.database_connection_active:
            return False

        schema = self.schemas_collection.find_one({'filename': filename})
        if schema:
            self.current_document_data = schema
            return True
        return False
