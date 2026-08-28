# Makefile for rpm scripts.

include $(top_srcdir)/rpm.am
AM_CFLAGS = @RPMCFLAGS@

CLEANFILES =
DISTCLEANFILES = os2deps.sh perl.prov perl.req pkgconfigdeps.sh script.req

EXTRA_DIST = \
	brp-compress brp-python-bytecompile brp-java-gcjcompile \
	brp-strip brp-strip-comment-note brp-python-hardlink \
	brp-strip-shared brp-strip-static-archive \
	check-files check-prereqs \
	check-buildroot check-rpaths check-rpaths-worker \
	debuginfo.prov \
	find-debuginfo.sh find-lang.sh \
	perl.prov.in perl.req.in pythondeps.sh pythondistdeps.py \
	rpmdb_loadcvt rpm.daily rpm.log rpm.supp rpm2cpio.sh \
	tgpg vpkg-provides.sh \
	find-requires find-provides \
	find-requires.php find-provides.php \
	ocaml-find-requires.sh ocaml-find-provides.sh \
	os2deps.sh.in pkgconfigdeps.sh.in libtooldeps.sh metainfo.prov \
	fontconfig.prov desktop-file.prov script.req.in

rpmconfig_SCRIPTS = \
	brp-compress brp-python-bytecompile brp-java-gcjcompile \
	brp-strip brp-strip-comment-note brp-python-hardlink \
	brp-strip-shared brp-strip-static-archive \
	os2deps.sh \
	check-files check-prereqs \
	check-buildroot check-rpaths check-rpaths-worker \
	debuginfo.prov \
	find-lang.sh find-requires find-provides \
	perl.prov perl.req pythondeps.sh pythondistdeps.py \
	metainfo.prov \
	pkgconfigdeps.sh libtooldeps.sh \
	ocaml-find-requires.sh ocaml-find-provides.sh \
	fontconfig.prov desktop-file.prov script.req \
	rpmdb_loadcvt rpm2cpio.sh tgpg 

rpmconfig_DATA = \
	rpm.daily rpm.log rpm.supp
