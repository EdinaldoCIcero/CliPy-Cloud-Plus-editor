from moviepy.editor import VideoFileClip , concatenate_videoclips
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import moviepy.video.fx.all as vfx

#from moviepy.editor import *

import os
import sys

class Video_Class():
	def __init__(self):

		pass

	def set_clip_timer_speed(self ,video_fl ,speed_clip , name_output_video ):
		ffmpeg_extract_subclip(video_fl , 0 ,2 , "cut.mp4" )

		speed       = float( speed_clip )
		video_clip  = VideoFileClip(video_fl)
		video_speed = video_clip.fx( vfx.speedx , speed )

		video_speed.write_videofile( name_output_video )
		pass

	def clip_fedein(self , video_fl , name_output_video ):
		ffmpeg_extract_subclip(video_fl , 0 ,2 , "cut.mp4" )

		video_clip      = VideoFileClip(video_fl)
		fade_in 		= video_clip.fx( vfx.fadein ,  duration= 2.0 )
		fade_out 		= fade_in.fx( vfx.fadeout ,  duration= 2.0 )

		fade_out.write_videofile( name_output_video , fps=30 , preset="ultrafast" )
		pass


	def clip_cut(self , clip_file , start_frame , end_frame ,  name_output_clip ):

		video_clip = VideoFileClip(clip_file)

		clip_cut   =  video_clip.cutout( float(start_frame) , float(end_frame) )

		clip_cut.write_videofile(name_output_clip , fps=30 , preset="ultrafast")
		
		pass



	def video_joins( self, 
		v_intro  , 
		video_fl ,
		clip_end , 

		fadein_intro , 
		fadeout_intro , 

		fadein_clip  , 
		fadeout_clip , 

		fadein_clip_end,
		fadeout_clip_end,

		name_output_video ):

		ffmpeg_extract_subclip(video_fl , 0 ,2 , "cut.mp4" )

		#-------------------------------------------------------------
		intro             = VideoFileClip(v_intro)

		fade_in_intro	  = intro.fx( vfx.fadein , duration = float(fadein_intro) )
		fade_out_intro	  = fade_in_intro.fx( vfx.fadeout , duration= float(fadeout_intro) )

		#-------------------------------------------------------------
		video_clip        = VideoFileClip(video_fl)

		fade_in_clip	  = video_clip.fx( vfx.fadein , duration= float(fadein_clip) ) 
		fade_out_clip	  = fade_in_clip.fx( vfx.fadeout  , duration= float(fadeout_clip) )

		#-------------------------------------------------------------
		video_clip_end    = VideoFileClip(clip_end)

		fade_in_clip	  = video_clip.fx( vfx.fadein , duration= float(fadein_clip) ) 
		fade_out_clip_end = video_clip_end.fx( vfx.fadeout , duration= float(fadeout_clip) )


		#-------------------------------------------------------------
		video_size_final  = fade_out_clip.fx( vfx.resize , (intro.size)  )


		#-------------------------------------------------------------

		video_complet    = concatenate_videoclips( [fade_out_intro , video_size_final , fade_out_clip_end ] , method="compose" )
		video_complet.write_videofile(name_output_video , fps=30 , preset="ultrafast")
		

		try:
			os.remove("cut.mp4")
		except:
			pass
		pass


	def create_video_add_audio( self,  video_fl  ,audio_file_name , name_output_video ):
		ffmpeg_extract_subclip(video_fl , 0 ,2 , "cut.mp4" )

		sound               = AudioFileClip(audio_file_name, fps = 44100)
		video_clip    	    = VideoFileClip(video_fl)

		sound.duration      = video_clip.duration

		add_audio_videoclip = video_clip.set_audio(sound)

		add_audio_videoclip.write_videofile(name_output_video , fps=30 , preset="ultrafast")
		

		try:
			os.remove("cut.mp4")
		except:
			pass
		pass

#-------------------------------------------------------
#-------------------------------------------------------

