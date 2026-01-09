from flask import jsonify
from utils import do_work
from config import config_summary

def demo_function(request):
    """
    HTTP entry point for Cloud Functions Gen 2
    """
    result = do_work()
    print("huhu")
    return jsonify({
        "message": "Cloud Functions Gen 2 demo",
        "result": result,
        "config": config_summary(),
    })
