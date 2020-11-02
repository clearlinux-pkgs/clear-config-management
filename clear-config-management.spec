#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clear-config-management
Version  : 5.3
Release  : 49
URL      : https://github.com/clearlinux/clear-config-management/archive/5.3.tar.gz
Source0  : https://github.com/clearlinux/clear-config-management/archive/5.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: clear-config-management-data = %{version}-%{release}
Requires: clear-config-management-license = %{version}-%{release}

%description
# Clear Config Management
This repository contains application roles to be used with Ansible
as Configuration Management Engine running on Clear Linux*.

%package data
Summary: data components for the clear-config-management package.
Group: Data

%description data
data components for the clear-config-management package.


%package license
Summary: license components for the clear-config-management package.
Group: Default

%description license
license components for the clear-config-management package.


%prep
%setup -q -n clear-config-management-5.3
cd %{_builddir}/clear-config-management-5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604356997
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1604356997
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clear-config-management
cp %{_builddir}/clear-config-management-5.3/LICENSE %{buildroot}/usr/share/package-licenses/clear-config-management/598f87f072f66e2269dd6919292b2934dbb20492
cp %{_builddir}/clear-config-management-5.3/roles/ceph-common/LICENSE %{buildroot}/usr/share/package-licenses/clear-config-management/af86318aebfa4c8a70da4e5d234b19b2ecc428f9
cp %{_builddir}/clear-config-management-5.3/roles/ceph-mds/LICENSE %{buildroot}/usr/share/package-licenses/clear-config-management/af86318aebfa4c8a70da4e5d234b19b2ecc428f9
cp %{_builddir}/clear-config-management-5.3/roles/ceph-mon/LICENSE %{buildroot}/usr/share/package-licenses/clear-config-management/af86318aebfa4c8a70da4e5d234b19b2ecc428f9
cp %{_builddir}/clear-config-management-5.3/roles/ceph-osd/LICENSE %{buildroot}/usr/share/package-licenses/clear-config-management/af86318aebfa4c8a70da4e5d234b19b2ecc428f9
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
/usr/share/ansible/plugins/action/_v1_config_template.py
/usr/share/ansible/plugins/action/_v2_config_template.py
/usr/share/ansible/plugins/action/config_template.py
/usr/share/ansible/roles/ceph-common/LICENSE
/usr/share/ansible/roles/ceph-common/README.md
/usr/share/ansible/roles/ceph-common/defaults/main.yml
/usr/share/ansible/roles/ceph-common/files/cephdev.asc
/usr/share/ansible/roles/ceph-common/files/cephstable.asc
/usr/share/ansible/roles/ceph-common/files/cephstablerhcs.asc
/usr/share/ansible/roles/ceph-common/handlers/main.yml
/usr/share/ansible/roles/ceph-common/handlers/restart-mds.yml
/usr/share/ansible/roles/ceph-common/handlers/restart-mon.yml
/usr/share/ansible/roles/ceph-common/handlers/restart-osd.yml
/usr/share/ansible/roles/ceph-common/handlers/restart-rgw.yml
/usr/share/ansible/roles/ceph-common/handlers/validate-mon.yml
/usr/share/ansible/roles/ceph-common/handlers/validate-osd.yml
/usr/share/ansible/roles/ceph-common/meta/main.yml
/usr/share/ansible/roles/ceph-common/plugins/actions/_v1_config_template.py
/usr/share/ansible/roles/ceph-common/plugins/actions/_v2_config_template.py
/usr/share/ansible/roles/ceph-common/plugins/actions/config_template.py
/usr/share/ansible/roles/ceph-common/tasks/checks/check_firewall.yml
/usr/share/ansible/roles/ceph-common/tasks/checks/check_mandatory_vars.yml
/usr/share/ansible/roles/ceph-common/tasks/checks/check_ntp_atomic.yml
/usr/share/ansible/roles/ceph-common/tasks/checks/check_ntp_debian.yml
/usr/share/ansible/roles/ceph-common/tasks/checks/check_ntp_redhat.yml
/usr/share/ansible/roles/ceph-common/tasks/checks/check_socket.yml
/usr/share/ansible/roles/ceph-common/tasks/checks/check_system.yml
/usr/share/ansible/roles/ceph-common/tasks/configure_cluster_name.yml
/usr/share/ansible/roles/ceph-common/tasks/create_ceph_initial_dirs.yml
/usr/share/ansible/roles/ceph-common/tasks/create_rbd_client_dir.yml
/usr/share/ansible/roles/ceph-common/tasks/docker/fetch_image.yml
/usr/share/ansible/roles/ceph-common/tasks/facts.yml
/usr/share/ansible/roles/ceph-common/tasks/facts_mon_fsid.yml
/usr/share/ansible/roles/ceph-common/tasks/generate_ceph_conf.yml
/usr/share/ansible/roles/ceph-common/tasks/generate_cluster_fsid.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/debian_ceph_repository.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_on_clear.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_on_debian.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_on_redhat.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_rh_storage_on_debian.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/install_rh_storage_on_redhat.yml
/usr/share/ansible/roles/ceph-common/tasks/installs/redhat_ceph_repository.yml
/usr/share/ansible/roles/ceph-common/tasks/main.yml
/usr/share/ansible/roles/ceph-common/tasks/misc/ntp_atomic.yml
/usr/share/ansible/roles/ceph-common/tasks/misc/ntp_debian.yml
/usr/share/ansible/roles/ceph-common/tasks/misc/ntp_redhat.yml
/usr/share/ansible/roles/ceph-common/tasks/misc/system_tuning.yml
/usr/share/ansible/roles/ceph-common/tasks/pre_requisites/prerequisite_rhcs_cdn_install.yml
/usr/share/ansible/roles/ceph-common/tasks/pre_requisites/prerequisite_rhcs_iso_install.yml
/usr/share/ansible/roles/ceph-common/tasks/release.yml
/usr/share/ansible/roles/ceph-common/templates/ceph.conf.j2
/usr/share/ansible/roles/ceph-common/templates/client_restapi_address.j2
/usr/share/ansible/roles/ceph-common/templates/client_restapi_interface.j2
/usr/share/ansible/roles/ceph-common/templates/ganesha.conf.j2
/usr/share/ansible/roles/ceph-common/templates/redhat_storage_repo.j2
/usr/share/ansible/roles/ceph-common/templates/rhcs.pref.j2
/usr/share/ansible/roles/ceph-mds/LICENSE
/usr/share/ansible/roles/ceph-mds/README.md
/usr/share/ansible/roles/ceph-mds/defaults/main.yml
/usr/share/ansible/roles/ceph-mds/meta/main.yml
/usr/share/ansible/roles/ceph-mds/tasks/docker/checks.yml
/usr/share/ansible/roles/ceph-mds/tasks/docker/dirs_permissions.yml
/usr/share/ansible/roles/ceph-mds/tasks/docker/fetch_configs.yml
/usr/share/ansible/roles/ceph-mds/tasks/docker/main.yml
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
/usr/share/ansible/roles/ceph-mon/tasks/check_mandatory_vars.yml
/usr/share/ansible/roles/ceph-mon/tasks/create_mds_filesystems.yml
/usr/share/ansible/roles/ceph-mon/tasks/deploy_monitors.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/checks.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/copy_configs.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/create_configs.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/dirs_permissions.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/fetch_configs.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/main.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/selinux.yml
/usr/share/ansible/roles/ceph-mon/tasks/docker/start_docker_monitor.yml
/usr/share/ansible/roles/ceph-mon/tasks/main.yml
/usr/share/ansible/roles/ceph-mon/tasks/openstack_config.yml
/usr/share/ansible/roles/ceph-mon/tasks/rbd_pool.yml
/usr/share/ansible/roles/ceph-mon/tasks/rbd_pool_pgs.yml
/usr/share/ansible/roles/ceph-mon/tasks/rbd_pool_size.yml
/usr/share/ansible/roles/ceph-mon/tasks/secure_cluster.yml
/usr/share/ansible/roles/ceph-mon/tasks/start_monitor.yml
/usr/share/ansible/roles/ceph-mon/templates/ceph-mon.service.j2
/usr/share/ansible/roles/ceph-osd/LICENSE
/usr/share/ansible/roles/ceph-osd/README.md
/usr/share/ansible/roles/ceph-osd/defaults/main.yml
/usr/share/ansible/roles/ceph-osd/meta/main.yml
/usr/share/ansible/roles/ceph-osd/tasks/activate_osds.yml
/usr/share/ansible/roles/ceph-osd/tasks/check_devices.yml
/usr/share/ansible/roles/ceph-osd/tasks/check_devices_auto.yml
/usr/share/ansible/roles/ceph-osd/tasks/check_devices_static.yml
/usr/share/ansible/roles/ceph-osd/tasks/check_mandatory_vars.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/checks.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/dirs_permissions.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/fetch_configs.yml
/usr/share/ansible/roles/ceph-osd/tasks/docker/main.yml
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
/usr/share/ansible/roles/ceph-osd/templates/ceph-osd-run.sh.j2
/usr/share/ansible/roles/ceph-osd/templates/ceph-osd.service.j2
/usr/share/ansible/roles/ceph-osd/templates/osd.conf.j2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clear-config-management/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/clear-config-management/af86318aebfa4c8a70da4e5d234b19b2ecc428f9
