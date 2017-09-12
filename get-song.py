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
org_song_name=args.name
video=args.video
hide=args.quiet
song_name=re.sub('\s\s*','+',org_song_name)
# print song_name
connection=urllib2.urlopen("https://www.youtube.com/results?search_query="+song_name)
data=connection.read()
# print data
video_ids=re.findall(r'href=\"\/watch\?v=(.{11})',data)
# print video_ids
# connection.close()
if len(video_ids)==0:
	print "No results found."
	exit()

if hide==True:
	vid=pafy.new("https://www.youtube.com/watch?v="+video_ids[0])
	print "Downloading "+vid.title+" by "+vid.author+"..."
	print "Duration : "+vid.duration+", Views : "+str(vid.viewcount)+"\n"
	if video==True:
		vid.getbestvideo().download()
		print "Download complete."
		print "Converting..."
		r=subprocess.call(["ffmpeg","-i",vid.title+".webm",re.sub('\s\s*','_',org_song_name)+".mp4","-loglevel","quiet"])
		r=subprocess.call(["rm","-f",vid.title+".webm"])
		print "Song downloaded as "+re.sub('\s\s*','_',org_song_name)+".mp4"
		ans=raw_input("\nNext step of action :\n[1] play last downloaded song and exit\n[2] exit without playing\n==> ")
		if ans=="1":
			r=subprocess.call(["xdg-open",re.sub('\s\s*','_',org_song_name)+".mp4"])
			exit()
		else:
			exit()
	else:
		vid.getbestaudio().download()
		print "Download complete."
		print "Converting..."
		r=subprocess.call(["ffmpeg","-i",vid.title+".webm",re.sub('\s\s*','_',org_song_name)+".mp3","-loglevel","quiet"])
		r=subprocess.call(["rm","-f",vid.title+".webm"])
		print "Song downloaded as "+re.sub('\s\s*','_',org_song_name)+".mp3"
		ans=raw_input("\nNext step of action :\n[1] play last downloaded song and exit\n[2] exit without playing\n==> ")
		if int(ans)==1:
			r=subprocess.call(["xdg-open",re.sub('\s\s*','_',org_song_name)+".mp3"])
			exit()
		else:
			exit()	
else:
	step=3
	st=0; end=min(step,len(video_ids))
	selected=[]
	
	while True:
		r=subprocess.call(["clear"])
		print "Select the song(s) :\n['n' : next set of songs] ['e' : end and start downloading]\n"
		for id in xrange(st,end):
			try:
				vid=pafy.new("https://www.youtube.com/watch?v="+video_ids[id])
				print "\n[{0}]  ".format(id+1)+vid.title+" : "+vid.author+"\t["+vid.duration+"]\n\tViews : "+str(vid.viewcount)+"\n\tRating : "+str(vid.rating)+"\n"
			except Exception as e:
				pass
				continue			
		choice=raw_input("==> ")
		if choice=="e":
			break
		elif choice=="n":
			st=end; end+=step; end=min(end,video_ids)
			continue
		else:
			selected.extend(map(int,choice.split()))
			st=end; end+=step; end=min(end,len(video_ids))
			continue

	songs_list=""
	if video==True:
		for id in selected:
			vid=pafy.new("https://www.youtube.com/watch?v="+video_ids[id-1])
			print "Downloading "+vid.title+" by "+vid.author+"...\n"
			vid.getbestvideo().download()
			r=subprocess.call(["ffmpeg","-i",vid.title+".webm",re.sub('\s\s*','_',org_song_name)+"_"+str(id)+".mp4","-loglevel","quiet"])
			r=subprocess.call(["rm","-f",vid.title+".webm"])
			songs_list+=re.sub('\s\s*','_',org_song_name)+"_"+str(id)+".mp4 "
			print "\n"
	else:
		for id in selected:
			vid=pafy.new("https://www.youtube.com/watch?v="+video_ids[id-1])
			print "Downloading "+vid.title+" by "+vid.author+"..."
			vid.getbestaudio().download()
			r=subprocess.call(["ffmpeg","-i",vid.title+".webm",re.sub('\s\s*','_',org_song_name)+"_"+str(id)+".mp3","-loglevel","quiet"])
			r=subprocess.call(["rm","-f",vid.title+".webm"])
			songs_list+=re.sub('\s\s*','_',org_song_name)+"_"+str(id)+".mp3 "
			print "\n"
	ans=raw_input("\nNext step of action :\n[1] open containing folder and exit\n[2] exit \n==> ")
	if ans=="1":
		r=subprocess.call(["xdg-open","."])
		exit()
	else:
		exit()



