from typing import Dict

class GraphDataAPI:
    def _get_data(self) -> Dict:
        return {'data': 'fetched'}

    def process_data(self, data: str) -> Dict:
        return {'data': 'processed'}