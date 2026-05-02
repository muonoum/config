.PHONY: all
all:

.PHONY: update
update:
	update-source
	brew update

.PHONY: upgrade
upgrade:
	brew upgrade
	cd $(HOME)/Desktop/source/helix && cargo install --path helix-term --locked
	make -C $(HOME)/Desktop/source/gleam install
	hx --grammar fetch
	hx --grammar build
