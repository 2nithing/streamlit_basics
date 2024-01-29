import streamlit as st
from streamlit_webrtc import webrtc_streamer,WebRtcMode,RTCConfiguration
import av

class VideoProcessor:
    def recv(self,frame):

        frm = frame.tondarray(format='bgr24')



        return av.VideoFrame.from_ndarray(frm,format='bgr24')

    
webrtc_streamer(key="key", 
                video_processor_factory=VideoProcessor,
                # video_frame_callback=recv,
				rtc_configuration=RTCConfiguration({"iceServers": [{"urls": ["stun:stun3.l.google.com:19302"]}]})
	            )