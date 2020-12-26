SUBDIRS = part1 part2
TARGETS = all clean distclean

define make-target
$1/$2: 
	make -C $1 $2
endef

define make-target-all
$1:
	$(MAKE) -C $1 all
endef

.PHONY: $(SUBDIRS)

all: $(SUBDIRS)

$(foreach SUBDIR, $(SUBDIRS), $(eval $(call make-target-all, $(SUBDIR))))
