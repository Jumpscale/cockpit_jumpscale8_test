from JumpScale import j


class Actions(ActionsBaseMgmt):

    def install(self, service):
        # include the tests!
        url = 'https://github.com/Jumpscale/cockpit_jumpscale8_test.git'
        cuisine = service.executor.cuisine
        cuisine.git.pullRepo(url)

        domain = service.hrd.getStr('dns.domain')
        client = j.clients.cockpit.getClient(domain, '')
        blueprints = client.listBlueprints('js8tests')
        for blueprint in blueprints:
            client.executeBlueprint(blueprint['name'], 'js8tests')
