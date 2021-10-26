import PySimpleGUI as sg
from class_video import Video_Class
import Base_Button as img_b
import json
from JSON import JsonClass 


jsn_class = JsonClass()
jsnt      = jsn_class.json_read( name_file = "data/jsons/Texts"  )
cjv       = jsn_class.json_read( name_file = "data/jsons/Colors" )



class ClipJoinClass():
    def __init__(self):
        sg.theme("DarkBlue")
        self.video_c             = Video_Class()

        self.size_buttons        = ( 20 , 10 )        
        self.cavas_x_y           = ( 65  ,2 )
        self.img_size            = ( 720 , 153)
        self.size_slides         = ( 18  , 10 )

        self.texto_aviso         = jsnt["text_aviso_protugues"]
        self.texto_aviso_ingles  = jsnt["text_aviso_ingles"]

#------- LAYOUT_1 --------------------
        self.layout_1 = [

                        #======================================================================v
                        [
                        sg.Canvas(background_color = cjv["sinza__escuro_1"]  ,s=( 30, 1)) ,
                        sg.Image("data/soft_img/covers/img_cover_1.png", 
                            background_color      = cjv["sinza__escuro_1"] ,
                            size                  = self.img_size , 
                            key                   = "img_teste")
                        ],
                        #======================================================================
                        [sg.HSeparator()],


                        ]


                        





                      
#-------LAYOUT_2 --------------------                  
        self.layout_2 = [
                        #======================================================================
                        [sg.Button(
                            button_text             = "",
                            button_color            = (cjv['sinza__escuro_1'], cjv['sinza__escuro_1'] ) ,
                            button_type             = 2 ,
                            s                       = self.size_buttons, 
                            key                     = "clip_1",
                            border_width            = 0,
                            image_data              = img_b.button_seach_clip
                            )
                        ],

                        [sg.Text("Fadein/intro", 
                            text_color             = cjv["branco"],
                            background_color       = cjv['sinza__escuro_1'] )
                        ],
                        #======================================================================
                        [
                        sg.Slider(
                            range                   = (0, 10), 
                            size                    = self.size_slides, 
                            default_value           = 0 ,
                            background_color        = cjv['sinza__escuro_1'] ,
                            orientation             = "horizontal" , 
                            key                     = "fadein_intro_slide" , 
                            trough_color            = cjv['branco'])
                        ],
                        #======================================================================

                        [
                        sg.Text("Fadeout/intro", 
                            text_color              = cjv["branco"],
                            background_color        = cjv['sinza__escuro_1'] )
                        ],
                        #======================================================================
                        [
                        sg.Slider(
                            range                   = (0, 10), 
                            size                    = self.size_slides, 
                            default_value           = 0, 
                            background_color        = cjv['sinza__escuro_1'] ,
                            orientation             = "horizontal", 
                            key                     = "fadeout_intro_slide", 
                            trough_color            = cjv['branco']),
                        ],
                        #======================================================================
                        ]

#------- LAYOUT_3 --------------------
        self.layout_3 = [

                        #======================================================================
                        [sg.Button(
                            button_text             = "",
                            button_color            = (cjv['sinza__escuro_1'], cjv['sinza__escuro_1'] ) ,
                            button_type             = 2 ,
                            s                       = self.size_buttons, 
                            key                     = "clip_2",
                            border_width            = 0,
                            image_data              = img_b.button_seach_clip
                            )
                        ],
                        [
                        sg.Text("Fadein/main", 
                            text_color              = cjv["branco"],
                            background_color        = cjv['sinza__escuro_1'])
                        ],

                        #======================================================================
                        [
                        sg.Slider(
                            range                   = (0,10), 
                            size                    = self.size_slides, 
                            default_value           = 0, 
                            background_color        = cjv['sinza__escuro_1'] ,
                            orientation             = "horizontal" , 
                            key                     = "fadein_clip_main_slide", 
                            trough_color            = cjv['branco'])
                        ],
                        
                        #======================================================================
                        [sg.Text("Fadeout/main", 
                            text_color              = cjv["branco"] ,
                            background_color        = cjv['sinza__escuro_1'])
                        ],

                        #======================================================================
                        [sg.Slider(
                            range                   = (0,10), 
                            size                    = self.size_slides, 
                            default_value           = 0, 
                            background_color        = cjv['sinza__escuro_1'] ,
                            orientation             = "horizontal" , 
                            key                     = "fadeout_clip_main_slide", 
                            trough_color            = cjv['branco'])
                        ],

                        ]

