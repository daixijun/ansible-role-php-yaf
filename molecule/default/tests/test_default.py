import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_yaf_extension(host):
    output = host.check_output('/usr/local/php/bin/php -m | grep yaf')

    assert output == 'yaf'


def test_yaf_so(host):
    extension_dir = host.check_output(
        '/usr/local/php/bin/php-config --extension-dir')

    so = host.file(os.path.join(extension_dir.strip(), 'yaf.so'))

    assert so.exists


def test_yaf_config_file(host):
    cf = host.file("/usr/local/php/etc/php.d/yaf.ini")

    assert cf.exists
