Here you'll find three blueprint templates to help you deploy your cockpit through AYS and run js8 tests through that cockpit
- On [packet.net](https://www.packet.net/):
    - Install the python client of packet.net with `pip3 install packet-python`
    - Fill in the [1_cockpit_packet.net.yaml](/blueprint_templates/1_cockpit_packet.net.yaml) template.
    - Write in the [blueprints](/blueprints) directory
    - Initialize your blueprint with `ays init`
    - Install with `ays install`
- On a [g8](http://greenitglobe.com/#gener8):
    - Fill in the [1_cockpit_g8.yaml](/blueprint_templates/1_cockpit_g8.yaml) template.
    - Write in the [blueprints](/blueprints) directory
    - Initialize your blueprint with `ays init`
    - Install with `ays install`
- On an existing cockpit:
    -  Fill in the [1_cockpit_configure_existing.yaml](/blueprint_templates/1_cockpit_configure_existing.yaml) template.
    - Write in the [blueprints](/blueprints) directory
    - Initialize your blueprint with `ays init`
    - Install with `ays install`



You can also deploy a cockpit using the cockpit-deployer telegram bot by following this [documentation](https://gig.gitbooks.io/cockpit/content/docs/jscockpit/installation.html)
