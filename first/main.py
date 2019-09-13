- hosts: all 
  become: yes
  tasks:
  - name: install nginx
    package: 
      name: nginx
      update_cache: yes
      state: present
  - name: Allow all access to http port 80
    ufw:
      rule: allow
      port: 80
      proto: Nginx HTTP
