# SpigotExporter
Prometheus exporter for Spigot accounts

## What it provides
SpigotExporter will output metrics for each of your plugins and a cumulative downloads metric.

Each plugin will have two metrics exposed:
```yml
# HELP PLUGIN_NAME_downloads The total number of downloads for PLUGIN_NAME.
# TYPE PLUGIN_NAME_downloads counter
PLUGIN_NAME_downloads 3832

# HELP PLUGIN_NAME_rating The current rating for PLUGIN_NAME.
# TYPE PLUGIN_NAME_rating gauge
PLUGIN_NAME_rating 5
```

`PLUGIN_NAME` will be replaced with the name of your plugin where spaces are converted to _.

The cumulative downloads metric:
```yml
# HELP total_downloads The total number of downloads for this account.
# TYPE total_downloads counter
total_downloads 5909
```

## How to use
You can either use the live instance [spigot.onlinemo.de](https://spigot.onlinemo.de) or host it yourself. You can load the exporter page by going to /SPIGOT_USER_ID. 

Example: To load my plugins [spigot.onlinemo.de/878178](https://spigot.onlinemo.de/878178)

Once you have confirmed that the page loads correctly you can add it to your prometheus exporter:
```yml
- job_name: 'spigot'
  metrics_path: /878178
  static_configs:
  - targets: ['spigot.onlinemo.de']
```

Replace `878178` with your spigot id

### Self hosting
Install requests:
`pip install requests`

Modify `serverPort` on line 5 to the port you want to use.

I recommend setting up a reverse proxy but it is not necessary.
