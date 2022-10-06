import yaml
import os


def get_work_path():
    return os.getcwd().split("common")[0]


def get_config(node):
    with open(get_work_path() + "/config.yaml", encoding="utf8") as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
    if data.get(node):
        return data[node]


if __name__ == "__main__":
    a = get_config("BrowserOptions")
    print(a)