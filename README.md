# tor-network-api

```
████████╗ ██████╗ ██████╗       ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
╚══██╔══╝██╔═══██╗██╔══██╗      ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
   ██║   ██║   ██║██████╔╝█████╗██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
   ██║   ██║   ██║██╔══██╗╚════╝██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
   ██║   ╚██████╔╝██║  ██║      ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝      ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
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
- 📦 BUILD
- ❤️️ TEST
- ⚠️ SECURITY

**RESOURCES**
- GitHub: https://github.com/IndexOffy/tor-network-api
- Docs:   http://www.indexoffy.com/
