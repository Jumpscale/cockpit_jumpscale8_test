from JumpScale import j


class Actions(ActionsBaseMgmt):

    def install(self, service):
        # include the tests!
        url = 'https://github.com/Jumpscale/cockpit_jumpscale8_test.git'
        cuisine = service.executor.cuisine
        cuisine.git.pullRepo(url)

