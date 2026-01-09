import time
import requests
from config import DEBUG, EXTERNAL_API

def do_work():
    """
    Simulate some processing + external call
    """
    start = time.time()

    # Simulated processing
    time.sleep(0.2)

    # Optional external call
    response_code = None
    try:
        r = requests.get(EXTERNAL_API, timeout=2)
        response_code = r.status_code
    except Exception as e:
        response_code = str(e)

    duration = round(time.time() - start, 3)

    return {
        "response_code": response_code,
        "duration_seconds": duration,
        "debug": DEBUG,
    }
