from typing import Dict, List, Union

from pydantic import BaseModel


class AnalyticsRequestData(BaseModel):
    data: List[Dict[str, Union[str, int]]]
    ties: bool
    target_col: str
    date_col: str
    user_id: str
    session_id: str
    external_data_id: str
