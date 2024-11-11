# VLC service preview

## Use

```bash
vlc rtsp://stream_address:port/stream_path
```

For example, if you want to test a specific RTSP stream, you could use:

```bash
vlc rtsp://192.168.1.100:554/stream1
```

Some useful VLC command line options you can add:
- `--verbose 2`: For detailed logging
- `--network-caching=1000`: Adjust network buffer (in ms)
- `-v`: Display verbose output
- `--rtsp-tcp`: Force RTSP over TCP instead of UDP

Would you like me to explain any specific aspects of using VLC with RTSP streams?

## Install

For Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ubuntu-restricted-extras
sudo apt install vlc-plugin-base
```

For Fedora:
```bash
sudo dnf install vlc-extras-multimedia
sudo dnf install gstreamer1-plugins-{bad-*,good-*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel
```

For Arch Linux:
```bash
sudo pacman -S vlc-plugin-base
sudo pacman -S gst-plugins-{base,good,bad,ugly}
```

After installing these packages, try running VLC again. If you're still having issues, you can also try:

1. Installing additional codecs:
```bash
sudo apt install libavcodec-extra # For Ubuntu/Debian
```

2. Or rebuild the VLC plugin cache:
```bash
vlc --reset-plugins-cache
```




Let's fix the codec issues on Fedora. Run these commands to install the necessary codecs and multimedia packages:

```bash
# Enable RPM Fusion repositories (if not already enabled)
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

# Update system
sudo dnf update

# Install necessary multimedia packages and codecs
sudo dnf install vlc
sudo dnf install vlc-extras-multimedia
sudo dnf groupupdate multimedia --setop="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin
sudo dnf groupupdate sound-and-video

# Install specific codec packages
sudo dnf install gstreamer1-plugins-{bad-*,good-*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel
sudo dnf install ffmpeg ffmpeg-libs

# Install additional multimedia packages
sudo dnf groupupdate multimedia --setop="install_weak_deps=False"
sudo dnf groupupdate sound-and-video
```

After installation:
1. Restart VLC
2. Clear the VLC cache:
```bash
rm -rf ~/.cache/vlc
```
3. Try playing your stream again

If you're still having issues, please let me know and we can try additional troubleshooting steps.