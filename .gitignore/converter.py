import os

def convert_avi_to_mp4(avi_file_path, output_name):
    #os.popen("ffmpeg -i '{input}' -ac 2 -b:v 128k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 '{output}.mp4'".format(input = avi_file_path, output = output_name))
    converter = os.system("ffmpeg -i '{input}' -vf yadif -strict -2 '{output}.mp4'".format(input=avi_file_path, output=output_name))
    return True

if __name__ == "__main__":
    convert_avi_to_mp4("/home/emerson/Videos/sample.dv", "sample_out")
