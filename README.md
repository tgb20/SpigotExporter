# SpigotExporter
Prometheus exporter for Spigot accounts

## What it provides
SpigotExporter will output metrics for each of your plugins and a cumulative downloads metric.

Each plugin will have two metrics exposed:
```yml
# HELP spigot_PLUGIN_NAME_downloads The total number of downloads for PLUGIN_NAME.
# TYPE spigot_PLUGIN_NAME_downloads counter
spigot_PLUGIN_NAME_downloads 3832

# HELP spigot_PLUGIN_NAME_rating The current rating for PLUGIN_NAME.
# TYPE spigot_PLUGIN_NAME_rating gauge
spigot_PLUGIN_NAME_rating 5
```

`PLUGIN_NAME` will be replaced with the name of your plugin where spaces are converted to _.

The cumulative downloads metric:
```yml
# HELP spigot_total_downloads The total number of downloads for this account.
# TYPE spigot_total_downloads counter
spigot_total_downloads 5909
```
