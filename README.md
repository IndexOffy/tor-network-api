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

### License

![GitHub](https://img.shields.io/github/license/IndexOffy/tor-network-dataset?style=flat-square)

This project is licensed under the terms of the MIT license.

**RESOURCES**
- GitHub: https://github.com/IndexOffy/tor-network-api
- Docs:   http://www.indexoffy.com/
