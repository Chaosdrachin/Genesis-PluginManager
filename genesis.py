import importlib
import os
import sys
import queue
import threading
 
PLUGINS = []
plugin_que = queue.Queue()
 
def storeInQueue(f):
  def wrapper(*args):
    plugin_que.put(f(*args))
  return wrapper
 
def get_plugins():
    PLUGINS.clear()
    for filename in os.listdir("plugins/"):
        if filename.endswith(".py"):
            PLUGINS.append("plugins." + str(filename.replace(".py", "")))
            continue
        else:
            continue
 
def list_plugins():
    result = ""
    for plugin in PLUGINS:
        result += "- " +str(plugin).replace("plugins.","") + ","
    return result
 
@storeInQueue
def run(plugin_name,*args):
    for plugin in PLUGINS:
        if plugin_name in plugin:
            try:
                modul = "plugins." + plugin_name
                if modul in sys.modules:
                    del sys.modules[modul]
            except Exception as err:
                print("########## ERROR ##########")
                print(err)
                break
 
    plugin_module = importlib.import_module(plugin, ".")
    plugin = plugin_module.Plugin()
    result = plugin.execute(*args)
    print(result)
    del plugin
 
    importlib.reload(plugin_module)
    return result
 
def run_plugin(plugin_name ,*args):
                t = threading.Thread(target=run, args=(plugin_name, *args,))
                t.start()
                my_data = plugin_que.get()
                print(my_data)
                result = my_data[plugin_name]
                return result
 
