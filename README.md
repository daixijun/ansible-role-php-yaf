# daixijun.php-yaf

[![Build Status](https://github.com/daixijun/ansible-role-php-yaf/workflows/build/badge.svg)](https://github.com/daixijun/ansible-role-php-yaf/actions)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-daixijun.php-yaf-660198.svg?style=flat)](https://galaxy.ansible.com/daixijun/php-yaf/)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/daixijun/ansible-role-php-yaf?sort=semver)](https://github.com/daixijun/ansible-role-php-yaf/tags)

Ansible 安装php yaf扩展

## 环境要求

* RHEL/Centos 7+
* Ansible 2.7 +
* php 7.1+

## 变量

```yaml
php_yaf_version: 3.0.8
php_yaf_download_url: http://pecl.php.net/get/yaf-{{ php_yaf_version }}.tgz
```

## 依赖

[daixijun.php](https://github.com/daixijun/ansible-role-php)

## 示例

```yaml
- hosts: servers
  roles:
    - role: daixijun.php
    - role: daixijun.php_yaf
```

## License

BSD

## 维护者

* Xijun Dai <daixijun1990@gmail.com>
