from JumpScale import j


class Actions(ActionsBaseMgmt):

    def init(self, service):
        node = service.aysrepo.new('node.dummy', args={}, instance="main")
        local_os = service.aysrepo.new('os.local', args={'node': 'main'}, instance='cockpit', parent=node)

        args = {
          'aysfs': False,
          'image': "jumpscale/ubuntu1604",
          'build': True,
          'build.url': 'https://github.com/Jumpscale/dockers',
          'build.path': 'js8/x86_64/ubuntu1604/2_ubuntu1604/',
          'os': 'cockpit',
          'ports': '82',
          'docker.local': True
        }

        js8_devel = service.aysrepo.new('node.docker', args=args, instance='js8_devel', parent=local_os)

        args = {
          'node': 'js8_devel',
          'aysfs': False
        }

        docker_devel_os = service.aysrepo.new('os.ssh.ubuntu', args=args, instance='docker_devel_os', parent=js8_devel)

        args = {
            'aysfs': False,
            'os': 'docker_devel_os'
        }
        devel = service.aysrepo.new('js8', args=args, instance='devel', parent=docker_devel_os)

        mongo = service.aysrepo.new('mongodb', args={'os': 'docker_devel_os'}, instance='main', parent=docker_devel_os)

        args = {
            'os': 'docker_devel_os',
            'spaces': ['/github/jumpscale/jumpscale_portal8/apps/gridportal/base/Cockpit'],
            'actors': ['/github/jumpscale/jumpscale_portal8/apps/gridportal/base/system__atyourservice/',
                       '/github/jumpscale/jumpscale_portal8/apps/gridportal/base/system__webhooks/',
                       '/github/jumpscale/jumpscale_portal8/apps/gridportal/base/system__gridmanager/'],
        }
        portal = service.aysrepo.new('portal', args=args, instance='main')
