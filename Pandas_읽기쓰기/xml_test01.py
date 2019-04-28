# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:47:29 2019

@author: Administrator
"""

import xml.etree.ElementTree as elemTree

tree = elemTree.parse('test002.xml')

xmlStr = '''
<users>
    <user grade="gold">
        <name>Kim Cheol Soo</name>
        <age>25</age>
        <birthday>19940215</birthday>
    </user>
    
    <user grade="diamond">
        <name>Kim Yoo Mee</name>
        <age>21</age>
        <birthday>19980417</birthday>
    </user>
</users>
        '''
        
        
# =============================================================================
# tree = elemTree.fromstring(xmlStr)
# 
# user = tree.find('./user[2]')
# 
# 
# print(user.tag)
# print(user.attrib)
# print(user.get('grade'))
# 
# userName = user.find('name')
# userName1 = user.find('age')
# userName2 = user.find('birthday')
# 
# 
# print(userName.text +","+ userName1.text +","+ userName2.text)
# 
# =============================================================================


for user in tree.findall('./user[1]'):print(user.tag)
for user02 in tree.findall('./user[2]'):print(user.tag)


useName01 = user.find('name').text
useName02 = user02.find('name').text

print("useName01"+","+ useName01)
print("useName02" +","+  useName02)

print("useName01"+":"+ useName01+","+ "useName02" +":"+  useName02)

