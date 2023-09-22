mkdir images
cd images
ffmpeg  -i ../input.mp4 %06d.png
cd ..