from typing import Dict

class GraphService:
    def _process_data(self, data: str) -> Dict:
        return {'data': 'processed'}

    def _store_data(self, data: str) -> Dict:
        return {'data': 'stored'}

    def get_data(self) -> list:
        return []

    def upload_excel_file(self, file: bytes) -> Dict:
        return {'file': 'uploaded'}