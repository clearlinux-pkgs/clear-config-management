#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clear-config-management
Version  : 1.2
Release  : 9
URL      : https://github.com/clearlinux/clear-config-management/archive/1.2.tar.gz
Source0  : https://github.com/clearlinux/clear-config-management/archive/1.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
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
%setup -q -n clear-config-management-1.2

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
/usr/share/ansible/examples/openstack/README.md
/usr/share/ansible/examples/openstack/group_vars/all
/usr/share/ansible/examples/openstack/hosts
/usr/share/ansible/examples/openstack/openstack_deployment.yml
/usr/share/ansible/plugins/action/config_template.py
/usr/share/ansible/plugins/action/config_template.pyc
/usr/share/ansible/plugins/action/config_template.pyo
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
/usr/share/ansible/roles/ceph-common/tasks/installs/redhat_ceph_repository.yml
/usr/share/ansible/roles/ceph-common/tasks/main.yml
/usr/share/ansible/roles/ceph-common/tasks/misc/system_tuning.yml
/usr/share/ansible/roles/ceph-common/tasks/pre_requisites/prerequisite_ice.yml
/usr/share/ansible/roles/ceph-common/tasks/pre_requisites/prerequisite_rh_storage_cdn_install.yml
/usr/share/ansible/roles/ceph-common/tasks/pre_requisites/prerequisite_rh_storage_iso_install.yml
/usr/share/ansible/roles/ceph-common/templates/ceph-extra.repo
/usr/share/ansible/roles/ceph-common/templates/ceph.conf.j2
/usr/share/ansible/roles/ceph-common/templates/httpd.conf
/usr/share/ansible/roles/ceph-common/templates/redhat_ice_repo.j2
/usr/share/ansible/roles/ceph-common/templates/redhat_storage_repo.j2
/usr/share/ansible/roles/ceph-common/templates/rgw.conf
/usr/share/ansible/roles/ceph-common/templates/s3gw.fcgi.j2
/usr/share/ansible/roles/ceph-common/vars/main.yml
/usr/share/ansible/roles/ceph-mon/LICENSE
/usr/share/ansible/roles/ceph-mon/README.md
/usr/share/ansible/roles/ceph-mon/defaults/main.yml
/usr/share/ansible/roles/ceph-mon/files/precise/92-ceph
/usr/share/ansible/roles/ceph-mon/meta/main.yml
/usr/share/ansible/roles/ceph-mon/tasks/ceph_keys.yml
/usr/share/ansible/roles/ceph-mon/tasks/create_mds_filesystems.yml
/usr/share/ansible/roles/ceph-mon/tasks/deploy_monitors.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/checks.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/copy_configs.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/fetch_configs.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/main.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/pre_requisite.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/selinux.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/start_docker_monitor.yml
/usr/share/ansible/roles/ceph-mon/tasks/main.yml
/usr/share/ansible/roles/ceph-mon/tasks/openstack_config.yml
/usr/share/ansible/roles/ceph-mon/tasks/secure_cluster.yml
/usr/share/ansible/roles/ceph-mon/tasks/start_monitor.yml
/usr/share/ansible/roles/ceph-osd/LICENSE
/usr/share/ansible/roles/ceph-osd/README.md
/usr/share/ansible/roles/ceph-osd/defaults/main.yml
/usr/share/ansible/roles/ceph-osd/meta/main.yml
/usr/share/ansible/roles/ceph-osd/tasks/activate_osds.yml
/usr/share/ansible/roles/ceph-osd/tasks/check_devices.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/checks.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/fetch_configs.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/main.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/pre_requisite.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/selinux.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/start_docker_osd.yml
/usr/share/ansible/roles/ceph-osd/tasks/main.yml
/usr/share/ansible/roles/ceph-osd/tasks/osd_fragment.yml
/usr/share/ansible/roles/ceph-osd/tasks/pre_requisite.yml
/usr/share/ansible/roles/ceph-osd/tasks/scenarios/journal_collocation.yml
/usr/share/ansible/roles/ceph-osd/tasks/scenarios/osd_directory.yml
/usr/share/ansible/roles/ceph-osd/tasks/scenarios/raw_multi_journal.yml
/usr/share/ansible/roles/ceph-osd/templates/osd.conf.j2
/usr/share/ansible/roles/mariadb/LICENSE
/usr/share/ansible/roles/mariadb/README.md
/usr/share/ansible/roles/mariadb/defaults/main.yml
/usr/share/ansible/roles/mariadb/tasks/install.yml
/usr/share/ansible/roles/mariadb/tasks/main.yml
/usr/share/ansible/roles/os-common/LICENSE
/usr/share/ansible/roles/os-common/README.md
/usr/share/ansible/roles/os-common/defaults/main.yml
/usr/share/ansible/roles/os-common/library/glance.py
/usr/share/ansible/roles/os-common/library/glance.pyc
/usr/share/ansible/roles/os-common/library/glance.pyo
/usr/share/ansible/roles/os-common/library/keystone.py
/usr/share/ansible/roles/os-common/library/keystone.pyc
/usr/share/ansible/roles/os-common/library/keystone.pyo
/usr/share/ansible/roles/os-common/tasks/common_interface_detect.yml
/usr/share/ansible/roles/os-common/tasks/main.yml
/usr/share/ansible/roles/os-glance/LICENSE
/usr/share/ansible/roles/os-glance/README.md
/usr/share/ansible/roles/os-glance/defaults/main.yml
/usr/share/ansible/roles/os-glance/handlers/main.yml
/usr/share/ansible/roles/os-glance/meta/main.yml
/usr/share/ansible/roles/os-glance/tasks/glance_configure_components.yml
/usr/share/ansible/roles/os-glance/tasks/glance_db_setup.yml
/usr/share/ansible/roles/os-glance/tasks/glance_db_sync.yml
/usr/share/ansible/roles/os-glance/tasks/glance_project_access.yml
/usr/share/ansible/roles/os-glance/tasks/glance_service_entities.yml
/usr/share/ansible/roles/os-glance/tasks/install.yml
/usr/share/ansible/roles/os-glance/tasks/main.yml
/usr/share/ansible/roles/os-glance/templates/glance-api.conf.j2
/usr/share/ansible/roles/os-glance/templates/glance-registry.conf.j2
/usr/share/ansible/roles/os-heat/LICENSE
/usr/share/ansible/roles/os-heat/README.md
/usr/share/ansible/roles/os-heat/defaults/main.yml
/usr/share/ansible/roles/os-heat/handlers/main.yml
/usr/share/ansible/roles/os-heat/meta/main.yml
/usr/share/ansible/roles/os-heat/tasks/heat_configure_components.yml
/usr/share/ansible/roles/os-heat/tasks/heat_db_setup.yml
/usr/share/ansible/roles/os-heat/tasks/heat_db_sync.yml
/usr/share/ansible/roles/os-heat/tasks/heat_project_access.yml
/usr/share/ansible/roles/os-heat/tasks/heat_service_entities.yml
/usr/share/ansible/roles/os-heat/tasks/install.yml
/usr/share/ansible/roles/os-heat/tasks/main.yml
/usr/share/ansible/roles/os-heat/templates/heat.conf.j2
/usr/share/ansible/roles/os-horizon/LICENSE
/usr/share/ansible/roles/os-horizon/README.md
/usr/share/ansible/roles/os-horizon/handlers/main.yml
/usr/share/ansible/roles/os-horizon/meta/main.yml
/usr/share/ansible/roles/os-horizon/tasks/install.yml
/usr/share/ansible/roles/os-horizon/tasks/main.yml
/usr/share/ansible/roles/os-keystone/LICENSE
/usr/share/ansible/roles/os-keystone/README.md
/usr/share/ansible/roles/os-keystone/defaults/main.yml
/usr/share/ansible/roles/os-keystone/handlers/main.yml
/usr/share/ansible/roles/os-keystone/meta/main.yml
/usr/share/ansible/roles/os-keystone/tasks/install.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_configure_components.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_db_setup.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_db_sync.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_demo_access.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_openrc.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_project_access.yml
/usr/share/ansible/roles/os-keystone/tasks/keystone_service_entities.yml
/usr/share/ansible/roles/os-keystone/tasks/main.yml
/usr/share/ansible/roles/os-keystone/templates/keystone.conf.j2
/usr/share/ansible/roles/os-keystone/templates/openrc.j2
/usr/share/ansible/roles/os-neutron/LICENSE
/usr/share/ansible/roles/os-neutron/README.md
/usr/share/ansible/roles/os-neutron/defaults/main.yml
/usr/share/ansible/roles/os-neutron/handlers/main.yml
/usr/share/ansible/roles/os-neutron/meta/main.yml
/usr/share/ansible/roles/os-neutron/tasks/install.yml
/usr/share/ansible/roles/os-neutron/tasks/main.yml
/usr/share/ansible/roles/os-neutron/tasks/neutron_configure_components.yml
/usr/share/ansible/roles/os-neutron/tasks/neutron_db_setup.yml
/usr/share/ansible/roles/os-neutron/tasks/neutron_db_sync.yml
/usr/share/ansible/roles/os-neutron/tasks/neutron_network_enabling.yml
/usr/share/ansible/roles/os-neutron/tasks/neutron_project_access.yml
/usr/share/ansible/roles/os-neutron/tasks/neutron_service_entities.yml
/usr/share/ansible/roles/os-neutron/tasks/scenarios/linuxbridge.yml
/usr/share/ansible/roles/os-neutron/tasks/scenarios/openvswitch.yml
/usr/share/ansible/roles/os-neutron/templates/dhcp_agent.ini.j2
/usr/share/ansible/roles/os-neutron/templates/l3_agent.ini.j2
/usr/share/ansible/roles/os-neutron/templates/linuxbridge_agent.ini.j2
/usr/share/ansible/roles/os-neutron/templates/metadata_agent.ini.j2
/usr/share/ansible/roles/os-neutron/templates/ml2_conf.ini.j2
/usr/share/ansible/roles/os-neutron/templates/neutron.conf.j2
/usr/share/ansible/roles/os-nova/LICENSE
/usr/share/ansible/roles/os-nova/README.md
/usr/share/ansible/roles/os-nova/defaults/main.yml
/usr/share/ansible/roles/os-nova/handlers/main.yml
/usr/share/ansible/roles/os-nova/meta/main.yml
/usr/share/ansible/roles/os-nova/tasks/install_compute.yml
/usr/share/ansible/roles/os-nova/tasks/install_compute_controller.yml
/usr/share/ansible/roles/os-nova/tasks/install_network.yml
/usr/share/ansible/roles/os-nova/tasks/main.yml
/usr/share/ansible/roles/os-nova/tasks/nova_compute.yml
/usr/share/ansible/roles/os-nova/tasks/nova_compute_services.yml
/usr/share/ansible/roles/os-nova/tasks/nova_configure_common.yml
/usr/share/ansible/roles/os-nova/tasks/nova_configure_controller.yml
/usr/share/ansible/roles/os-nova/tasks/nova_configure_network.yml
/usr/share/ansible/roles/os-nova/tasks/nova_controller.yml
/usr/share/ansible/roles/os-nova/tasks/nova_db_setup.yml
/usr/share/ansible/roles/os-nova/tasks/nova_db_sync.yml
/usr/share/ansible/roles/os-nova/tasks/nova_project_access.yml
/usr/share/ansible/roles/os-nova/tasks/nova_service_entities.yml
/usr/share/ansible/roles/os-nova/tasks/nova_virt_detect.yml
/usr/share/ansible/roles/os-nova/templates/linuxbridge_agent.ini.j2
/usr/share/ansible/roles/os-nova/templates/neutron.conf.j2
/usr/share/ansible/roles/os-nova/templates/nova.conf.j2
/usr/share/ansible/roles/rabbitmq/LICENSE
/usr/share/ansible/roles/rabbitmq/README.md
/usr/share/ansible/roles/rabbitmq/defaults/main.yml
/usr/share/ansible/roles/rabbitmq/tasks/install.yml
/usr/share/ansible/roles/rabbitmq/tasks/main.yml
