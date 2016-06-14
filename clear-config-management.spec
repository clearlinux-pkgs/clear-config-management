#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clear-config-management
Version  : 3.4
Release  : 23
URL      : https://github.com/clearlinux/clear-config-management/archive/3.4.tar.gz
Source0  : https://github.com/clearlinux/clear-config-management/archive/3.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: clear-config-management-data

%description
Clear Config Management
######################
This repository contains application roles to be used with Ansible
as Configuration Management Engine running on Clear Linux*.

%package data
Summary: data components for the clear-config-management package.
Group: Data

%description data
data components for the clear-config-management package.


%prep
%setup -q -n clear-config-management-3.4

%build
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/ansible/examples/ceph/ceph_deploy.yml
/usr/share/ansible/examples/ceph/group_vars/all
/usr/share/ansible/examples/ceph/group_vars/osds
/usr/share/ansible/examples/ceph/hosts
/usr/share/ansible/examples/ciao/ciao.yml
/usr/share/ansible/examples/ciao/group_vars/all
/usr/share/ansible/examples/ciao/hosts
/usr/share/ansible/plugins/action/config_template.py
/usr/share/ansible/plugins/action/config_template.pyc
/usr/share/ansible/plugins/action/config_template.pyo
/usr/share/ansible/roles/OpenSSL/LICENSE.md
/usr/share/ansible/roles/OpenSSL/README.md
/usr/share/ansible/roles/OpenSSL/files/openssl.cnf
/usr/share/ansible/roles/OpenSSL/library/ca
/usr/share/ansible/roles/OpenSSL/library/certificate
/usr/share/ansible/roles/OpenSSL/library/keytool
/usr/share/ansible/roles/OpenSSL/tasks/main.yml
/usr/share/ansible/roles/ceph-common/LICENSE
/usr/share/ansible/roles/ceph-common/README.md
/usr/share/ansible/roles/ceph-common/defaults/main.yml
/usr/share/ansible/roles/ceph-common/files/cephdev.asc
/usr/share/ansible/roles/ceph-common/files/cephstable.asc
/usr/share/ansible/roles/ceph-common/files/cephstableice.asc
/usr/share/ansible/roles/ceph-common/handlers/main.yml
/usr/share/ansible/roles/ceph-common/meta/main.yml
/usr/share/ansible/roles/ceph-common/plugins/actions/config_template.py
/usr/share/ansible/roles/ceph-common/plugins/actions/config_template.pyc
/usr/share/ansible/roles/ceph-common/plugins/actions/config_template.pyo
/usr/share/ansible/roles/ceph-common/tasks/checks/check_firewall.yml
/usr/share/ansible/roles/ceph-common/tasks/checks/check_mandatory_vars.yml
/usr/share/ansible/roles/ceph-common/tasks/checks/check_system.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/debian_ceph_repository.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_on_clear.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_on_debian.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_on_redhat.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_rgw_on_debian.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_rgw_on_redhat.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_rh_storage_on_debian.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/redhat_ceph_repository.yml
/usr/share/ansible/roles/ceph-common/tasks/main.yml
/usr/share/ansible/roles/ceph-common/tasks/misc/system_tuning.yml
/usr/share/ansible/roles/ceph-common/tasks/pre_requisites/prerequisite_ice.yml
/usr/share/ansible/roles/ceph-common/tasks/pre_requisites/prerequisite_rh_storage_cdn_install.yml
/usr/share/ansible/roles/ceph-common/tasks/pre_requisites/prerequisite_rh_storage_iso_install.yml
/usr/share/ansible/roles/ceph-common/templates/ceph-extra.repo
/usr/share/ansible/roles/ceph-common/templates/ceph.conf.j2
/usr/share/ansible/roles/ceph-common/templates/client_restapi_address.j2
/usr/share/ansible/roles/ceph-common/templates/client_restapi_interface.j2
/usr/share/ansible/roles/ceph-common/templates/httpd.conf
/usr/share/ansible/roles/ceph-common/templates/mon_addr_address.j2
/usr/share/ansible/roles/ceph-common/templates/mon_addr_interface.j2
/usr/share/ansible/roles/ceph-common/templates/redhat_ice_repo.j2
/usr/share/ansible/roles/ceph-common/templates/redhat_storage_repo.j2
/usr/share/ansible/roles/ceph-common/templates/rgw.conf
/usr/share/ansible/roles/ceph-common/templates/s3gw.fcgi.j2
/usr/share/ansible/roles/ceph-mon/LICENSE
/usr/share/ansible/roles/ceph-mon/README.md
/usr/share/ansible/roles/ceph-mon/defaults/main.yml
/usr/share/ansible/roles/ceph-mon/files/precise/92-ceph
/usr/share/ansible/roles/ceph-mon/meta/main.yml
/usr/share/ansible/roles/ceph-mon/tasks/calamari.yml
/usr/share/ansible/roles/ceph-mon/tasks/ceph_keys.yml
/usr/share/ansible/roles/ceph-mon/tasks/create_mds_filesystems.yml
/usr/share/ansible/roles/ceph-mon/tasks/deploy_monitors.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/checks.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/copy_configs.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/create_configs.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/dirs_permissions.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/fetch_configs.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/main.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/pre_requisite.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/selinux.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/start_docker_monitor.yml
/usr/share/ansible/roles/ceph-mon/tasks/main.yml
/usr/share/ansible/roles/ceph-mon/tasks/openstack_config.yml
/usr/share/ansible/roles/ceph-mon/tasks/secure_cluster.yml
/usr/share/ansible/roles/ceph-mon/tasks/start_monitor.yml
/usr/share/ansible/roles/ceph-mon/templates/ceph-mon.service.j2
/usr/share/ansible/roles/ceph-osd/LICENSE
/usr/share/ansible/roles/ceph-osd/README.md
/usr/share/ansible/roles/ceph-osd/defaults/main.yml
/usr/share/ansible/roles/ceph-osd/meta/main.yml
/usr/share/ansible/roles/ceph-osd/tasks/activate_osds.yml
/usr/share/ansible/roles/ceph-osd/tasks/check_devices.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/checks.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/dirs_permissions.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/fetch_configs.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/main.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/pre_requisite.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/selinux.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/start_docker_osd.yml
/usr/share/ansible/roles/ceph-osd/tasks/main.yml
/usr/share/ansible/roles/ceph-osd/tasks/osd_fragment.yml
/usr/share/ansible/roles/ceph-osd/tasks/pre_requisite.yml
/usr/share/ansible/roles/ceph-osd/tasks/scenarios/bluestore.yml
/usr/share/ansible/roles/ceph-osd/tasks/scenarios/journal_collocation.yml
/usr/share/ansible/roles/ceph-osd/tasks/scenarios/osd_directory.yml
/usr/share/ansible/roles/ceph-osd/tasks/scenarios/raw_multi_journal.yml
/usr/share/ansible/roles/ceph-osd/templates/ceph-osd.service.j2
/usr/share/ansible/roles/ceph-osd/templates/osd.conf.j2
/usr/share/ansible/roles/ciao-common/LICENSE
/usr/share/ansible/roles/ciao-common/README.md
/usr/share/ansible/roles/ciao-common/handlers/main.yml
/usr/share/ansible/roles/ciao-common/tasks/install.yml
/usr/share/ansible/roles/ciao-common/tasks/main.yml
/usr/share/ansible/roles/ciao-compute/LICENSE
/usr/share/ansible/roles/ciao-compute/README.md
/usr/share/ansible/roles/ciao-compute/defaults/main.yml
/usr/share/ansible/roles/ciao-compute/handlers/main.yml
/usr/share/ansible/roles/ciao-compute/meta/main.yml
/usr/share/ansible/roles/ciao-compute/tasks/main.yml
/usr/share/ansible/roles/ciao-compute/tasks/setup_certs.yml
/usr/share/ansible/roles/ciao-compute/tasks/setup_image.yml
/usr/share/ansible/roles/ciao-compute/tasks/start_compute_service.yml
/usr/share/ansible/roles/ciao-compute/templates/ciao-compute.service.j2
/usr/share/ansible/roles/ciao-controller/LICENSE
/usr/share/ansible/roles/ciao-controller/README.md
/usr/share/ansible/roles/ciao-controller/files/tables/resources.csv
/usr/share/ansible/roles/ciao-controller/files/tables/workload_resources.csv
/usr/share/ansible/roles/ciao-controller/files/tables/workload_template.csv
/usr/share/ansible/roles/ciao-controller/handlers/main.yml
/usr/share/ansible/roles/ciao-controller/meta/main.yml
/usr/share/ansible/roles/ciao-controller/tasks/ciaorc.yml
/usr/share/ansible/roles/ciao-controller/tasks/create_certs.yml
/usr/share/ansible/roles/ciao-controller/tasks/install_cnci.yml
/usr/share/ansible/roles/ciao-controller/tasks/main.yml
/usr/share/ansible/roles/ciao-controller/tasks/setup_certs.yml
/usr/share/ansible/roles/ciao-controller/tasks/start_services.yml
/usr/share/ansible/roles/ciao-controller/templates/ciao-controller.service.j2
/usr/share/ansible/roles/ciao-controller/templates/ciao-scheduler.service.j2
/usr/share/ansible/roles/ciao-controller/templates/ciaorc.j2
/usr/share/ansible/roles/ciao-controller/templates/configuration.yaml.j2
/usr/share/ansible/roles/ciao-controller/templates/workloads/docker-iperf.yaml.j2
/usr/share/ansible/roles/ciao-controller/templates/workloads/docker-ubuntu.yaml.j2
/usr/share/ansible/roles/ciao-controller/templates/workloads/test.yaml.j2
/usr/share/ansible/roles/ciao-network/LICENSE
/usr/share/ansible/roles/ciao-network/README.md
/usr/share/ansible/roles/ciao-network/cnci_image.sh
/usr/share/ansible/roles/ciao-network/defaults/main.yml
/usr/share/ansible/roles/ciao-network/handlers/main.yml
/usr/share/ansible/roles/ciao-network/meta/main.yml
/usr/share/ansible/roles/ciao-network/tasks/cnci_image.yml
/usr/share/ansible/roles/ciao-network/tasks/main.yml
/usr/share/ansible/roles/ciao-network/tasks/setup_certs.yml
/usr/share/ansible/roles/ciao-network/tasks/start_services.yml
/usr/share/ansible/roles/ciao-network/templates/ciao-network.service.j2
/usr/share/ansible/roles/mariadb/LICENSE
/usr/share/ansible/roles/mariadb/README.md
/usr/share/ansible/roles/mariadb/defaults/main.yml
/usr/share/ansible/roles/mariadb/tasks/install.yml
/usr/share/ansible/roles/mariadb/tasks/main.yml
/usr/share/ansible/roles/os-cinder/defaults/main.yml
/usr/share/ansible/roles/os-cinder/handlers/main.yml
/usr/share/ansible/roles/os-cinder/meta/main.yml
/usr/share/ansible/roles/os-cinder/tasks/cinder_certificates.yml
/usr/share/ansible/roles/os-cinder/tasks/cinder_configure_common.yml
/usr/share/ansible/roles/os-cinder/tasks/cinder_controller.yml
/usr/share/ansible/roles/os-cinder/tasks/cinder_db_setup.yml
/usr/share/ansible/roles/os-cinder/tasks/cinder_db_sync.yml
/usr/share/ansible/roles/os-cinder/tasks/cinder_project_access.yml
/usr/share/ansible/roles/os-cinder/tasks/cinder_service_entities.yml
/usr/share/ansible/roles/os-cinder/tasks/install_cinder.yml
/usr/share/ansible/roles/os-cinder/tasks/install_cinder_controller.yml
/usr/share/ansible/roles/os-cinder/tasks/main.yml
/usr/share/ansible/roles/os-cinder/templates/cinder.conf.j2
/usr/share/ansible/roles/os-cinder/templates/nginx-cinder.conf.j2
/usr/share/ansible/roles/os-common/LICENSE
/usr/share/ansible/roles/os-common/README.md
/usr/share/ansible/roles/os-common/defaults/main.yml
/usr/share/ansible/roles/os-common/handlers/main.yml
/usr/share/ansible/roles/os-common/library/glance.py
/usr/share/ansible/roles/os-common/library/glance.pyc
/usr/share/ansible/roles/os-common/library/glance.pyo
/usr/share/ansible/roles/os-common/library/keystone.py
/usr/share/ansible/roles/os-common/library/keystone.pyc
/usr/share/ansible/roles/os-common/library/keystone.pyo
/usr/share/ansible/roles/os-glance/LICENSE
/usr/share/ansible/roles/os-glance/README.md
/usr/share/ansible/roles/os-glance/defaults/main.yml
/usr/share/ansible/roles/os-glance/handlers/main.yml
/usr/share/ansible/roles/os-glance/meta/main.yml
/usr/share/ansible/roles/os-glance/tasks/glance_certificates.yml
/usr/share/ansible/roles/os-glance/tasks/glance_configure_components.yml
/usr/share/ansible/roles/os-glance/tasks/glance_db_setup.yml
/usr/share/ansible/roles/os-glance/tasks/glance_db_sync.yml
/usr/share/ansible/roles/os-glance/tasks/glance_project_access.yml
/usr/share/ansible/roles/os-glance/tasks/glance_service_entities.yml
/usr/share/ansible/roles/os-glance/tasks/install.yml
/usr/share/ansible/roles/os-glance/tasks/main.yml
/usr/share/ansible/roles/os-glance/templates/glance-api.conf.j2
/usr/share/ansible/roles/os-glance/templates/glance-registry.conf.j2
/usr/share/ansible/roles/os-glance/templates/nginx-glance.conf.j2
/usr/share/ansible/roles/os-keystone/LICENSE
/usr/share/ansible/roles/os-keystone/README.md
/usr/share/ansible/roles/os-keystone/defaults/main.yml
/usr/share/ansible/roles/os-keystone/handlers/main.yml
/usr/share/ansible/roles/os-keystone/meta/main.yml
/usr/share/ansible/roles/os-keystone/tasks/install.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_bootstrap.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_certificates.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_configure_components.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_db_setup.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_db_sync.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_openrc.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_project_access.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_service_entities.yml
/usr/share/ansible/roles/os-keystone/tasks/main.yml
/usr/share/ansible/roles/os-keystone/templates/keystone.conf.j2
/usr/share/ansible/roles/os-keystone/templates/nginx-keystone.conf.j2
/usr/share/ansible/roles/os-keystone/templates/openrc.j2
/usr/share/ansible/roles/os-swift/README.md
/usr/share/ansible/roles/os-swift/defaults/main.yml
/usr/share/ansible/roles/os-swift/handlers/main.yml
/usr/share/ansible/roles/os-swift/meta/main.yml
/usr/share/ansible/roles/os-swift/tasks/install.yml
/usr/share/ansible/roles/os-swift/tasks/main.yml
/usr/share/ansible/roles/os-swift/tasks/swift_certificates.yml
/usr/share/ansible/roles/os-swift/tasks/swift_configure_common.yml
/usr/share/ansible/roles/os-swift/tasks/swift_configure_controller.yml
/usr/share/ansible/roles/os-swift/tasks/swift_configure_storage.yml
/usr/share/ansible/roles/os-swift/tasks/swift_project_access.yml
/usr/share/ansible/roles/os-swift/tasks/swift_service_entities.yml
/usr/share/ansible/roles/os-swift/templates/account-server.conf.j2
/usr/share/ansible/roles/os-swift/templates/container-server.conf.j2
/usr/share/ansible/roles/os-swift/templates/nginx-swift-proxy.conf.j2
/usr/share/ansible/roles/os-swift/templates/object-server.conf.j2
/usr/share/ansible/roles/os-swift/templates/proxy-server.conf.j2
/usr/share/ansible/roles/os-swift/templates/rsyncd.conf.j2
/usr/share/ansible/roles/os-swift/templates/swift-ring-builder.sh.j2
/usr/share/ansible/roles/os-swift/templates/swift.conf.j2
