# Goodwill Coupon Bot
Discord bot that posts Goodwill coupon when command is invoked.

## Installation & Usage
I recommend either using pythons venv module or a Docker container; preferably the latter.

### Docker
```bash
# git submodule setup
git submodule update --init --recursive

# Docker setup
docker build --pull --rm -t gw_coupon_bot:latest "."
docker run --rm -d gw_coupon_bot:latest
```

### venv
```bash
# git submodule setup
git submodule update --init --recursive

# venv setup
python3 -m pip venv .venv
source .venv/bin/activate

# bot setup
python3 -m pip install --no-cache-dir -r requirements.txt
python3 bot.py
```

### Discord Usage
```
!gw_coupon
```
