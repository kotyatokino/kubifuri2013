#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

class CRancidWorker:
    def DoRancid(dicConfig,strPname):
        strHostname = dicConfig['hostname']
        strConfig = self.GenConfig(dicConfig['config'],strPname)

        strConfig = "jlogin %s -c 'configure ; %s ; commit' " (strHostname,strConfig)

        print strConfig

    def GenConfig(dicProjs,strPname):
        strConfig = ""
        strSet = ""
        strDel = ""

        for dicProj in dicProjs:
            lstIF = re.split('\.',dicProj['oif'])
            oif = lstIF[0]
            ounit = lstIF[1]

            if(dicProj['pname'] == strPname): # match proj, will set this project's config
                strSet = strSet + " set int %s unit %s family bridge vlan-id-list %s ; " % (oif,ounit,dicProj['ivid'])
                if(dicProj['ivid'] == dicProj['ovid']): #need tagrans or not
                    strSet = strSet + " set int %s unit %s family bridge vlan-rewrite translate %s %s ;" % (oif,ouint,dicProj['ovid'],dicProj['ivid'])

            else: # unmatch proj. will delete this project's config
                if(dicProj['ivid'] == dicProj['ovid']): #need tagrans or not
                    strDel = strDel + " delete int %s unit %s family bridge vlan-rewrite translate %s %s ;" % (oif,ouint,dicProj['ovid'],dicProj['ivid'])
                strDel = strDel + " delete int %s unit %s family bridge vlan-id-list %s ; " % (oif,ounit,dicProj['ivid'])
        
        strConfig = strDel + strSet
        return strConfig
