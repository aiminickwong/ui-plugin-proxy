# Introduction
An easy cgi script serve as a proxy on the oVirt engine machine to access the oVirt hosts resources.
This is convenient for users whose machine is outside the oVirt environment network and have only the access to oVirt engine but not the hosts.

# Installation and Setup
1. Copy plugin-proxy.cgi to http server's cgi directory on the server that running oVirt engine
2. Configure the abovementioned http server properly to run the cgi script

# Usage
* Change the direct-to-host URLs in ui-plugin pages/scripts to "PATH/TO/plugin-proxy.cgi?url=encodeURIComponent(ORIGINAL_URL)"
  * like "http://example_host/example_resource" to "/cgi-bin/plugin-proxy.cgi?url=http%3A%2F%2Fexample_host%2Fexample_resource"

# Known Issues
* Quite a naive script, though it works fine
