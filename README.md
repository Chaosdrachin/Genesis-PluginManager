# Genesis-PluginManager
A Python Based Plugin Manager Framework

Genesis are able to run Python Scripts at Runtime and you can make changes while the your Core Programm is Running
Without Interrupt your Main Code.

You can Add on Runtime new Plugins and test Arround.


## Base Usage :

### Load the Plugins

```
get_plugins()
```
### Run Example

```
# the Arguments the Plugin will get
args = ["1", "2"]
data = run_plugin("one", *args)
# Print Output
print(data)

```
### List Plugins
```
pl_list = list_plugins()
print(pl_list)
```

