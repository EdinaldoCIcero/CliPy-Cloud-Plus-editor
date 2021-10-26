import PySimpleGUI as sg
from class_video import Video_Class
import Base_Button as img_b
import json
from JSON import JsonClass 



jsn_class = JsonClass()
jsnt      = jsn_class.json_read( name_file = "data/jsons/Texts")
cjv       = jsn_class.json_read( name_file = "data/jsons/Colors")



class ClipSpeedClass():
    def __init__(self):
        sg.theme("DarkBlue")

        self.video_c             = Video_Class()
        self.size_buttons        = ( 20 , 10 )
        self.cavas_x_y           = ( 65 ,2 )
        self.img_size            = ( 720 , 153)
        self.size_slides         = ( 50 , 10 )
        self.texto_aviso         = jsnt["text_aviso_slide_speed"]
        self.texto_aviso_ingles  = jsnt["text_aviso_ingles"]
        #======================================================================
        

#------------------------------------------------------

        self.layout_1 = [
                        #======================================================================
                        [
                        sg.Image("data/soft_img/covers/img_cover_3.png", 
                            background_color        = cjv["sinza__escuro_1"] ,
                            size                    = self.img_size , 
                            key                     = "img_teste")
                        ],

                        #======================================================================
                        [sg.HSeparator()],

                        #======================================================================
                        [
                        sg.Canvas(background_color  = cjv["sinza_70"]  ,s = ( 110, 1)),

                        sg.Slider(
                            range                   = (0,10), 
                            size                    = self.size_slides, 
                            default_value           = 0, 
                            background_color        = cjv['sinza__escuro_1'] ,
                            orientation             = "horizontal" , 
                            key                     = "duration_slide" , 
                            trough_color            = cjv['branco'] )],

                        #======================================================================
                        #[sg.Canvas(background_color = cjv["sinza_70"]  ,s=( 1, 20))],

                        #======================================================================
                        [
                        sg.Canvas(background_color  = cjv["sinza_70"]  ,s=( 130, 1)),

                        sg.Text(self.texto_aviso,
                            text_color              = cjv["branco"] ,
                            background_color        = cjv['sinza__escuro_1'])
                        ],
                        
                        #======================================================================
                        [sg.HSeparator()],

                        #======================================================================
                        [
                        sg.Canvas(background_color  = cjv["sinza_70"]  ,s=( 90, 1)) ,

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
                            button_text             = " ", 
                            button_color            = (cjv['sinza__escuro_1'], cjv['sinza__escuro_1'] ) ,
                            button_type             = 3 ,
                            s                       = self.size_buttons , 
                            key                     = "text_path_save",
                            border_width            = 0,
                            image_data              = img_b.button_save_clip_in
                            ) ,


                        sg.Button("",
                            button_color            = (cjv["branco"] , cjv["azul_claro"]),
                            key                     = "criar_clip",
                            size                    = self.size_buttons,
                            border_width            = 0,
                            image_data              = img_b.button_sexport_clip),
                        ],
                        #======================================================================


                        ]
                        
#------------------------------------------------------
        self.layouts = [ 
                        [self.layout_1]
                      ],
                   


        self.win = sg.Window("Clips_Speed_Time",
                            background_color = cjv["sinza__escuro_1"],
                            icon             = "IconCliPyCloundPlus.ico",
                            size             = (720,440)).layout(self.layouts)

    #----------------------------------------------------------------------------------
    def Update(self):
       
        while True:
            self.events, self.values = self.win.Read()
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break
 

            if self.events == "criar_clip":
                
                try:
                    slide_value = self.values["duration_slide"]
                    video       = self.values["path_clip_main"] 
                    output_v    = self.values["text_path_save"] + str(".mp4")

                    self.video_c.set_clip_timer_speed(
                        video_fl          = video ,
                        speed_clip        = slide_value , 
                        name_output_video = output_v)


                except Exception as e:
                    print(f"ocorreu um erro {e}")

                    pass



#app = ClipSpeedClass()
#app.Update()