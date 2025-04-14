# Home Data Monitoring
## Aranet4
The Aranet4 project is setup to scrape CO2 data from a near by Aranet4 device and present the data for Prometheus at port 8000.


## Development
### Packages to Install for development:
```
pip3 install aranet4
pip3 install prometheus-client
pip3 install python-dotenv
```

### Create .env file in /Aranet4/
```
touch .env
```

#### Populate .env with the following data:
```
# Recommended:
target_mac=[mac address of target device]

# Optional: 
scrape_delay=[time in seconds]
```

