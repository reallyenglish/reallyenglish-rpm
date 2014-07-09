# Generated from chef-vault-2.2.3.gem by gem2rpm -*- rpm-spec -*-
%global gemname chef-vault

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Data encryption support for Chef using data bags
Name: rubygem-%{gemname}
Version: 2.2.3
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/Nordstrom/chef-vault
Source0: %{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Data encryption support for Chef using data bags.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -pa .%{gemdir}/* \
        %{buildroot}%{gemdir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%files
%dir %{geminstdir}
%{_bindir}/chef-vault
%{geminstdir}/bin
%{geminstdir}/lib
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%exclude %{geminstdir}/.gitignore
%exclude %{geminstdir}/.rspec
%exclude %{geminstdir}/.travis.yml
%exclude %{geminstdir}/Gemfile
%exclude %{geminstdir}/Rakefile
%{geminstdir}/spec/chef-vault_spec.rb
%{geminstdir}/spec/item_keys_spec.rb
%{geminstdir}/spec/item_spec.rb
%{geminstdir}/spec/spec_helper.rb
%{geminstdir}/%{gemname}.gemspec
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%{geminstdir}/CONTRIBUTING.md
%{geminstdir}/Changelog.md
%{geminstdir}/DEMO.md
%{geminstdir}/KNIFE_EXAMPLES.md
%{geminstdir}/LICENSE
%{geminstdir}/README.md


%changelog
* Wed Jul 09 2014  <mitsuruy@rpmbuild56> - 2.2.3-1
- Initial package
