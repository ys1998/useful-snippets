# CITATIONS
# https://martin-thoma.com/how-to-parse-command-line-arguments-in-python/
# https://www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video
import pafy
import argparse
import urllib2
import re
import subprocess

parser=argparse.ArgumentParser("get-song.py")
parser.add_argument('-n','--name',type=str,action="store",dest="name",help="name of the song",required=True)
parser.add_argument('-v','--video',action="store_true",dest="video",default=False,help="downloads the video when specified, and only the audio otherwise")
parser.add_argument('-s','--select',action="store_false",dest="quiet",default=True,help="when specified shows all details and allows for selection, otherwise downloads the top match")

args=parser.parse_args()

connection = urllib2.urlopen("https://www.youtube.com/results?search_query=" + re.sub('\s+','+', args.name))
data = connection.read()

raw_ids = re.findall(r'href=\"\/watch\?v=(.{11})', data)
video_ids = []
for idx in raw_ids:
	if idx not in video_ids:
		video_ids.append(idx)

if len(video_ids) == 0:
    print "No results found."
    exit()

if args.quiet:
    vid = pafy.new("https://www.youtube.com/watch?v=" + video_ids[0])
    print "Downloading " + vid.title + " by " + vid.author + " ..."
    print "Duration : " + vid.duration + ", Views : " + str(vid.viewcount) + "\n"
    if args.video:
        vid.getbestvideo().download()
        print "Download complete."
        print "Converting..."
        r = subprocess.call(["ffmpeg","-i",vid.title + ".webm", re.sub('\s+','_',org_song_name) + ".mp4", "-loglevel", "quiet"])
        r = subprocess.call(["rm","-f", vid.title + ".webm"])
        print "Song downloaded as " + re.sub('\s+','_', org_song_name) + ".mp4"
    else:
        vid.getbestaudio().download()
        print "Download complete."
        print "Converting..."
        r=subprocess.call(["ffmpeg", "-i", vid.title + ".webm", re.sub('\s\s*','_',org_song_name) + ".mp3", "-loglevel", "quiet"])
        r=subprocess.call(["rm", "-f", vid.title + ".webm"])
        print "Song downloaded as " + re.sub('\s+', '_', org_song_name) + ".mp3"
else:
    step = 3
    st = 0 
    end = min(step,len(video_ids))
    selected = []
    print "\nSelect the song(s) :\n['n' : next set of songs] ['e' : end and start downloading]\n"
    while True:
        for idx in xrange(st, end):
            try:
                vid=pafy.new("https://www.youtube.com/watch?v=" + video_ids[idx])
                print "\n[{0}]  ".format(idx+1)+vid.title+" : "+vid.author+"\t["+vid.duration+"]\n\tViews : "+str(vid.viewcount)+"\n\tRating : "+str(vid.rating)+"\n"
            except Exception as e:
                pass
                continue            
        choice = raw_input(">>> ").split()
        indices = [int(c) for c in choice if c != 'e' and c != 'n']
        selected.extend(indices)
        if 'e' in choice:
            break
        elif 'n' in choice:
            st = end
            end += step
            end = min(end, video_ids)
        else:
            break

    songs_list=""
    if args.video:
        for idx in selected:
            vid = pafy.new("https://www.youtube.com/watch?v=" + video_ids[idx-1])
            print "Downloading " + vid.title + " by " + vid.author + " ...\n"
            vid.getbestvideo().download()
            r=subprocess.call(["ffmpeg","-i",vid.title+".webm",re.sub('\s\s*','_',org_song_name)+"_"+str(idx)+".mp4","-loglevel","quiet"])
            r=subprocess.call(["rm","-f",vid.title+".webm"])
            songs_list+=re.sub('\s\s*','_',org_song_name)+"_"+str(idx)+".mp4"
            print "\n"
    else:
        for idx in selected:
            vid=pafy.new("https://www.youtube.com/watch?v="+video_ids[idx-1])
            print "Downloading "+vid.title+" by "+vid.author+"..."
            vid.getbestaudio().download()
            r=subprocess.call(["ffmpeg","-i",vid.title+".webm",re.sub('\s\s*','_',org_song_name)+"_"+str(idx)+".mp3","-loglevel","quiet"])
            r=subprocess.call(["rm","-f",vid.title+".webm"])
            songs_list+=re.sub('\s\s*','_',org_song_name)+"_"+str(idx)+".mp3 "
            print "\n"