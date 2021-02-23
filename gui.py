from tkinter import *



def excitingWorld():
    root=Tk()
    frame=Frame(root)
    frame.pack()
    root.title('The tragedy of')
    button=Button(frame,text='  Quit  ',fg='dark blue',command=frame.quit)
    button.pack(side=LEFT)
    hi_there=Button(frame,text='Darth plagueis',fg='dark red',command=lambda:print('Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.'))
    hi_there.pack(side=RIGHT)
    bye_there=Button(frame,text='Cut the check',fg='dark green',command=lambda:print('Please cut the check to receive my services. Like just give slice of pizza and 20 bucks, just kidding I want more.'))
    bye_there.pack(side=BOTTOM)
    root.mainloop()
    root.destroy
excitingWorld()

     
                