#------- LAYOUT_4 --------------------
        self.layout_4 = [
                        #======================================================================
                        [sg.Button(
                            button_text             = "",
                            button_color            = (cjv['sinza__escuro_1'], cjv['sinza__escuro_1'] ) ,
                            button_type             = 2 ,
                            s                       = self.size_buttons, 
                            key                     = "clip_3",
                            border_width            = 0,
                            image_data              = img_b.button_seach_clip
                            )
                        ],
                        [sg.Text("Fadein/end", 
                            text_color              = cjv["branco"] ,
                            background_color        = cjv['sinza__escuro_1']  )
                        ],

                        #======================================================================
                        [sg.Slider(
                            range                   = (0,10), 
                            size                    = self.size_slides, 
                            default_value           = 0, 
                            background_color        = cjv['sinza__escuro_1'] ,
                            orientation             = "horizontal" , 
                            key                     = "fadein_clip_end_slide", 
                            trough_color            = cjv['branco'])
                        ],

                        #======================================================================
                        [sg.Text("Fadeout/end", 
                            text_color              = cjv["branco"] ,
                            background_color        = cjv['sinza__escuro_1'])
                        ],

                        #======================================================================
                        [sg.Slider(
                            range                   = (0,10), 
                            size                    = self.size_slides, 
                            default_value           = 0, 
                            background_color        = cjv['sinza__escuro_1'] ,
                            orientation             = "horizontal" , 
                            key                     = "fadeout_clip_end_slide", 
                            trough_color            = cjv['branco'] )],
                        ]

#------- LAYOUT_5 --------------------
        self.layout_5 = [
                        #[sg.HSeparator()],

                        #======================================================================
                        
                        [sg.Button(
                            button_text             = "",
                            button_color            = (cjv['sinza__escuro_1'], cjv['sinza__escuro_1'] ) ,
                            button_type             = 3 ,
                            s                       = self.size_buttons , 
                            key                     = "clip_save",
                            border_width            = 0,
                            image_data              = img_b.button_save_clip_in
                            )] ,

                        [sg.Button(
                            button_text             =" ",
                            button_color            = (cjv["branco"] , cjv["azul_claro"]),
                            key                     = "criar_clip",
                            size                    = self.size_buttons,
                            border_width            = 0,
                            image_data              = img_b.button_sexport_clip
                            )],
                        
                        #======================================================================

                        ]

#------- LAYOUT_JOINS --------------------
        self.layouts = [
                    
                    [self.layout_1],

                    [

                    sg.Column(self.layout_2, background_color = cjv["sinza__escuro_1"]),

                    sg.VSeparator(),

                    sg.Column(self.layout_3, background_color = cjv["sinza__escuro_1"]),

                    sg.VSeparator(),

                    sg.Column(self.layout_4, background_color = cjv["sinza__escuro_1"]),

                    sg.VSeparator(),

                    sg.Column(self.layout_5, background_color = cjv["sinza__escuro_1"]),
                
                    ],


                    ],
                   



        self.win = sg.Window("Clips_Joins",
                            background_color = cjv["sinza__escuro_1"],
                            icon             = "IconCliPyCloundPlus.ico",
                            size             = (820,560)).layout(self.layouts)

    #----------------------------------------------------------------------------------
    def Update(self):
       
        while True:
            self.events, self.values = self.win.Read()
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break
 

            if self.events == "criar_clip":
                try:
                    into     = self.values["clip_1"] 
                    video    = self.values["clip_2"] 
                    end      = self.values["clip_3"]
                    output_v = self.values["clip_save"] + str(".mp4")

                    self.video_c.video_joins(
                                            v_intro            = into   , 
                                            video_fl           = video  ,
                                            clip_end           = end    , 

                                            fadein_intro       = self.values['fadein_intro_slide'] , 
                                            fadeout_intro      = self.values['fadeout_intro_slide'],

                                            fadein_clip        = self.values['fadein_clip_main_slide'] , 
                                            fadeout_clip       = self.values['fadeout_clip_main_slide'], 

                                              
                                            fadein_clip_end    = self.values['fadein_clip_end_slide'] ,
                                            fadeout_clip_end   = self.values['fadeout_clip_end_slide'],

                                            name_output_video  = output_v

                                            )

                except Exception as e:
                    print(f"ocorreu um erro {e}")

                    pass


#app = ClipJoinClass()
#app.Update()