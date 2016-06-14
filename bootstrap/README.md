Here you'll find three blueprint templates to help you deploy your cockpit through AYS and run js8 tests through that cockpit
- On [packet.net](https://www.packet.net/):
    - Install the python client of packet.net with `pip3 install packet-python`
    - Fill in the [1_cockpit_packet.net.yaml](/bootstrap/blueprint_templates/1_cockpit_packet.net.yaml) template.
        - To get the `packet.token`, login to your packet.net account, create a project and go to your management portal.
          See: ![packet token](/bootstrap/_packet_token.jpg)
        - The `packet.project.name` is your created project name.
        - You can get the `telegram.token` by connecting to telegram and talking to `@botfather`. Type the command `/newbot` and choose a name and username for your bot. botfather will give you a token for this bot which you can then use here.
        - The `dns.domain` is what you want your cockpit's domain to be.
        - `dns.sshkey` is the path to your dns sshkey. You must follow this [documentation](https://gig.gitbooks.io/ovcdoc_internal/content/InternalIT/internal_it.html) to get the dns key.
        - For `oauth.client_id`, `oauth.client_secret`, `oauth.jwt_key` parameters, please refer to [itsyou.online documentation](https://gig.gitbooks.io/itsyouonline/content)
    - Write in the [blueprints](/bootstrap/blueprints) directory
    - Initialize your blueprint with `ays init`
    - Install with `ays install`
- On a [g8](http://greenitglobe.com/#gener8):
    - Fill in the [1_cockpit_g8.yaml](/bootstrap/blueprint_templates/1_cockpit_g8.yaml) template.
    - Write in the [blueprints](/bootstrap/blueprints) directory
    - Initialize your blueprint with `ays init`
    - Install with `ays install`
- On an existing cockpit:
    - Fill in the [1_cockpit_configure_existing.yaml](/bootstrap/blueprint_templates/1_cockpit_configure_existing.yaml) template.
    - Write in the [blueprints](/bootstrap/blueprints) directory
    - Initialize your blueprint with `ays init`
    - Install with `ays install`




You can also deploy a cockpit using the cockpit-deployer telegram bot by following this [documentation](https://gig.gitbooks.io/cockpit/content/docs/jscockpit/installation.html)
