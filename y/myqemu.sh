qemu-system-x86_64 \
  -enable-kvm \
  -cpu host \
  -smp 1 \
  -m 1G \
  -drive file=disk.qcow2,if=virtio,discard=unmap,detect-zeroes=on \
  -net nic,model=virtio \
  -net tap,ifname=tap0,script=no,downscript=no \
  -vga virtio
