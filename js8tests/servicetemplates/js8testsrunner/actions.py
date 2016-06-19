from JumpScale import j


class Actions(ActionsBaseMgmt):

    def install(self, service):
        service.executor.cuisine.pip.install('nose')
        service.executor.cuisine.core.file_link('$codeDir/github/jumpscale/jumpscale_core8/tests', '$base/tests')
        rc, tests = service.executor.cuisine.core.run("nosetests $base/tests", die=False)
        self.report(service, tests)

    def report(self, service, message=''):
        telegram_channel = service.hrd.getStr('telegram.channel', None)
        self.ask_telegram(channel=telegram_channel, message=message, keyboard=[], expect_response=False, timeout=900, redis=None)
        return
