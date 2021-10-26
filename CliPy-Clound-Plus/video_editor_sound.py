import PySimpleGUI as sg
from class_video import Video_Class
import Base_Button as img_b
import json
from JSON import JsonClass 
import Base_Button as img_b


jsn_class = JsonClass()
jsnt      = jsn_class.json_read( name_file = "data/jsons/Texts" )
cjv       = jsn_class.json_read( name_file = "data/jsons/Colors")


class ClipSoundClass():
    def __init__(self):
        sg.theme("DarkBlue")
        self.video_c             = Video_Class()
        self.size_buttons        = ( 20 , 10 )
        self.cavas_x_y           = ( 65 ,2 )
        
        self.img_size            = ( 720 , 153)
        self.size_slides         = ( 18 , 10 )
        self.text_sound_aviso    = jsnt["text_sound_aviso"]
        

        self.layout_1 = [

                        #======================================================================
                        [
                        sg.Image("data/soft_img/covers/img_cover_2.png", 
                            background_color       = cjv["sinza__escuro_1"] ,
                            size                   = self.img_size , 
                            key                    = "img_teste")
                        ],

                        #======================================================================
                        [
                        sg.Canvas(background_color = cjv["sinza__escuro_1"]  ,s=( 20, 1)) ,

                        sg.Text(
                            self.text_sound_aviso,
                            text_color             = cjv["branco"] ,
                            background_color       = cjv['sinza__escuro_1'])
                        ],

                        #======================================================================
                        [sg.HSeparator()],

                        #======================================================================
                        [
                        sg.Button(
                            button_text             = "",
                            button_color            = (cjv['sinza__escuro_1'], cjv['sinza__escuro_1'] ) ,
                            button_type             = 2 ,
                            s                       = self.size_buttons, 
                            key                     = "path_audio",
                            border_width            = 0,
                            image_data              = img_b.button_seach_audio
                            ) ,

                        sg.Button(
                            button_text             = "",
                            button_color            = (cjv['sinza__escuro_1'], cjv['sinza__escuro_1'] ) ,
                            button_type             = 2 ,
                            s                       = self.size_buttons , 
                            key                     = "path_clip_main",
                            border_width            = 0,
                            image_data              = img_b.button_seach_clip
                            ) ,

                        sg.Button(
                            button_text             = "",
                            button_color            = (cjv['sinza__escuro_1'], cjv['sinza__escuro_1'] ) ,
                            button_type             = 3 ,
                            s                       = self.size_buttons , 
                            key                     = "button_save",
                            border_width            = 0,
                            image_data              = img_b.button_save_clip_in
                            ) ,

                        sg.Button(
                            button_text             =" ",
                            button_color            = (cjv["branco"] , cjv["azul_claro"]),
                            key                     = "criar_clip",
                            size                    = self.size_buttons,
                            border_width            = 0,
                            image_data              = img_b.button_sexport_clip
                            ),

                        ],

                        #======================================================================
                        
                        ]

                
#---------------------------------------------

        self.layout_5 = [
                        [sg.HSeparator()],
                        ]


        self.layouts = [
                        [self.layout_1],
                        #[self.layout_5]
                    ],
                   



        self.win = sg.Window("Clips_Sound_Add",
                            background_color = cjv["sinza__escuro_1"],
                            icon             = "IconCliPyCloundPlus.ico",
                            size             = (720,400)).layout(self.layouts)

    #----------------------------------------------------------------------------------
    def Update(self):
       
        while True:
            self.events, self.values = self.win.Read()
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break
 

            if self.events == "criar_clip":
                try:
                    sound     = self.values["path_audio"] 
                    video     = self.values["path_clip_main"] 
                    output_v  = self.values["button_save"] + str(".mp4")


                    self.video_c.create_video_add_audio(
                        video_fl          = video ,
                        audio_file_name   = sound , 
                        name_output_video = output_v 
                        )

 
                except Exception as e:
                    print(f"ocorreu um erro {e}")

                    pass


#app = ClipSoundClass()
#app.Update()