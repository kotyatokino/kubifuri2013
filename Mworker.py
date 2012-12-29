#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import subprocess

import Mconfig

class CRancidWorker:
    def DoWorker(self,dicConfig,strPname):
        strHostname = dicConfig['hostname']
        strConfig = self.GenConfig(dicConfig['config'],strPname)

        strConfig = "jlogin %s -c 'configure ; edit logical-systems %s ; %s commit' " % (strHostname,Mconfig.strLRname,strConfig)

        print strConfig
        #subprocess.call(strConfig, shell=True)

    def GenConfig(self,dicProjs,strPname):
        strConfig = ""
        strSet = ""
        strDel = ""

        for dicProj in dicProjs:
            if(dicProj['pname'] == strPname): # match proj, will set this project's config
                for dicCfg in dicProj['config']:
                    lstIF = re.split('\.',dicCfg['oif'])
                    oif = lstIF[0]
                    ounit = lstIF[1]

                    strSet = strSet + " set int %s unit %s family bridge vlan-id-list %s ; " % (oif,ounit,dicCfg['ivid'])
                    if(not(dicCfg['ivid'] == dicCfg['ovid'])): #need tagrans or not
                        strSet = strSet + " set int %s unit %s family bridge vlan-rewrite translate %s %s ;" % (oif,ounit,dicCfg['ovid'],dicCfg['ivid'])

            else: # unmatch proj. will delete this project's config
                for dicCfg in dicProj['config']:
                    lstIF = re.split('\.',dicCfg['oif'])
                    oif = lstIF[0]
                    ounit = lstIF[1]
                    if(not(dicCfg['ivid'] == dicCfg['ovid'])): #need tagrans or not
                        strDel = strDel + " delete int %s unit %s family bridge vlan-rewrite translate %s %s ;" % (oif,ounit,dicCfg['ovid'],dicCfg['ivid'])
                    strDel = strDel + " delete int %s unit %s family bridge vlan-id-list %s ; " % (oif,ounit,dicCfg['ivid'])
                        
        strConfig = strDel + strSet
        return strConfig
