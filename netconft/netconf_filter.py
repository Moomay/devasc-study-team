from ncclient import manager

m = manager.connect(
    host = "10.0.15.188",
    port = 830,
    username = "admin",
    password = "cisco",
    hostkey_verify = False
)

netconf_filter = """
<filter>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface
    </interfaces-state>
</filter>
"""

#netconf_reply = m.get_config(source="running", filter=netconf_filter)
netconf_reply = m.get(filter=netconf_filter)
print(netconf_reply)
