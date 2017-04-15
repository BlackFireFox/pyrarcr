pre=/usr/local/bin

install:
  mkdir -p $(pre)
  cp pyrarcr.py $(pre)/pyrarcr
  chmod +x $(pre)/pyrarcr

uninstall:
  rm $(pre)/pyrarcr
