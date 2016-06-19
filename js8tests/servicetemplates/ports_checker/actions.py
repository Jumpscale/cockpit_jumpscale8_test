from JumpScale import j

class Actions(ActionsBaseMgmt):



    def install(self, service):
        e = service.executor
        ports = service.hrd.getList('ports')
        for p in ports:
            rc, out = e.cuisine.core.run("netstat -nltp | grep {0}".format(p), die=False)
            if rc == 0:
                j.logger.log("Service is running on port {0}".format(p))
            else:
                j.logger.log("No service is running on port {0}".format(p))
