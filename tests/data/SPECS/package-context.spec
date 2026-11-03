%global package_name context
# Defer context references until each generated section has been parsed.
%define generated_parts() \
%package -n %%{package_name}-generated\
Summary: %%{!?package_section_package:missing-marker }%%{?package_section_files:leaked-marker }%%{package_section} %%{package_name} %%{package_evr}\
Version: 7\
Release: 8\
Epoch: 9\
%description -n context-generated\
%%{!?package_section_description:missing-marker }%%{?package_section_package:leaked-marker }%%{package_section} %%{package_name} %%{package_evr} (%%{package_scriptlet})\
%post -n context-generated\
%%{!?package_scriptlet_post:missing-marker }%%{?package_section_description:leaked-marker }echo '%%{package_scriptlet} %%{package_name} %%{package_evr} (%%{package_section})'\
echo '%%%%{package_name}'\
echo '%%{_bindir} %%{?package_scriptlet_post:%%{_libdir}} %%{?name:%%{package_evr}} %%%%'\
%if 0\
echo 'inactive %%{package_evr}'\
%endif\
%files -n context-generated\
%%{!?package_section_files:missing-marker }%%{?package_scriptlet_post:leaked-marker }%ghost /%%{package_name}-%%{package_version}-%%{package_release}

%define generated_commands() \
test '%%{package_evr}' = '%''{package_evr}'\
:

%{?context_features:BuildFeatures: %{context_features}}
%{!?context_features:BuildFeatures: package-context}
Name: context
Version: 1
Release: 2
Epoch: 3
%define vendor Example %{package_section} %{package_name} %{package_evr}
Summary: %{!?package_section_package:%{error:Missing package marker}}%{?package_section_description:%{error:Leaked description marker}}%{package_section} %{package_name} %{package_evr}
License: MIT
BuildArch: noarch

%package tools
Summary: %{!?package_section_package:%{error:Missing package marker}}%{?package_section_description:%{error:Leaked description marker}}%{package_section} %{package_name} %{package_evr}
Version: 4
Release: 5
Epoch: 6
Requires: context = %{package_evr}

# Header expansion must restore the pre-existing package_name macro.
%description -n %{package_name}
%{!?package_section_description:%{error:Missing description marker}}%{?package_section_package:%{error:Leaked package marker}}%{package_section} %{package_name} %{package_evr} (%{package_scriptlet})

%description tools
%{!?package_section_description:%{error:Missing description marker}}%{?package_section_package:%{error:Leaked package marker}}%{package_section} %{package_name} %{package_evr} (%{package_scriptlet})

%prep
%if 0%{?context_check_setup}
%define _fixperms test '%{package_section} %{package_evr}' = 'prep 3:1-2' || exit 1; :
%setup -c -T
%endif
test \
  '%%{package_evr}' = '%''{package_evr}'
%generated_commands
%if "%{package_name}" != "context" || "%{package_evr}" != "3:1-2" || "%{package_section}" != "prep" || "%{package_scriptlet}" != "" || !0%{?package_section_prep} || 0%{?package_section_description:1}
%{error:Incorrect prep context}
%endif
%if !0%{?buildfeature_package_context}
%{error:Missing enabled build feature}
%endif
mkdir -p %{_builddir}
cat > %{_builddir}/context-post <<'SCRIPT'
%%{!?package_scriptlet_postun:%%{error:Missing external scriptlet marker}}%%{?package_scriptlet_post:%%{error:Leaked post marker}}echo '%%{package_scriptlet} %%{package_name} %%{package_evr} (%%{package_section})'
SCRIPT
cat > %{_builddir}/context-trigger <<'SCRIPT'
%%{!?package_scriptlet_triggerin:%%{error:Missing external scriptlet marker}}%%{?package_scriptlet_post:%%{error:Leaked post marker}}echo '%%{package_scriptlet} %%{package_name} %%{package_evr} (%%{package_section})'
SCRIPT
cat > %{_builddir}/context-files <<'FILES'
%%{!?package_section_files:%%{error:Missing manifest marker}}%%{?package_scriptlet_triggerin:%%{error:Leaked trigger marker}}%%ghost /external-%%{package_name}-%%{package_evr}
FILES

%generate_buildrequires
%{!?package_section_generate_buildrequires:%{error:Missing generate_buildrequires marker}}%{?package_section_prep:%{error:Leaked prep marker}}
%if "%{package_name}" != "context" || "%{package_evr}" != "3:1-2" || "%{package_section}" != "generate_buildrequires" || "%{package_scriptlet}" != ""
%{error:Incorrect generate_buildrequires context}
%endif
:

%build
%{!?package_section_build:%{error:Missing build marker}}%{?package_section_generate_buildrequires:%{error:Leaked generate_buildrequires marker}}
%if "%{package_name}" != "context" || "%{package_evr}" != "3:1-2" || "%{package_section}" != "build" || "%{package_scriptlet}" != ""
%{error:Incorrect build context}
%endif
:

%install
%{!?package_section_install:%{error:Missing install marker}}%{?package_section_build:%{error:Leaked build marker}}
%if "%{package_name}" != "context" || "%{package_evr}" != "3:1-2" || "%{package_section}" != "install" || "%{package_scriptlet}" != ""
%{error:Incorrect install context}
%endif
mkdir -p %{buildroot}

%check
%{!?package_section_check:%{error:Missing check marker}}%{?package_section_install:%{error:Leaked install marker}}
%if "%{package_name}" != "context" || "%{package_evr}" != "3:1-2" || "%{package_section}" != "check" || "%{package_scriptlet}" != ""
%{error:Incorrect check context}
%endif
:

%clean
%{!?package_section_clean:%{error:Missing clean marker}}%{?package_section_check:%{error:Leaked check marker}}
%if "%{package_name}" != "context" || "%{package_evr}" != "3:1-2" || "%{package_section}" != "clean" || "%{package_scriptlet}" != ""
%{error:Incorrect clean context}
%endif
:

%post tools
%{!?package_scriptlet_post:%{error:Missing post marker}}%{?package_section_description:%{error:Leaked section marker}}echo '%{package_scriptlet} %{package_name} %{package_evr} (%{package_section})'

%postun tools -f context-post

%triggerin tools -f context-trigger -- context

%files
%{!?package_section_files:%{error:Missing files marker}}%{?package_scriptlet_postun:%{error:Leaked postun marker}}%ghost /%{package_name}-%{package_version}-%{package_release}

%files tools -f context-files
%{!?package_section_files:%{error:Missing files marker}}%{?package_scriptlet_postun:%{error:Leaked postun marker}}%ghost /%{package_name}-%{package_version}-%{package_release}

%generated_parts

%changelog
%if 0%{?package_section:1} || 0%{?package_scriptlet:1} || 0%{?package_section_files:1} || 0%{?package_section_clean:1}
%{error:Package context leaked into changelog}
%endif
