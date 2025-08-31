from datetime import datetime
from app.models.metric_model import MetricModel

def insert_metric_access(metrics: MetricModel) -> tuple[bool, str]:
    return True, ""