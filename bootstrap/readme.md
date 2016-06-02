will contain ays templates which are relevant for 

- creating cockpit to test js8

## how does the bootstrap work

- create an ubuntu 16.04 node (call ays install - ...)
    - use packet.net
    - use pre-installed server with ub 16.04
    - G8 2.1 (GIG)
- deploy cockpit on the ubuntu 16.04

result

- aysi for node.ssh & sshkey
- docker with deployed cockpit (ub 16.04) on top of the ssh node
    - there will be a git repo which represents the cockpit
- this repo checked out in the cockpit and make sure cockpit gets linked to these templates (in $thisrepo/aystemplates_test/)
- push ssh key so we can access it
- push used key to the cockpit (so that in the cockpit we don't have to specify private/public key)


 