#!/usr/bin/env python3
"""
Print basic stats for Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def log_stats() -> None:
    """
    Print total logs, per-method counts, and /status count.
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    col = client.logs.nginx

    total = col.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        c = col.count_documents({"method": m})
        print(f"\tmethod {m}: {c}")

    status = col.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    log_stats()
