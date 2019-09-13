- hosts: all
  tasks:
  - name: "ping all the nodes"
    ping: 
      data: ping