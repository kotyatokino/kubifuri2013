# configure
# delete int xe-0/0/1 unit 0 family bridge vlan-id-list 999
# delete int xe-0/0/1 unit 0 family bridge vlan-rewrite translate 1001 1000

# set int xe-0/0/1 unit 0 family bridge vlan-id-list 1000
# set int xe-0/0/1 unit 0 family bridge vlan-rewrite translate 1001 1000

#### set bridge-domains v1000-Snow13kubifuri vlan-id 1000
#### set bridge-domains v1000-Snow13kubifuri domain-type bridge
# commit

strLRname = "kubifuri"

lstConfig = [
    {"hostname":"sapporo-mx80-1",
     "config":[
            {'pname':'proj1',
             'config':[
                    {'ivid':1000,'ouf':'xe-0/0/2.1001','ovid':1001},
                    {'ivid':1002,'ouf':'xe-0/0/2.1003','ovid':1003}
                    ]
             },
            {'pname':'proj2',
             'config':[
                    {'ivid':1000,'ouf':'xe-0/0/2.1001','ovid':1001},
                    {'ivid':1002,'ouf':'xe-0/0/2.1003','ovid':1003}
                    ]
             }
            ]
     },
    {"hostname":"nagomm-mx80-1",
     "config":[
            {'pname':'proj1',
             'config':[
                    {'ivid':1000,'ouf':'xe-0/0/2.1001','ovid':1001},
                    {'ivid':1002,'ouf':'xe-0/0/2.1003','ovid':1003}
                    ]
             },
            {'pname':'proj2',
             'config':[
                 [
                    {'ivid':1000,'ouf':'xe-0/0/2.1001','ovid':1001},
                    {'ivid':1002,'ouf':'xe-0/0/2.1003','ovid':1003}
                    ]
             }
            ]
     },
    {"hostname":"ndojima-mx80-1",
     "config":[
            {'pname':'proj1',
             'config':[
                 [
                    {'ivid':1000,'ouf':'xe-0/0/2.1001','ovid':1001},
                    {'ivid':1002,'ouf':'xe-0/0/2.1003','ovid':1003}
                    ]
             },
            {'pname':'proj2',
             'config':[
                    {'ivid':1000,'ouf':'xe-0/0/2.1001','ovid':1001},
                    {'ivid':1002,'ouf':'xe-0/0/2.1003','ovid':1003}
                    ]
             }
            ]
     },

]
