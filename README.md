### Build

-   go to Ubuntu machine
-   clone repo
-   start LXD: `lxd init --auto`
-   in folder with the project run: `snapcraft`
-   check, we have file `*.snap` in the folder

### Publish

```bash
# sudo snap login
# snap whoami

snapcraft export-login cred.json
export SNAPCRAFT_STORE_CREDENTIALS=$(cat cred.json)
echo $SNAPCRAFT_STORE_CREDENTIALS

snapcraft whoami

snapcraft register salam
snapcraft upload --release=edge salam_*_amd64.snap
snapcraft upload  salam_*_amd64.snap
# Revision 1 created for 'salam' and released to 'edge'
```

### Release

```bash
snapcraft release salam 4 stable
sudo snap install salam
```

### Install

```bash
sudo snap install --edge salam --devmode
which salam
```

### Update

```bash
sudo snap refresh salam --devmode
```

### Info

```bash
snap info salam
snap list
snap list --all
snap list --all | grep salam
snap list --all | grep salam | grep edge
snap list --all | grep salam | grep edge | awk '{print $1}'
# snap list --all | grep salam | grep edge | awk '{print $1}' | xargs snap remove
```
