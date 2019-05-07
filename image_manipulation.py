import os
def transform_img_to_mov(src, dest):
    os.makedirs(os.path.dirname(dest))
    cmd = "./ffmpeg -loop 1 -i {} -t 5 -pix_fmt yuv420p {}".format(src, dest)
    os.system(cmd)
