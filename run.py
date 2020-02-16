import subprocess
cmd = 'ffmpeg -i /dev/video0 -c copy -map 0 -segment_time 00:00:05 -f segment -reset_timestamps 1 output%03d.mp4 -y'
print(cmd)
subprocess.Popen("nohup "+cmd+" >/dev/null 2>&1 &", shell=True)