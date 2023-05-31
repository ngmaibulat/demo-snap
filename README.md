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
snapcraft upload --release=edge salam_0.0.1_amd64.snap

# Revision 1 created for 'salam' and released to 'edge'
```

### Install

```bash
sudo snap install --edge salam --devmode
```
