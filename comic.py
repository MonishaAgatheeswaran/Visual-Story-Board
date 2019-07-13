from PIL import Image, ImageFont,ImageDraw, ImageOps
import sys
from resizeimage import resizeimage
import textwrap

textFileChat = None
specifiedBackground = None
specifiedTitle  = None
nextToFill = None
for arg in sys.argv:
	if arg[0] == '-':
		nextToFill = arg[1:].lower()
	else:
		if nextToFill is not None:
			if nextToFill[0] == 'f':
				textFileChat = arg
			if nextToFill[0] == 'b':
				specifiedBackground = arg
			if nextToFill[0] == 't':
				specifiedTitle = arg
		nextToFill = None
def panel(scene):
    final=Image.open('600x600.png')
    file_type='.png'
    i=1
    if scene==1:
            pic_path=str(scene)+file_type
            final=Image.open(pic_path)
            
    elif scene==2:
            i=1
            while(i<=scene):
                    pic_path=str(i)+file_type
                    pic=Image.open(pic_path)
                    pic=resizeimage.resize_height(pic,300)
                    final.paste(pic,((i-1)*300,150))
                    i+=1
    elif scene==3:
            i=1
            while(i<=scene):
                    pic_path=str(i)+file_type
                    pic=Image.open(pic_path)
                    pic=resizeimage.resize_height(pic,200)
                    final.paste(pic,((i-1)*200,200))
                    i+=1
    elif scene==4:
            i=1
            while(i<=(scene/2)):
                    pic_path=str(i)+file_type
                    pic=Image.open(pic_path)
                    pic=resizeimage.resize_height(pic,300)
                    final.paste(pic,(((i-1)*300),0))
                    i+=1
            
            pic_path=str(i)+file_type
            pic=Image.open(pic_path)
            pic=resizeimage.resize_height(pic,300)
            final.paste(pic,(0,300))
            i+=1
            pic_path=str(i)+file_type
            pic=Image.open(pic_path)
            pic=resizeimage.resize_height(pic,300)
            final.paste(pic,(300,300))
    elif scene==5:
            i=1
            while(i<=3):
                    pic_path=str(i)+file_type
                    pic=Image.open(pic_path)
                    pic=resizeimage.resize_height(pic,200)
                    final.paste(pic,((i-1)*200,100))
                    i+=1
            pic_path=str(i)+file_type
            pic=Image.open(pic_path)
            pic=resizeimage.resize_height(pic,200)
            final.paste(pic,(100,300))
            i+=1       
            pic_path=str(i)+file_type
            pic=Image.open(pic_path)
            pic=resizeimage.resize_height(pic,200)
            final.paste(pic,(300,300))
            i+=1
    elif scene==6:
            i=1
            while(i<=3):
                    pic_path=str(i)+file_type
                    pic=Image.open(pic_path)
                    pic=resizeimage.resize_height(pic,200)
                    final.paste(pic,((i-1)*200,100))
                    i+=1
            
            while(i<=6):
                    pic_path=str(i)+file_type
                    pic=Image.open(pic_path)
                    pic=resizeimage.resize_height(pic,200)
                    final.paste(pic,((i-1)*200,300))
                    i+=1
    final.save('res.png')
    final.show('res.png')
        

def main():
    file_type=".png"
    f=open(textFileChat,"r")
    font=ImageFont.truetype(r'C:\Users\Monisha\AppData\Local\Programs\Python\Python36\Comic\fonts\Averia\Averia\AveriaGWF-Bold.ttf',50)
    scene=0
    count=0
    
    arrow=Image.open('bubblearrow.png')
    lines=f.readlines()
    for i in lines:
        count=count+1
        if(count%3)==1:
            scene=scene+1
            (xyz,k)=i.split(" ")
            bg_path=xyz + file_type
            bg=Image.open(bg_path)
            bg_width,bg_height=bg.size
            x=int(bg_width/4);
            y=int(bg_height/3);





        elif (count%3)==2:
            (ch,dialogue)=i.split("\t")
            print(dialogue)
            sentence=textwrap.wrap(dialogue,width=15)
            bubble=Image.open('bubble.png')
            bubble_w,bubble_h=bubble.size
            y_text=20
            draw=ImageDraw.Draw(bubble)
            for line in sentence:
                sen_w,sen_h=font.getsize(line)
                draw.text(((bubble_w-sen_w)/2,y_text),line,font=font,fill='black')
                y_text+=sen_h+20
            bubble.save('test.png')
            img_ch_path=ch + file_type
            img_ch=Image.open(img_ch_path)
            text_img=Image.open('test.png')
            arrow=Image.open('bubblearrow.png')
            img_ch=resizeimage.resize_height(img_ch,y)
            text_img=resizeimage.resize_height(text_img,y)
            arrow=resizeimage.resize_height(arrow,20)
            bg.paste(img_ch,(x-int(x/2),(2*y)-10),img_ch)
            if(dialogue!='\n'):
                    bg.paste(text_img,(x-int(x/2),y-10))
                    bg.paste(arrow,(x,(y*2)-10),arrow)
                    
            
            
            name=str(scene)+file_type
            bg.save(name)
            






        elif (count%3)==0:
            if i!="\t\n":
                    (ch,dia)=i.split("\t")
                    print(dia)
                    sen=textwrap.wrap(dia,width=15)
                    bubble=Image.open('bubble.png')
                    bubble_w,bubble_h=bubble.size
                    y_text=20
                    draw=ImageDraw.Draw(bubble)
                    for lin in sen:
                            sen_w,sen_h=font.getsize(lin)
                            draw.text(((bubble_w-sen_w)/2,y_text),lin,font=font,fill='black')
                            y_text+=sen_h+20
                    bubble.save('test.png')
                    img_ch_path=ch +'rot'+ file_type
                    img_ch=Image.open(img_ch_path)
                    text_img=Image.open('test.png')
                    arrow=Image.open('bubblearrow.png')
                    img_ch=resizeimage.resize_height(img_ch,y)
                    text_img=resizeimage.resize_height(text_img,y)
                    arrow=resizeimage.resize_height(arrow,20)
                    bg.paste(img_ch,((3*x)-int(x/2),(2*y)-10),img_ch)
                    if(dia!='\n'):
                            bg.paste(text_img,((3*x)-int(x/2),y-10))
                            bg.paste(arrow,((3*x),(y*2)-10),arrow)
                    
                    
                    name=str(scene)+file_type
                    bg.save(name)
                
                
    panel(scene)

if __name__ == "__main__":
    main()
