Very simple external authentication script for NSO, backed by a csv file

Configuration needed on ncs.conf:
<aaa>
    <external-authentication>
        <enabled>true</enabled>
        <executable><path to script>/nso-authenticator.py</executable>
    </external-authentication>
</aaa>

Sample auth.csv file:
U8888	rw	service1
U6666	ro	service2
U8888	ro	service2
U5555	ro	service3
U1111	ro	service4
