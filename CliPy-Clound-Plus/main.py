from PIL import  Image, ImageFont, ImageDraw , ImagePalette , PSDraw
import PySimpleGUI as sg
import Base_Button as img_b
from video_editor import ClipJoinClass
from video_editor_sound import ClipSoundClass
from video_editor_speed import ClipSpeedClass
from JSON import JsonClass 
import credits as cr
import json



jsn_class = JsonClass()
cjv       = jsn_class.json_read( name_file = "data/jsons/Colors")


class App_input_Wind():
    def __init__(self):
        #sg.theme("DarkBlue")

        self.size_buttons = ( 20 , 10 )
        self.cavas_x_y    = ( 500 , 20 )


        self.lay1 = [
                    #======================================================================
                    [
                    sg.Image("data//soft_img/covers/cover_CliPyClound-Plus.png", 
                        background_color        = cjv["sinza__escuro_1"] ,
                        size                    = (773 , 198 ))
                    ],

                    #======================================================================
                    [sg.Canvas(background_color = cjv['sinza__escuro_1'] ,s=( 5 , 10) )],

                    #======================================================================
                    [
                    sg.Canvas(
                        background_color        = cjv['sinza__escuro_1']  ,
                        s                       = ( 120 ,1) ),

                    sg.Button("", 
                        button_color            = ( cjv['sinza__escuro_1'], cjv['sinza__escuro_1'] ) ,
                        key                     = "b1",
                        border_width            = 0,
                        size                    = self.size_buttons,
                        image_data              = img_b.button_1),

                    sg.Button("",
                        button_color            = (cjv['sinza__escuro_1'], cjv['sinza__escuro_1'] ) ,
                        key                     = "b2",
                        border_width            = 0,
                        size                    = self.size_buttons,
                        image_data              = img_b.button_2),

                    sg.Button("", 
                        button_color            = (cjv['sinza__escuro_1'], cjv['sinza__escuro_1'] ) ,
                        key                     = "b3",
                        border_width            = 0,
                        size                    = self.size_buttons,
                        image_data              = img_b.button_3),
                    ],

                    #======================================================================
                    [
                    sg.Canvas(background_color  = cjv['sinza__escuro_1'] ,s=( 720, 1) ),

                    sg.Button("", 
                                button_color    = (cjv['sinza__escuro_1'], cjv['sinza__escuro_1'] ) ,
                                key             = "credits_button",
                                border_width    = 0,
                                #size           = (6,2),
                                image_data      = img_b.button_credits)
                    ],
                    
                    
                    ]


        self.layouts = [
                        [self.lay1] 
                      ]


        self.win = sg.Window(   "CliPy Clound-Plus_v0.5",
                                background_color = cjv['sinza__escuro_1'], 
                                size             = ( 800 , 480) ,
                                icon             = "IconCliPyCloundPlus.ico",
                                no_titlebar      = False ).layout(self.layouts)
        
    #----------------------------------------------------------------------------------
    def Update(self):
        while True:
            self.events, self.values = self.win.Read()
            if self.values == sg.WIN_CLOSED or self.values == "Sair":
                break
 
            if self.events == "b1":
                app = ClipJoinClass()
                app.Update()

            if self.events == "b2":
                app = ClipSoundClass()
                app.Update()

            if self.events == "b3":
                app = ClipSpeedClass()
                app.Update()

            if self.events == "credits_button":
                cr.Credits()

                pass






Input_App = App_input_Wind()
Input_App.Update()

