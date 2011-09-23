#!/usr/bin/perl

my $specfile = shift;

open my $fh, "<", $specfile or die "cannot open $specfile, $!";

my %value_of;
while (<$fh>) {
    chomp;
    last if /^\%description/;
    my ($k, $v) = $_ =~ /^(\w+):\s+(.+)$/;
    $k = lc $k;
    $value_of{$k} = $v;
}

my @sources = grep { /^source\d*$/ } keys %value_of;
foreach my $s (@sources) {

    # expand macro in the value
    my @matches = $value_of{$s} =~ /%{(\w+)}/g;
    foreach my $m (@matches) {
        $value_of{$s} =~ s/%{$m}/$value_of{$m}/g;
    }
    printf "%s\n", $value_of{$s} if $value_of{$s} =~ /^(?:http|ftp)s?:\/\//;
}

=head1 NAME

sources_from_spec.pl - Extract source URLs from specfile.

=head1 USAGE

 wget --no-clobber --directory-prefix=SOURCES `tools/sources_from_spec.pl SPECS/*.spec`


