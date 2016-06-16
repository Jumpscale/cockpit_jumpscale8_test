from JumpScale import j

class Actions(ActionsBaseMgmt):



    def install(self, service):
        # import os
        e = service.executor
        e.execute("nosetests /opt/jumpscale8/tests")
        #c=e.cuisine
        #c.git.pullRepo('https://github.com/Jumpscale/cockpit_jumpscale8_test')
        # os.chdir('cockpit_jumpscale8_test/js8tests')
        #c.core.run_script("cd /opt/code/github/jumpscale/cockpit_jumpscale8_test/js8tests\nays simulate install\nays install")

        # e.execute("ays install")


