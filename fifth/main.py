- hosts: testserver
  tasks:
  - name: "ping all the nodes"
    ping: 
      data: pong