#!/usr/bin/bash

# Disco a configurar
NVME_DEVICE="/dev/nvme0n1"

# Tamaño particiones
SIZE_PART1="+120G"
SIZE_PART2="+100G"

# Instalamos aplicaciones necesarias
## - gdisk : para particionar modo gpt
## - xfsprogs : configurar particiones FS xfs
## - ntfs-3g : configurar particiones FS NTFS
echo "Instalando aplicaciones necesarias"
/bin/apt update && /bin/apt install gdisk xfsprogs ntfs-3g -y

# Particionamos con GPT
### /bin/echo -e "o\ny\nw\ny\n" | /sbin/gdisk ${NVME_DEVICE}
/bin/echo -e "o\ny\nn\n1\n\n${SIZE_PART1}\n\nn\n2\n\n${SIZE_PART2}\n0700\nn\n3\n\n\n\nw\ny\n" | /sbin/gdisk ${NVME_DEVICE}

# Instalando los sistemas de archivos en las particiones
/bin/echo "Instalando los sistemas de archivos en las particiones"
/sbin/mkfs.xfs -L 'DATOS_XFS' ${NVME_DEVICE}p1
/sbin/mkfs.ntfs -L 'DATOS_NTFS' -Q ${NVME_DEVICE}p2

# Creamos los puntos de montaje
echo "Creamos los puntos de montaje y sus permisos"
/bin/mkdir -p /mnt/data1
/bin/chmod 777 /mnt/data1

/bin/mkdir -p /mnt/data2
/bin/chmod 777 /mnt/data2

# Configurar el montaje permanente de las particiones /etc/fstab
## Eliminamos los puntos de montaje de las particiones si ya existen
NVME_DEVICE_ESC=$(echo ${NVME_DEVICE} | sed 's/\//\\\//g')
sudo sed -i "/^${NVME_DEVICE_ESC}p1/d" /etc/fstab
sudo sed -i "/^${NVME_DEVICE_ESC}p2/d" /etc/fstab

## Añadimos las lineas necesarias
echo "Añadimos lineas necesarias en /etc/fstab"
### Particion 1 : XFS -> /mnt/data1
/bin/echo -e "${NVME_DEVICE}p1\t/mnt/data1\txfs\tdefaults\t0\t0" | tee -a /etc/fstab
### Particion 2 : NTFS -> /mnt/data2
/bin/echo -e "${NVME_DEVICE}p2\t/mnt/data2\tntfs-3g\tdefaults,locale=es_ES.utf8\t0\t0" | tee -a /etc/fstab

# Montamos los sistemas de archivos configurados
echo "Vamos a re-montar"
/bin/mount -a
/bin/systemctl daemon-reload