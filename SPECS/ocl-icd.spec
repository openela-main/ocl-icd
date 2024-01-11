Name:           ocl-icd
Version:        2.2.12
Release:        1%{?dist}
Summary:        OpenCL ICD Bindings

License:        BSD
URL:            https://forge.imag.fr/projects/ocl-icd/
Source0:        https://forge.imag.fr/frs/download.php/836/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  opencl-headers
BuildRequires:  ruby rubygems
%if 0%{?fedora}
Recommends:     beignet
Recommends:     mesa-libOpenCL
Recommends:     pocl
%endif

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opencl-headers

%description devel
This package contains the development files for %{name}.

%prep
%autosetup

%build
autoreconf -vfi
%configure
%make_build

%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.la
rm -vrf %{buildroot}%{_defaultdocdir}

%check
make check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README
%{_libdir}/libOpenCL.so.*

%files devel
%doc ocl_icd_loader_gen.map ocl_icd_bindings.c
%{_includedir}/ocl_icd.h
%{_libdir}/libOpenCL.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/OpenCL.pc

%changelog
* Fri Mar 23 2018 Simone Caronni <negativo17@gmail.com> - 2.2.12-1
- Update to 2.2.12, adds OpenCL 2.2 support.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 09 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.2.11-2
- Add Recommends for all OpenCL implementations

* Fri Jan 20 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.2.11-1
- Update to 2.2.11 (RHBZ #1415150)

* Sun Dec 04 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.2.10-1
- Update to 2.2.10

* Mon Nov 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.2.9-3
- Drop unneeded BR on rubypick

* Wed Aug 31 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.2.9-2
- Rebuild for OpenCL 2.1

* Sun Aug 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.2.9-1
- Update to 2.2.9
- Drop requires for opencl-icd

* Fri Apr 08 2016 Björn Esser <fedora@besser82.io> - 2.2.8-3.git20151217.0122332
- add Requires for virtual Provides: opencl-icd (RHBZ #1317600)
- add rubygems and rubypick to BuildRequires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-2.git20151217.0122332
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 François Cami <fcami@fedoraproject.org> - 2.2.8-1.git20151217.0122332
- Update to 2.2.8.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-2.git20150606.ebbc4c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 François Cami <fcami@fedoraproject.org> - 2.2.7-1.git20150609.ebbc4c1
- Update to 2.2.7.

* Sun Jun 07 2015 François Cami <fcami@fedoraproject.org> - 2.2.5-1.git20150606.de64dec
- Update to 2.2.5 (de64dec).

* Mon May 18 2015 Fabian Deutsch <fabiand@fedorproject.org> - 2.2.4-1.git20150518.7c94f4a
- Update to 2.2.4 (7c94f4a)

* Mon Jan 05 2015 François Cami <fcami@fedoraproject.org> - 2.2.3-1.git20141005.7cd0c2f
- Update to 2.2.3 (7cd0c2f).

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3.git20131001.4ee231e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2.git20131001.4ee231e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 01 2013 Björn Esser <bjoern.esser@gmail.com> - 2.0.4-1.git20131001.4ee231e
- update to recent git-snapshot
- general cleanup, squashed unneeded BuildRequires
- cleanup the %%doc mess.
- add %%check for running the testsuite

* Wed Aug 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Specfile cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Rob Clark <rclark@redhat.com> 2.0.2-1
- ocl-icd 2.0.2
