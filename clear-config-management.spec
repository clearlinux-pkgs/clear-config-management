#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clear-config-management
Version  : 4.4
Release  : 33
URL      : https://github.com/clearlinux/clear-config-management/archive/4.4.tar.gz
Source0  : https://github.com/clearlinux/clear-config-management/archive/4.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: clear-config-management-data

%description
# Clear Config Management
This repository contains application roles to be used with Ansible
as Configuration Management Engine running on Clear Linux*.

%package data
Summary: data components for the clear-config-management package.
Group: Data

%description data
data components for the clear-config-management package.


%prep
%setup -q -n clear-config-management-4.4

%build
export LANG=C
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/ansible/examples/ceph/ansible.cfg
/usr/share/ansible/examples/ceph/ceph_deploy.yml
/usr/share/ansible/examples/ceph/group_vars/all
/usr/share/ansible/examples/ceph/group_vars/osds
/usr/share/ansible/examples/ceph/hosts
/usr/share/ansible/examples/ciao/README.md
/usr/share/ansible/examples/ciao/ansible.cfg
/usr/share/ansible/examples/ciao/ciao.yml
/usr/share/ansible/examples/ciao/ciao_computes.yml
/usr/share/ansible/examples/ciao/ciao_controllers.yml
/usr/share/ansible/examples/ciao/ciao_networks.yml
/usr/share/ansible/examples/ciao/ciao_prepare.yml
/usr/share/ansible/examples/ciao/ciao_wait.yml
/usr/share/ansible/examples/ciao/cleanup/cache.yml
/usr/share/ansible/examples/ciao/cleanup/ciao.yml
/usr/share/ansible/examples/ciao/group_vars/all
/usr/share/ansible/examples/ciao/hosts
/usr/share/ansible/examples/ciao/requirements.yml
/usr/share/ansible/plugins/action/_v1_config_template.py
/usr/share/ansible/plugins/action/_v1_config_template.pyc
/usr/share/ansible/plugins/action/_v1_config_template.pyo
/usr/share/ansible/plugins/action/_v2_config_template.py
/usr/share/ansible/plugins/action/_v2_config_template.pyc
/usr/share/ansible/plugins/action/_v2_config_template.pyo
/usr/share/ansible/plugins/action/config_template.py
/usr/share/ansible/plugins/action/config_template.pyc
/usr/share/ansible/plugins/action/config_template.pyo
/usr/share/ansible/roles/ceph-common/LICENSE
/usr/share/ansible/roles/ceph-common/README.md
/usr/share/ansible/roles/ceph-common/defaults/main.yml
/usr/share/ansible/roles/ceph-common/files/cephdev.asc
/usr/share/ansible/roles/ceph-common/files/cephstable.asc
/usr/share/ansible/roles/ceph-common/files/cephstablerhcs.asc
/usr/share/ansible/roles/ceph-common/handlers/main.yml
/usr/share/ansible/roles/ceph-common/meta/main.yml
/usr/share/ansible/roles/ceph-common/plugins/actions/_v1_config_template.py
/usr/share/ansible/roles/ceph-common/plugins/actions/_v1_config_template.pyc
/usr/share/ansible/roles/ceph-common/plugins/actions/_v1_config_template.pyo
/usr/share/ansible/roles/ceph-common/plugins/actions/_v2_config_template.py
/usr/share/ansible/roles/ceph-common/plugins/actions/_v2_config_template.pyc
/usr/share/ansible/roles/ceph-common/plugins/actions/_v2_config_template.pyo
/usr/share/ansible/roles/ceph-common/plugins/actions/config_template.py
/usr/share/ansible/roles/ceph-common/plugins/actions/config_template.pyc
/usr/share/ansible/roles/ceph-common/plugins/actions/config_template.pyo
/usr/share/ansible/roles/ceph-common/tasks/checks/check_firewall.yml
/usr/share/ansible/roles/ceph-common/tasks/checks/check_mandatory_vars.yml
/usr/share/ansible/roles/ceph-common/tasks/checks/check_ntp_atomic.yml
/usr/share/ansible/roles/ceph-common/tasks/checks/check_ntp_debian.yml
/usr/share/ansible/roles/ceph-common/tasks/checks/check_ntp_redhat.yml
/usr/share/ansible/roles/ceph-common/tasks/checks/check_system.yml
/usr/share/ansible/roles/ceph-common/tasks/docker/fetch_image.yml
/usr/share/ansible/roles/ceph-common/tasks/facts.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/debian_ceph_repository.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_on_clear.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_on_debian.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_on_redhat.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_rgw_on_debian.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_rgw_on_redhat.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_rh_storage_on_debian.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_rh_storage_on_redhat.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/redhat_ceph_repository.yml
/usr/share/ansible/roles/ceph-common/tasks/main.yml
/usr/share/ansible/roles/ceph-common/tasks/misc/ntp_atomic.yml
/usr/share/ansible/roles/ceph-common/tasks/misc/ntp_debian.yml
/usr/share/ansible/roles/ceph-common/tasks/misc/ntp_redhat.yml
/usr/share/ansible/roles/ceph-common/tasks/misc/system_tuning.yml
/usr/share/ansible/roles/ceph-common/tasks/pre_requisites/prerequisite_rh_storage_cdn_install.yml
/usr/share/ansible/roles/ceph-common/tasks/pre_requisites/prerequisite_rh_storage_iso_install.yml
/usr/share/ansible/roles/ceph-common/templates/ceph-extra.repo
/usr/share/ansible/roles/ceph-common/templates/ceph.conf.j2
/usr/share/ansible/roles/ceph-common/templates/client_restapi_address.j2
/usr/share/ansible/roles/ceph-common/templates/client_restapi_interface.j2
/usr/share/ansible/roles/ceph-common/templates/ganesha.conf.j2
/usr/share/ansible/roles/ceph-common/templates/httpd.conf
/usr/share/ansible/roles/ceph-common/templates/mon_addr_address.j2
/usr/share/ansible/roles/ceph-common/templates/mon_addr_interface.j2
/usr/share/ansible/roles/ceph-common/templates/redhat_storage_repo.j2
/usr/share/ansible/roles/ceph-common/templates/rgw.conf
/usr/share/ansible/roles/ceph-common/templates/s3gw.fcgi.j2
/usr/share/ansible/roles/ceph-mds/LICENSE
/usr/share/ansible/roles/ceph-mds/README.md
/usr/share/ansible/roles/ceph-mds/defaults/main.yml
/usr/share/ansible/roles/ceph-mds/meta/main.yml
/usr/share/ansible/roles/ceph-mds/tasks/docker/checks.yml
/usr/share/ansible/roles/ceph-mds/tasks/docker/dirs_permissions.yml
/usr/share/ansible/roles/ceph-mds/tasks/docker/fetch_configs.yml
/usr/share/ansible/roles/ceph-mds/tasks/docker/main.yml
/usr/share/ansible/roles/ceph-mds/tasks/docker/pre_requisite.yml
/usr/share/ansible/roles/ceph-mds/tasks/docker/selinux.yml
/usr/share/ansible/roles/ceph-mds/tasks/docker/start_docker_mds.yml
/usr/share/ansible/roles/ceph-mds/tasks/main.yml
/usr/share/ansible/roles/ceph-mds/tasks/pre_requisite.yml
/usr/share/ansible/roles/ceph-mds/templates/ceph-mds.service.j2
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
/usr/share/ansible/roles/ceph-osd/tasks/scenarios/dmcrypt-dedicated-journal.yml
/usr/share/ansible/roles/ceph-osd/tasks/scenarios/dmcrypt-journal-collocation.yml
/usr/share/ansible/roles/ceph-osd/tasks/scenarios/journal_collocation.yml
/usr/share/ansible/roles/ceph-osd/tasks/scenarios/osd_directory.yml
/usr/share/ansible/roles/ceph-osd/tasks/scenarios/raw_multi_journal.yml
/usr/share/ansible/roles/ceph-osd/templates/ceph-osd.service.j2
/usr/share/ansible/roles/ceph-osd/templates/osd.conf.j2
/usr/share/ansible/roles/ciao-common/LICENSE
/usr/share/ansible/roles/ciao-common/README.md
/usr/share/ansible/roles/ciao-common/defaults/main.yml
/usr/share/ansible/roles/ciao-common/handlers/main.yml
/usr/share/ansible/roles/ciao-common/meta/main.yml
/usr/share/ansible/roles/ciao-common/tasks/install_clearlinux.yml
/usr/share/ansible/roles/ciao-common/tasks/install_fedora.yml
/usr/share/ansible/roles/ciao-common/tasks/install_ubuntu.yml
/usr/share/ansible/roles/ciao-common/tasks/main.yml
/usr/share/ansible/roles/ciao-compute/LICENSE
/usr/share/ansible/roles/ciao-compute/README.md
/usr/share/ansible/roles/ciao-compute/handlers/main.yml
/usr/share/ansible/roles/ciao-compute/meta/main.yml
/usr/share/ansible/roles/ciao-compute/tasks/images.yml
/usr/share/ansible/roles/ciao-compute/tasks/install.yml
/usr/share/ansible/roles/ciao-compute/tasks/main.yml
/usr/share/ansible/roles/ciao-compute/tasks/startservices.yml
/usr/share/ansible/roles/ciao-compute/templates/ciao-compute.service.j2
/usr/share/ansible/roles/ciao-controller/LICENSE
/usr/share/ansible/roles/ciao-controller/README.md
/usr/share/ansible/roles/ciao-controller/defaults/main.yml
/usr/share/ansible/roles/ciao-controller/files/tables/resources.csv
/usr/share/ansible/roles/ciao-controller/files/tables/workload_resources.csv
/usr/share/ansible/roles/ciao-controller/files/tables/workload_template.csv
/usr/share/ansible/roles/ciao-controller/handlers/main.yml
/usr/share/ansible/roles/ciao-controller/meta/main.yml
/usr/share/ansible/roles/ciao-controller/tasks/build.yml
/usr/share/ansible/roles/ciao-controller/tasks/certificates.yml
/usr/share/ansible/roles/ciao-controller/tasks/create_cnci_image.yml
/usr/share/ansible/roles/ciao-controller/tasks/endpoints.yml
/usr/share/ansible/roles/ciao-controller/tasks/images.yml
/usr/share/ansible/roles/ciao-controller/tasks/install.yml
/usr/share/ansible/roles/ciao-controller/tasks/main.yml
/usr/share/ansible/roles/ciao-controller/tasks/startservices.yml
/usr/share/ansible/roles/ciao-controller/templates/admin-ciaorc.j2
/usr/share/ansible/roles/ciao-controller/templates/ciao-cnci-agent.service.j2
/usr/share/ansible/roles/ciao-controller/templates/ciao-controller.service.j2
/usr/share/ansible/roles/ciao-controller/templates/ciao-scheduler.service.j2
/usr/share/ansible/roles/ciao-controller/templates/configuration.yaml.j2
/usr/share/ansible/roles/ciao-controller/templates/demo-ciaorc.j2
/usr/share/ansible/roles/ciao-controller/templates/workloads/docker-iperf.yaml.j2
/usr/share/ansible/roles/ciao-controller/templates/workloads/docker-ubuntu.yaml.j2
/usr/share/ansible/roles/ciao-controller/templates/workloads/test.yaml.j2
/usr/share/ansible/roles/ciao-network/LICENSE
/usr/share/ansible/roles/ciao-network/README.md
/usr/share/ansible/roles/ciao-network/handlers/main.yml
/usr/share/ansible/roles/ciao-network/meta/main.yml
/usr/share/ansible/roles/ciao-network/tasks/images.yml
/usr/share/ansible/roles/ciao-network/tasks/install.yml
/usr/share/ansible/roles/ciao-network/tasks/main.yml
/usr/share/ansible/roles/ciao-network/tasks/startservices.yml
/usr/share/ansible/roles/ciao-network/templates/ciao-network.service.j2
/usr/share/ansible/roles/ciao-webui/LICENSE
/usr/share/ansible/roles/ciao-webui/README.md
/usr/share/ansible/roles/ciao-webui/defaults/main.yml
/usr/share/ansible/roles/ciao-webui/meta/main.yml
/usr/share/ansible/roles/ciao-webui/tasks/certificates.yml
/usr/share/ansible/roles/ciao-webui/tasks/main.yml
/usr/share/ansible/roles/docker/LICENSE
/usr/share/ansible/roles/docker/README.md
/usr/share/ansible/roles/docker/meta/main.yml
/usr/share/ansible/roles/docker/tasks/install_clearlinux.yml
/usr/share/ansible/roles/docker/tasks/install_fedora.yml
/usr/share/ansible/roles/docker/tasks/install_ubuntu.yml
/usr/share/ansible/roles/docker/tasks/main.yml
/usr/share/ansible/roles/keystone/LICENSE
/usr/share/ansible/roles/keystone/README.md
/usr/share/ansible/roles/keystone/defaults/main.yml
/usr/share/ansible/roles/keystone/library/keystone
/usr/share/ansible/roles/keystone/meta/main.yml
/usr/share/ansible/roles/keystone/tasks/access.yml
/usr/share/ansible/roles/keystone/tasks/certificates.yml
/usr/share/ansible/roles/keystone/tasks/main.yml
/usr/share/ansible/roles/keystone/templates/clouds.yaml.j2
/usr/share/ansible/roles/keystone/templates/openrc.j2
