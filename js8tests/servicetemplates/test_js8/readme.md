This service is equal this blueprint:
```
node.dummy__main:

os.local__cockpit:
  node: 'main'

node.docker__js8_devel:
  aysfs: false
  image: "jumpscale/ubuntu1604"
  build: True
  build.url: 'https://github.com/Jumpscale/dockers'
  build.path: 'js8/x86_64/ubuntu1604/2_ubuntu1604/'
  os: 'cockpit'
  ports: '82'
  docker.local: True

os.ssh.ubuntu__docker_devel_os:
  node: 'js8_devel'
  aysfs: false

js8__devel:
  aysfs: false
  os: 'docker_devel_os'

portal__main:
  os: 'docker_devel_os'
  spaces': 
    - '/github/jumpscale/jumpscale_portal8/apps/gridportal/base/Cockpit'
  actors':
    - '/github/jumpscale/jumpscale_portal8/apps/gridportal/base/system__atyourservice/'
    - '/github/jumpscale/jumpscale_portal8/apps/gridportal/base/system__webhooks/'
    - '/github/jumpscale/jumpscale_portal8/apps/gridportal/base/system__gridmanager/'
```

It creates a docker, installs js8 in development mode, installs mongo, and portal

it *recurrs* every 12 hours


I