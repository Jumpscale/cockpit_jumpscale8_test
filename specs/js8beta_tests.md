## ays tests

 - use KDS's account on packet.net (use the cheapest server)
 - install docker on the server on packet.net
 - in docker get ubuntu 16.04 with ssh access & our key
 - save this docker locally

### docker 1:

 - in the docker deploy js8 in development mode

### docker 2: (LESS PRIO)

 - in the docker deploy js8 in sandbox mode
 - start portal
 - do basic tests on portal

### docker 3:

 - wait till docker 1 done, (do this through consumption)
 - start from docker 1 who was completed
 - deploy portal
 - do basic tests on portal

### docker 4:

 - start from docker 1
 - deploy cockpit
 - do some basic tests

### docker 5:

 - start from docker 1
 - deploy ays8
 - do some basic tests (there are tests implemented in ays factory I believe)

### docker 6: build js8 sandbox

 - if all tests in all dockers before ok
 - build sandbox js8 (make sure portal & cockpit items are in there as well)

## remarks

 - deploy all using cuisine
 - use basics of ays8: consumption, ...
 - run in gevent scheduled & make sure that in 1 step in a run all things go in parallel e.g. docker 1 & 2 would be parallel
 - report to the cockpit telegram !
