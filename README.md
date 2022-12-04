# tor-network-api

```
 _                        _                      _    
| |_ ___  _ __ _ __   ___| |___      _____  _ __| | __
| __/ _ \| '__| '_ \ / _ | __\ \ /\ / / _ \| '__| |/ /
| || (_) | |  | | | |  __| |_ \ V  V | (_) | |  |   < 
 \__\___/|_|  |_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_\ v1.0
 ```

### Running the project with [Docker]

 - Building the Docker image

```bash
$ sudo docker build --tag tor-api --file docker/Dockerfile .
```

 - Starting the Docker Container

```bash
$ sudo docker run -d -t -p 8080:8080 tor-api/dev
```

### Commit Style
- ⚙️ NO-TASK
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS
- 📦 PyPI

**RESOURCES**
- GitHub: https://github.com/IndexOffy/tor-network-api
- Docs:   http://www.indexoffy.com/
