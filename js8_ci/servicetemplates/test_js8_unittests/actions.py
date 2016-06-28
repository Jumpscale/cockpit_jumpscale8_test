from JumpScale import j


class Actions(ActionsBaseMgmt):

    def install(self, service):
        cuisine = service.executor.cuisine
        cuisine.pip.install('nose')
        cuisine.core.file_link('$codeDir/github/jumpscale/jumpscale_core8/tests', '$base/tests')
        cuisine.git.pullRepo("https://github.com/Jumpscale/jumpscale_core8")
        cuisine.git.pullRepo("https://github.com/Jumpscale/ays_jumpscale8")
        cuisine.git.pullRepo("https://github.com/Jumpscale/jscockpit")

        rc, tests = cuisine.core.run("nosetests $base/tests", die=False)
        self.report(service, tests)

    def report(self, service, message=''):
        telegram_channel = service.hrd.getStr('telegram.channel', None)
        self.ask_telegram(channel=telegram_channel, message="""JS8 UNITTESTS:\n```%s```""" % message, keyboard=[], expect_response=False, timeout=900, redis=None)
        return
