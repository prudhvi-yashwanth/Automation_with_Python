disk_raw = "Disk free: 25GB"
threshold_gb = "20"

disk_usage = int(disk_raw.split(":")[1].strip().replace("GB", ''))
threshold_data = int(threshold_gb)

if disk_usage < threshold_data:
    print("LOW DISK SPACE")
else:
    print("Disk OK")


