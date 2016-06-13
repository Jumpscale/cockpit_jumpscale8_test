from JumpScale import j


class Actions(ActionsBaseMgmt):

    def install(self, service):
        for ip in j.sal.nettools.getIpAddresses():
            if ip not in ['127.0.0.1', 'localhost']:
                service.hrd.set('ssh.addr', ip)
        for child in service.children:
            child.hrd.set('node.addr', ip)

    def getExecutor(self, service):
        return j.tools.executor.getLocal()
