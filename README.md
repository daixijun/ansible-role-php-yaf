Role Name
=========

[![Build Status](https://travis-ci.org/daixijun/ansible-role-php-yaf.svg?branch=master)](https://travis-ci.org/daixijun/ansible-role-php-yaf)

Ansible 安装php yaf扩展

Requirements
------------

* RHEL/Centos 7
* Ansible 2.7 +

Role Variables
--------------

```yaml
php_yaf_version: 3.0.8
php_yaf_download_url: http://pecl.php.net/get/yaf-{{ php_yaf_version }}.tgz

```

Dependencies
------------

[daixijun.php](https://galaxy.ansible.com/daixijun/php)

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: daixijun.php
    - role: daixijun.php_yaf
```

License
-------

BSD

Author Information
------------------

Xijun Dai <daixijun1990@gmail.com>
