from JumpScale import j

class Actions(ActionsBaseMgmt):



    def install(self, service):
        e = service.executor
        e.execute("nosetests /opt/jumpscale8/tests")
 


