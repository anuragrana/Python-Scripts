import os
import time

config = [
    {
        "folder": "/tmp",
        "delete_older_seconds": 3600
    }
]


def delete_file(f, item):
    ctime = os.path.getctime(f)
    delete_older = item.get("delete_older_seconds")
    if delete_older is None:
        return

    if (time.time() - ctime) > delete_older:
        try:
            if os.path.isfile(f):
                os.remove(f)
                print("deleted: ", f)
        except Exception as e:
            print("Error in deleting: ", f)
            print(e)


def start():
    for item in config:
        folder = item.get("folder")
        if folder is None:
            continue

        files = os.listdir(folder)

        for f in files:
            delete_file(f, item)


if __name__ == "__main__":
    start()