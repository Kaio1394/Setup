from datetime import datetime

def insert_metric_access(bot_proccess_name: str, result_execution: str, user_execution: str, hostname: str, date_init: datetime, date_end: datetime) -> tuple[bool, str]:
    return True, ""