# TODO Remove copied code
obj/i3-config-dark: ./config/i3-config.j2 ./apply-style.py
	@mkdir -p obj/
	@./apply-style.py ./config/i3-config.j2 dark > ./obj/i3-config-dark

obj/i3status-config-dark: ./config/i3status-config.j2 ./apply-style.py
	@mkdir -p obj/
	@./apply-style.py ./config/i3status-config.j2 dark > ./obj/i3status-config-dark

obj/i3-config-light: ./config/i3-config.j2 ./apply-style.py
	@mkdir -p obj/
	@./apply-style.py ./config/i3-config.j2 light > ./obj/i3-config-light

obj/i3status-config-light: ./config/i3status-config.j2 ./apply-style.py
	@mkdir -p obj/
	@./apply-style.py ./config/i3status-config.j2 light > ./obj/i3status-config-light

install-dark: obj/i3-config-dark obj/i3status-config-dark
	@cp ./obj/i3-config-dark ~/.config/i3/config
	@cp ./obj/i3status-config-dark ~/.config/i3status/config
	@i3 restart

install-light: obj/i3-config-light obj/i3status-config-light
	@cp ./obj/i3-config-light ~/.config/i3/config
	@cp ./obj/i3status-config-light ~/.config/i3status/config
	@i3 restart
