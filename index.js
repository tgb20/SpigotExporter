const express = require('express');
const JSONdb = require('simple-json-db');
const axios = require('axios');
const config = require('./config.json');
const app = express();
const port = config.port;

const db = new JSONdb('storage.json');

fetchAPIData = (async () => {
    const spigotData = await axios.get('https://api.spigotmc.org/simple/0.1/index.php?action=getResourcesByAuthor&id=' + config.spigot_id);
    let totalDownloads = 0;
    spigotData.data.forEach(resource => {
        totalDownloads += parseInt(resource.stats.downloads);
    });
    db.set('resources', spigotData.data);
    db.set('total_downloads', totalDownloads);
});

fetchAPIData();

setInterval(fetchAPIData, config.interval * 1000);

app.get('/', (req, res) => {
    res.send('Metrics are on /metrics');
});

app.get('/metrics', (req, res) => {
    res.set('Content-Type', 'text/plain');
    let responseString = '';
    responseString += `# HELP spigot_total_downloads The total number of downloads for this account.\n# TYPE spigot_total_downloads counter\nspigot_total_downloads ${db.get('total_downloads')}\n\n`;
    db.get('resources').forEach(resource => {
        responseString += `# HELP spigot_${resource.title}_downloads The downloads for this plugin.\n# TYPE spigot_${resource.title}_downloads counter\nspigot_${resource.title}_downloads ${resource.stats.downloads}\n\n`;
        responseString += `# HELP spigot_${resource.title}_rating The rating for this plugin.\n# TYPE spigot_${resource.title}_rating counter\nspigot_${resource.title}_rating ${resource.stats.rating}\n\n`;
    });
    res.send(responseString);
});

app.listen(port, () => {
    console.log(`SpigotExporter listening at http://localhost:${port}`);
})